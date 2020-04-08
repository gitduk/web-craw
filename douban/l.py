import numpy as np
import pandas as pd
from tools.logger import Logger

lg = Logger()

s = pd.Series([1, 3, 5, np.nan, 6, 8])
lg.sp(s)
dates = pd.date_range('20130101', periods=6)
lg.sp(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
lg.sp(df)

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'oo'})

lg.sp(df2)
lg.sp(df2.dtypes)
lg.sp(df2.head(2))
lg.sp(df2.tail(2))
lg.sp(df2.index)
lg.sp(df2.columns)
lg.sp(df2.describe())
lg.sp(df.sort_index(axis=1, ascending=False))
lg.sp(df.sort_index(axis=1, ascending=True))
lg.sp(df.sort_values(by='B'))
lg.sp(df['A'][:2])
lg.sp(df.loc[dates[0]], df, dates[0])
lg.sp(df, df.loc[:, ['A', 'B']])
lg.sp(df, df.loc['20130102':'20130104', ['A', 'B']])
lg.sp(df2, df2.loc[:2, ['A', 'B']])
lg.sp(df, df.loc['20130102', ['A', 'B']])
lg.sp(df, df.loc[dates[0], 'A'])
lg.sp(df, df.at[dates[0], 'A'])
lg.sp(df, df.iloc[1:3])
lg.sp(df, df.iloc[[1, 2, 4], [0, 2]])
lg.sp(df, df.iloc[1:3, :])
lg.sp(df, df.iloc[:, 1:3])
lg.sp(df, df[df.A > 0])
lg.sp(df, df[df > 0])

df3 = df.copy()
df3['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
lg.sp(df3)
lg.sp(df3, df3[df3['E'].isin(['two', 'four'])])
lg.sp(df3, df3['E'].isin(['two', 'four']))

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
df['F'] = s1
lg.sp(df)
df.at[dates[0], 'A'] = 0
lg.sp(df)
df.iat[0, 1] = 0
lg.sp(df)
df.loc[:, 'D'] = np.array([5] * len(df))
lg.sp(df)
df.loc[:, 'D'] = [i for i in range(len(df))]
lg.sp(df)
df4 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df4.loc[dates[0]:dates[1], 'E'] = 1
lg.sp('df4', df4)
df4.dropna(how='any')
lg.sp('df4', df4)
