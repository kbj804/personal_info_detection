from random import uniform
import pandas as pd
import numpy as np

def random_list(size):
    result=[]
    for i in range(size):
        result.append(uniform(-5.0,5.0))
    
    return result

df_A = pd.DataFrame({"A":random_list(5), "B":random_list(5), "C":random_list(5), "D":random_list(5)})
df_A.index=['2020-01-01','2020-01-02','2020-01-03','2020-01-04','2020-01-05']
# print(df_A.sort_values(by='C',ascending=False))
# print(df_A.[loc[:,['A']]])
# print(df_A.iloc[[2,4]])
# print(df_A.iloc[4])
# row coulmn
# print(df_A.iloc[1:4,0:2])
# df_A.loc[df_A.values>0.3] = np.nan
print(df_A[df_A>0])

# def generate_list(s, size):
#     result=[]
#     for i in range(size):
#         result.append(s+str(i))
#     return result
# column = ["A", "B", "C", "D"]
# df_B = pd.DataFrame({column[0]:generate_list(column[0],12), column[1]:generate_list(column[1],12), column[2]:generate_list(column[2],12), column[3]:generate_list(column[3],12)})

# print(df_B.info())