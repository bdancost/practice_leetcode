class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l, r = 0, 0
        _max = 1
        counter = {}

        counter[s[0]] = 1

        while r < len(s) -1:
            r+=1
            if counter.get(s[r]):
                counter[s[r]] += 1
            else:
                counter[s[r]] = 1

            while counter[s[r]] == 3:
                counter[s[l]] -= 1
                l += 1
            _max = max(_max, r-l+1)
        return _max

# --- COMO EXECUTAR ---
# 1. Instanciamos a classe Solution
solicitacao = Solution()

# 2. Passamos uma string de teste
# Na string "bcbbbcba", o maior pedaço válido com no máximo duas letras repetidas é "cbcba" (tamanho 5)
resultado = solicitacao.maximumLengthSubstring("bcbbbcba")

# 3. Mostramos o resultado no terminal
print(f"O comprimento máximo da substring válida é: {resultado}")