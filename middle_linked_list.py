from typing import Optional


# Definimos a estrutura do nó (caso queira rodar de forma independente)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solutions:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ahead = head  # Esse será o nosso ponteiro RÁPIDO (Lebre)

        # Enquanto o ponteiro rápido puder dar 2 passos à frente
        while ahead and ahead.next:
            ahead = ahead.next.next  # Ponteiro RÁPIDO anda 2 passos
            head = head.next  # Ponteiro LENTO (head) anda 1 passo

        return head  # Quando a lebre chega ao fim, a tartaruga estará no meio!


# --- FUNÇÕES AUXILIARES PARA TESTAR ---

def criar_lista(valores: list[int]) -> Optional[ListNode]:
    if not valores: return None
    head = ListNode(valores[0])
    current = head
    for val in valores[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def imprimir_daqui_em_diante(head: Optional[ListNode]):
    valores = []
    current = head
    while current:
        valores.append(str(current.val))
        current = current.next
    print(" -> ".join(valores) if valores else "Lista Vazia")


# --- EXECUTANDO OS TESTES ---

validador = Solutions()

# Caso 1: Quantidade ÍMPAR de elementos (1 -> 2 -> 3 -> 4 -> 5)
# O meio exato é o 3.
lista1 = criar_lista([1, 2, 3, 4, 5])
meio1 = validador.middleNode(lista1)
print("Caso 1 (Ímpar) - Do meio até o fim:")
imprimir_daqui_em_diante(meio1)  # Deve mostrar: 3 -> 4 -> 5

# Caso 2: Quantidade PAR de elementos (1 -> 2 -> 3 -> 4 -> 5 -> 6)
# Existem dois elementos no meio (3 e 4). O LeetCode pede para retornar o segundo (4).
lista2 = criar_lista([1, 2, 3, 4, 5, 6])
meio2 = validador.middleNode(lista2)
print("\nCaso 2 (Par) - Do meio até o fim:")
imprimir_daqui_em_diante(meio2)  # Deve mostrar: 4 -> 5 -> 6