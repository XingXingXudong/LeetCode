# coding: utf-8

class Solution(object):

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if len(image) == 0:
            return [[]]

        self._old_color = image[sr][sc]
        if newColor == self._old_color:
            return image

        self.image = image
        self._stack = list()
        self._traversed = set()
        self._rows = len(image)
        self._cols = len(image[0])
        self._stack.append((sr, sc))
        self._traversed.add((sr, sc))

        while self._stack:
            cur = self._stack.pop()
            image[cur[0]][cur[1]] = newColor
            self._helper(cur)
        return image

    def _helper(self, coord):
        for new_coord in [(coord[0], coord[1] + 1), (coord[0], coord[1] - 1), 
                (coord[0] - 1, coord[1]), (coord[0] + 1, coord[1])]:
            if 0 <= new_coord[0] < self._rows and \
                    0 <= new_coord[1] < self._cols and \
                    self.image[new_coord[0]][new_coord[1]] == self._old_color and \
                    new_coord not in self._traversed:
                self._stack.append(new_coord)
                self._traversed.add(new_coord)

    def recursive(self, image, sr, sc, newColor):
        self._image = image
        self._old_color = image[sr][sc]
        self._recursived_set = set()
        self._recursive(self._image, sr, sc, newColor)
        return self._image

    def _recursive(self, img, r, c, nc):
        if img[r][c] == self._old_color and (r, c) not in self._recursived_set:
            img[r][c] = nc
            self._recursived_set.add((r, c))
            if 0 <= r-1 < len(img):
                self._recursive(img, r-1, c, nc)
            if 0 <= r+1 < len(img):
                self._recursive(img, r+1, c, nc)
            if 0 <= c-1 < len(img[0]):
                self._recursive(img, r, c-1, nc)
            if 0 <= c+1 < len(img[0]):
                self._recursive(img, r, c+1, nc)

if __name__ == '__main__':
    image = [[1,1,1],[1,1,0],[1,0,1]]
    solution = Solution()
    rtn = solution.recursive(image, 1, 1, 2)
    print(rtn)





        

