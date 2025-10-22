def binary(T):
   n = len(T)
   l = 0
   r = n-1
   while l<=r:
       temp = (l+r)//2
       if T[temp] == temp:
           l = temp + 1
       else:
           r = temp - 1
   return l



T = [0, 1, 2, 4, 5, 8]

print(binary(T))