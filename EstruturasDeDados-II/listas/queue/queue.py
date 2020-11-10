from base.baselist import ListaBase
from base.node import Node

class Queue(ListaBase):

    def insert(self, element):

        node = Node(element)

        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self.size = self.size + 1
