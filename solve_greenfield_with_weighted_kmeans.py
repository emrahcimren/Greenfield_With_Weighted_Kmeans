'''
Function to solve greenfield with weighted k-means
'''

from src import ini


def solve_greenfield_with_weighted_kmeans():

    inputs = ini.IniInput('inputs.ini')
    number_of_clusters_list = range(inputs.minimum_number_of_clusters, inputs.maximum_number_of_clusters)

    #for number_of_clusters in number_of_clusters_list:

    number_of_clusters = 3
    minimum_elements_in_a_cluster = minimum_elements_in_a_cluster_ratio
    maximum_elements_in_a_cluster = maximum_elements_in_a_cluster_ratio




