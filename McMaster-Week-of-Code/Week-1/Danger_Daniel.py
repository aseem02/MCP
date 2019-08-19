# Enter your code here. Read input from STDIN. Print output to STDOUT
#create tree and while creating track start/end
n, m = map(int, raw_input().strip().split())
visited = [0]*n
room_tree = {i: [] for i in range(1, n+1)}
for i in range(m):
    one, two = map(int, raw_input().strip().split())
    room_tree[one].append(two)
    room_tree[two].append(one)
start, end = map(int, raw_input().strip().split())
search = [start]
output = "NO"
while(search != []):
    nxt = search.pop()
    visited[nxt-1] = 1
    for i in room_tree[nxt]:
        if(visited[i-1] == 0):
            if(i == end):
                output = "YES"
                search = []
                break
            else:
                search.append(i)
print output