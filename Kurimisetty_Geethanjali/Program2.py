def generate_odd_numbers(a):  
    odd_numbers = [i for i in range(1, 2 * a) if i % 2 != 0]
    print(", ".join(map(str, odd_numbers)))
a = int(input("Enter an integer: "))
generate_odd_numbers(a)
