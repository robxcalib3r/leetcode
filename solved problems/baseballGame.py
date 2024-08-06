class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        sum = []
        ans = 0
        for i in range(len(operations)):
            if operations[i] == "C":
                sum.pop()
            elif operations[i] == "D":
                sum.append(2 * sum[-1])
            elif operations[i] == "+":
                sum.append(sum[-2] + sum[-1])
            else:
                sum.append(int(operations[i]))
            
            print(sum)
        for i in sum:
            ans += i
        print(ans)
        return ans
    
if __name__ == "__main__":
    ops = ["5","2","C","D","+"]
    # ops = ["5","-2","4","C","D","9","+","+"]

    sol = Solution()
    sol.calPoints(ops)