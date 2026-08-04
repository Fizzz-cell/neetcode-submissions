class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
      count = {}

      for i in nums:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

      sorted_nums = sorted(count, key=lambda i: count[i], reverse=True)

      return sorted_nums[:k]


        