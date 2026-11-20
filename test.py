
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("lego_sets.csv")

print("Dimensions :", df.shape)
display(df.head())
display(df.info())
display(df.isnull().sum())
