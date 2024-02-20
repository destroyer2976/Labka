num=int(input("enter"))
def square_generator(N):
    for i in range(1, N + 1):
        if i ** 2<N:
            yield i**2


# squares_up_to_N = list(square_generator(num))
generator=square_generator(num)
for square in generator:
    print(square)
# for square in squares_up_to_N:
#     print(square)
