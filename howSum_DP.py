# Function howSum will return the result in array form

#Using brute force

# def howSum(targetsum, numbers, arrResult = None): #Time: O(N * M^2)  
#     if arrResult is None: arrResult = []
    
#     if targetsum == 0: return arrResult
#     if targetsum < 0: return None

#     for num in numbers:
#         remainder = targetsum - num
#         if howSum(remainder, numbers, arrResult) != None: 
#             arrResult.append(num)
#             return arrResult

#     return None

#Using Memoization
def howSum(targetsum, numbers, arrResult = None, memo = None): #Time: O(N * M^2)  
    if arrResult is None: arrResult = []
    if memo is None: memo = {}
    if targetsum in memo: return memo[targetsum]
    if targetsum == 0: return arrResult
    if targetsum < 0: return None

    for num in numbers:
        remainder = targetsum - num
        if howSum(remainder, numbers, arrResult,memo) != None: 
            arrResult.append(num)
            memo[targetsum] = arrResult
            return arrResult
    
    memo[targetsum] = None
    return None

print(howSum(7,[2,3])) # [3,2,2]
print(howSum(7,[5,3,4,7])) # [4,3]
print(howSum(7,[2,4])) # [None]
print(howSum(8,[2,3,5])) # [2,2,2,2]
print(howSum(300,[7,14])) # [None]
