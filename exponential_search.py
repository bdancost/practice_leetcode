def binary_search(nums, n, lo=0, hi=None):
    if hi is None:
        hi = len(nums) - 1

    while lo <= hi:  # Corrigido para <= para garantir que avalia o último elemento
        mid = (lo + hi) // 2

        if nums[mid] == n:
            return mid
        elif nums[mid] < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    n = len(arr)
    i = 1

    # Multiplica o índice por 2 até achar o intervalo ou estourar o tamanho do array
    while i < n and arr[i] < target:
        i *= 2

    # Se o elemento exato foi achado no limite superior do salto
    # (Adicionada a checagem 'i < n' para evitar o erro de índice)
    if i < n and arr[i] == target:
        return i

    # CORREÇÃO: Passamos os índices limites (lo e hi) em vez de fatiar o array,
    # e adicionamos o 'return' para devolver a resposta da busca binária.
    return binary_search(arr, target, lo=i // 2, hi=min(i, n - 1))


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
       31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
target = 32
result = exponential_search(arr, target)

print(f"Element found at index {result}")