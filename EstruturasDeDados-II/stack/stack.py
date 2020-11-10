from base.baselist import ListaBase
from base.node import Node

class Stack(ListaBase):

    def insert(self, element):

        node = Node(element)
        node.next = self.first
        self.first = node
        self.size = self.size + 1