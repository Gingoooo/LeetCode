class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        dic = {1: 0, 0: 1}
        for idx, row in enumerate(image):
            image[idx] = [dic[n] for n in row[::-1]]
        return image