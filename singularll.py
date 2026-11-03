
import ast


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

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
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at(self, position, data):
        if position < 0 or position > self.length():
            raise IndexError("Invalid position")

        if position == 0:
            self.prepend(data)
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

        if self.head.data == value:
            self.head = self.head.next
            return True

        current = self.head

        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return True

            current = current.next

        return False

    def delete_at(self, position):
        if position < 0 or position >= self.length():
            raise IndexError("Invalid position")

        if position == 0:
            self.head = self.head.next
            return

        current = self.head

        for _ in range(position - 1):
            current = current.next

        current.next = current.next.next

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
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return

        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

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


def get_data():
    value = input("Enter data: ")

    try:
        return ast.literal_eval(value)
    except (ValueError, SyntaxError):
        return value


def main():
    sll = SinglyLinkedList()

    while True:
        print("\n--- SINGLY LINKED LIST ---")
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
                sll.append(get_data())
                print("Element inserted")

            elif choice == "2":
                sll.prepend(get_data())
                print("Element inserted")

            elif choice == "3":
                position = int(input("Enter position (0-based): "))
                data = get_data()
                sll.insert_at(position, data)
                print("Element inserted")

            elif choice == "4":
                value = get_data()
                if sll.delete_value(value):
                    print("Element deleted")
                else:
                    print("Element not found")

            elif choice == "5":
                position = int(input("Enter position (0-based): "))
                sll.delete_at(position)
                print("Element deleted")

            elif choice == "6":
                value = get_data()
                result = sll.search(value)
                print("Found at index:", result) if result != -1 else print("Not found")

            elif choice == "7":
                sll.display()

            elif choice == "8":
                print("Length:", sll.length())

            elif choice == "9":
                sll.reverse()
                print("Linked List reversed")

            elif choice == "10":
                print("Empty" if sll.is_empty() else "Not empty")

            elif choice == "11":
                print(sll.to_list())

            elif choice == "12":
                sll.clear()
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
