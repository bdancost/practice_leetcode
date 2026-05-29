from typing import Optional


# CORREÇÃO: Definimos a estrutura real do nó
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solutions:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None
        current = head

        while current:
            next_node = current.next  # 1. Salva o resto da lista original
            current.next = new_list  # 2. Inverte o ponteiro (aponta para trás)
            new_list = current  # 3. Move a nova lista para frente
            current = next_node  # 4. Avança na lista original

        return new_list


# --- FUNÇÕES AUXILIARES PARA TESTAR ---

def criar_lista_encadeada(valores: list[int]) -> Optional[ListNode]:
    """Transforma uma lista comum do Python em uma Lista Encadeada"""
    if not valores:
        return None
    head = ListNode(valores[0])
    current = head
    for val in valores[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def imprimir_lista(head: Optional[ListNode]):
    """Imprime a lista de forma visual no terminal"""
    valores = []
    current = head
    while current:
        valores.append(str(current.val))
        current = current.next
    print(" -> ".join(valores) if valores else "Lista Vazia")


# --- EXECUTANDO O TESTE ---

# 1. Criamos a lista: 1 -> 2 -> 3 -> 4 -> 5
lista_original = criar_lista_encadeada([1, 2, 3, 4, 5])
print("Lista Original:")
imprimir_lista(lista_original)

# 2. Instanciamos a solução e invertemos
validador = Solutions()
lista_invertida = validador.reverseList(lista_original)

print("\nLista Invertida:")
imprimir_lista(lista_invertida)  # Deve mostrar: 5 -> 4 -> 3 -> 2 -> 1