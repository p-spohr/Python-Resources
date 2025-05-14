# Improved Model Based on Course
# %%

from torch import nn
from torch import cuda
from torch import optim
from torch import tensor, round, sigmoid, eq, inference_mode, float64, float32

from helper_functions import plot_decision_boundary

# import matplotlib.pyplot as plt
from matplotlib.pyplot import subplots, show

from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split

# %%

device = 'cuda' if cuda.is_available() else 'cpu'
print(device)
print(cuda.get_device_name())

# %%

X, y = make_circles(n_samples=1000, noise= 0.3, factor= 0.01, random_state=42)
fig, ax = subplots(1,1)
ax.scatter(X[:,0], X[:,1], c= y)
show()

# %%

X_tn, X_tt, y_tn, y_tt = train_test_split(X, y, test_size= 0.2, random_state= 42)

# %%

X_tn, X_tt = tensor(X_tn, device= device, dtype= float64), tensor(X_tt, device= device, dtype= float64)
y_tn, y_tt = tensor(y_tn, device= device, dtype= float64), tensor(y_tt, device= device, dtype= float64)

# %%

print(X_tn.dtype)
print(X_tt.dtype)
print(y_tn.dtype)
print(y_tt.dtype)

# %%

print(X_tn.shape)
print(X_tt.shape)
print(y_tn.shape)
print(y_tt.shape)

# %%

y_tn = y_tn.detach().clone().unsqueeze(1).to(float64)
y_tt =  y_tt.detach().clone().unsqueeze(1).to(float64)

# %%

print(X_tn.shape)
print(X_tt.shape)
print(y_tn.shape)
print(y_tt.shape)

# %%

class CircleModelV1(nn.Module):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layer_1 = nn.Linear(2,10)
        self.layer_2 = nn.Linear(10,10)
        self.layer_3 = nn.Linear(10,1)
        
    def forward(self, x):
        # z = self.layer_1(x)
        # z = self.layer_2(x)
        # z = self.layer_3(x)
        
        # leverages speed ups
        return self.layer_3(self.layer_2(self.layer_1(x)))
        
model_1 = CircleModelV1().to(device).to(float64)

# calculate accuracy
def accuracy_fn(y_true, y_pred):
    correct = eq(y_true, y_pred).sum().item()
    return (correct / len(y_pred)) * 100

loss_fn = nn.BCEWithLogitsLoss()
optimizer = optim.SGD(model_1.parameters(), lr= 0.1)

epochs = 1000

# %%

for epoch in range(epochs):
    model_1.train()

    y_logits = model_1(X_tn)
    y_pred = round(sigmoid(y_logits))
    
    loss = loss_fn(y_logits, y_tn)
    acc = accuracy_fn(y_pred= y_pred, y_true= y_tn)
    
    optimizer.zero_grad()

    loss.backward()

    optimizer.step()
    
    model_1.eval()
    with inference_mode():
        test_logits = model_1(X_tt)
        test_pred = round(sigmoid(test_logits))
        
        test_loss = loss_fn(test_logits, y_tt)
        test_acc = accuracy_fn(y_true= y_tt, y_pred= test_pred)
        
        
    if epoch % 100 == 0:
        print(f'E: {epoch} | L: {round(loss, decimals= 2)} | A: {acc} | TL: {round(test_loss, decimals= 2)} | TA: {test_acc}')
    
    
# %%

plot_decision_boundary(model_1.to(float32), X_tt, y_tt)

# %%
