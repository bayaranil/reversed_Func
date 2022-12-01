# reversed_Func
Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.

Write a function that reverses the elements inside the given list.  If the elements inside the list also contain the list, reverse their elements as well.
Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]




```ruby
l = [[1, 2], [3, 4], [5, 6, 7]]

def reversed(l):
  l.reverse()
  for i in l:
    if type(i) == list:
      reversed(i)
  return l
print(reversed(l))
```
