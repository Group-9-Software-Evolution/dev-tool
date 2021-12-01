from mne.viz import circular_layout, plot_connectivity_circle

# only for the exemple
import numpy as np


N = 6  # Number of nodes
node_names = [f"N{i}" for i in range(N)]  # List of labels [N]

# Random connectivity
ran = np.random.rand(N, N)
#print(ran)
con = np.where(ran > 0.7, ran, np.nan)  # NaN so it doesn't display the weak links
print(con)
print(type(con))
"""
matrix = [
    [0, 5, 6, 4, 7, 4],
    [5, 0, 5, 4, 6, 5],
    [6, 5, 0, 4, 5, 5],
    [4, 4, 4, 0, 5, 5],
    [7, 6, 5, 5, 0, 4],
    [4, 5, 5, 5, 4, 0],
]

names = ["Action", "Adventure", "Comedy", "Drama", "Fantasy", "Thriller"]
"""

matrix = [
    [0, 5, 6, 4],
    [5, 0, 5, 4],
    [6, 5, 0, 4],
    [4, 4, 4, 0],
]

label_names = ["Action", "Adventure", "Comedy", "Drama"]

def divide_list_by_10(l):
    return list(map(lambda i: float(i/10), l))

print(matrix)
print("con type: " + str(type(con)))
matrix = list(map(lambda l: divide_list_by_10(l), matrix))
matrix = np.array(matrix)
print("matrix type: " + str(type(matrix)))
print(matrix)


nan_matrix = np.where(matrix > 0.1, matrix, np.nan)
print("nan_matrix type: " + str(type(nan_matrix)))


node_angles = circular_layout(label_names, label_names, start_pos=90,
                              group_boundaries=[0, len(label_names) / 2])

#fig, axes = plot_connectivity_circle(con, node_names)
fig, axes = plot_connectivity_circle(nan_matrix, label_names, indices=None, n_lines=None,
                                     node_angles=node_angles,
                                     node_width=None, node_colors=None, facecolor='gray',
                                     textcolor='black', node_edgecolor='black', linewidth=1.5,
                                     colormap='hot', vmin=0.2, vmax=None, colorbar=True, title="Test",
                                     colorbar_size=0.6, colorbar_pos=(-0.3, 0.1), fontsize_title=12,
                                     fontsize_names=8, fontsize_colorbar=8, padding=5.0, fig=None,
                                     subplot=111, interactive=True, node_linewidth=2.0, show=True)