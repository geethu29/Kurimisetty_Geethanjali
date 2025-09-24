def generate_series(a: int):
    series = []
    for i in range(1, a+1, 2): 
        series.append(i)
    return series
a = int(input("Enter a number: "))
result = generate_series(a)
print("Output:", ", ".join(map(str, result)))