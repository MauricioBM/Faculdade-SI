operacao = -1
while operacao != 0:

    title_option = '\n\nSelecione o exercício que deseja executar: '
    opcoes = '\n0 -Sair\n1 - Pilha\n2 - Fila\n3 - Deque\n4 - Árvore Binária\n5 - Árvore AVL\n'
    operacao = int(input('{} \n {} :'.format(title_option, opcoes)))

    if operacao == 0:
        print('Até mais.')

    elif operacao == 1:
        from stack.views import view

        view()
    elif operacao == 2:
        from queue.views import view

        view()
    elif operacao == 3:
        from deque.test import test

        test()
    elif operacao == 4:
        from binary_tree.test import test

        test()
    elif operacao == 5:
        from treeAVL.treeAVL2 import AVL_Tree

        AVL_Tree()
