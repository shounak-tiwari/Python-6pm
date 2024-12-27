from abc import ABC,abstractmethod

class implementation(ABC):
    # @abstractclassmethod
    @abstractmethod
    def methods(self,x):
        return x**2


class child(implementation):
    def show(self):
        print('this is child class')


x = implementation()

print(x.methods(10))
