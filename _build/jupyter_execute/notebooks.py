#!/usr/bin/env python
# coding: utf-8

# # You can show some codes & plots

# You can use Jupyter Lab to present code and plots. Sometimes, this is even used in [published research](https://www.nature.com/articles/d41586-018-07196-1/) ! 

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed()

N = 10
data = np.logspace(0, 1, 100) + np.random.randn(100)

plt.plot(data,'.')


# And even in some cases have a user-interface for the plots; e.g. by using nilearn.

# In[2]:


from nilearn import datasets, plotting
from matplotlib import cm
data = datasets.fetch_haxby().anat[0]
plotting.view_img(stat_map_img=data,colorbar=False)

