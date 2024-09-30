def fibonacci_sequence(n):
    sequence = [0, 1]
    while True:
        next_value = sequence[-1] + sequence[-2]
        if next_value > n:
            break
        sequence.append(next_value)
    return sequence

def main():
    num = int(input("Informe um número: "))

   
    fib_sequence = fibonacci_sequence(num)

    if num in fib_sequence:
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
