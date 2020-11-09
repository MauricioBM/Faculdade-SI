operacao = -1
while operacao != 0:

    title_option = 'Selecione o exercício que deseja executar: '
    opcoes = '\n0 -Sair\n1 - Pilhas\n2- Fila \n'
    operacao = int(input('{} \n {} :'.format(title_option, opcoes)))

    if operacao == 0:
        print('Até mais.')

    elif option == 1:
        from stack.views import view
        view()
    elif option == 2:
        from queue.views import view
        view()