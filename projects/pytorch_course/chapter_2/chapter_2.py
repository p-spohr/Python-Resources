# chapter 2
# %%

import sklearn as skl
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split

import torch as th
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

# %%

n_samples = 1000

X, y = make_circles(n_samples,
                    noise= 0.03,
                    factor= 0.5,
                    random_state= 42)

# %%

fig, ax = plt.subplots(1,1)
ax.scatter(X[:,0], X[:,1], c= y)
plt.show()

# %%

X_raw = th.from_numpy(X)
y_raw = th.from_numpy(y)

# %%

# check to see if CUDA is available
device = 'cuda' if th.cuda.is_available() else 'cpu'
print(th.cuda.get_device_name()) if device == 'cuda' else print('on cpu')

# %%

# subclass nn.Module
# create nn.Linear model
# define forward model
# instantiate instance of model

class CircleModelV00(th.nn.Module):
    
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        
        # linear layers
        # first in_features are the input features from data
        # first out_features are the number nodes in the next hidden layer
        self.layer_1 = th.nn.Linear(in_features= 4, out_features= 5, dtype= th.float64)
        
        # the last out_features need to match up with the target labels
        self.layer_2 = th.nn.Linear(in_features= 5, out_features= 1, dtype= th.float64)
    
    # overwrite forward method with own forward function
    def forward(self, x: th.Tensor):
        return self.layer_2(self.layer_1(x))
    

# instantiate the model
model_00 = CircleModelV00().to(device)

# loss function and optimizer
# this loss combines a Sigmoid layer and the BCELoss
loss_fn = th.nn.BCEWithLogitsLoss()
optimizer = th.optim.SGD(model_00.parameters(), lr= 0.01)

# calculate accuracy
def accuracy_fn(y_true, y_pred):
    correct = th.eq(y_true, y_pred).sum().item()
    return (correct / len(y_pred)) * 100

X_tn, X_tt, y_tn, y_tt = train_test_split(X_raw,
                                          y_raw,
                                          test_size= 0.2,
                                          random_state= 42)

# train model
th.manual_seed(42)
th.cuda.manual_seed(42)
epochs = 1000

# prepare training and testing data
X_tn, y_tn = X_tn.to(device), y_tn.to(device).unsqueeze(1).to(th.float64)
X_tt, y_tt = X_tt.to(device), y_tt.to(device).unsqueeze(1).to(th.float64)

# %%
# improve model prediction by using squared, sin, cos on input data

X_tn_base = X_tn
X_tt_base = X_tt

X_tn = th.hstack([X_tn, th.pow(X_tn_base, 2)])
X_tt = th.hstack([X_tt, th.pow(X_tt_base, 2)])

# X_tn = th.hstack([X_tn, th.sin(X_tn_base)])
# X_tt = th.hstack([X_tt, th.sin(X_tt_base)])

# X_tn = th.hstack([X_tn, th.cos(X_tn_base)])
# X_tt = th.hstack([X_tt, th.cos(X_tt_base)])

print(X_tn_base.shape)
print(X_tt_base.shape)
print(X_tn.shape)
print(X_tt.shape)

# %%

# start training
for epoch in range(epochs):
    # training mode
    model_00.train()

    # forward pass
    y_logits = model_00(X_tn)
    y_pred = th.round(th.sigmoid(y_logits))

    # calculate loss
    loss = loss_fn(y_logits, y_tn) # BCEWithLogitsLoss, expects raw logits (has sigmoid layer before)
    acc = accuracy_fn(y_true=y_tn, y_pred=y_pred)

    # optimizer zero grad
    optimizer.zero_grad()

    # loss backward (backpropagation)
    loss.backward()

    # optimizer step (gradient descent and update weights)
    optimizer.step()
    
    # testing
    # eval mode
    model_00.eval()
    
    with th.inference_mode():
        test_logits = model_00(X_tt)
        test_pred = th.round(th.sigmoid(test_logits))
        
        # test loss and acc
        test_loss = loss_fn(test_logits, y_tt)
        test_acc = accuracy_fn(y_true=y_tt, y_pred=test_pred)
        
    # print out info
    if epoch % 10 == 0:
        print(f'Epoch: {epoch} | Loss: {loss:.02f} | Test Loss: {test_loss:.02f} | Test acc: {test_acc}')

# %%

th.manual_seed(123)
x_st = np.linspace(-1,1,1000)
y_rand = (th.randint(high=100, low=-100, size= (1000,1)).to(th.float64) / 100).numpy()

# %%

fig, ax = plt.subplots(1,1)
ax.scatter(x_st, y_rand)
plt.show()

# %%

# use permute not reshape!!!
# permute is like transpose but with more dimensions
# reshape just arranges things sequentially along the rows
X_rand_test = th.tensor([x_st, y_rand.flatten()]).permute(1,0)

# %%

X_rand_base = X_rand_test.detach().clone().requires_grad_(True)

print(X_rand_base.shape)

# %%

X_rand_test = th.hstack([X_rand_test, th.pow(X_rand_base, 2)])
# X_rand_test = th.hstack([X_rand_test, th.sin(X_rand_base)])
# X_rand_test = th.hstack([X_rand_test, th.cos(X_rand_base)])

print(X_rand_test.shape)

# %%

X_rand_test

# %%

model_00.eval()
with th.inference_mode():
    y_circle_logits = model_00(X_rand_test.to(device))
    y_circle_pred = th.round(th.sigmoid(y_circle_logits))

# %%

fig, ax = plt.subplots(1,1)
ax.scatter(x_st, y_rand, c= y_circle_pred.cpu().numpy().flatten())
plt.show()
