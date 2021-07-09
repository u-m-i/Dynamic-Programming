
import sys


# classic algo
def fibonacci(number):
    """ O(n^2)
    """

    if number == 0 or number == 1:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)

def f_dynamic(n, memo = {} ):
    """ O(1)
    """
    if n == 0 or n == 1:
        return 1
    
    try:
        return memo[n]
    except KeyError:
        result = f_dynamic(n - 1, memo) + f_dynamic(n - 2, memo)
        memo[n] = result
        return result


    
if __name__ == "__main__":

    sys.setrecursionlimit(10002)

    user_n = int(input("Write a number: "))
    result = f_dynamic(user_n)
    print(result)