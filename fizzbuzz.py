# Approach: loop 1 to n, check divisible by 15 first, then 3, then 5
# Time O(n), space O(n) for the result list
class Solution(object):
    def fizzBuzz(self, n):
        answer=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                answer.append("FizzBuzz")
            elif i%3==0:
                answer.append("Fizz")
            elif i%5==0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer
