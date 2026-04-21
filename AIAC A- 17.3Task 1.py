# TASK-01
import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

# Read the CSV file
csv_path = 'loanapproval.csv'
if not os.path.exists(csv_path):
    raise FileNotFoundError(
        f"Dataset file not found: {csv_path}.\n" \
        "Place the CSV in the same folder as this script or update csv_path to the correct file location."
    )

df = pd.read_csv(csv_path)

# Display original dataset info
print("Original Dataset Shape:", df.shape)
print("\nFirst few rows:")
print(df.head())
print("\nMissing values:")
print(df.isnull().sum())

# Handle missing values in loan_amount and credit_score
df['loan_amount'].fillna(df['loan_amount'].mean(), inplace=True)
df['credit_score'].fillna(df['credit_score'].mean(), inplace=True)

print("\nMissing values after handling:")
print(df.isnull().sum())

# Encode loan_status (Approved/Rejected) into numeric labels
le = LabelEncoder()
df['loan_status'] = le.fit_transform(df['loan_status'])
print("\nLoan Status Encoding:", dict(zip(le.classes_, le.transform(le.classes_))))

# Separate features and target
X = df.drop('loan_status', axis=1)
y = df['loan_status']

# Select only numerical features for scaling
numerical_features = X.select_dtypes(include=[np.number]).columns.tolist()
X_numerical = X[numerical_features]

# Scale numerical features using StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_numerical)
X_scaled = pd.DataFrame(X_scaled, columns=numerical_features)

# Split the data into training and testing sets (80-20 split)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

print("\nPreprocessed Dataset Summary:")
print(f"Training set size: {X_train.shape}")
print(f"Testing set size: {X_test.shape}")
print(f"\nTraining features shape: {X_train.shape}")
print(f"Training target shape: {y_train.shape}")
print(f"Testing features shape: {X_test.shape}")
print(f"Testing target shape: {y_test.shape}")

# Display sample of preprocessed training data
print("\nSample of preprocessed training data:")
print(X_train.head())
print("\nTarget distribution in training set:")
print(y_train.value_counts())



# TASK-02 
import os
import pandas as pd
import numpy as np

# Update this path if the CSV file is located elsewhere.
csv_path = 'SocialMediaTop100.csv'
output_path = 'SocialMediaTop100_cleaned.csv'

if not os.path.exists(csv_path):
    raise FileNotFoundError(
        f"Dataset file not found: {csv_path}.\n"
        "Place the CSV in the same folder as this script or update csv_path to the correct file location."
    )

# Read the social media dataset
print(f"Loading dataset from: {csv_path}")
df = pd.read_csv(csv_path)

print("Original dataset shape:", df.shape)
print("Columns:", list(df.columns))
print("\nPreview:")
print(df.head(5))
print("\nMissing values by column:")
print(df.isnull().sum())

# 1. Remove duplicate user profiles
# If the dataset contains a profile identifier like 'profile', 'username', or 'name', deduplicate on that column.
profile_keys = [c for c in df.columns if c.lower() in {'profile', 'username', 'name', 'handle'}]
if profile_keys:
    dedup_cols = profile_keys
else:
    dedup_cols = df.columns.tolist()

before_duplicates = df.shape[0]
df = df.drop_duplicates(subset=dedup_cols, keep='first').reset_index(drop=True)
after_duplicates = df.shape[0]
print(f"\nRemoved duplicates: {before_duplicates - after_duplicates}")
print("Shape after duplicate removal:", df.shape)

# 2. Handle missing values
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

for col in numeric_cols:
    if df[col].isna().any():
        median_value = df[col].median()
        df[col].fillna(median_value, inplace=True)
        print(f"Filled missing numeric values in '{col}' with median: {median_value}")

for col in cat_cols:
    if df[col].isna().any():
        mode_value = df[col].mode(dropna=True)
        fill_value = mode_value.iloc[0] if not mode_value.empty else 'missing'
        df[col].fillna(fill_value, inplace=True)
        print(f"Filled missing categorical values in '{col}' with mode: {fill_value}")

print("\nMissing values after imputation:")
print(df.isnull().sum())

# 3. Encode categorical columns
# Keep textual identifiers like profile names as-is; encode non-identifier categorical attributes.
identifier_cols = [c for c in cat_cols if c.lower() in {'profile', 'username', 'name', 'handle'}]
encode_cols = [c for c in cat_cols if c not in identifier_cols]

if encode_cols:
    print(f"\nEncoding categorical columns: {encode_cols}")
    df = pd.get_dummies(df, columns=encode_cols, drop_first=True)
else:
    print("\nNo categorical columns found for encoding.")

print("\nFinal cleaned dataset shape:", df.shape)
print("Final columns:", list(df.columns))
print("\nPreview of cleaned data:")
print(df.head(5))

# Save cleaned dataset for engagement prediction
print(f"\nSaving cleaned dataset to: {output_path}")
df.to_csv(output_path, index=False)
print("Saved cleaned dataset successfully.")


# TASK-03

import os
import pandas as pd
import numpy as np

# Update this path if the CSV file is located elsewhere.
csv_path = 'weather_forecast_data.csv'
output_path = 'weather_forecast_data_processed.csv'

DATE_CANDIDATES = ['date', 'Date', 'datetime', 'Timestamp', 'timestamp']
TEMP_CANDIDATES = ['temp', 'temperature', 'Temp', 'Temperature']
HUMIDITY_CANDIDATES = ['humidity', 'Humidity']
RAINFALL_CANDIDATES = ['rainfall', 'Rainfall', 'precipitation', 'Precipitation', 'rain']

SEASON_MAP = {
    12: 'Winter', 1: 'Winter', 2: 'Winter',
    3: 'Spring', 4: 'Spring', 5: 'Spring',
    6: 'Summer', 7: 'Summer', 8: 'Summer',
    9: 'Autumn', 10: 'Autumn', 11: 'Autumn'
}


def detect_column(columns, candidates):
    for candidate in candidates:
        if candidate in columns:
            return candidate
    lower_cols = {c.lower(): c for c in columns}
    for candidate in candidates:
        if candidate.lower() in lower_cols:
            return lower_cols[candidate.lower()]
    return None


def season_from_date(dt: pd.Timestamp) -> str:
    return SEASON_MAP.get(dt.month, 'Unknown')


if not os.path.exists(csv_path):
    raise FileNotFoundError(
        f"Dataset file not found: {csv_path}.\n"
        "Place the CSV in the same folder as this script or update csv_path to the correct file location."
    )

print(f"Loading dataset from: {csv_path}")
df = pd.read_csv(csv_path)
print("Original dataset shape:", df.shape)
print("Columns:", list(df.columns))
print("\nMissing values by column:")
print(df.isnull().sum())

# 1. Convert date column into datetime format

date_col = detect_column(df.columns, DATE_CANDIDATES)
if date_col is None:
    raise ValueError(
        "No date column found in the dataset. "
        "Expected a column like 'date', 'datetime', or 'timestamp'."
    )

print(f"Converting '{date_col}' to datetime...")
try:
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
except Exception as e:
    raise ValueError(f"Unable to convert '{date_col}' to datetime: {e}")

if df[date_col].isnull().any():
    print(f"Warning: {df[date_col].isnull().sum()} rows have invalid or missing dates after conversion.")

# 2. Handle missing values in temperature and humidity

temp_col = detect_column(df.columns, TEMP_CANDIDATES)
humidity_col = detect_column(df.columns, HUMIDITY_CANDIDATES)

if temp_col is None and humidity_col is None:
    raise ValueError("No temperature or humidity columns found for missing-value handling.")

if temp_col is not None:
    if df[temp_col].isna().any():
        median_temp = df[temp_col].median()
        df[temp_col].fillna(median_temp, inplace=True)
        print(f"Filled missing values in '{temp_col}' with median: {median_temp}")
    else:
        print(f"No missing values found in temperature column '{temp_col}'.")

if humidity_col is not None:
    if df[humidity_col].isna().any():
        median_humidity = df[humidity_col].median()
        df[humidity_col].fillna(median_humidity, inplace=True)
        print(f"Filled missing values in '{humidity_col}' with median: {median_humidity}")
    else:
        print(f"No missing values found in humidity column '{humidity_col}'.")

# 3. Create new features: season and week_number

print("Creating season and week_number features...")
df['season'] = df[date_col].apply(lambda x: season_from_date(x) if pd.notnull(x) else 'Unknown')
df['week_number'] = df[date_col].dt.isocalendar().week

# 4. Normalize rainfall values
rain_col = detect_column(df.columns, RAINFALL_CANDIDATES)
if rain_col is None:
    print("Warning: No rainfall column found. Skipping rainfall normalization.")
else:
    min_rain = df[rain_col].min()
    max_rain = df[rain_col].max()
    if pd.isna(min_rain) or pd.isna(max_rain) or min_rain == max_rain:
        print(f"Cannot normalize '{rain_col}' because values are constant or missing.")
    else:
        df[f'{rain_col}_normalized'] = (df[rain_col] - min_rain) / (max_rain - min_rain)
        print(f"Normalized rainfall column '{rain_col}' into '{rain_col}_normalized'.")

print("\nProcessed dataset shape:", df.shape)
print("Columns after processing:", list(df.columns))
print("\nPreview of processed data:")
print(df.head(5))

print(f"\nSaving processed dataset to: {output_path}")
df.to_csv(output_path, index=False)
print("Saved processed dataset successfully.")



# TASK-04

print("\n# TASK-04: Movie Ratings Dataset Preparation")

csv_path = 'imdb_data.csv'
output_path = 'imdb_data_processed.csv'

RATING_CANDIDATES = ['rating', 'Rating', 'score', 'Score']
GENRE_CANDIDATES = ['genre', 'Genre', 'genres', 'Genres']
LANGUAGE_CANDIDATES = ['language', 'Language', 'lang', 'Lang']
TITLE_CANDIDATES = ['title', 'Title', 'movie', 'Movie', 'name', 'Name']
YEAR_CANDIDATES = ['year', 'Year', 'release_year', 'Release Year', 'release year']

if not os.path.exists(csv_path):
    raise FileNotFoundError(
        f"Dataset file not found: {csv_path}.\n"
        "Place the CSV in the same folder as this script or update csv_path to the correct file location."
    )

print(f"Loading dataset from: {csv_path}")
df = pd.read_csv(csv_path)
print("Original dataset shape:", df.shape)
print("Columns:", list(df.columns))
print("\nMissing values by column:")
print(df.isnull().sum())

rating_col = detect_column(df.columns, RATING_CANDIDATES)
genre_col = detect_column(df.columns, GENRE_CANDIDATES)
language_col = detect_column(df.columns, LANGUAGE_CANDIDATES)
title_col = detect_column(df.columns, TITLE_CANDIDATES)
year_col = detect_column(df.columns, YEAR_CANDIDATES)

# Handle missing values in rating and genre
if rating_col is None:
    raise ValueError("No rating column found in the dataset. Expected a column like 'rating' or 'score'.")
if genre_col is None:
    print("Warning: No genre column found in the dataset. Genre encoding will be skipped.")
if language_col is None:
    print("Warning: No language column found in the dataset. Language encoding will be skipped.")

if df[rating_col].isna().any():
    rating_median = df[rating_col].median()
    df[rating_col].fillna(rating_median, inplace=True)
    print(f"Filled missing values in '{rating_col}' with median: {rating_median}")
else:
    print(f"No missing values found in rating column '{rating_col}'.")

if genre_col is not None:
    if df[genre_col].isna().any():
        genre_mode = df[genre_col].mode(dropna=True)
        fill_value = genre_mode.iloc[0] if not genre_mode.empty else 'Unknown'
        df[genre_col].fillna(fill_value, inplace=True)
        print(f"Filled missing values in '{genre_col}' with mode: {fill_value}")
    else:
        print(f"No missing values found in genre column '{genre_col}'.")

# Remove duplicate movie entries
if title_col is not None:
    dedup_cols = [title_col]
    if year_col is not None:
        dedup_cols.append(year_col)
else:
    dedup_cols = df.columns.tolist()

before_duplicates = df.shape[0]
df = df.drop_duplicates(subset=dedup_cols, keep='first').reset_index(drop=True)
after_duplicates = df.shape[0]
print(f"Removed duplicate movie entries: {before_duplicates - after_duplicates}")
print("Shape after duplicate removal:", df.shape)

# Encode categorical variables
encode_cols = [col for col in [genre_col, language_col] if col is not None]
if encode_cols:
    for col in encode_cols:
        if df[col].dtype == object or pd.api.types.is_categorical_dtype(df[col]):
            df[col] = df[col].fillna('Unknown')
    print(f"Encoding categorical columns: {encode_cols}")
    df = pd.get_dummies(df, columns=encode_cols, drop_first=True)
else:
    print("No categorical columns found for encoding.")

# Scale rating values between 0 and 1
min_rating = df[rating_col].min()
max_rating = df[rating_col].max()
if pd.isna(min_rating) or pd.isna(max_rating) or min_rating == max_rating:
    raise ValueError(f"Cannot scale '{rating_col}' because values are constant or missing.")
df[f'{rating_col}_scaled'] = (df[rating_col] - min_rating) / (max_rating - min_rating)
print(f"Scaled rating column '{rating_col}' into '{rating_col}_scaled'.")

print("\nProcessed movie ratings dataset shape:", df.shape)
print("Columns after processing:", list(df.columns))
print("\nPreview of processed movie ratings data:")
print(df.head(5))

print(f"\nSaving processed movie ratings dataset to: {output_path}")
df.to_csv(output_path, index=False)
print("Saved processed movie ratings dataset successfully.")