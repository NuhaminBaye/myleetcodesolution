from threading import Condition

class Foo:
    def __init__(self):
        self.condition = Condition()
        self.order = 0  # To track the order of method calls

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # Print "first"
        printFirst()
        with self.condition:
            self.order = 1  # Update the order after first is called
            self.condition.notify_all()  # Notify other threads

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.condition:
            while self.order < 1:  # Wait until first() is called
                self.condition.wait()
            # Print "second"
            printSecond()
            self.order = 2  # Update the order after second is called
            self.condition.notify_all()  # Notify other threads

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.condition:
            while self.order < 2:  # Wait until second() is called
                self.condition.wait()
            # Print "third"
            printThird()

# Example usage with threading
import threading

def print_first():
    print("first", end="")

def print_second():
    print("second", end="")

def print_third():
    print("third", end="")

# Create an instance of Foo
foo = Foo()

# Create threads
thread1 = threading.Thread(target=foo.first, args=(print_first,))
thread2 = threading.Thread(target=foo.second, args=(print_second,))
thread3 = threading.Thread(target=foo.third, args=(print_third,))

# Start threads
thread1.start()
thread2.start()
thread3.start()

# Wait for threads to finish
thread1.join()
thread2.join()
thread3.join()