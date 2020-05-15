#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import scipy
from scipy.integrate import odeint

class SEIRModelSolver():
    def __init__(self, β_0, σ_0, γ_0, E0, I0, R0, N):
        self.β0_ = β_0
        self.σ0_ = σ_0
        self.γ0_ = γ_0
        self.N_ = N
        self.S0_ = N - E0 - I0 - R0
        self.E0_ = E0
        self.I0_ = I0
        self.R0_ = R0
        self.β_ = None
        self.σ_ = None
        self.γ_ = None
        
    def fit(self, X, y):
        self.β_ = self.β0_
        self.γ_ = self.γ0_
        self.σ_ = self.σ0_
        y0 = self.S0_, self.E0_, self.I0_, self.R0_
        f = lambda t, β, σ, γ : (odeint(self.deriv, y0, t, args=(self.N_, β, σ, γ)).T)[1]
        params, errsb = scipy.optimize.curve_fit(f, X, y)
        print("[β,σ,γ] = [%s], Barres d'erreur = [%s]" % (params, errsb))
        return self
        
    def deriv(self, y, t, N, β, σ, γ):
        S,E,I,R = y
        dSdt = -β * S * I/N
        dEdt = β * S * I/N - (σ * E)
        dIdt = σ * E - γ * I
        dRdt = γ * I
        return dSdt, dEdt, dIdt, dRdt
    
    def predict(self, X):
        pass

