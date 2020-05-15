#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import scipy
from scipy.integrate import odeint

class SIRModelSolver():
    def __init__(self, β_0, γ_0, R0, I0, N):
        self.β0_ = β_0
        self.γ0_ = γ_0
        self.N_ = N
        self.R0_ = R0
        self.I0_ = I0
        self.S0_ = N - I0 - R0
        self.β_ = None
        self.γ_ = None
        
    def fit(self, X, y):
        self.β_ = self.β0_
        self.γ_ = self.γ0_
        y0 = self.S0_, self.I0_, self.R0_
        f = lambda t, β, γ : (odeint(self.deriv, y0, t, args=(self.N_, β, γ)).T)[1]
        params, errsb = scipy.optimize.curve_fit(f, X, y)
        print("[β,γ] = [%s], Barres d'erreur = [%s]" % (params, errsb))
        return self
        
    def deriv(self, y, t, N, β, γ):
        S,I,R = y
        dSdt = -β * S * I / N
        dIdt = β * S * I / N - γ * I
        dRdt = γ * I
        return dSdt, dIdt, dRdt
    
    def predict(self, X):
        pass

