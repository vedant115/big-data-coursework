import json
import numpy as np
from scipy.spatial.distance import euclidean

def parse_centroid(centroid_list):
    """
    Convert a list of dictionaries (each with a single key-value pair) into a single dict.
    Example: [{"0":1.63}, {"334":6.03}, ...] -> {0: 1.63, 334: 6.03, ...}
    """
    centroid = {}
    for d in centroid_list:
        for key, value in d.items():
            # Convert key to integer (if not already) and value to float
            centroid[int(key)] = float(value)
    return centroid

def dict_to_array(d, dim):
    """
    Convert a sparse centroid dictionary into a numpy array of length dim.
    Missing indices will be 0.
    """
    arr = np.zeros(dim)
    for idx, val in d.items():
        if idx < dim:
            arr[idx] = val
    return arr

# Path to your clusterdump output file
input_file = "kmeans_output.txt"

# Parse the file and extract centroids
centroids = []
identifiers = []
max_index = 0

with open(input_file, "r") as f:
    for line in f:
        # Each line is expected to be a JSON object.
        obj = json.loads(line)
        identifiers.append(obj.get("identifier", ""))
        centroid_dict = parse_centroid(obj.get("r", []))
        centroids.append(centroid_dict)
        if centroid_dict:
            max_idx = max(centroid_dict.keys())
            if max_idx > max_index:
                max_index = max_idx

# We set the vector dimension to max_index + 1
dim = max_index + 1

# Convert centroids (dictionaries) into numpy arrays
centroid_arrays = [dict_to_array(c, dim) for c in centroids]

# Compute pairwise Euclidean distances between centroids
n_clusters = len(centroid_arrays)
distance_matrix = np.zeros((n_clusters, n_clusters))

for i in range(n_clusters):
    for j in range(n_clusters):
        if i < j:
            dist = euclidean(centroid_arrays[i], centroid_arrays[j])
            distance_matrix[i, j] = dist
            distance_matrix[j, i] = dist

print("Cluster identifiers:", identifiers)
print("Pairwise Euclidean distance matrix between cluster centroids:")
print(distance_matrix)

# For a simple evaluation:
# - Higher distances indicate better separation.
# You can also compute the average inter-cluster distance:
if n_clusters > 1:
    # Sum distances over upper triangle (excluding diagonal)
    total = 0
    count = 0
    for i in range(n_clusters):
        for j in range(i+1, n_clusters):
            total += distance_matrix[i, j]
            count += 1
    avg_distance = total / count
    print("Average inter-cluster distance: {:.4f}".format(avg_distance))
else:
    print("Only one cluster; cannot compute inter-cluster distance.")
