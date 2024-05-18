def nonConsecutiveDigits(N):

    N_string = str(N)
    for i in range(len(N_string) - 1):
        if N_string[i] == N_string[i + 1]:
            return True
    return False

def trouve_nombre_suivant(N):

    J = N + 1
    while J < float('inf'):
        if not nonConsecutiveDigits(J):
            return J
        J += 1
    return 0

# Exemple
print(trouve_nombre_suivant(44432))


