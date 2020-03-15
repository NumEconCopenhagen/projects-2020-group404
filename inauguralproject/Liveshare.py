
# importint packages
import numpy as np
import itertools as it
from scipy import optimize

import matplotlib.pyplot as plt # baseline modul
from mpl_toolkits.mplot3d import Axes3D # for 3d figures
plt.style.use('seaborn-whitegrid') # whitegrid nice with 3d

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
w_rand = np.random.uniform(0.5,1.5,size = 10000)

# calculation total tax revenue
for wrand in w_rand:
    sol = solver(m,v,epsilon,tao0,tao1,kappa,wrand,cl,f)
    ltax = sol.x[1]
    Tax = Tax + T(wrand,ltax)
print(f'Total tax revenue = {Tax:.8f}')



#Opgave 4
#clearing total tax
Tax = 0

#Defining a function for Tax revenue
def T(w, l, tao0 = tao0, tao1 = tao1, kappa = kappa):
    return tao0*w*l+tao1*max(w*l-kappa,0)

# defining uniform distribution of wages
w_rand = np.random.uniform(0.5,1.5,size = 10000)

# calculation total tax revenue
for wrand in w_rand:
    sol = solver(m,v,epsilon = 0.1,tao0,tao1,kappa,wrand,cl,f)
    ltax = sol.x[1]
    Tax = Tax + T(wrand,ltax)
print(f'Total tax revenue = {Tax:.8f}')



# Opgave 5


# Hvad med sådan her?:
w2 = np.zeros(np.size(wliste))
l2 = np.zeros(np.size(lliste))


t0_t1_ka = (1,1,1)

def Tsolver():
    def objtm(t0_t1_ka):
        tao0 = t0_t1_ka[0]
        tao1 = t0_t1_ka[1]
        kappa = t0_t1_ka[2]
        return -T(tao0, tao1, kappa)

# Bounds
boundt0 = (0,1)
boundt1 = (tao0,1)
boundk = kappa > 0
bounds = (boundt0, boundt1, boundk)

guess3 = np.array([1,1,1])

soltm = optimize.minimize(objtm, guess3, method = 'SLSQP', bounds = bounds)
return soltm










w2 = 1
l2 = 0.39999449
x = [0.1,0.1,0.1]


def T2(tao0 = tao0, tao1 = tao1, kappa = kappa, w = w2, l = l2):
    return tao0*w*l+tao1*max(w*l-kappa,0)

# Defining a function that will solve the model.
def maxtax(tao0, tao1, kappa, w = w2, l = l2):

    # converting utility function to list
    def obj(x):
        tao0 = x[0]
        tao1 = x[1]
        kappa = x[2]
        return -T2(tao0,tao1,kappa)

    # constraints and bounds
    # bounds for c and l
    boundtao0 = (0.0,1)
    boundtao1 = (tao0,1)
    boundk = (0,1)
    # combining constraints and bounds for the optimizer
    bounds = (boundtao0,boundtao1,boundk)

    #initial guess
    initial_guess = np.array([0.1,0.1,0.1])

    # c. call solver
    sol2 = optimize.minimize(obj,initial_guess,
    method='SLSQP', bounds=bounds)

    return sol2
sol2 = maxtax(tao0, tao1, kappa, w = w2, l = l2)
print(sol2)
