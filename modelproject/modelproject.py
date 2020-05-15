#importing optimize
from scipy import optimize

# function to solve for the optimal AD
def solve_for_ss(pi_t1, gamma, ybar, pistar, alpha):
    # define objective function
    def AS(y_t):
        return pi_t1 + gamma*(y_t - ybar)
    def obj(y_t):
        return alpha * (AS(y_t) - pistar)

    # def constraints
    # AS cannot be more than the goal for inlation.
    con = lambda y_t: alpha * (AS(y_t) - pistar)
    cons = ({'type': 'ineq', 'fun': con})
    # call optimizer
    #result = optimize.minimize_scalar(obj, bounds=(0,100), method='bounded')
    result = optimize.minimize(obj,1, method='SLSQP', constraints = cons)
    return result
