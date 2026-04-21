'''# Build a Smart Contact Manager using two approaches:Array (Python list),Linked List
#Implement add_contact(name, phone),Implement search_contact(name),Implement delete_contact(name)
# For Linked List:Create a Node class,Use dynamic memory (next pointer)
#Both implementations support all operations correctly,Return "Not Found" if contact does not exist
#Compare array vs linked list based on:insertion efficiency and deletion efficiency
# Generate clean, readable Python code with example test cases
# -------- ARRAY IMPLEMENTATION --------
class ContactManagerArray:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        self.contacts.append({"name": name, "phone": phone})
        print("Contact added")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact["name"] == name:
                print("Found:", contact["name"], "-", contact["phone"])
                return
        print("Contact not found")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact["name"] == name:
                self.contacts.remove(contact)
                print("Contact deleted")
                return
        print("Contact not found")

    def display_contacts(self):
        print("\nArray Contacts:")
        for contact in self.contacts:
            print(contact["name"], "-", contact["phone"])


# -------- LINKED LIST IMPLEMENTATION --------
class Node:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.next = None


class ContactManagerLinkedList:
    def __init__(self):
        self.head = None

    def add_contact(self, name, phone):
        new_node = Node(name, phone)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print("Contact added")

    def search_contact(self, name):
        temp = self.head
        while temp:
            if temp.name == name:
                print("Found:", temp.name, "-", temp.phone)
                return
            temp = temp.next
        print("Contact not found")

    def delete_contact(self, name):
        temp = self.head
        prev = None
        while temp:
            if temp.name == name:
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                print("Contact deleted")
                return
            prev = temp
            temp = temp.next
        print("Contact not found")

    def display_contacts(self):
        print("\nLinked List Contacts:")
        temp = self.head
        while temp:
            print(temp.name, "-", temp.phone)
            temp = temp.next


# -------- TESTING --------
print("ARRAY IMPLEMENTATION")
array_manager = ContactManagerArray()
array_manager.add_contact("Rahul", "9876543210")
array_manager.add_contact("Anita", "9123456780")
array_manager.display_contacts()
array_manager.search_contact("Rahul")
array_manager.delete_contact("Rahul")
array_manager.display_contacts()

print("\nLINKED LIST IMPLEMENTATION")
linked_manager = ContactManagerLinkedList()
linked_manager.add_contact("Rahul", "9876543210")
linked_manager.add_contact("Anita", "9123456780")
linked_manager.display_contacts()
linked_manager.search_contact("Anita")
linked_manager.delete_contact("Rahul")
linked_manager.display_contacts()'''

'''# Generate a python code to Build a Library Book Request System using:Queue (FIFO),Priority Queue (faculty > student)
#Implement enqueue() and dequeue() methods,Queue should process requests in FIFO order,Priority Queue should prioritize faculty over students
#Each request should include name and type (student/faculty),Test with mixed requests,Print processed order
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, name, user_type):
        self.queue.append({"name": name, "type": user_type})
        print(f"Request added: {name} ({user_type})")

    def dequeue(self):
        if not self.queue:
            print("No requests to process")
            return None
        request = self.queue.pop(0)
        print(f"Processing request: {request['name']} ({request['type']})")
        return request
    
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, name, user_type):
        self.queue.append({"name": name, "type": user_type})
        print(f"Request added: {name} ({user_type})")

    def dequeue(self):
        if not self.queue:
            print("No requests to process")
            return None
        # Prioritize faculty over students
        for i, request in enumerate(self.queue):
            if request["type"] == "faculty":
                print(f"Processing request: {request['name']} ({request['type']})")
                return self.queue.pop(i)
        # If no faculty requests, process the first student request
        request = self.queue.pop(0)
        print(f"Processing request: {request['name']} ({request['type']})")
        return request
# Testing the Queue and PriorityQueue
print("QUEUE (FIFO) IMPLEMENTATION")
fifo_queue = Queue()
fifo_queue.enqueue("Alice", "student")
fifo_queue.enqueue("Bob", "faculty")
fifo_queue.enqueue("Charlie", "student")
fifo_queue.dequeue()
fifo_queue.dequeue()
fifo_queue.dequeue()
print("\nPRIORITY QUEUE (Faculty > Student) IMPLEMENTATION")
priority_queue = PriorityQueue()
priority_queue.enqueue("Alice", "student")
priority_queue.enqueue("Bob", "faculty")
priority_queue.enqueue("Charlie", "student")
priority_queue.dequeue()
priority_queue.dequeue()
priority_queue.dequeue()'''

'''#Generate a python code to build  an emergency Help Desk system using Stack (LIFO)
#Implement stack operations:push(ticket), pop(), peek(),Add methods to check,is_empty(),is_full() (optional with size limit)
#Simulate at least 5 tickets being raised and resolved,Show LIFO behavior clearly,Print actions while pushing and popping
class HelpDeskStack:
    def __init__(self, size_limit=10):
        self.stack = []
        self.size_limit = size_limit

    def push(self, ticket):
        if len(self.stack) >= self.size_limit:
            print("Help Desk is full. Cannot add more tickets.")
            return
        self.stack.append(ticket)
        print(f"Ticket added: {ticket}")

    def pop(self):
        if self.is_empty():
            print("No tickets to resolve.")
            return None
        ticket = self.stack.pop()
        print(f"Resolving ticket: {ticket}")
        return ticket

    def peek(self):
        if self.is_empty():
            print("No tickets in the stack.")
            return None
        print(f"Next ticket to resolve: {self.stack[-1]}")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) >= self.size_limit
# Simulating the Help Desk system
help_desk = HelpDeskStack(size_limit=5) 
help_desk.push("Ticket 1: Computer not working")
help_desk.push("Ticket 2: Internet connectivity issue")
help_desk.push("Ticket 3: Software installation request")
help_desk.push("Ticket 4: Printer not responding")
help_desk.push("Ticket 5: Email access problem")
help_desk.push("Ticket 6: Cannot add this ticket, stack is full")  # This should show a message that the stack is full
help_desk.peek()  # Should show the last ticket added (Ticket 5)
help_desk.pop()  # Resolves Ticket 5
help_desk.pop()  # Resolves Ticket 4
help_desk.pop()  # Resolves Ticket 3
help_desk.pop()  # Resolves Ticket 2
help_desk.pop()  # Resolves Ticket 1
help_desk.pop()  # This should show a message that there are no tickets to resolve'''

'''#Generate a python code to build a Hash Table with collision handling using chaining
# insert(key, value),search(key),delete(key)
#Use chaining (list inside each bucket) to handle collisions,Add comments for clarity,Test with sample inputs
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Create a list of empty lists for chaining

    def _hash(self, key):
        return hash(key) % self.size  # Simple hash function to determine bucket index

    def insert(self, key, value):
        index = self._hash(key)
        # Check if the key already exists in the bucket
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # Update existing key
                print(f"Updated key: {key} with value: {value}")
                return
        # If key does not exist, add new key-value pair
        self.table[index].append((key, value))
        print(f"Inserted key: {key} with value: {value}")

    def search(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                print(f"Found key: {key} with value: {v}")
                return v
        print(f"Key: {key} not found")
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]  # Remove the key-value pair from the bucket
                print(f"Deleted key: {key}")
                return
        print(f"Key: {key} not found for deletion")
# Testing the Hash Table with chaining
hash_table = HashTable(size=5)  # Create a hash table with 5 buckets
hash_table.insert("name", "Alice")
hash_table.insert("age", 30)
hash_table.insert("city", "New York")
hash_table.search("name")  # Should find Alice
hash_table.search("age")   # Should find 30
hash_table.search("country")  # Should not find this key
hash_table.delete("age")  # Should delete the key "age"
hash_table.search("age")   # Should not find "age" after deletion'''

# Generate a python code to design a Campus Resource Management System
# 1.Map features to suitable data structures:
# Student Attendance Tracking,Event Registration System,Library Book Borrowing,Bus Scheduling System,Cafeteria Order Queue
# 2.Provide justification (2-3 sentences each)
# 3.Implement one feature using Python
# 1. Student Attendance Tracking: Use a Hash Table to store student IDs and their attendance records. This allows for O(1) average time complexity for lookups, making it efficient for tracking attendance in real-time.
# 2. Event Registration System: Use a Queue to manage event registrations. This ensures that registrations are processed in the order they were received, which is fair and easy to manage for event organizers.
# 3. Library Book Borrowing: Use a Linked List to manage the list of borrowed books. This allows for dynamic memory allocation and easy insertion/deletion of book records as students borrow and return books.
# 4. Bus Scheduling System: Use a Priority Queue to manage bus schedules. This allows for prioritizing certain routes or times based on demand, ensuring efficient resource allocation for the campus transportation system.
# 5. Cafeteria Order Queue: Use a Stack to manage cafeteria orders. This allows for a LIFO approach where the most recent orders are processed first, which can be useful during peak hours to ensure quick service for customers.
# Implementing the Event Registration System using a Queue
class EventRegistrationQueue:
    def __init__(self):
        self.queue = []

    def register(self, name):
        self.queue.append(name)
        print(f"{name} has registered for the event.")

    def process_registration(self):
        if not self.queue:
            print("No registrations to process.")
            return None
        name = self.queue.pop(0)
        print(f"Processing registration for {name}.")
        return name     
# Testing the Event Registration System
event_queue = EventRegistrationQueue()
event_queue.register("Alice")
event_queue.register("Bob")
event_queue.register("Charlie")
event_queue.process_registration()  # Should process Alice first    
event_queue.process_registration()  # Should process Bob next
event_queue.process_registration()  # Should process Charlie last
event_queue.process_registration()  # Should show no registrations to process