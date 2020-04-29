# importint packages
import numpy as np
import itertools as it
from scipy import optimize
from tqdm import tqdm

# question 1 #

#defining f as in the ipynb file
def f(c = 1, l = 1, v = 10, epsilon = 0.3):
    return np.log(c) - v*(l**(1+1/epsilon))/(1+1/epsilon)

# Defining a function that will solve the model.
def solver(m,v,epsilon,tao0,tao1,kappa,w,cl,f):

    # converting utility function to list
    def obj(cl):
        c = cl[0]
        l = cl[1]
        return -f(c,l)

    # constraints and bounds
    # eq constraint for x
    con = lambda cl: np.array([m + w*cl[1] - \
        (tao0*w*cl[1] + tao1*max(w*cl[1]-kappa,0)) - cl[0]])
    # bounds for c and l
    boundc = (0.0, m + w*cl[1] - (tao0*w*cl[1] + tao1*max(w*cl[1]-kappa,0)))
    boundl = (0.0,1.0)
    # combining constraints and bounds for the optimizer
    bounds = (boundc,boundl)
    cons = ({'type': 'eq', 'fun': con})

    #initial guess
    initial_guess = np.array([1,1])

    # call solver
    sol = optimize.minimize(obj,initial_guess,
    method='SLSQP', bounds=bounds, constraints = cons)

    return sol

# defining print solution, for values find by the solver
def print_solution(c,l,u):
    print(f'c = {c:.8f}')
    print(f'l = {l:.8f}')
    print(f'u = {u:.8f}')

def print_solution2(c,l,u,TTR):
    print(f'tao0 = {c:.8f}')
    print(f'tao1 = {l:.8f}')
    print(f'kappa = {u:.8f}')
    print(f'Total tax revenue = {TTR:.8f}')

# question 3 and 4 #

# defining a function for calculating total tax revenue
def totaltax(tao0, tao1, kappa, m, v, epsilon, w, cl, f):
    global TTR
    TTR = 0
    np.random.seed(2020)
    #Defining a function for Tax revenue
    def T(tao0, tao1, kappa, w, l):
        return tao0*w*l+tao1*max(w*l-kappa,0)

    # defining uniform distribution of wages
    w_rand = np.random.uniform(0.5,1.5,size = 10)

    # calculation total tax revenue
    for wrand in w_rand:
        sol = solver(m,v,epsilon,tao0,tao1,kappa,wrand,cl, f)
        ltax = sol.x[1]
        TTR = TTR + T(tao0, tao1, kappa, wrand, ltax)
    return TTR

# question 5
#Defining a Tax function that does not use SLSQP as we are unable to get it to work.
TTR2 = 0
def totaltax2(tao0, tao1, kappa, m, v, epsilon, w):
    global TTR2
    TTR2 = 0
    #Defining the total resources with variable l
    def x(l):
        x = 0
        for wrand in w:
            x = x + m + wrand*l - (tao0*wrand*l + tao1*np.fmax(wrand*l-kappa,0))
        return x
    #Defining the tax function to optimize with l as variable
    def obj3(l):
        c = x(l)
        return -f(c,l)

    # calculation total tax revenue now with bounded, and create a list with the optimal taxes
    for wrand in w:
        sol = optimize.minimize_scalar(obj3, bounds=(0,1), method='bounded')
        ltax = sol.x # the current optimal l given wage
        TTR2 = TTR2 + tao0*wrand*ltax+tao1*np.fmax(wrand*ltax-kappa,0) # sum total tax revenue
    #The total tax is the sum of all the individual taxes.
    return TTR2