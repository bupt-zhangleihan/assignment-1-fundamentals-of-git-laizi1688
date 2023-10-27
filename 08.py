import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
path = 'form.csv'
form_df = pd.read_csv(path)

import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])

print(form_df.isnull())
print(form_df.dropna())
print(form_df.dropna(axis='columns'))
print(form_df.duplicated())