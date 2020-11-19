from .Fila import Queue

ROOT = "root"


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class ArvoreBinariaDeBusca:

    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def percurso_pos_ordem(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.percurso_pos_ordem(node.left)
        if node.right:
            self.percurso_pos_ordem(node.right)
        print(node)

    def percurso_simetrico(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.percurso_simetrico(node.left)
        print(node, end=' >> ')
        if node.right:
            self.percurso_simetrico(node.right)

    def percurso_nivel(self, node=ROOT):
        if node == ROOT:
            node = self.root

        queue = Queue()
        queue.push(node)
        while len(queue):
            node = queue.pop()
            if node.left:
                queue.push(node.left)
            if node.right:
                queue.push(node.right)
            print(node, end=" ")

    def mostrar_altura(self, node=None):
        if node is None:
            node = self.root
        alt_left = 0
        alt_right = 0
        if node.left:
            alt_left = self.mostrar_altura(node.left)
        if node.right:
            alt_right = self.mostrar_altura(node.right)
        if alt_right > alt_left:
            return alt_right + 1
        return alt_left + 1

    def contar_folhas(self, node=ROOT):

        if node == ROOT:
            node = self.root

        queue = Queue()

        cont = 0
        queue.push(node)

        while len(queue):
            node = queue.pop()

            if node.left:
                queue.push(node.left)
            if node.right:
                queue.push(node.right)
            if node.left is None and node.right is None:
                cont += 1

        return cont

    def arvore_eh_cheia(self, node=ROOT):

        if node == ROOT:
            node = self.root

        altura = self.mostrar_altura()
        qtdNodes_ultNivel = 2 ** (altura - 1)

        qtdFolhas = self.contar_folhas()

        if qtdNodes_ultNivel == qtdFolhas:
            return print("Esta árvore binária é cheia !")
        else:
            return print("Esta árvore binária não é cheia !")

    def invertTree(self, node=ROOT):

        if node == ROOT:
            node = self.root

        queue = Queue()
        queue.push(node)

        while len(queue):
            node = queue.pop()

            if node:
                node.left, node.right = node.right, node.left
                queue.push(node.left)
                queue.push(node.right)

        return self.root

    def insert(self, value):

        pai = None
        aux = self.root

        while aux:
            pai = aux

            if value < aux.data:
                aux = aux.left
            else:
                aux = aux.right
        if pai is None:
            self.root = Node(value)
        elif value < pai.data:
            pai.left = Node(value)
        else:
            pai.right = Node(value)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node=0):

        if node == 0:
            node = self.root
        if node is None:
            return ArvoreBinariaDeBusca()
        if value < node.data:
            return self.search(value, node.left)
        return self.search(value, node.right)

    def min(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.left:
            node = node.left
        return node.data

    def max(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.right:
            node = node.right
        return node.data

    def remove(self, value, node=ROOT):
        # Se for o valor padrão, executa a partir da raiz
        if node == ROOT:
            node = self.root
        # Se desceu até um ramo nulo, não há nada a fazer
        if node is None:
            return node
        # Se o valor for menor, desce à esquerda
        if value < node.data:
            node.left = self.remove(value, node.left)
        # Se o valor for maior, desce à direita
        elif value > node.data:
            node.right = self.remove(value, node.right)
        # Se não for nem menor, nem maior, encontramos! Então o valor procurado é removido
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Substituto é o sucessor do valor a ser removido
                substituto = self.min(node.right)
                # Ao invés de trocar a posição dos nós, troca o valor
                node.data = substituto
                # Depois, remove o substituto da subárvore à direita
                node.right = self.remove(substituto, node.right)

        return node
