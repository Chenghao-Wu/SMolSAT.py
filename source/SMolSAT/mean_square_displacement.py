#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 14:58:21 2018

@author: bruce
"""

from ._SMolSAT import *

import numpy as np

class msd:
    def __init__(self,system=None,trajs=None,listname=None,out=None):
        self.system=system
        self.trajs=trajs
        self.listname=listname
        self.out=out

        self.analysis=Mean_Square_Displacement(system)
        self.analysis.run(trajs,listname)
        self.analysis.write(out)
        self.read()

    def get(self):
        return self.data["msd"]
    
    def get_t(self):
        return self.data["t"]

    def read(self):
        with open(self.out) as f:
            lines = (line.strip() for line in f if len(line.strip().split())==2)
            self.data = np.loadtxt(lines, delimiter='\t',dtype={'names': ('t', 'msd'),'formats': ('f4','f4')})