from pickletools import optimize
from turtle import forward
import torch 
import torch.nn as nn 
import torch.nn.functional as F 
import numpy as np 
import pandas as pd 
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import math

file = r"C:\Users\suyash\Downloads\50_Startups.csv"
data = pd.read_csv(file)
col = data.columns
x = data[col[:-2]].values 
y = data[col[-1]].values 
xtrain, xtest, ytrain, ytest = train_test_split(x,y, test_size=0.2, random_state=1234)

scx = StandardScaler()
scy = StandardScaler()

scx.fit_transform(xtrain)
scx.fit_transform(xtest)
scy.fit_transform(ytrain.reshape(-1, 40))
scy.fit_transform(ytest.reshape(-1, 10))

xtrain = torch.from_numpy(xtrain.astype(np.float32))
ytrain = torch.from_numpy(ytrain.astype(np.float32))
xtest = torch.from_numpy(xtest.astype(np.float32))
ytest = torch.from_numpy(ytest.astype(np.float32))

data, features = xtrain.shape

class Model(nn.Module):
    def __init__(self, n_features):
        super(Model, self).__init__()
        self.linear = nn.Linear(n_features, 1)

    def forward(self, x):
        ypred = nn.LeakyReLU(0.2)(self.linear(x))
        return ypred 

model = Model(features)

learning_rate = 0.01
optimizer = torch.optim.Adam(model.parameters(), lr= learning_rate)
criteria = nn.MSELoss()

epochs = 1000 

for epoch in range(epochs):
    ypreds = model(xtrain)
    loss = criteria(ypreds, ytrain)
    loss.backward()
    optimizer.step()

    optimizer.zero_grad()
    if (epoch+1)%10 == 0:
        print(f"epoch: {epoch+1}, loss: {math.pow(loss, 1/2):.4f}")





    
