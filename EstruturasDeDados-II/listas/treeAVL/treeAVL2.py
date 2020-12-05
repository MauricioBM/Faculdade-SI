from .Fila import Queue

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree(object):

    def insert(self, root, key):

        if not root:
            return Node(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Atualizar a altura do node anterior
        root.height = 1 + max(self.getAltura(root.left), self.getAltura(root.right))

        # Definir o valor/fator de balanceamento da arvore
        balanco = self.getBalanceamento(root)

        # Caso a árvore ou sub-arvore esteja desbalanceada, entra no if's e
        # passa pelas condições de balanceamento e rotação

        # Caso 1 - Simples Esquerda
        if balanco > 1 and key < root.left.val:
            return self.rightRotate(root)

        # Caso 2 - Simples Direita
        if balanco < -1 and key > root.right.val:
            return self.leftRotate(root)

        # Caso 3 - Dupla Direita
        if balanco > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Caso 4 - Dupla Esquerda
        if balanco < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    # Remoção recursiva para excluir um nó,
    # através de uma entrada, de uma sub-arvore,
    # da arvore em que está contida. Retorna a
    # raiz da sub-arvore modificada
    def delete(self, root, key):

        if not root:
            return root

        elif key < root.val:
            root.left = self.delete(root.left, key)

        elif key > root.val:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getNodeComMenorValor(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)

        if root is None:
            return root

        # Atualizar a altura do node anterior
        root.height = 1 + max(self.getAltura(root.left), self.getAltura(root.right))

        # Definir o valor/fator de balanceamento da arvore
        balanco = self.getBalanceamento(root)

        # Caso a árvore ou sub-arvore esteja desbalanceada, entra nos if's e
        # passa pelas condições de balanceamento e rotação

        # Caso 1 - Simples Esquerda
        if balanco > 1 and self.getBalanceamento(root.left) >= 0:
            return self.rightRotate(root)

        # Caso 2 - Simples Direita
        if balanco < -1 and self.getBalanceamento(root.right) <= 0:
            return self.leftRotate(root)

        # Caso 3 - Dupla Direita
        if balanco > 1 and self.getBalanceamento(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Caso 4 - Dupla Esquerda
        if balanco < -1 and self.getBalanceamento(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):

        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.getAltura(z.left), self.getAltura(z.right))

        y.height = 1 + max(self.getAltura(y.left), self.getAltura(y.right))

        # Return the new root
        return y

    def rightRotate(self, z):

        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.getAltura(z.left), self.getAltura(z.right))

        y.height = 1 + max(self.getAltura(y.left), self.getAltura(y.right))

        # Return the new root
        return y

    def getAltura(self, root):
        if not root:
            return 0

        return root.height

    def getBalanceamento(self, root):
        if not root:
            return 0

        return self.getAltura(root.left) - self.getAltura(root.right)

    def getNodeComMenorValor(self, root):
        if root is None or root.left is None:
            return root

        return self.getNodeComMenorValor(root.left)

    def preOrder(self, root):

        if not root:
            return

        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def percurso_nivel(self, root):
        if root is None:
            return

        queue = Queue()
        queue.push(root)

        while len(queue) > 0:
            node = queue.pop()

            if node.left is not None:
                queue.push(node.left)

            if node.right is not None:
                queue.push(node.right)

            print(node.val, end=" ")


avl = AVL_Tree()
root = None
nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]

for num in nums:
    root = avl.insert(root, num)

print("Percurso em Largura (por nivel) depois da inserção -")
avl.percurso_nivel(root)
print()

# Delete
key = 10
root = avl.delete(root, key)

# Preorder Traversal
print("Percurso em Largura (por nivel) depois da remoção -")
avl.percurso_nivel(root)
print()
