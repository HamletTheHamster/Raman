#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit as curveFit
import datetime
import os
import sys

timestamp = datetime.datetime.now()

if len(sys.argv) > 0:
    note = sys.argv[1]

path = "6-22-23 1um TeO2 (re-re-annealed)"
save = "Plots/" + timestamp.strftime("%Y-%b-%d") + "/" + timestamp.strftime("%X") + ": " + note + "/"
if not os.path.exists(save):
  os.makedirs(save)

# import data
run = "10"
df = {}
df = pd.read_csv(f"{path}/Joel-6-22-23-1um-Te-oxide-re-re-annealed_{run}.csv", delim_whitespace=True)
df["Y"] /= 1e3

#plot
plt.figure(dpi=600)
plt.title(f"Raman: 1μm TeO₂ Run {run}")
plt.xlabel("cm⁻¹")
plt.ylabel("a.u.")
#plt.xlim()
#plt.ylim()
plt.minorticks_on()
plt.tick_params(which='both', direction='in', pad=5)

plt.plot(df["X"], df["Y"], color="#099e7d")
plt.savefig(f"{save} Raman Spectra.png", format="png")
plt.savefig(f"{save} Raman Spectra.pdf", format="pdf")
plt.savefig(f"{save} Raman Spectra.svg", format="svg")
