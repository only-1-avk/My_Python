def prime_number(nos):
    is_prime = True
    for i in range(2, nos):
        if nos % i == 0:
            is_prime = False
    if is_prime:
        print("It is a prime number")
    else:
        print("It's not a prime number")


n = (int(input("Check this number:")))

prime_number(nos=n)
