from abc import ABCMeta, abstractmethod

class ListaBase(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
        self.items = []

    def is_empty(self):
        return self._size == 0

    @abstractmethod
    def insert(self, element = None):
        pass

    def __len__(self):
        return self._size

    def items_is_empty(self):
        return self.__len__() == 0

    def remove(self):
        if self.is_empty():
            raise Exception("A lista está vazia !")
        else:
            element = self.first
            data = element.data
            self.first = element.next
            self._size = self._size - 1

            del element
            return data

    def show(self):
        self.items = []

        if self.is_empty():
            raise Exception("A lista está vazia !")
        else:
            element = self.first

            while element is not None:
                data = element.data
                element = element.next
                self.items.append(data)

                return self.items