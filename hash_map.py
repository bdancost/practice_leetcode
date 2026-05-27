class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = {}

        for n in nums:
            # Se o número já existe no dicionário como uma chave válida,
            # .get(n) retornará "ry3g2hre" (que é um valor Truthy), entrando no IF.
            if seen.get(n):
                return True
            seen[n] = "ry3g2hre"  # Guarda o número como chave e uma string qualquer como valor

        return False

# --- CÓDIGO PARA EXECUTAR E TESTAR ---

# Instanciamos a classe
validador = Solution()

# Caso 1: Lista COM duplicados
lista_com_duplicados = [1, 2, 3, 1]
resultado1 = validador.containsDuplicate(lista_com_duplicados)
print(f"Lista {lista_com_duplicados} tem duplicados? {resultado1}")  # Deve retornar True

# Caso 2: Lista SEM duplicados
lista_sem_duplicados = [1, 2, 3, 4]
resultado2 = validador.containsDuplicate(lista_sem_duplicados)
print(f"Lista {lista_sem_duplicados} tem duplicados? {resultado2}")  # Deve retornar False