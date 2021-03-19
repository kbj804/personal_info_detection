'''
pip install requests
pip install tabulate
pip install "colorama>=0.3.8"
pip install future
pip install -f http://h2o-release.s3.amazonaws.com/h2o/latest_stable_Py.html h2o

'''

import h2o
from h2o.automl import H2OAutoML

h2o.init()

import pandas as pd
origin = pd.read_csv("origin.txt",sep='\t')

df = h2o.H2OFrame(origin)

train, test = df.split_frame(ratios = [.8], seed = 1234)

x = train.columns
y = "y"
x.remove(y)

train[y] = train[y].asfactor()
test[y] = test[y].asfactor()

aml = H2OAutoML(max_models=3
                , seed=1
               )
aml.train(x=x, y=y, training_frame=train)

lb = aml.leaderboard
lb.head(rows=lb.nrows)

# test1 = test.drop('y')

preds = aml.predict(test)
preds = aml.leader.predict(test)

type(test[y])
type(preds)

test[y].cbind(preds)