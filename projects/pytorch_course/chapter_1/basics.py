# Check PyTorch and CUDA

# %%

import torch

# %%

torch.__version__

# %%

torch.cuda.is_available()

# %%

torch.cuda.device_count()

# %%

torch.version.cuda

# %%

torch.cuda.current_device()

# %%

torch.cuda.get_device_name()

# %%

torch.cuda.get_device_capability()

# %%

torch.tensor(1)

# %%

torch.tensor([1,1])

# %%
torch.manual_seed(123)
INT_TENSOR = torch.randint(size= [2,4,2], high= 4, low= 0)
INT_TENSOR

# %%

INT_TENSOR.sum(dim=[2,0])

# %%

XTensor = torch.rand(size=[7,7])

# %%

YTensor = torch.rand(size=[1,7])

# %%

XTensor @ YTensor.T

# %%

torch.manual_seed(123)

# %%

torch.cuda.manual_seed(1234)

# %%

ZTensor = torch.rand(size=[2,3], device= 'cuda')

# %%

ZZTensor = ZTensor

# %%

ZZTensor = 0

# %%

ZTensor

# %%

ZTensor.is_cuda

# %%

ATensor = torch.rand(size= [2, 3], device= 'cuda')

# %%

ZATensor = ZTensor @ ATensor.T

# %%

ZATensor.max(), ZATensor.min()

# %%

ZATensor.argmax(), ZATensor.argmin()

# %%
torch.manual_seed(7)
BTensor = torch.rand([1, 1, 1, 10])

# %%

print(BTensor.reshape(10)[0])
print(BTensor.reshape(10)[1])
print(BTensor.reshape(10).shape)

# %%
