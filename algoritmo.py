import time
import matplotlib.pyplot as plt

MOD = 998244353

def pow_mod(a, b, mod=MOD):
    """Exponenciación rápida: calcula (a^b) mod MOD en O(log b)."""
    res = 1
    while b > 0:
        if b & 1:
            res = (res * a) % mod
        a = (a * a) % mod
        b >>= 1
    return res

def ans(s: str) -> int:
    """
    Calcula el número de formas válidas de reemplazar los '?' en la cadena s
    para que sea perfecta, siguiendo el pseudocódigo del informe.
    """
    if not s:
        return 0

    rest = s[1:]             # sufijo
    q = rest.count('?')      # cantidad de '?'
    pw = pow_mod(2, q, MOD)  # total combinaciones del sufijo

    # Caso base: cadena de longitud 1
    if not rest:
        if s[0] == '?':
            return 2
        else:
            return 1

    hasZero = 1 if '0' in rest else 0

    A = 0
    B = 0

    # Caso primer carácter '1' o '?'
    if s[0] in ['1', '?']:
        A = pw

    # Caso primer carácter '0' o '?'
    if s[0] in ['0', '?']:
        if hasZero == 1:
            B = pw
        else:
            B = (pw - 1 + MOD) % MOD  # evitar negativos

    return (A + B) % MOD


# ========================
#  PRUEBAS DE CORRECTITUD
# ========================
print("Pruebas manuales:")
print(ans("00"))  # Esperado: 1
print(ans("01"))  # Esperado: 0
print(ans("0?"))  # Esperado: 1 ("00")
print(ans("??"))  # Esperado: 3 ("00","10","11")
print(ans("1?"))  # Esperado: 2 ("10","11")
print(ans("?1"))  # Esperado: 1

# =========================
#  EXPERIMENTO DE TIEMPOS
# =========================
sizes = [10, 100, 1000, 5000, 10000, 50000, 100000, 200000]
times = []

for n in sizes:
    s = "?" * n  # peor caso, todo '?'
    start = time.time()
    ans(s)
    end = time.time()
    times.append(end - start)

# Gráfico tiempo vs tamaño
plt.plot(sizes, times, marker="o")
plt.xlabel("Tamaño de la cadena (n)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Tiempo de ejecución vs tamaño de la entrada")
plt.grid(True)
plt.show()
