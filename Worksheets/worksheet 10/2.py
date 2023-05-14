class TwoSum:
 def __init__(self):
  self.nums = []
  self.target = 0
 def get_input(self):
  self.nums = list(map(int, input("Enter a list of numbers: ").split()))
  self.target = int(input("Enter the target number: "))
 def find_indices(self):
  indices = {}
  for i, num in enumerate(self.nums):
   if self.target - num in indices:
    return [indices[self.target - num],i] 
   indices[num] = i

twosum = TwoSum()
twosum.get_input()
indices = twosum.find_indices()
print(indices)
