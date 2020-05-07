#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

class SIRModelSolver():
    def __init__(self, β_0, γ_0, S_0, I_0, R_0):
        self.β_= β_0
        self.γ_ = γ_0
        self.S_ = S_0
        self.I_ = I_0
        self.R_ = R_0
        
    def fit(self, y):
        pass
    
    def deriv(self, y, t, N, β, γ):
        S,I,R = y
        dSdt = -β * S * I / N
        dIdt = β * S * I / N - γ * I
        dRdt = γ * I
        return dSdt, dIdt, dRdt
    
    def predict(self, X):
        pass

