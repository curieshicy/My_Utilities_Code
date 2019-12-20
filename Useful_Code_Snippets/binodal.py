import numpy as np
from scipy.optimize import fminbound, brentq, minimize, fsolve
import matplotlib.pyplot as plt
import math

# some global variables
m = 46.663

def chi_temp(temp): # temp in kelvin
    return -18.767 + 7830.4 / temp
    
def convert_degree_to_kevlin(degree):
    return degree + 273.15

def knowledge_from_spinodal_curve(temp):
    def spinodal_curve_know_phi_find_temp(phi): # phi [0, 1]
        numerator = 2 * 7830.4 * phi * (1 - phi)
        denominator = 1. + (1./ m - 1) * phi - 2 * (-18.767) * phi * (1 - phi)
        return numerator / denominator

    critical_phi = fminbound(lambda x: -spinodal_curve_know_phi_find_temp(x), 0, 1)
    critical_temp = spinodal_curve_know_phi_find_temp(critical_phi)
    
    def spinodal_curve_know_T_find_two_phis(temp, c_phi): # temp in Kelvin:
        func = lambda x: spinodal_curve_know_phi_find_temp(x) - temp
        phi_min = brentq(func, 0, c_phi)
        phi_max = brentq(func, c_phi, 1.)
        return phi_min, phi_max
    try:
        phi_min, phi_max = spinodal_curve_know_T_find_two_phis(temp, critical_phi)
        return critical_phi, critical_temp, phi_min, phi_max
        
    except:
        print ('Test temperature is above the critical temperature!!!')
        return critical_phi, critical_temp

# test
#test_temp = convert_degree_to_kevlin(100)
# spinodal_knowledge = knowledge_from_spinodal_curve(test_temp)
#  (0.87230326547610426, 403.12795062225075)
#  (0.87230326547610426, 403.12795062225075, 0.10581687816578154, 0.9974703768509097)

def binodal_powerpoint_fsolve(temp):

    chi = chi_temp(temp)
    spinodal_knowledge = knowledge_from_spinodal_curve(temp)
    phi_min = spinodal_knowledge[2]
    phi_max = spinodal_knowledge[3]

    print (phi_min, phi_max)
    
    def equations(p):
        x, y = p
        out = []
        out.append(math.log(x) + (1 - x) * (1 - 1./m) + chi * (1 - x)**2 - (math.log(y) + (1 - y) * (1 - 1./m) + chi * (1 - y)**2))
        out.append(math.log(1 - x) + x * (1 - m) + chi * m * x**2 - (math.log(1 - y) + y * (1 - m) + chi * m * y**2))

        return out
    
    initial_guess = [0.05, 0.999999999999999999]
    ans = fsolve(equations, initial_guess)

    return ans


degree = 100
test_temp = convert_degree_to_kevlin(degree)
res = binodal_powerpoint_fsolve(test_temp)

print (res)
#def binodal_powerpoint_minimization(temp):
#
#    chi = chi_temp(temp)
#    spinodal_knowledge = knowledge_from_spinodal_curve(temp)
#    phi_min = spinodal_knowledge[2]
#    phi_max = spinodal_knowledge[3]
#
#    print (phi_min, phi_max)
#
#    def equations(p):
#        x, y = p
#
#        part_1 = math.log(x) +  (1 - x) * (1 - 1./m) + chi * (1 - x)**2
#        part_2 = math.log(y) +  (1 - y) * (1 - 1./m) + chi * (1 - y)**2
#
#        part_3 = math.log(1 - x) + x * (1 - m) + chi * m * x**2
#        part_4 = math.log(1 - y) + y * (1 - m) + chi * m * y**2
#        return (part_1 - part_2)**2 + (part_3 - part_4)**2
#
#    optimized = minimize(equations,
#                         [0.05, phi_max],
#                         bounds = tuple([(0.000001, phi_min), (phi_max, 0.999999)])
#                                )
#
#    p = optimized.x
#    print (equations(p))
#
#    return optimized

        

    


