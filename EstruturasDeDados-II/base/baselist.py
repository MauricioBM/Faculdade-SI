from abc import ABCMeta, abstractmethod


class ListaBase(object):
    __metaclass__ = ABCMeta

    first = None
    last = None
    size = 0
    items = []

    def is_empty(self):
        return self.size == 0

    @abstractmethod
    def insert(self, element=None):
        pass

    def __len__(self):
        return self.size

    def items_is_empty(self):
        return self.__len__() == 0

    def remove(self):
        if self.is_empty():
            raise Exception("A lista está vazia !")
        else:
            element = self.first
            data = element.data
            self.first = element.next
            self.size = self.size - 1

            del element
            return data

    def swap(self, data1, data2):

        aux = data1
        data1 = data2
        data2 = aux

        return data1, data2

    def bubble_sort(self):

        self.items = self.show()

        for i in range(self.size - 1):
            j = i + 1
            while j < self.size:
                if self.items[i] > self.items[j]:
                    self.items[i], self.items[j] = self.swap(self.items[i], self.items[j])
                j = j + 1
            i = i + 1

        return self.items

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
