import os

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
        print(sorted_arr)

        for i in sorted_arr:
            print(i)
    #print(sorted_arr)
    #import pdb; pdb.set_trace()
    #sorted_tuples = []
    #for elem in sorted_arr:
     #   val = None
      #  val = [item for item in p_t if item[1] == elem]
       # sorted_tuples.append(val)

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


paths_sorted = quicksort(paths)

print(paths)
print("\n")
print(paths_sorted)