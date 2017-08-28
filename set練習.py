# encoding=utf-8
# set是不能重複的，然後沒有順序，因為是用RBtree做的
set1 = {'P', 'I', 'N', 'E', 'A', 'P', 'P', 'L', 'E'}
set2 = {'B', 'A', 'N', 'A', 'N', 'A'}
print set1
print set2

# &交集 ^XOR
print set1 & set2, set1 | set2, set1 ^ set2
print ((set1|set2) - (set1&set2))
print len(set1), len(set2)
print set2 < {'B','A','N','C'}
print set1 > {'Z'}, set1 > {'P','I'}
set1.add('G')
print set1
