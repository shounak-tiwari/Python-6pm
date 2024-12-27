from abc import ABC, abstractmethod

class Implementation(ABC):
    @abstractmethod
    def methods(self, x):
        return x**2  # Abstract methods should not have an implementation

# class Child(Implementation):
#     def methods(self, x):
#         return x**2  # Providing concrete implementation

#     def show(self):
#         print('This is child class')

# # Instantiate the child class
# child_instance = Child()
# print(child_instance.methods(10))  # Output: 100
# child_instance.show()


x = Implementation()


result = x.methods(10)
