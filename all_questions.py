# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "because it builds clusters step by step, allowing for more flexibility. In contrast, k-means is sensitive to outliers since the mean is easily influenced by extreme values"

    # type: bool (True/False)
    answers["(b)"] = True 
 
    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Because the agglomerative hierarchical clustering procedures will always produce the same clustering. While on the other handK-means clustering results can vary with different initializations of centroids, leading to potentially different clusterings"

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)

    answers["(c) explain"] = "Because it's just partially true While, K-means is generally more efficient than agglomerative hierarchical clustering in terms of time and memory usage because it requires fewer distance calculations. However, declaring it the most efficient clustering algorithm possible is too broad, as efficiency depends on the context and data, special clustering algorithms can be more efficient for specific needs of the task."

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "Splitting a cluster and reassigning points to the closest centroid will generally result in a lower SSE because points are moved to a centroid that is closer on average, thus reducing the sum of squared distances and increasing the cohesion."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "SSE is a measure of how closely related the points within a cluster are (cohesion). A decrease in SSE indicates that points are closer to their centroid, implying increased cohesion."

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "SSB measures the separation between clusters. An increase in SSB indicates that clusters are further apart, implying increased separation."

    # type: bool (True/False)
    answers["(g)"] = True

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "It's possible to improve cohesion without affecting separation, as these metrics measure different aspects of the clustering quality. Improving one does not guarantee improvement in the other."

    # type: bool (True/False)
    answers["(h)"] = False

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "The sum of SSE (within-cluster variation) and BSS (between-cluster variation) is not necessarily constant across different clusterings because changes in cluster assignments can alter both SSE and BSS in ways that do not sum up to a constant value."

    # type: bool (True/False)
    answers["(i)"] = False

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "Increasing cohesion (decreasing SSE) does not automatically lead to increased separation (increased SSB). They are related but not directly proportional; optimizing one does not inherently optimize the other."

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "since both the centroids are initialized with in the shaded circles respectively, when we will find the actual position of centroids they will reposion them to the centers of their respecteve circles"

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "given the two initial centroids within the two shaded crescents and assuming uniform density within those shapes, k-means should place one centroid in the center of each crescent. The algorithm will minimize the distance of points to centroids, so each crescent will form a separate cluster with the centroid placed at its center due to the symmetry of the points around the initial centroid position."

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "The centroid in the center is equidistant from the points on both sides so its position might not change and hence will be an empty cluster"

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = '4*(R**2)'

    # type: a string that evaluates to a float
    answers["(b) SSE"] = '4*(a**2 + b**2 + R**2)'

    # type: a string that evaluates to a float
    answers["(c) SSE"] = '4*((R/2)**2 + R**2)'

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 0

    # type: int
    answers["(a) Circle (b)"] = 0

    # type: int
    answers["(a) Circle (c)"] = 3

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Since the centroids are initialized closer to the much larger circle C, K-means will likely assign all three centroids to capture the majority of the data points, even though circles A and B are equidistant to B."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 2

    # type: int
    answers["(b) Circle (c)"] = 0

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Here 2 of the initialized centroids are in B and one is in A, when K-means finishes the closest didtances would be in the respective Circles and hence we will get on cluster in A 2 in B and 0 in C."

    # type: int
    answers["(c) Circle (a)"] = 1

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Here 2 of the inialized centroids are in C and one in A and C is far from A and B, Therefore when K-means finishes sinsce the closest points to the centroid would be from their respective circle we will get 1 cluster in A, 2 in C and 0 in B"

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = set('Group A', 'Group B')

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Single linkage clustering aims to minimize the distance between the closest points in two separate clusters."

    # type: set
    answers["(b)"] = set('Group A', 'Group C')

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Complete link clustering considers the farthest points between clusters for merging decisions, aiming to form more compact and well-separated clusters by ensuring all points in a cluster are relatively close to all points in another cluster before merging."

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = set('B', 'C', 'E', 'F', 'I', 'J', 'L', 'M')

    # type: set
    answers["(a) boundary"] = set('D', 'G')

    # type: set
    answers["(a) noise"] = set('A', 'H')

    # type: set
    answers["(b) cluster 1"] = set('D', 'B', 'C', 'E', 'F', 'G')

    # type: set
    answers["(b) cluster 2"] = set('I', 'J', 'L', 'M')

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = set('B','C','D','E','F','G','I','J','L','M')

    # type: set
    answers["(c)-a boundary"] = set('A', 'H')

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = set('B','C','D','E','F','G','H','I','J','L','M')

    # type: set
    answers["(c)-b cluster 2"] = set('A')

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Because the categories are imbalanced the most in the Cluster 1"

    # type: string
    answers["(b)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "This has the most uniform distribution of the categories therefore it has the lowest entropy"

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "The bright blue color along the diagonal elements shows strong connections within clusters. This means that data points within a cluster are very close together, indicating a high degree of consistency within each group."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "The different colors in the off-diagonal cells (those that are not directly on the diagonal) show that rows 1 and 3 belong to clusters A and C, respectively. Similarly, rows 2 and 4 are associated with clusters B and D based on the same color patterns."

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "The diagonal entries are a striking blue, much more so than the rest. This suggests that clusters B and C are highly cohesive, meaning the data points within these clusters are tightly grouped together."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "Rows 1 and 4 have diverse colors which suggests varying distances from other clusters, with weaker internal relationships (less defined diagonals). On the other hand rows 2 and 3 have Identical colors imply equal distances to two clusters, but potentially further from a third compared to rows 1 and 4."

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "The striking blue diagonals in clusters B and C reveal strong internal cohesion, suggesting closer relationships within these groups."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "Each row shows two clusters linked by matching off-diagonal colors, while the remaining color indicates a cluster with a weaker connection. This suggests varying degrees of closeness between different clusters."

    # type: string
    answers["(b) Row 1"] = "Cluster A"

    # type: string
    answers["(b) Row 2"] = "Cluster B"

    # type: string
    answers["(b) Row 3"] = "Cluster C"

    # type: string
    answers["(b) Row 4"] = "Cluster D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "Mismatched colors across all off-diagonal entries reveal varying distances from other clusters for Cluster A. This, along with a weaker diagonal, suggests lower internal cohesion within this cluster."

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "Row 2 pinpoints Cluster B with two matching off-diagonal colors, signifying equal distances, likely between B and A, and B and C. Despite strong internal cohesion (clear diagonal), B remains farther from D."

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "Row 3 signifies Cluster C with a strong diagonal, indicating high internal cohesion. Two matching off-diagonal colors point to equal distances, likely between C and B, and C and D. However, C remains farther from A."

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "Cluster D stands out with mismatched off-diagonal colors, revealing unequal distances to other clusters. Notably, it's closest to C, followed by B, and furthest from A. This weaker internal connection (less defined diagonal) reinforces its classification as Cluster D."

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}
# type: list
    answers["(a)"] = ['Overlapping', 'Partial', 'Hierarchical']

    # type: list
    answers["(b)"] = ['Complete', 'Exclusive', 'Partitional']

    # type: list
    answers["(c)"] = ['Complete', 'Partitional', 'Fuzzy']

    # type: list
    answers["(d)"] = ['Overlapping', 'Hierarchical','Partial']

    # type: list
    answers["(e)"] = ['Partial','Exclusive','Partitional']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Students with similar scores and mark levels can also be grouped together in a hierarchical structure."
    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "No"

    # type: string
    answers["(a) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "in figure (b) since the smile, nose and eyes are densly populted areas the initialized cetroids will move towards these dense areas"

    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-means will be able torecognise smile, nose and eyes but it will also be affected by the lower density areas as well"


    # type: string
    answers["(c)"] = "DBSCAN"

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
