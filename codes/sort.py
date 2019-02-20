import os
'''

['182.jpg', '164.jpg', '46.jpg', '80.jpg', '212.jpg']

# make tuples for mapping
[('182.jpg', 182), ('164.jpg', 164), ('46.jpg', 46), ('80.jpg', 80), ('212.jpg', 212)]

[46, 80, 164, 182, 212]
'''

def quicksort(p_t):

    arr = [num[1] for num in p_t]
    #import pdb; pdb.set_trace()

    if len(arr) < 2:
        return arr
    
    else:
        pivot = arr[0]
        pivot_tuple = [item for item in p_t if item[1] == pivot]
        smaller, bigger = [], []
        for elem in arr[1:]:
            if elem <= pivot:
                the_culprit = [item for item in p_t if item[1] == elem]
                smaller.append(the_culprit[0])
            else:
                the_culprit = [item for item in p_t if item[1] == elem]
                bigger.append(the_culprit[0])

        sorted_arr = quicksort(smaller) + [pivot] + quicksort(bigger)
        return sorted_arr

# read all paths in directory
paths_to_images= os.listdir("frames")[:5]
#print(paths_to_images)

paths = []

for p in paths_to_images:

    path_tuple = None
    count = int(p[:-4])
    path_tuple = (p, count)
    paths.append(path_tuple) 


arr_sorted = quicksort(paths)
paths_sorted = []


for p in arr_sorted:
    val = [item for item in paths if item[1] == p]
    val.append(paths_sorted)

print(paths_sorted)

print(paths_to_images)
#print("\n")
#print(arr_sorted)