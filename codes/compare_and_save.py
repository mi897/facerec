import helpers

'''
    - Load all images from A folder
    - Load all images from B folder
    - Compare first image with all in B folder
    - If similar put them together in a new folder
    - Do this for all images in folder A with B
'''

# main folder which has all folders 
path_main = "all_faces"

# get image paths of a folder
paths_1 = helpers.get_image_paths(197, path_main)
paths_2 = helpers.get_image_paths(198, path_main)


for p1 in paths_1:
    for p2 in paths_2:
        print("Comparing {} and {}...".format(p1, p2))
        sim = helpers.similarity_score(p1, p2)
        print(sim)