def view(cls):

    operacao = -1

    while operacao != 0:
        opcoes = "\n 0 - Sair \n 1 - Inserir \n 2 - Remover \n 3 - Listar\n:"

        operacao = int(input(opcoes))

        if operacao == 0:
            print("Até logo.")
        elif operacao == 1:
            element = int(input("Digite um número para ser inserido:"))
            cls.insert(element)

            print("Item inserido com sucesso !")
        elif operacao == 2:
            print('Item {} foi removido.'.format(cls.remove()))
        elif operacao == 3:
            print(cls.show())