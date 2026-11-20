import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("lego_sets.csv", sep=',')
print(df.shape())
print(df.head())
print(df.info())
print(df.isnull().sum())

