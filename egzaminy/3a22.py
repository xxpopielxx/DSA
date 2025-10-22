#nlogn

def snow(T, I):
   res = []
   for a,b in I:
       res.append((a,1))
       res.append((b+1,-1))
   res.sort()

   maxi = 0
   current = 0
   for point, change in res:
       current += change
       if current > maxi:
           maxi = current

   return maxi







