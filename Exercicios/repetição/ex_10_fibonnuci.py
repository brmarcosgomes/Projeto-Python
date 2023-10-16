def fibonacci_series(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        temp = a
        a = b
        b = temp + b

def fibonacci_series_500(a):
    a = 0
    b = 1
    while a <= 500:
            print(a)
            temp = a
            a = b
            b = temp + b
    

fibonacci_series_500(500)
    