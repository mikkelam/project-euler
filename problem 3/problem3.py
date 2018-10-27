from pyprimesieve import factorize

number = 600851475143

factors = [i[0]for i in factorize(600851475143)]
answer = max(factors)

print(answer)