l = [[1, 2], [3, 4], [5, 6, 7]]

def reversed(l):
  l.reverse()
  for i in l:
    if type(i) == list:
      reversed(i)
  return l
print(reversed(l))
