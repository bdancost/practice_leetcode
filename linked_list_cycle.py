from typing import Optional


# Definimos a estrutura do nó de forma independente
class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # CORREÇÃO: Mudamos de 'show' para 'slow' para fazer sentido com o algoritmo
        slow = head
        fast = head

        # Enquanto a lebre (fast) puder avançar 2 passos
        while fast and fast.next:
            slow = slow.next  # Tartaruga (slow) anda 1 passo
            fast = fast.next.next  # Lebre (fast) anda 2 passos

            # Se eles se encontrarem no mesmo nó da memória, há um ciclo!
            if slow == fast:
                return True

        return False


# --- TEST CODE ---
validator = Solution()

# CASO 1: Criando uma lista COM ciclo infinito (1 -> 2 -> 3 -> 4 -> aponta de volta para o 2)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # <-- Aqui criamos o ciclo! O 4 aponta de volta para o 2.

has_cycle_1 = validator.hasCycle(node1)
print(f"Test 1 - Does the linked list have a cycle? {has_cycle_1}")  # Deve exibir: True

# CASO 2: Criando uma lista comum SEM ciclo (10 -> 20)
node_a = ListNode(10)
node_b = ListNode(20)
node_a.next = node_b

has_cycle_2 = validator.hasCycle(node_a)
print(f"Test 2 - Does the linked list have a cycle? {has_cycle_2}")  # Deve exibir: False