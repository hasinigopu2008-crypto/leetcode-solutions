class Solution(object):
    def getRow(self, rowIndex):
        triangle=[]
        for i in range(rowIndex+1):
            sublst=[]
            for j in range(i+1):
                if j==0 or j==i:
                    sublst.append(1)
                else:
                    sublst.append(triangle[i-1][j-1]+triangle[i-1][j])
            triangle.append(sublst)
        return triangle[rowIndex]
