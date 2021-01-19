##############################################
#This solution will not work because of memo

# def canSum(targetSum, numbers, memo = None):
#   if memo is None: memo = {}

#   if (targetSum in memo): 
#     return memo[targetSum]
#   if (targetSum == 0): 
#     return True
#   if (targetSum < 0): 
#     return False
    
#   for num in numbers: 
#     remainder = targetSum - num
#     if (canSum(remainder, numbers,memo)==True):
#         memo[targetSum] = True
#         return True
    
#     memo[targetSum] = False
#     return False, memo

# print(canSum(7,[2,3])) # True
# print(canSum(7,[5,3,4,7])) # True
# print(canSum(7,[2,4])) # False
# print(canSum(8,[2,3,5])) # True
# print(canSum(300,[7,14])) # False

###########################################
# def canSum(targetsum, numbers):
#     memo = dict()

#     def canSum_helper(targetsum, numbers):
#         # check in memory
#         if targetsum in memo:
#             return memo[targetsum]
#         if targetsum < 0:
#             return False
#         if targetsum == 0:
#             return True
#         for number in numbers:
#             remainder = targetsum - number
#             if canSum_helper(remainder, numbers) == True:
#                 memo[targetsum] = True
#                 return True
#         memo[targetsum] = False
#         return False

#     result = canSum_helper(targetsum, numbers)

#     return result

# print(canSum(7,[2,3]))
# print(canSum(7,[5,3,4,7]))
# print(canSum(7,[2,4]))
# print(canSum(8,[2,3,5]))
# print(canSum(300,[7,14]))
