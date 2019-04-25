#this function converts between vector form and matrix form (see the examples below)
def convert_vec_mat(vector):
    if type(vector[0]) == list:
        return [vector[i][0] for i in range(len(vector))]
    else:
        return [[vector[i]] for i in range(len(vector))]

#print(convert_vec_mat([1, 2, 3, 4, 5]))
#print(convert_vec_mat([[1], [2], [3], [4], [5]]))