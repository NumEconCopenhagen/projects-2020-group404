
# importint packages
import numpy as np
import itertools as it
from scipy import optimize

import matplotlib.pyplot as plt # baseline modul
from mpl_toolkits.mplot3d import Axes3D # for 3d figures
plt.style.use('seaborn-whitegrid') # whitegrid nice with 3d

#Defining model
def f(c = cl[0], l = cl[1], v = v, epsilon = epsilon):
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

    # c. call solver
    sol = optimize.minimize(obj,initial_guess,
    method='SLSQP', bounds=bounds, constraints = cons)

    return sol

# defining print solution, for values find by the solver
def print_solution(c,l,u):
    print(f'c = {c:.8f}')
    print(f'l = {l:.8f}')
    print(f'u = {u:.8f}')

# Opgave 2

m = 1
v = 10
epsilon = 0.3
tao0 = 0.4
tao1 = 0.1
kappa = 0.4
w = 1
cl = (1,1)

#Defining model
def f(c = cl[0], l = cl[1], v = v, epsilon = epsilon):
    return np.log(c) - v*(l**(1+1/epsilon))/(1+1/epsilon)






wliste = np.arange(0.5, 1.5, 0.01).tolist()
cliste = []
lliste = []
for w in wliste:
    sol = solver(m,v,epsilon,tao0,tao1,kappa,w,cl,f)
    c = sol.x[0]
    l = sol.x[1]
    cliste.append(c)
    lliste.append(l)
fig = plt.figure(figsize=(10,4))# figsize is in inches...
ax = fig.add_subplot(1,2,1)
ax.plot(cliste,lliste) # create surface plot in the axis


# Question 3
#clearing total tax
Tax = 0

#Defining a function for Tax revenue
def T(w, l, tao0 = tao0, tao1 = tao1, kappa = kappa):
    return tao0*w*l+tao1*max(w*l-kappa,0)

# defining uniform distribution of wages
w_rand = np.random.uniform(0.5,1.5,size = 10)

# calculation total tax revenue
for wrand in w_rand:
    sol = solver(m,v,epsilon,tao0,tao1,kappa,wrand,cl,f)
    ltax = sol.x[1]
    Tax = Tax + T(wrand,ltax)
print(f'Total tax revenue = {Tax:.8f}')




def ltst(w_rand = w_rand, epsilon = epsilon, tao0 = tao0, tao1 = tao1, kappa = kappa):
    lt = np.empty(np.size(w_rand))
    for i,w in enumerate(w_rand):
        lt[i] = solver(m, v, epsilon, tao0, tao1, kappa, w, cl, f).x[0]
    return lt
type(lt)

def sum_T(w_rand = w_rand, epsilon = epsilon, tao0 = tao0, tao1 = tao1, kappa = kappa):
    lt = ltst(w_rand = w_rand, epsilon = epsilon, tao0 = tao0, tao1 = tao1, kappa = kappa)
    
    sum = 0
    for i in range(np.size(w_rand)):
        w = w_rand[i]
        lt = lt[i]
        sum += tao0*w*lt+tao1*np.max(w*lt-kappa,0)
    return sum
print(sum_T())


#Opgave 5



# define a function that calculates total tax
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




# putting everything into a solver :D
def solvetax(x, c = cl[0], l = cl[1], w = w, m = m, v = v, epsilon = epsilon):

    # converting utility function to list
    def obj(x):
        tao0 = x[0]
        tao1 = x[1]
        kappa = x[2]
        return -totaltax(tao0, tao1, kappa, m, v, epsilon, w, cl, f)

    # constraints and bounds
    # bounds for tao0, tao1, and kappa
    #bndt0 = (0.0,tao1) # maybe upper bound tao1
    #bndt1 = (tao0,1.0) # maybe lower bound tao0
    #bndk = (0.0,1000000000)
    #conk = lambda x: kappa
    # combining constraints and bounds for the optimizer
    #bounds = (bndt0, bndt1, bndk)
    #cons = ({'type': 'ineq', 'fun': conk})

    #initial guess
    initial_guess = np.array([0,0,0])

    # c. call solver
    optimaltax = optimize.minimize(obj,initial_guess,
    method='Nelder-Mead') # , bounds=bounds, constraints = cons

    return optimaltax

solvetax = solvetax(x, c, l, w, m, v, epsilon)

print(solvetax)
print(solvetax.x[0])
print(solvetax.x[1])
print(solvetax.x[2])



