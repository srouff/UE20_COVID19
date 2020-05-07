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
        return odeint(deriv, y)
    
    def deriv(self, ndays, dt=1):
        for i in range(ndays-1):
            self.S_[i+1] = self.S_[i] - self.β_ * (self.S_[i] * self.I_[i]) * dt
            self.I_[i+1] = self.I_[i] + (self.β_ * self.S_[i] * self.I_[1] - self.γ_ * self.I_[i]) * dt
            self.R_[i+1] = self.R_[i] + (self.γ_ * self.I_[i]) * dt
        return self.S_, self.I_, self.R_
    
    def predict(self, X):
        pass

