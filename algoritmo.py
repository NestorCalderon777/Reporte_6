import time
import random
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

# -------------------
# Experimento tiempo vs n
# -------------------
tamanos = [i for i in range(0, 200001, 20000)]  # tamaños desde 0 hasta 200000
tiempos = []

for n in tamanos:
    # generar cadena aleatoria con '0', '1' y '?'
    s = ''.join(random.choice(['0', '1', '?']) for _ in range(max(1, n)))
    
    inicio = time.time()
    ans(s)
    fin = time.time()
    
    tiempos.append(fin - inicio)

# Graficar
plt.figure(figsize=(8,6))
plt.plot(tamanos, tiempos, marker='o', linestyle='-', color='b', label="Tiempo de ejecución")
plt.xlabel("Tamaño de la entrada n")
plt.ylabel("Tiempo (segundos)")
plt.title("Tiempo de ejecución vs Tamaño de entrada n")
plt.grid(True)
plt.legend()
plt.xlim(0, 200000)
plt.ylim(0, max(tiempos)*1.2)  # margen extra para visualizar bien
plt.show()