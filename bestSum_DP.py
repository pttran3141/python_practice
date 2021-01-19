# Function bestSum return the best result in the array

# # Brute force 
# def bestSum(targetSum, numbers):
#     if targetSum == 0: return []
#     if targetSum < 0: return None

#     shortestCombination = None

#     for num in numbers: 
#         remainder = targetSum - num
#         remainderCombination = bestSum(remainder, numbers)

#         if remainderCombination!= None:
#             combination = [*remainderCombination, num]  # python * is = js ...         
#             if shortestCombination == None or len(combination) < len(shortestCombination) :
#                 shortestCombination = combination

#     return shortestCombination

def bestSum(target_sum, numbers, memo = None):
    if memo is None:
        memo = {0:[]}
        print(memo)
    if target_sum < 0:
        return None
    if target_sum in memo:
        return memo[target_sum]

    shortest_combination = None

    for num in numbers:
        remainder = target_sum - num

        remainder_combination = bestSum(remainder, numbers, memo)
        if remainder_combination != None:
            combination = [*remainder_combination, num] # Python * equivalent to JavaSscript ...
            if shortest_combination == None or len(combination) < len(shortest_combination):
                shortest_combination = combination

    memo[target_sum] = shortest_combination

    return memo[target_sum]

print(bestSum(7,[5,3,4,7])) # [7]
print(bestSum(8,[2,3,5])) # [3,5]
print(bestSum(8,[1,4,5])) # [4,4]
print(bestSum(100,[1,2,5,25])) # [25,25,25,25]
