class Solutions:
    def reverseOnlyLetters(self, s: str) -> str:
        arr = [ch for ch in s]
        left = 0
        right = len(arr)-1

        while left < right:
            if arr[left].isalpha() and arr[right].isalpha():
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            elif arr[left].isalpha():
                right -= 1

            elif arr[right].isalpha():
                left += 1
            else:
                left += 1
                right -= 1

        return "".join(arr)


# --- CÓDIGO PARA EXECUTAR E TESTAR ---

validador = Solutions()

# Caso 1: Apenas letras e um hífen no meio. O hífen deve continuar no mesmo lugar.
texto1 = "ab-cd"
resultado1 = validador.reverseOnlyLetters(texto1)
print(f"Original: {texto1} -> Invertido: {resultado1}")  # Esperado: "dc-ba"

# Caso 2: Vários hífens e caracteres. Apenas as letras invertem.
texto2 = "a-bC-dEf-ghIj"
resultado2 = validador.reverseOnlyLetters(texto2)
print(f"Original: {texto2} -> Invertido: {resultado2}")  # Esperado: "j-Ih-gfE-dCba"

