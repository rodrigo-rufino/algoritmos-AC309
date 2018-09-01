# -*- coding: utf-8 -*-

def counting_sort(data, range):
    index = [0]*(range[1]-range[0]+1)
    sorted_array = [0]*len(data)

    # número de ocorrências
    for i in data:
        index[i] += 1

    # soma cumulativa
    for i in xrange(len(index)-1):
        index[i+1] += index[i]

    # colocar posicao correta
    for i in data:
        sorted_array[index[i]-1] = i
        index[i] -= 1

    return sorted_array

if __name__=="__main__":
    data = [1,4,1,2,7,5,2]
    print "Data:", data
    print "Sorted data:", counting_sort(data, [0,9])
