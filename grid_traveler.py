def grid_traveler(n,m, memo = {}):
    
    key = str(n) + ',' + str(m)
    
    if(m == 1 and n == 1): return 1
    if(m == 0 or n == 0): return 0
    if key in memo: return memo[key]
    else:
        result = grid_traveler(n-1,m) + grid_traveler(n, m-1)
        memo[key] = result
    return result

print(grid_traveler(1,1))
print(grid_traveler(2,3))
print(grid_traveler(3,2))
print(grid_traveler(3,3))
print(grid_traveler(18,18))