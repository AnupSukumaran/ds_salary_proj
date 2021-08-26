#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 14:09:49 2021

@author: anupsukumaran
"""

import glassdoorScrapper2 as gs
import pandas as pd

path = "/Users/anupsukumaran/Desktop/MyDataScienceProj/chromedriver"

df = gs.get_jobs("data scientist", 1000, False, path, 15)

df.to_csv("glassdoor_jobs.csv", index = False)