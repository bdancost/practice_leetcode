class Solutions:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))

    # --- CÓDIGO PARA EXECUTAR E TESTAR ---

validador = Solutions()

# Exemplo 1
lista_A = [1, 2, 2, 1]
lista_B = [2, 2, 3]
resultado1 = validador.intersection(lista_A, lista_B)
print(f"Interseção 1: {resultado1}")  # Deve retornar [2]

# Exemplo 2
lista_X = [4, 9, 5]
lista_Y = [9, 4, 9, 8, 4]
resultado2 = validador.intersection(lista_X, lista_Y)
print(f"Interseção 2: {resultado2}")  # Deve retornar [4, 9] (ou [9, 4], a ordem não importa)