# class Solution:

numbers = [ 1, 2 , 3, 4 ,5 ,6 ]
def solution(lst:list , sum:int)->None:
    indexes = {}
    for index , value in enumerate(numbers):
        sol = sum - value
        if sol in indexes:
            return [indexes[sol] , index]
        indexes[value] = index
    return None

answer = solution(numbers, 11)
print (answer)
    
