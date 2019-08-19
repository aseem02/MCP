# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input().strip())
for i in range(n):
    a, b, x = map(int, raw_input().strip().split())
    print a*b*(x**(b-1))