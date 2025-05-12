# chapter 1
# %%

import torch
from torch import nn
import matplotlib.pyplot as plt
import numpy as np

# %%

torch.__version__

# %%

# know parameters
weight = 0.7
bias = 0.3

# initialization
start = 0
end = 1
step = 0.02

# %%

X = torch.arange(start, end, step).unsqueeze(dim=1)
X

# %%

y = weight * X + bias

# %%

X[:10], y[:10]

# %%

len(X), len(y)

# %%

fig, ax = plt.subplots(1,1)
ax.plot(X, y, color='green')
plt.show()

# %%
train_split = int(0.8 * len(X))
X_train, y_train = X[:train_split], y[:train_split]
X_test, y_test = X[train_split:], y[train_split:]

# %%

len(X_train), len(y_train), len(X_test), len(y_test)

# %%

def plot_predictions(train_data, 
                     test_data, 
                     predictions= None):
    """plots training data and test data, and then compares predictions

    Args:
        train_data (torch.Tensor): data for training
        train_labels (str): label for training
        test_data (torch.Tensor): data for testing
        test_labels (str): labels for testing
        predictions (torch.Tensor, optional): model predictions. Defaults to None.
    """
    
    #plt.figure(figsize= (10, 7))
    fig, ax = plt.subplots(1,1)
    ax.scatter(train_data[0], train_data[1], label= 'Training Data')
    ax.scatter(test_data[0], test_data[1], label= 'Testing Data')
    
    if predictions is not None:
        plt.scatter(test_data[0], predictions, label= 'Predictions')
    
    fig.suptitle('ML Data')
    
    ax.legend(prop={'size': 14})
    
    plt.show()
    
# %%

plot_predictions(train_data= (X_train, y_train), test_data= (X_test, y_test))

# %%
# build model
# create linear regression model class

class LinearRegressionModel(nn.Module):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.weights = nn.Parameter(torch.randn(1,
                                                requires_grad= True,
                                                dtype= torch.float))
        
        self.bias = nn.Parameter(torch.randn(1,
                                                requires_grad= True,
                                                dtype= torch.float))
        self.loss = nn.MSELoss
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.weights * x + self.bias

# %%

torch.manual_seed(42)
model_0 = LinearRegressionModel()

# InferenceMode is a context manager analogous to no_grad
# code peforms better by disabling view tracking and version counter bumps
with torch.inference_mode(): # == torch.no_grad()
    y_hat_test = model_0(X_test)

plot_predictions((X_train, y_train), (X_test, y_test), y_hat_test)

# %%

optimizer = torch.optim.Adam(model_0.parameters(), lr= 0.001)
loss_fn = nn.MSELoss()

n_epoch = 0
for epoch in np.arange(start=0,stop=3500, step=1):
    
    # set model to training mode
    model_0.train()
     
    # clears previous gradients
    optimizer.zero_grad()
    
    # get predictions
    y_preds = model_0(X_train)
    loss = loss_fn(y_preds, y_train)
    
    # computes gradients
    loss.backward()
    
    # updates model parameters/weights
    optimizer.step()

    if n_epoch % 500 == 0:
                
        print(f'Loss: {loss}')
        
        with torch.inference_mode(): # == torch.no_grad()
            y_hat_test = model_0(X_test)

        plot_predictions((X_train, y_train), (X_test, y_test), y_hat_test)

    n_epoch += 1

# %%
model_0.eval()
print(model_0.training)
print(model_0.state_dict()['weights'])
print(model_0.state_dict()['bias'])

# %%
