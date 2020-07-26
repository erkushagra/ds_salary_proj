# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 20:47:47 2020

@author: Harshit
"""


import glassdoor_scrapper as gs
import pandas as pd 

path = "C:/Users/Harshit/Documents/ds_salary_proj/chromedriver" 

df= gs.get_jobs('data scientist',15,False, path,15)