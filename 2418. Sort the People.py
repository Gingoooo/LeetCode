class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        output = [n for h, n in sorted(zip(heights, names))][::-1]
        return output