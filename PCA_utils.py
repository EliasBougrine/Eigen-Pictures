# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def plot_gallary(X):
    fig, axs = plt.subplots(3,3, figsize = (4,4))
    axs = axs.ravel()
    for i in range(9):
        axes = axs[i]
        axes.imshow(X[i, :, :], cmap = plt.cm.gray)
        axes.set_xticks(())
        axes.set_yticks(())
    plt.show()