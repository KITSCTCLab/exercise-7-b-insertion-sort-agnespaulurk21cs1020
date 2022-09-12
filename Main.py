from typing import List

def insertionSort(array) -> List[int]:
  for i in range(len(array)-1):
    if array[i]>array[i+1]:
      temp=array[i]
      array[i]=array[i+1]
      array[i+1]=array[i]
  return array

# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
