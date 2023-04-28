#creating fibonacci series using generators
def fibo(first_value, second_value, limit):
    c=0
    while c<=limit:
        result = first_value
        yield result
        first_value, second_value = second_value, first_value + second_value
        c+=1

FO = fibo(2,5,10)
for i in FO:
    print(i)