import numpy as np
import matplotlib.pyplot as plt

class regression:
  # Constructor
  def __init__(self, name='reg'):
    self.name = name  # Create an instance variable

  def grad_update(self,w_old,lr,y,x):
    w = w_old + (2*lr)*(x@(y-(x.T@w_old)))/(y.shape[0])
    return w

  def error(self,w,y,x):
    return (np.sum(y - (x.T@w)))/(y.shape[0])

  def mat_inv(self,y,x_aug):
    return (np.linalg.pinv(x_aug@x_aug.T))@(x_aug@y)

    # by Gradien descent
  def Regression_grad_des(self,x,y,lr):
    eps = 0.000001
    w_old = np.random.rand(x.shape[0],1)
    error1 = 100001.
    error2 = 100000.
    err = []
    while (error1 - error2)>eps:
      error1 = self.error(w_old,y,x)
      w_old = self.grad_update(w_old,lr,y,x)
      error2 = self.error(w_old,y,x)
      err.append(error1)
    w_pred = w_old
    return w_pred,err


############################################################################################################
# Generation of data
sim_dim = 5
sim_no_data = 1000
x = np.random.uniform(-1,1,(sim_dim,sim_no_data))
print(x.shape)

w = np.array([[1],[2],[3],[5],[9],[3]]) # W=[w0,w1,.....,wM]'
print(w.shape)

# augment feature

x_aug = np.concatenate((np.ones((1,x.shape[1])), x),axis=0)
print(x_aug.shape)


y=x_aug.T @ w  # vector multiplication
print(y.shape)


## corrupted by noise
nois = np.random.uniform(0, 1, y.shape)
y = y + 0.1*nois

### the data (x_aug and y is generated)#####
###############################################################################################################
# by computation (Normal equation)

reg=regression()
w_opt=reg.mat_inv(y,x_aug)
print(w_opt)

# by Gradien descent

lr=0.01
w_pred,err = reg.Regression_grad_des(x_aug, y, lr)
print(w_pred)

plt.plot(err)
plt.show()