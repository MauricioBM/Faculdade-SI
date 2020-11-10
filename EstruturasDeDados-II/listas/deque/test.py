from .deque import DequeDinamico

def test():

    deque = DequeDinamico()

    deque.inserir_direita("Mendonça")
    deque.inserir_esquerda("Barreto")
    deque.inserir_esquerda("Maurício")

    print('\n')
    print(deque)

    print('\n')
    print(len(deque))
