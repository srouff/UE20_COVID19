#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

from scipy.optimize import curve_fit
from scipy.integrate import solve_ivp

class SEIRDModelSolver():
    def __init__(self, alpha, beta, delta, gamma, rho):
        self.params = None
        self.param_cov_ = None
        self.alpha_ = alpha
        self.beta_ = beta
        self.delta_ = delta
        self.gamma_ = gamma
        self.rho_ = rho
        
    def _update_params(self, new_params):
        self.alpha_, self.beta_, self.delta_, self.gamma_, self.rho_ = new_params
        
    def _deriv(self, t, S, E, I, R, D, alpha, beta, delta, gamma, rho):
        N = S+E+I+R+D
        lambda_ = beta * I / N
        dS_dt = -lambda_ * S
        dE_dt = lambda_ * S - delta * E
        dI_dt = delta * E - (1-alpha) * gamma * I - alpha * rho * I
        dR_dt = gamma * I
        dD_dt = alpha * rho * I
        return dS_dt, dE_dt, dI_dt, dR_dt, dD_dt
    
    def _integrate(self, t, y_0, params):
        t_span = (min(t), max(t))
        deriv = lambda t,y : self.deriv(t, *y, *params)
        ode_result = solve_ivp(deriv, t_span, y_0, t_eval=t)
        return ode_result
    
    def _predict(self, t, y_0, params):
        ode_result = self._integrate(t, y_0, params)
        y_t = ode_result.y
        return y_t
    
    def _curve_fit(self, f, t, y, bounds=(0, np.inf)):
        params_init = self.params
        fitted_params, pcov = curve_fit(f, t, y, p0=params_init, bounds=bounds)
        self.param_cov_ = pcov
        self._update_params(fitted_params)
    
    def _fit(self, t, N, I, R, D):
        y = np.hstack([I,R,D])
        E0 = 1
        I0 = I[0]
        R0 = R[0]
        D0 = D[0]
        S0 = N - E0 - I0 - R0 - D0
        y_0 = (S0, E0, I0, R0, D0)
        def f(t, *params):
            y_t = self._predict(t, y_0, params)
            I_pred = y_t[2]
            R_pred = y_t[3]
            D_pred = y_t[4]
            pred = np.hstack(I_pred, R_pred, D_pred)
            return pred
        
        self._curve_fit(f, t, y)
        return self

