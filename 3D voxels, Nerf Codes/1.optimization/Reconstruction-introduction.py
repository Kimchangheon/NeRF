import torch
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from simulator import simulator

x0 = torch.tensor([0, 0])
v0 = torch.tensor([10, 10])

x = torch.cat((x0, v0))

y = simulator(x, t=3)

all_pos = []
for t in range(100) :
    y = simulator(x, t=t/20)
    all_pos.append(y[:2].tolist())
all_pos = np.array(all_pos)
plt.scatter(all_pos[:,0], all_pos[:,1])


b = simulator(x, t=3)
print(b)

x = torch.tensor([0., 0., 0., 0.], requires_grad=True)
optimizer = torch.optim.SGD({x}, lr=1e-4)

training_loss = []
for epoch in range(10000):
    Ax = simulator(x, t=3)
    loss = ((Ax - b) ** 2).mean()

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    training_loss.append(loss.item())

plt.plot(training_loss)
