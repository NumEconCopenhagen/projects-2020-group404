def square(x):
    """ square numpy array
    
    Args:
    
        x (ndarray): input array
        
    Returns:
    
        y (ndarray): output array
    
    """
    
    y = x**2
    return y

# importint packages
import numpy as np
import itertools as it
from scipy import optimize

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

    # c. call solver
    sol = optimize.minimize(obj,initial_guess,
    method='SLSQP', bounds=bounds, constraints = cons)

    return sol

# defining print solution, for values find by the solver
def print_solution(c,l,u):
    print(f'c = {c:.8f}')
    print(f'l = {l:.8f}')
    print(f'u = {u:.8f}')

# defining a function for calculating total tax revenue
def totaltax(tao0, tao1, kappa, m, v, epsilon, w, cl, f):
    global TTR
    TTR = 0
    np.random.seed(2020)
    #Defining a function for Tax revenue
    def T(tao0, tao1, kappa, w, l):
        return tao0*w*l+tao1*max(w*l-kappa,0)

    # defining uniform distribution of wages
    w_rand = np.random.uniform(0.5,1.5,size = 10000)

    # calculation total tax revenue
    for wrand in w_rand:
        sol = solver(m,v,epsilon,tao0,tao1,kappa,wrand,cl, f)
        ltax = sol.x[1]
        TTR = TTR + T(tao0, tao1, kappa, wrand, ltax)
    return TTR