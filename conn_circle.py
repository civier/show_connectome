import matplotlib.pyplot as plt
import numpy as np

def conn_circle(cnctm, labels):
	num_labels = len(labels)

	# Calculate the positions of nodes on the circle
	angles = np.linspace((np.pi / 2) + (2 * np.pi / num_labels / 2), (np.pi / 2) + (2 * np.pi / num_labels / 2) + (2 * np.pi), num_labels, endpoint=False)
	x = np.cos(angles)
	y = np.sin(angles)

	# Initialise figure
	fig, ax = plt.subplots(figsize=(10, 10))

	# Plot nodes
	for i in range(num_labels):
	  ax.scatter(x[i], y[i], s=100, c='blue', zorder=5)

	# Plot edges, assuming matrix is upper right
	for i in range(num_labels):
	    for j in range(i + 1, num_labels):
	        if cnctm[i,j] > 0:  # Only plot edges with strength greater than 0
	            if cnctm[i,j] != np.nan:   # Only plot edges different than nan
	              ax.plot([x[i], x[j]], [y[i], y[j]], 'k-', alpha=cnctm[i, j] / cnctm.max(), lw=2)

	# Plot labels next to nodes
	for i in range(num_labels):
	  angle = angles[i] * 180 / np.pi
	  ax.text(x[i], y[i], '  '+labels[i], fontsize=12, ha='left', va='center', color='black',
	                rotation=angle, rotation_mode='anchor')

	# Finalise figure
	ax.set_aspect('equal')
	ax.axis('off')
	plt.show()
