import random

def modulo(m_base, m_exp, m_mod):
    a = 1
    b = m_base
    while m_exp > 0:
        if m_exp % 2 == 1:
            a = (a * b) % m_mod
        b = (b * b) % m_mod
        m_exp //= 2
    return a % m_mod

def jacobian(a, n):
    if a == 0:
        return 0 
    answer = 1
    if a < 0:
        a = -a
        if n % 4 == 3:
            answer = -answer
    if a == 1:
        return answer
    while a != 0:
        if a < 0:
            a = -a
            if n % 4 == 3:
                answer = -answer
        while a % 2 == 0:
            a //= 2
            if n % 8 == 3 or n % 8 == 5:
                answer = -answer
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            answer = -answer
        a %= n
        if a > n // 2:
            a -= n
    if n == 1:
        return answer
    return 0

def solovay_strassen(p, itr):
    # Solovay-Strassen Primality Test
    if p < 2:
        return False
    if p != 2 and p % 2 == 0:
        return False
    for _ in range(itr):
        a = random.randint(1, p - 1)
        jacob = (p + jacobian(a, p)) % p
        mod = modulo(a, (p - 1) // 2, p)
        if jacob == 0 or mod != jacob:
            return False
    return True

if __name__ == "__main__":
    iter = 50
    num1 = int(input("Enter the first number: "))
    if solovay_strassen(num1, iter):
        print(f"{num1} is a prime number\n")
    else:
        print(f"{num1} is a composite number\n")

    num2 = int(input("Enter another number: "))
    if solovay_strassen(num2, iter):
        print(f"{num2} is a prime number\n")
    else:
        print(f"{num2} is a composite number\n")
