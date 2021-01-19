# memoization
# store duplicalte problem that can be use later.

# def memoFib(n, memo = {}):
#     if n == 0: return 0
#     elif (n > 0 and n <= 2): return 1
#     else:
#         if n in memo:
#             return memo[n]
#         else:
#             result = memoFib(n-1, memo) + memoFib(n-2, memo)
#             memo[n] = result
#             return result

# print(memoFib(50))
# print(memoFib(40))
# print(memoFib(20))
# print(memoFib(10))

#######################################
class Memoize:

    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

@Memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(50))
print(fib(40))
print(fib(20))
print(fib(10))