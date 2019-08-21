# Enter your code here. Read input from STDIN. Print output to STDOUT
g, m, n = map(int, raw_input().strip().split())

layer = -1
lookup = [None]*g
glyphs = {}
for i in range(m):
    one, two = map(int, raw_input().strip().split())
    if (lookup[one] == None and lookup[two] == None):
        layer += 1
        glyphs[layer] = [one, two]
        lookup[one] = layer
        lookup[two] = layer
    elif (lookup[one] == None):
        glyphs[lookup[two]].append(one)
        lookup[one] = lookup[two]
    elif (lookup[two] == None):
        glyphs[lookup[one]].append(two)
        lookup[two] = lookup[one]
    elif (lookup[one] != lookup[two]):
        #fuse them
        temp = lookup[one]
        for j in glyphs[lookup[one]]:
            lookup[j] = lookup[two]
        glyphs[lookup[two]] += glyphs[temp]
        del glyphs[temp]

count = 0
for i in range(n):
    l = int(raw_input().strip())
    w1 = map(int, raw_input().strip().split())
    w2 = map(int, raw_input().strip().split())
    count +=1
    for j in range(l):
        if((lookup[w1[j]] != lookup[w2[j]] or (lookup[w1[j]] == None and w1[j] != w2[j]))):
            count -= 1
            break
print count