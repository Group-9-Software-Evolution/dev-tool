from mne.viz import circular_layout, plot_connectivity_circle

# only for the exemple
import numpy as np
import json


def build_matrix(jsonobject):
    # Read the json file into a python object
    #file = open(jsonobject,)
    #data = json.load(file)
    #file.close()

    file = open(jsonobject, "r", encoding="utf8")
    reached = False

    nodelist = {}
    singelton = True
    matrix = [[]]
    filenames = []

    for line in file:
        if not reached:
            if ">];" in line:
                reached = True
        else:
            if "subgraph cluster_" in line:
                break
            if "->" not in line:
                if "}" == line[0]:
                    line = line[1:]
                nodeinfo = line.split("[label=")
                nodename = nodeinfo[0]
                if " " in nodename:
                    nodename = nodename[:-1]
                temp = nodeinfo[1].split('name=\"')
                filename = temp[1].split("::")[0]
                # funktionsnamn ??
                # classnamn?
                nodelist[nodename] = {}
                nodelist[nodename].update({"filename": filename})
                if filename not in filenames:
                    filenames.append(filename)
            else:
                if singelton:
                    length = len(filenames)
                    matrix = np.zeros([length, length])
                    singelton = False
                nodes = line.split(" -> ")
                firstnode = nodes[0]
                secondnode = nodes[1].split(" [color=")
                secondnode = secondnode[0]
                file_firstnode = nodelist[firstnode].get("filename")
                file_secondnode = nodelist[secondnode].get("filename")
                index_of_first = filenames.index(file_firstnode)
                index_of_second = filenames.index(file_secondnode)
                matrix[index_of_first][index_of_second] = matrix[index_of_first][index_of_second] + 1
                matrix[index_of_second][index_of_first] = matrix[index_of_second][index_of_first] + 1
    return matrix, filenames

def print_matrix(matrix, filenames):
    matrix = np.array(matrix)
    nan_matrix = np.where(matrix > 0.1, matrix, np.nan)

    #node_angles = circular_layout(filenames, filenames, start_pos=90,
    #                              group_boundaries=[0, len(filenames) / 2])

    #fig, axes = plot_connectivity_circle(con, node_names)
    fig, axes = plot_connectivity_circle(nan_matrix, filenames, indices=None, n_lines=None,
                                         node_angles=None,
                                         node_width=None, node_colors=None, facecolor='black',
                                         textcolor='white', node_edgecolor='gray', linewidth=3,
                                         colormap='hot', vmin=0.2, vmax=None, colorbar=True, title=None,
                                         colorbar_size=0.8, colorbar_pos=(0.6, 0.5), fontsize_title=22,
                                         fontsize_names=18, fontsize_colorbar=18, padding=2.5, fig=None,
                                         subplot=111, interactive=True, node_linewidth=2.0, show=True)

    # fname_fig = data_path + '/MEG/sample/plot_inverse_connect.png'
    fig.savefig("nme-diagram", facecolor='black')




def testmatrix():
    matrix = [
        [0, 0, 0, 4, 7, 0],
        [0, 0, 5, 4, 6, 5],
        [0, 5, 0, 4, 5, 5],
        [4, 4, 4, 0, 0, 5],
        [7, 6, 5, 0, 0, 4],
        [0, 5, 5, 5, 4, 0],
    ]

    label_names = ["Action", "Adventure", "Comedy", "Drama", "Fantasy", "Thriller"]
    #matrix = list(map(lambda l: divide_list_by_10(l), matrix))
    matrix = np.array(matrix)
    nan_matrix = np.where(matrix > 0.1, matrix, np.nan)

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

def divide_list_by_10(l):
    return list(map(lambda i: float(i/10), l))



if __name__ == '__main__':\caption{Tasks done in sprint 2.} \label{tab:sprint2}
    #if sys.argv[1:] == ['init']:
    #    build_tram_network("../data/tramstops.json", "../data/tramlines.txt")
    #else:
    #testmatrix()
    matrix, filenames = build_matrix("code2flow-master/out.json")
    print_matrix(matrix, filenames)