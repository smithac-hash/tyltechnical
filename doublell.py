
import ast


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def length(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at(self, position, data):
        if position < 0 or position > self.length():
            raise IndexError("Invalid position")

        if position == 0:
            self.prepend(data)
            return

        if position == self.length():
            self.append(data)
            return

        new_node = Node(data)
        current = self.head

        for _ in range(position):
            current = current.next

        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node

    def delete_value(self, value):
        current = self.head

        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                return True

            current = current.next

        return False

    def delete_at(self, position):
        if position < 0 or position >= self.length():
            raise IndexError("Invalid position")

        current = self.head

        for _ in range(position):
            current = current.next

        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next

        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev

    def search(self, value):
        current = self.head
        index = 0

        while current:
            if current.data == value:
                return index

            current = current.next
            index += 1

        return -1

    def reverse(self):
        current = self.head

        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev

        self.head, self.tail = self.tail, self.head

    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return

        current = self.head

        while current:
            print(current.data, end=" <-> ")
            current = current.next

        print("None")

    def display_reverse(self):
        if self.tail is None:
            print("Linked List is empty")
            return

        current = self.tail

        while current:
            print(current.data, end=" <-> ")
            current = current.prev

        print("None")

    def to_list(self):
        result = []
        current = self.head

        while current:
            result.append(current.data)
            current = current.next

        return result

    def clear(self):
        self.head = None
        self.tail = None


def get_data():
    value = input("Enter data: ")

    try:
        return ast.literal_eval(value)
    except (ValueError, SyntaxError):
        return value


def main():
    dll = DoublyLinkedList()

    while True:
        print("\n--- DOUBLY LINKED LIST ---")
        print("1. Insert at end")
        print("2. Insert at beginning")
        print("3. Insert at position")
        print("4. Delete by value")
        print("5. Delete at position")
        print("6. Search")
        print("7. Display forward")
        print("8. Display backward")
        print("9. Length")
        print("10. Reverse")
        print("11. Check if empty")
        print("12. Convert to Python list")
        print("13. Clear")
        print("14. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                dll.append(get_data())
                print("Element inserted")

            elif choice == "2":
                dll.prepend(get_data())
                print("Element inserted")

            elif choice == "3":
                position = int(input("Enter position (0-based): "))
                data = get_data()
                dll.insert_at(position, data)
                print("Element inserted")

            elif choice == "4":
                value = get_data()
                if dll.delete_value(value):
                    print("Element deleted")
                else:
                    print("Element not found")

            elif choice == "5":
                position = int(input("Enter position (0-based): "))
                dll.delete_at(position)
                print("Element deleted")

            elif choice == "6":
                value = get_data()
                result = dll.search(value)
                print("Found at index:", result) if result != -1 else print("Not found")

            elif choice == "7":
                dll.display()

            elif choice == "8":
                dll.display_reverse()

            elif choice == "9":
                print("Length:", dll.length())

            elif choice == "10":
                dll.reverse()
                print("Linked List reversed")

            elif choice == "11":
                print("Empty" if dll.is_empty() else "Not empty")

            elif choice == "12":
                print(dll.to_list())

            elif choice == "13":
                dll.clear()
                print("Linked List cleared")

            elif choice == "14":
                print("Exiting...")
                break

            else:
                print("Invalid choice")

        except (ValueError, IndexError) as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
