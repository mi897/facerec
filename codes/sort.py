'''
Sorts a list of filenames based on the number before the '.' (dot)

Input: ['182.jpg', '164.jpg', '46.jpg', '80.jpg', '212.jpg']
Output: ['46.jpg', '80.jpg', '164.jpg', '182.jpg', '212.jpg']
'''

# Helper function to extract the number from the filename
def get_number(filename):
    return int(filename[:filename.find('.')])

# Sort the array paths using the number returned by the function get_number
def sort_paths(paths):
    paths.sort(key = get_number)
    return paths