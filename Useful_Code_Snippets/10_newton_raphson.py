# this is to implement Newton-Raphson method to find the root of a function
# initial guess is updated by guess = guess - f(guess) / f'(guess)
import math

def newton_raphson(f, guess, tolerance):
    # find derivative of function f
    def derivative_f(f, x, delta = 1e-6):
        return (f(x + delta) - f(x)) / delta

    while abs(f(guess)) > tolerance:
        guess = guess - f(guess) / derivative_f(f, guess)
    return guess
# test
print (newton_raphson(lambda x: x**2 - 24, 4, 1e-6))
print (newton_raphson(lambda x: x**3 + math.cos(x), 4, 1e-6))




