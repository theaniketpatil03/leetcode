string = 'nanbanananan'

class Solution:

    def getCommonChar(self):
        res = ''
        counter = 0
        condition = True
        while condition:
            if string[counter] == string[-(counter+1)]:
                res += string[counter]
                counter +=1
            else:
                condition = False

        return res

sol = Solution()
print(sol.getCommonChar())

            