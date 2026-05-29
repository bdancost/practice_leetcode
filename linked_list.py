class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # Ponteiro para o próximo nó
        self.prev = None  # Ponteiro para o nó anterior


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Início da lista
        self.tail = None  # Fim da lista

    def add_to_front(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_to_end(self, value):
        new_node = Node(value)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_front(self):
        if not self.head:
            return None

        # CORREÇÃO: Pegamos o valor ANTES de mexer nos ponteiros ou dar return
        removed_value = self.head.value

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return removed_value

    def remove_from_end(self):
        if not self.tail:
            return None

        # CORREÇÃO: Pegamos o valor ANTES de mexer nos ponteiros ou dar return
        removed_value = self.tail.value

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return removed_value

    # Função auxiliar para conseguirmos enxergar a lista no terminal
    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.value))
            current = current.next
        print(" <-> ".join(elements) if elements else "Lista Vazia")


# --- CÓDIGO PARA EXECUTAR E TESTAR ---

minha_lista = DoublyLinkedList()

print("--- Adicionando elementos ---")
minha_lista.add_to_end(20)  # Lista: 20
minha_lista.add_to_end(30)  # Lista: 20 <-> 30
minha_lista.add_to_front(10)  # Lista: 10 <-> 20 <-> 30
minha_lista.display()  # Deve mostrar: 10 <-> 20 <-> 30

print("\n--- Removendo do início ---")
removido_inicio = minha_lista.remove_from_front()
print(f"Elemento removido: {removido_inicio}")
minha_lista.display()  # Deve mostrar: 20 <-> 30

print("\n--- Removendo do fim ---")
removido_fim = minha_lista.remove_from_end()
print(f"Elemento removido: {removido_fim}")
minha_lista.display()  # Deve mostrar: 20