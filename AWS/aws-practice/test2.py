# Flask api for generating prime numbers using normal method and prime sieve

def primes_sieve2(Limit):
    a = [True] * Limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, Limit, i):
                a[n] = False
