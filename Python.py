# Task 1: Isomorphic Strings

def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    map_s_t = {}
    map_t_s = {}

    for c1, c2 in zip(s, t):
        if c1 in map_s_t and map_s_t[c1] != c2:
            return False
        if c2 in map_t_s and map_t_s[c2] != c1:
            return False

        map_s_t[c1] = c2
        map_t_s[c2] = c1

    return True


# Task 2: Missing Number

def missing_number(nums):
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)


# Task 3: Prime Factorization

def prime_factors(n):
    factors = []
    i = 2

    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1

    if n > 1:
        factors.append(n)

    return factors
