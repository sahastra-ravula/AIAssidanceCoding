'''# Implement a Stack class in Python
#Methods:
#push(item)
#pop()
#peek()
#is_empty()
#Add proper docstrings for each method
#Handle edge cases (empty stack)
#Include test cases with output

class Stack:
    """A simple implementation of a stack data structure."""
    
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []
    
    def push(self, item):
        """Add an item to the top of the stack.
        
        Args:
            item: The item to be added to the stack.
        """
        self.items.append(item)
    
    def pop(self):
        """Remove and return the item at the top of the stack.
        
        Returns:
            The item at the top of the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()
    
    def peek(self):
        """Return the item at the top of the stack without removing it.
        
        Returns:
            The item at the top of the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]
    
    def is_empty(self):
        """Check if the stack is empty.
        
        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0
# Test cases
if __name__ == "__main__":

    stack = Stack()
    
    # Test is_empty on an empty stack
    print(stack.is_empty())  # Output: True
    
    # Test push and peek
    stack.push(1)
    stack.push(2)
    print(stack.peek())  # Output: 2
    
    # Test pop
    print(stack.pop())  # Output: 2
    print(stack.peek())  # Output: 1
    
    # Test pop on the last item
    print(stack.pop())  # Output: 1
    
    # Test is_empty after popping all items
    print(stack.is_empty())  # Output: True
    
    # Test pop on an empty stack (should raise an error)
    try:
        stack.pop()
    except IndexError as e:
        print(e)  # Output: Pop from an empty stack
    
    # Test peek on an empty stack (should raise an error)
    try:
        stack.peek()
    except IndexError as e:
        print(e)  # Output: Peek from an empty stack'''

'''# Implement a Queue class using Python list
#Methods:
#enqueue(item)
#dequeue()
#peek()
#size()
#Follow FIFO (First In First Out)
#Handle empty queue cases
#Add docstrings
#Include test cases with output 
class Queue:
    """
    Queue implementation using Python list.
    Follows FIFO (First In First Out).
    """

    def __init__(self):
        """Initialize an empty queue."""
        self.queue = []

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.queue.append(item)
        print("Enqueued:", item)

    def dequeue(self):
        """Remove and return the front item from the queue."""
        if not self.queue:
            print("Queue is empty")
            return None
        return self.queue.pop(0)

    def peek(self):
        """Return the front item without removing it."""
        if not self.queue:
            print("Queue is empty")
            return None
        return self.queue[0]

    def size(self):
        """Return the number of elements in the queue."""
        return len(self.queue)


# -------- TESTING --------
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front element:", q.peek())
print("Dequeued:", q.dequeue())
print("Queue size:", q.size())'''

'''#Implement a Singly Linked List in Python
#Create Node class
#Create LinkedList class
#Methods:
#insert(data)  → insert at end
#display()     → print all elements
#Add proper docstrings
class Node:
    """A node in a singly linked list."""
    
    def __init__(self, data):
        """Initialize a node with data and a pointer to the next node."""
        self.data = data
        self.next = None

class LinkedList:
    """A singly linked list implementation."""
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
    
    def insert(self, data):
        """Insert a new node with the given data at the end of the list.
        
        Args:
            data: The data to be stored in the new node.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def display(self):
        """Print all elements in the linked list."""
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()  # for a new line after printing all elements
# Test cases
if __name__ == "__main__":
    linked_list = LinkedList()
    
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    
    print("Linked List elements:")
    linked_list.display()  # Output: 1 2 3'''

#Implement a Hash Table in Python
#Methods:
#insert(key, value)
#search(key)
#delete(key)
#Use chaining (list in each bucket) for collision handling
#Add proper comments and docstrings
#Handle duplicate keys (update value)

class HashTable:
    """
    Hash Table implementation using chaining for collision handling.
    """

    def __init__(self, size=10):
        """Initialize hash table with empty buckets."""
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        """Generate index using built-in hash function."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert or update key-value pair."""
        index = self.hash_function(key)
        bucket = self.table[index]

        # Check if key exists → update
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                print("Updated:", key, value)
                return

        # Insert new key
        bucket.append((key, value))
        print("Inserted:", key, value)

    def search(self, key):
        """Search for a key and return its value."""
        index = self.hash_function(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v

        return "Not Found"

    def delete(self, key):
        """Delete a key-value pair."""
        index = self.hash_function(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                print("Deleted:", key)
                return

        print("Key not found")


# -------- TESTING --------
ht = HashTable()

ht.insert("A", 10)
ht.insert("B", 20)
ht.insert("C", 30)

print(ht.search("A"))   # 10
print(ht.search("B"))   # 20

ht.delete("B")
print(ht.search("B"))   # Not Found
ht.insert("A", 100)  # Update value for key "A"
print(ht.search("A"))   # 100 

'''# Genearate a python code to Implement a Graph using adjacency list
#Create Graph class
# Methods:
#add_vertex(vertex)
#add_edge(v1, v2)
#display()
#Use adjacency list representation (dictionary)
#Add docstrings and comments
#Include test cases with output
class Graph:
    """
    Graph implementation using an adjacency list representation.
    """

    def __init__(self):
        """Initialize an empty graph."""
        self.graph = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.graph:
            self.graph[vertex] = []
            print("Added vertex:", vertex)
        else:
            print("Vertex already exists:", vertex)

    def add_edge(self, v1, v2):
        """Add an edge between two vertices."""
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)  # For undirected graph
            print("Added edge between:", v1, "and", v2)
        else:
            print("One or both vertices not found:", v1, v2)

    def display(self):
        """Display the graph as an adjacency list."""
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")
# -------- TESTING --------
if __name__ == "__main__":
    g = Graph()

    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")

    g.add_edge("A", "B")
    g.add_edge("A", "C")

    print("Graph adjacency list:")
    g.display()'''

'''# Design a Smart Hospital Management System

# Tasks:
# 1. Map each feature to a suitable data structure:
#    - Patient Check-In System
#    - Emergency Case Handling
#    - Medical Records Storage
#    - Doctor Appointment Scheduling
#    - Hospital Room Navigation

# 2. Provide 2–3 sentence justification for each

# 3. Implement one feature using Python:
#    - Use appropriate data structure
#    - Include methods, comments, and docstrings
#    - Add test cases with output

# Generate clean and readable code
import heapq

class EmergencyQueue:
    """
    Priority Queue for handling emergency patients.
    Lower number = higher priority (more critical).
    """

    def __init__(self):
        self.queue = []

    def add_patient(self, name, severity):
        """
        Add patient with severity level.
        severity: 1 (critical) → high priority
        """
        heapq.heappush(self.queue, (severity, name))
        print(f"Patient added: {name} (Severity {severity})")

    def treat_patient(self):
        """Treat highest priority patient."""
        if not self.queue:
            print("No patients in queue")
            return

        patient = heapq.heappop(self.queue)
        print(f"Treating: {patient[1]} (Severity {patient[0]})")

    def display(self):
        """Display current queue."""
        print("\nCurrent Queue:")
        for p in self.queue:
            print(p[1], "- Severity", p[0])


# -------- TESTING --------
eq = EmergencyQueue()

eq.add_patient("Ravi", 3)
eq.add_patient("Anita", 1)   # critical
eq.add_patient("John", 2)

eq.display()

eq.treat_patient()
eq.treat_patient()
eq.treat_patient()
eq.treat_patient()  # No patients in queue'''

'''# Design a Smart Traffic Management System

# Tasks:
# 1. Map each feature to a suitable data structure:
#    - Traffic Signal Queue
#    - Emergency Vehicle Priority Handling
#    - Vehicle Registration Lookup
#    - Road Network Mapping
#    - Parking Slot Availability

# 2. Provide 2–3 sentence justification for each

# 3. Implement one feature using Python:
#    - Include methods, comments, and docstrings
#    - Add test cases with output

# Generate clean and readable code
import heapq

class TrafficPriorityQueue:
    """
    Priority Queue for emergency vehicle handling.
    Lower number = higher priority.
    """

    def __init__(self):
        self.queue = []

    def add_vehicle(self, vehicle, priority):
        """
        Add vehicle with priority.
        priority: 1 = emergency, 2 = normal
        """
        heapq.heappush(self.queue, (priority, vehicle))
        print(f"Vehicle added: {vehicle} (Priority {priority})")

    def process_vehicle(self):
        """Process highest priority vehicle."""
        if not self.queue:
            print("No vehicles in queue")
            return

        vehicle = heapq.heappop(self.queue)
        print(f"Processing: {vehicle[1]} (Priority {vehicle[0]})")

    def display(self):
        """Display queue."""
        print("\nCurrent Vehicles:")
        for v in self.queue:
            print(v[1], "- Priority", v[0])


# -------- TESTING --------
tpq = TrafficPriorityQueue()

tpq.add_vehicle("Car", 2)
tpq.add_vehicle("Ambulance", 1)
tpq.add_vehicle("Bike", 2)
tpq.add_vehicle("Fire Truck", 1)

tpq.display()

tpq.process_vehicle()
tpq.process_vehicle()
tpq.process_vehicle()
tpq.process_vehicle()
tpq.process_vehicle()  # No vehicles in queue'''

# Design a Smart E-Commerce Platform

# Tasks:
# 1. Map each feature to a suitable data structure:
#    - Shopping Cart Management
#    - Order Processing System
#    - Top-Selling Products Tracker
#    - Product Search Engine
#    - Delivery Route Planning

# 2. Provide 2–3 sentence justification for each

# 3. Implement one feature using Python:
#    - Include methods, comments, and docstrings
#    - Add test cases with output

# Generate clean and readable code
class ShoppingCart:
    """
    Shopping Cart implementation using a dictionary to store items and their quantities.
    """

    def __init__(self):
        """Initialize an empty shopping cart."""
        self.cart = {}

    def add_item(self, item, quantity=1):
        """Add an item to the cart with the specified quantity."""
        if item in self.cart:
            self.cart[item] += quantity
        else:
            self.cart[item] = quantity
        print(f"Added {quantity} of {item} to cart.")

    def remove_item(self, item, quantity=1):
        """Remove a specified quantity of an item from the cart."""
        if item in self.cart:
            if self.cart[item] > quantity:
                self.cart[item] -= quantity
                print(f"Removed {quantity} of {item} from cart.")
            elif self.cart[item] == quantity:
                del self.cart[item]
                print(f"Removed {item} from cart.")
            else:
                print(f"Cannot remove {quantity} of {item}. Only {self.cart[item]} in cart.")
        else:
            print(f"{item} not found in cart.")

    def view_cart(self):
        """Display the contents of the shopping cart."""
        if not self.cart:
            print("Your shopping cart is empty.")
            return
        print("Shopping Cart Contents:")
        for item, quantity in self.cart.items():
            print(f"{item}: {quantity}")
# -------- TESTING --------
cart = ShoppingCart()
cart.add_item("Laptop", 1)
cart.add_item("Headphones", 2)
cart.view_cart()
cart.remove_item("Headphones", 1)
cart.view_cart()
cart.remove_item("Laptop", 1)
cart.view_cart()
cart.remove_item("Headphones", 2)  # Attempt to remove more than in cart
cart.view_cart()