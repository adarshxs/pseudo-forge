'''There is a horizontal row of n cubes. The length of each cube is given.
You need to create a new vertical pile of cubes.
The new pile should follow these directions:
If cube[i] is on top of cube[j] then sideLength[j]>sideLength[i].
When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time.
Print Yes if it is possible to stack the cubes. Otherwise, print No.'''


from collections import deque
t = int(input())
for i in range(t):
    n = int(input())
    l = deque(map(int, input().split()))
    s = [max(l[0], l[-1])]
    flag = True
    for i in range(len(l)):
        if l[0]>=l[-1] and l[0]<=s[-1]:
            s.append(l[0])
            l.popleft()
        elif l[0]< l[-1] and l[-1]<=s[-1]:
            s.append(l[-1])
            l.pop()
        else:
            flag = False
            break
    d = {True: 'Yes', False: 'No'}
    print(d[flag])
