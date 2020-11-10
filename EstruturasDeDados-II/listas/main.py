operacao = -1
while operacao != 0:

    title_option = '\nSelecione o exercício que deseja executar: '
    opcoes = '\n0 -Sair\n1 - Pilha\n2 - Fila\n3 - Deque\n'
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
