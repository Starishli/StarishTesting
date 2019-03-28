import pandas as pd


def foo(df):
    df.iloc[0, 0] = 100


df_ = pd.DataFrame({'a': [1, 2, 3], 'b': [2, 3, 4]})
foo(df_)


print(df_)