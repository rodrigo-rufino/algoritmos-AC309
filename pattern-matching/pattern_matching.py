# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

def check_pattern(i, p):
    count = 0
    for j in range(len(p)):
        if text[i+count] == p[count]:
            count = count + 1
        else:
            return False
    return True


def pattern_matching(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        if check_pattern(i, pattern):
            index.append(i)
    print "Padrao encontrado em", index   
    
def pattern_matching_regex():
    
    return


if __name__=="__main__":
    index = []
    text = ['a','a','b','a','a','c','a','a','d','a','a','b','a','a','b','a']
    pattern = ['a','a','b','a']
    
    pattern_matching(text, pattern)
    
    
