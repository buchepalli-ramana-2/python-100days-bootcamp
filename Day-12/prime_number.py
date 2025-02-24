def is_prime(num):
    factors = []
    if num > 1:
        for i in range(2,(num//2)+1):
            if num % i == 0 and i < num:
                factors.append(i)
    # return factors
    if len(factors) >= 1:
        return f"{num} is not prime"
        return factors
    else:
        return f"{num} is prime"
    
print(is_prime(121))
print(is_prime(169))
print(is_prime(289))
print(is_prime(361))
print(is_prime(529))
print(is_prime(729))

