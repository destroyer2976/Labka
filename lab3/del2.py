num=int(input("enter"))
def generate_histogram(num_stars):

    max_stars = 10
    remaining_stars = max_stars - num_stars

    print(num_stars * " ", end="")
    print('*' * remaining_stars)

generate_histogram(num)
