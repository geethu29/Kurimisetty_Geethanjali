def count_multiples(input_list):
    multiples_count = {i: 0 for i in range(1, 10)}
    for number in input_list:
        for i in range(1, 10):
            if number % i == 0:
                multiples_count[i] += 1
    return multiples_count
input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
result = count_multiples(input_list)
print(result)
