
# importint packages
import numpy as np
import itertools as it
from scipy import optimize

%matplotlib inline
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









# solution to question 2 :D

wliste = np.arange(0.5, 1.5, 0.01).tolist()
uliste = []
for w in wliste:
    sol = solver(m,v,epsilon,tao0,tao1,kappa,w,cl,f)
    c = sol.x[0]
    l = sol.x[1]
    u = f(c,l)
    uliste.append(u)
print(uliste)
print(wliste)
fig = plt.figure(figsize=(10,4))# figsize is in inches...
ax = fig.add_subplot(1,2,1)
ax.plot(wliste,uliste) # create surface plot in the axis
