
import ast


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def length(self):
        if self.head is None:
            return 0

        count = 0
        current = self.head

        while True:
            count += 1
            current = current.next

            if current == self.head:
                break

        return count

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = self.head
            return

        new_node.next = self.head
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = self.head
            return

        new_node.next = self.head
        self.tail.next = new_node
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

        for _ in range(position - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def delete_value(self, value):
        if self.head is None:
            return False

        current = self.head
        previous = self.tail

        while True:
            if current.data == value:

                if self.head == self.tail:
                    self.head = self.tail = None
                    return True

                previous.next = current.next

                if current == self.head:
                    self.head = current.next

                if current == self.tail:
                    self.tail = previous

                self.tail.next = self.head
                return True

            previous = current
            current = current.next

            if current == self.head:
                break

        return False

    def delete_at(self, position):
        if position < 0 or position >= self.length():
            raise IndexError("Invalid position")

        if position == 0:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
            return

        current = self.head

        for _ in range(position - 1):
            current = current.next

        node_to_delete = current.next
        current.next = node_to_delete.next

        if node_to_delete == self.tail:
            self.tail = current

        self.tail.next = self.head

    def search(self, value):
        if self.head is None:
            return -1

        current = self.head
        index = 0

        while True:
            if current.data == value:
                return index

            current = current.next
            index += 1

            if current == self.head:
                break

        return -1

    def reverse(self):
        if self.head is None or self.head == self.tail:
            return

        previous = self.tail
        current = self.head

        while True:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

            if current == self.head:
                break

        self.tail = self.head
        self.head = previous
        self.tail.next = self.head

    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return

        current = self.head

        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.head:
                break

        print("(back to head)")

    def to_list(self):
        result = []

        if self.head is None:
            return result

        current = self.head

        while True:
            result.append(current.data)
            current = current.next

            if current == self.head:
                break

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
    cll = CircularLinkedList()

    while True:
        print("\n--- CIRCULAR LINKED LIST ---")
        print("1. Insert at end")
        print("2. Insert at beginning")
        print("3. Insert at position")
        print("4. Delete by value")
        print("5. Delete at position")
        print("6. Search")
        print("7. Display")
        print("8. Length")
        print("9. Reverse")
        print("10. Check if empty")
        print("11. Convert to Python list")
        print("12. Clear")
        print("13. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                cll.append(get_data())
                print("Element inserted")

            elif choice == "2":
                cll.prepend(get_data())
                print("Element inserted")

            elif choice == "3":
                position = int(input("Enter position (0-based): "))
                data = get_data()
                cll.insert_at(position, data)
                print("Element inserted")

            elif choice == "4":
                value = get_data()
                if cll.delete_value(value):
                    print("Element deleted")
                else:
                    print("Element not found")

            elif choice == "5":
                position = int(input("Enter position (0-based): "))
                cll.delete_at(position)
                print("Element deleted")

            elif choice == "6":
                value = get_data()
                result = cll.search(value)
                print("Found at index:", result) if result != -1 else print("Not found")

            elif choice == "7":
                cll.display()

            elif choice == "8":
                print("Length:", cll.length())

            elif choice == "9":
                cll.reverse()
                print("Linked List reversed")

            elif choice == "10":
                print("Empty" if cll.is_empty() else "Not empty")

            elif choice == "11":
                print(cll.to_list())

            elif choice == "12":
                cll.clear()
                print("Linked List cleared")

            elif choice == "13":
                print("Exiting...")
                break

            else:
                print("Invalid choice")

        except (ValueError, IndexError) as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
