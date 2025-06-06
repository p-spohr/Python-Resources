# simple linear regression: regress price on time
# %%

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

import torch

# %%

# get ticker
aapl_tkr = yf.Ticker('AAPL')

# %%

# period is length of time
# 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max,

# download price history
aapl_df = aapl_tkr.history(period= '6mo')

# %%

fig, ax = plt.subplots(1,1)
ax.plot(aapl_df.index, aapl_df.Close)
plt.show()

# %%

# nonlinear regression
# y = w1 * x^1 + ... + wn * x^n + b

class NonLinearRegression01v(torch.nn.Module):
    
    # initialze model class with parameters
    def __init__(self, price_data, *args, **kwargs):

        super().__init__(*args, **kwargs)
        
        self.price_data_mean = torch.tensor(price_data).mean()
        
        self.w1 = torch.nn.Parameter(torch.rand(1, dtype= torch.float32), requires_grad= True)
        self.w2 = torch.nn.Parameter(torch.rand(1, dtype= torch.float32), requires_grad= True)
        self.w3 = torch.nn.Parameter(torch.rand(1, dtype= torch.float32), requires_grad= True)
        self.w4 = torch.nn.Parameter(torch.rand(1, dtype= torch.float32), requires_grad= True)
   
        self.bias = torch.nn.Parameter(self.price_data_mean + torch.normal(mean= torch.tensor(0.0), std= torch.tensor(10.0)), requires_grad= True) 

    
    # define forward function (all models must override base class forward)  
    def forward(self, x):
        return self.w1 * x.pow(1) + self.w2 * x.pow(2) + self.bias
    
# %%

# instantiate linreg model
model_0 = NonLinearRegression01v(price_data = aapl_df.Close.values)

# prepare training data (testing data not needed)
X_train = torch.tensor(range(1,len(aapl_df.Close) + 1), dtype= torch.int16).unsqueeze(1)
y_train = torch.tensor(aapl_df.Close.values, dtype= torch.float32).unsqueeze(1)

print(len(X_train), len(y_train))
print(X_train.shape, y_train.shape)

loss_fn = torch.nn.MSELoss()

# Adam is far superior than SGD in this model by utilizing 
# a much lower learning rate to achieve the results in less epochs
optimizer = torch.optim.Adam(model_0.parameters(), lr= 0.01)

# %%

EPOCHS = 5000
loss_plt = []

for epoch in range(1, EPOCHS):
    
    
    # set model to training mode
    model_0.train()
    
    # forward pass
    y_hat = model_0(X_train)
    
    # calculate the loss
    loss = loss_fn(y_hat, y_train)
    
    # zero out gradients to avoid accumulating gradients
    optimizer.zero_grad()
    
    # calculate gradients of loss function with backpropagation
    loss.backward()

    # update parameters based on loss function gradients
    optimizer.step()
    
    # inference and eval mode
    if epoch % 1 == 0:
        model_0.eval()
        with torch.inference_mode():
            
            y_hat_test = model_0(X_train)
            test_loss = loss_fn(y_hat_test, y_train)
            
            loss_plt.append(test_loss)
            
            print(f'Epoch: {epoch} | Loss: {test_loss:0.2f}')
        
            # ax1 = plt.subplot(111)
            # ax1.plot(X_train, y_train, color= 'blue', label= 'real')
            # ax1.plot(X_train, y_hat_test, color= 'red', label= 'prediction')
            # ax1.legend()
            # plt.show()

# %%

ax1 = plt.subplot(111)
ax1.plot(range(1, len(loss_plt)+1), loss_plt, color= 'blue')
plt.show()

# %%

ax1 = plt.subplot(111)
ax1.plot(X_train, y_train, color= 'blue', label= 'real')
ax1.plot(X_train, y_hat_test, color= 'red', label= 'prediction')
ax1.legend()
plt.show()

# %%


model_0.state_dict()

# %%

model_0.price_data_mean

# %%

aapl_10y = aapl_tkr.history('10y')

# %%

aapl_10y.head()

# %%

aapl_10y.tail()

# %%

plt.plot(aapl_10y.index, aapl_10y.Close.values)
plt.show()

# %%
