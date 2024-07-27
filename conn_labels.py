import os
import sys
import math
import numpy as np
import pandas as pd

def conn_labels(cnctm, labels):

	# Convert the numpy matrix to panda
	cnctm_pd = pd.DataFrame(cnctm, index=labels, columns=labels)

	# Display the DataFrame
	print(cnctm_pd)
