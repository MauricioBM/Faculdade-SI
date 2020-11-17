from .binary_tree import ArvoreBinariaDeBusca


def arvore_exemplo():
    values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32]
    tree = ArvoreBinariaDeBusca()
    for v in values:
        tree.insert(v)
    return tree


def test():
    bst = arvore_exemplo()
    bst.percurso_nivel()

    print("\n--------------------------------------")

    bst.arvore_eh_cheia()

    print("\n--------------------------------------")

    bst.invertTree()

    print("\n Árvore invertida: ")
    bst.percurso_nivel()
