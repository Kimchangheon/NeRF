import numpy as np
import matplotlib.pyplot as plt

H = 400
W = 400
f = 1200

rays_o = np.zeros((H*W, 3))
rays_d = np.zeros((H*W, 3))

u = np.arange(W)
v = np.arange(H)
u, v = np.meshgrid(u, v)

dirs = np.stack((u - W / 2,
                 -(v - H / 2),
                 - np.ones_like(u) * f), axis=-1)
rays_d = dirs / np.linalg.norm(dirs, axis=-1, keepdims=True)
rays_d = rays_d.reshape(-1, 3)
print()


def plot_rays(o, d, t):
    fig = plt.figure(figsize=(12, 12))
    ax = plt.axes(projection='3d')

    pt1 = o
    pt2 = o + t * d

    # for p1, p2 in zip(pt1[::100], pt2[::100]):
    #     plt.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]])
    for p1, p2 in zip(pt1, pt2):
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]])
    plt.show()

plot_rays(rays_o, rays_d, 1)
