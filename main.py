from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

file_path = './lotto.csv'
lotto_df = pd.read_csv(file_path)
# print(lotto_df)
lotto_df.index = lotto_df['round']
lotto_df.set_index('round', inplace=True)

# lotto_df.values = lotto_df['N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'Bonus']


lotto_df.plot()
plt.show()