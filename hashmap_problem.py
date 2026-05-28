class Solutions:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for idx, ch in enumerate(s):
            if not d.get(ch):
                d[ch] = [idx, 1]
            else:
                d[ch][1] +=1

        for ch, val in d.items():
            if val[1] == 1:
                return val[0]
        return -1

# --- CÓDIGO PARA EXECUTAR E TESTAR ---

validador = Solutions()

# Caso 1: A primeira letra que não se repete é 'l' (índice 0)
texto1 = "leetcode"
resultado1 = validador.firstUniqChar(texto1)
print(f"Na palavra '{texto1}', o índice do primeiro caractere único é: {resultado1}")

# Caso 2: 'l' e 'v' se repetem. A primeira que não se repete é 't' (índice 2)
texto2 = "loveleetcode"
resultado2 = validador.firstUniqChar(texto2)
print(f"Na palavra '{texto2}', o índice do primeiro caractere único é: {resultado2}")

# Caso 3: Todas as letras se repetem
texto3 = "aabb"
resultado3 = validador.firstUniqChar(texto3)
print(f"Na palavra '{texto3}', o índice do primeiro caractere único é: {resultado3}")