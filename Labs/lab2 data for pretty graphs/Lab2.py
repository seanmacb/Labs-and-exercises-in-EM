
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fname = "test - Sheet1.csv"

df = pd.read_csv(fname)
print(df) # The dataframe of our sheet


# In[3]:


plt.scatter(df["1/R(m)^2"],df["Twist Angle(Theta)2"],c="g",s=20)

# Graph from Q1 analysis

plt.grid()
plt.xlabel("$1/R^2$ $[m^2]$")
plt.ylabel("Twist Angle [Theta]")
plt.savefig("inverseRsqrVStwistAng.png",dpi=300)
plt.show()


# In[5]:


C = 2.11*10**-12
fourKVAng = [34,34,35]
threeKVAng = [12,14,15]
twoKVAng = [9,10,10]
fourQ = [C*4000,C*4000,C*4000]
threeQ = [C*3000,C*3000,C*3000]
twoQ = [C*2000,C*2000,C*2000]
for i in range(3):
    fourQ[i] = fourQ[i]**2
    threeQ[i] = threeQ[i]**2
    twoQ[i] = twoQ[i]**2


# In[6]:


# Graph for Q3 Analysis

plt.scatter(fourQ,fourKVAng,label="4 kV")
plt.scatter(threeQ,threeKVAng,label="3 kV")
plt.scatter(twoQ,twoKVAng,label = "2 kV")
plt.grid()
plt.legend()

plt.xlim((C*1900)**2,(C*4100)**2)

plt.ylabel("Twist Angle [Theta]")
plt.xlabel("Charge$^2$ [Coulombs$^2$]")

plt.text(3.8*10**-17,8,"R=0.05m was used instead of R=0.08m")

plt.savefig("angleAndChargesquared.png",dpi=300)

plt.show()


# In[7]:


afrac = (0.019**3)/(df["R(m)2"]**1.5)
B = 1-4*(afrac)
df["Twist Angle(Theta)2 corrected"] = np.sqrt(df["Twist Angle(Theta)2"])/B


# In[8]:


# Graph from Q1 Data correction

plt.scatter(df["1/R(m)^2"],df["Twist Angle(Theta)2 corrected"],c="b",s=20,label = "Theta corrected")
plt.scatter(df["1/R(m)^2"],df["Twist Angle(Theta)2"],c="g",s=20,label = "Theta uncorrected")
plt.legend()

plt.grid()
plt.xlabel("$1/R^2$ $[m^2]$")
plt.ylabel("Twist Angle [Theta]")
plt.savefig("inverseRsqrVStwistAngCorr.png",dpi=300)
plt.show()

