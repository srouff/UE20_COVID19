#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

class SIRModelSolver():
    def __init__(self, β_0, γ_0):
        self.β0_ = β_0
        self.γ0_ = γ_0
        self.β_ = None
        self.γ_ = None
        
    def _fit(self, X, y):
        self.β_ = self.β0_
        self.γ_ = self.γ0_
        return self
        
    def _deriv(self, y, t, N, β, γ):
        S,I,R = y
        dSdt = β * S * I / N
        dIdt = β * S * I / N - γ * I
        dRdt = γ * I
        return dSdt, dIdt, dRdt
    
    def _predict(self, X):
        pass

