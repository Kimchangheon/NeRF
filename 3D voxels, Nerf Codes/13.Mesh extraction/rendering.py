import torch
import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np

def plot_rays(o: np.array, pt2: np.array):
    fig = plt.figure(figsize=(12, 12))
    ax = plt.axes(projection='3d')

    pt1 = o
    for p1, p2 in tqdm(zip(pt1[::100], pt2[::100])):
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]])

    plt.show()

def compute_accumulated_transmittance(betas):
    accumulated_transmittance = torch.cumprod(betas, 1)     
    return torch.cat((torch.ones(accumulated_transmittance.shape[0], 1, device=accumulated_transmittance.device),
                      accumulated_transmittance[:, :-1]), dim=1)

def rendering(model, rays_o, rays_d, tn, tf, nb_bins=100, device='cpu', white_bckgr=True):
    
    t = torch.linspace(tn, tf, nb_bins).to(device) # [nb_bins]
    delta = torch.cat((t[1:] - t[:-1], torch.tensor([1e10], device=device)))
    
    x = rays_o.unsqueeze(1) + t.unsqueeze(0).unsqueeze(-1) * rays_d.unsqueeze(1) # [nb_rays, nb_bins, 3] = [16000, 100, 3)

    plot_rays(rays_o, x[:, 0, :])
    colors, density = model.intersect(x.reshape(-1, 3), # [nb_rays*nb_bins, 3]=[1600000, 3]
                                      rays_d.expand(x.shape[1], x.shape[0], 3).transpose(0, 1).reshape(-1, 3))
    
    colors = colors.reshape((x.shape[0], nb_bins, 3)) # [nb_rays, nb_bins, 3]
    density = density.reshape((x.shape[0], nb_bins))
    
    alpha = 1 - torch.exp(- density * delta.unsqueeze(0)) # [nb_rays, nb_bins, 1]
        
    weights = compute_accumulated_transmittance(1 - alpha) * alpha # [nb_rays, nb_bins]
    
    if white_bckgr:
        c = (weights.unsqueeze(-1) * colors).sum(1) # [nb_rays, 3]
        weight_sum = weights.sum(-1) # [nb_rays]
        return c + 1 - weight_sum.unsqueeze(-1)
    else:
        c = (weights.unsqueeze(-1) * colors).sum(1) # [nb_rays, 3]
    
    return c