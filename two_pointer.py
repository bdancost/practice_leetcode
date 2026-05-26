class Solutions:
    def reverseWords(self, s):
        res = ''
        l, r = 0, 0

        while r < len(s):
            if s[r] != ' ':
                r += 1
            else:
                res += s[l:r+1][::-1]
                r += 1
                l = r

        res += ' '
        res += s[l:r + 2][::-1]
        return res[1:]

# --- CÓDIGO DE TESTE ---
# 1. Criamos um objeto da classe Solutions
solucao = Solutions()

# 2. Chamamos a função passando uma frase e guardamos o resultado
resultado = solucao.reverseWords("O rato roeu a roupa")

# 3. Exibimos o resultado no terminal
print(resultado)
