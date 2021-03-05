# import autograd.numpy as np
from minimc import neg_log_normal, hamiltonian_monte_carlo
import matplotlib.pyplot as plt

samples = hamiltonian_monte_carlo(2_000, neg_log_normal(0, 0.1), initial_position=0.)
plt.hist(samples)
plt.show()
x=1
