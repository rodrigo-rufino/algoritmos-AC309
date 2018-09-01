
import math


def first_set_bit_pos(n):
    return 


def construct_bit_tree(data):
    n = len(data)
    # bit tree recebe 0 inicialmente
    bit_tree = [0 for i in range(0, n+1)]
    #atualiza valores da bit tree
    for i in range(n):
        update(bit_tree, i, data[i])

    return bit_tree


def update(bit_tree, index, val):
    n = len(bit_tree)-1
    index += 1
    while(index <= n):
        bit_tree[index] += val
        index += index&-index
    return bit_tree


def get_sum(bit_tree, index):
    n = len(bit_tree)-1
    sum = 0
    index += 1
    while(index > 0):
        sum += bit_tree[index]
        index -= index&-index
    return sum

if __name__ == "__main__":
    data = [3,2,-1,6,5,4,-3]
    n = 4
    print "data =", data
    bit_tree = construct_bit_tree(data)
    print "bit_tree =", bit_tree
    print "sum(", n ,")=", get_sum(bit_tree, n)
    

    
    