import math

def taylor_approx_exp(x, terms):
    approximation = 0
    for n in range(terms):
        approximation += (x**n) / math.factorial(n)
    return approximation


x = 3/4  # ejemplo
num_terms = 10  # Número de términos 
approximation = taylor_approx_exp(x, num_terms)
real_value = math.exp(x)

# Error entre la aproximación y el valor real
error = abs(real_value - approximation)

print(f"Aproximación de e^{x} con {num_terms} términos: {approximation}")
print(f"Valor real de e^{x}: {real_value}")
print(f"Error: {error}")
