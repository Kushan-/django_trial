#!/usr/bin/env python
import pandas as pd
df = pd.read_csv("dogs.csv", skiprows=1)
#print(df)
print(df.count())