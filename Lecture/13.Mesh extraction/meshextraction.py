import mcubes
import trimesh
import torch
import torch.nn as nn
import numpy as np

import os
import imageio
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader

from dataset import get_rays
from rendering import rendering
from model import Voxels, Nerf
from ml_helpers import training

device = 'cpu'
tn = 8.
tf = 12.
model = torch.load('model_voxels').to(device)

N = 100
scale = 1.5

x = torch.linspace(-scale, scale, N)
y = torch.linspace(-scale, scale, N)
z = torch.linspace(-scale, scale, N)

x, y, z = torch.meshgrid((x, y, z))

xyz = torch.cat((x.reshape(-1, 1), # 1000000, 1
                 y.reshape(-1, 1),
                 z.reshape(-1, 1)), dim=1)

with torch.no_grad():
    _, density = model.forward(xyz.to(device), torch.zeros_like(xyz).to(device))

density = density.cpu().numpy().reshape(N, N, N)

vertices, triangles = mcubes.marching_cubes(density, 30 * np.mean(density))
mesh = trimesh.Trimesh(vertices / N, triangles)
mesh.show()