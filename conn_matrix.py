import os
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

def conn_matrix(cnctm, is_structural):
	if is_structural:
	  cnctm = np.log(cnctm)

	fig, (ax1) = plt.subplots(nrows=1, figsize=(10,10))
	ax1.imshow(cnctm)
