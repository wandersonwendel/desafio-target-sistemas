def is_fibonacci(n):
    a, b = 0, 1
    fibonacci_sequence = [a]

    while b < n:
        fibonacci_sequence.append(b)
        a, b = b, a + b

    fibonacci_sequence.append(b)

    if b == n or a == n:
        print(f"O número {n} pertence à sequência de Fibonacci.")
        print(f"Sequência gerada: {fibonacci_sequence}")
    else:
        print(f"O número {n} NÃO pertence à sequência de Fibonacci.")
        print(f"Sequência gerada: {fibonacci_sequence}")

numero = int(input("Informe um número: "))
is_fibonacci(numero)
