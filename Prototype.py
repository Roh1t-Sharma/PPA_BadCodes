import copy
from abc import ABC, abstractmethod

class Document(ABC):
    def __init__(self, title, content):
        self.title = title
        self.content = content

    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def display(self):
        pass

class Report(Document):
    def __init__(self, title, content, author):
        super().__init__(title, content)
        self.author = author

    def clone(self):
        return copy.deepcopy(self)

    def display(self):
        print(f"Report Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Content: {self.content}")

class Letter(Document):
    def __init__(self, title, content, recipient):
        super().__init__(title, content)
        self.recipient = recipient

    def clone(self):
        return copy.deepcopy(self)

    def display(self):
        print(f"Letter Title: {self.title}")
        print(f"Recipient: {self.recipient}")
        print(f"Content: {self.content}")

class Invoice(Document):
    def __init__(self, title, content, amount):
        super().__init__(title, content)
        self.amount = amount

    def clone(self):
        return copy.deepcopy(self)

    def display(self):
        print(f"Invoice Title: {self.title}")
        print(f"Amount: ${self.amount}")
        print(f"Content: {self.content}")

documents = []

def add_document():
    doc_type = input("Enter document type (Report/Letter/Invoice): ").strip().lower()
    title = input("Enter document title: ")
    content = input("Enter document content: ")

    if doc_type == "report":
        author = input("Enter author: ")
        new_document = Report(title, content, author)
    elif doc_type == "letter":
        recipient = input("Enter recipient: ")
        new_document = Letter(title, content, recipient)
    elif doc_type == "invoice":
        amount = float(input("Enter amount: "))
        new_document = Invoice(title, content, amount)
    else:
        print("Invalid document type.")
        return

    documents.append(new_document)
    print("\nDocument added successfully.")

def clone_document():
    if not documents:
        print("\nNo documents found to clone.")
        return

    print("\nDocuments:")
    for index, doc in enumerate(documents):
        print(f"{index + 1}. {doc.title} ({type(doc).__name__})")

    doc_index = int(input("\nEnter the number of the document to clone: ")) - 1

    if 0 <= doc_index < len(documents):
        cloned_document = documents[doc_index].clone()
        documents.append(cloned_document)
        print("\nDocument cloned successfully.")
    else:
        print("\nInvalid document number.")

def show_documents():
    if not documents:
        print("\nNo documents found.")
    else:
        print("\nDocuments:")
        for doc in documents:
            print("\n--------------------------------")
            doc.display()
            print("--------------------------------")

while True:
    print("\nDocument Management System")
    print("1. Add Document")
    print("2. Clone Document")
    print("3. Show Documents")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_document()
    elif choice == "2":
        clone_document()
    elif choice == "3":
        show_documents()
    elif choice == "4":
        print("\nExiting...")
        break
    else:
        print("\nInvalid choice. Please try again.")
