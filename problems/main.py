
# region Write a program for Kaprekar number
# https://www.hackerrank.com/challenges/kaprekar-numbers/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
# Function Description
#
# Complete the kaprekarNumbers function in the editor below.
#
# kaprekarNumbers has the following parameter(s):
#
#     int p: the lower limit
#     int q: the upper limit
#
# Prints
#
# It should print the list of modified Kaprekar numbers, space-separated on one line and in ascending order. If no modified Kaprekar numbers exist in the given range, print INVALID RANGE. No return value is required.
#
# Input Format
#
# The first line contains the lower integer limit p.
# .
# The second line contains the upper integer limit q.
#
# .
#
# Note: Your range should be inclusive of the limits.

def kaprekarNumbers(p, q):
    kNos = []
    for n in range(p, q + 1):
        d = len(str(n))
        if n == 1:
            kNos += [1]
        else:
            n_sq = n * n
            str_n_sq = str(n_sq)
            right = int(str_n_sq[-d:])
            left = 0 if str_n_sq[0:len(str_n_sq) - d] == '' else int(str_n_sq[0:len(str_n_sq) - d])

            if left != 0 and right != 0 and left + right == n:
                kNos += [n]

    if len(kNos) == 0:
        print('INVALID RANGE')
    else:
        print(' '.join(map(str, kNos)))




# endregion

# region Non Divisible Subset
# Given a set of distinct integers , print the size of a maximal subset of S
# where the sum of any 2 numbers in S~ is not evenly divisible by k
#
# For example, the array S = [19, 10, 12, 10, 24, 25, 22] and k = 4
# One of the arrays that can be created is S`=[10, 12, 15]. Another is S``=[19, 22, 24]
#
# Sample Input
#
# 4 3
# 1 7 2 4
#
# Sample Output
#
# 3
#
# Explanation
#
# The sums of all permutations of two elements from
# are:
# 1 + 7 = 8
# 1 + 2 = 3
# 1 + 4 = 5
# 7 + 2 = 9
# 7 + 4 = 11
# 2 + 4 = 6
#
# We see that only S` = [1, 7, 4]
# will not ever sum to a multiple of k = 3
#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
# s = [2375782, 21836421, 2139842193, 2138723, 23816, 21836219, 2948784, 43864923, 283648327, 23874673]
# k = 13
# print(nonDivisibleSubset(k, s))
# https://www.hackerrank.com/challenges/non-divisible-subset/forum

def nonDivisibleSubset(k, s):

    # Write your code here
    # this condition is to make sure we initialize all array index here
    # this will save us checking value at every index later.
    rem_lst = [0] * k

    for item in s:
        rem_lst[item % k] += 1

    # handle 0 case
    count = 0
    count += min(rem_lst[0], 1)

    # handle other cases
    for i in range(1, k // 2 + 1):  # here divide by 2 is to make sure we don't repeat cases again.
        if i != k - i:
            count += max(rem_lst[i], rem_lst[k-i])
        else:
            count += 1 if rem_lst[i] > 0 else 0  # case to handle scenarios where value sum = k.

    return count

# endregion

# region matching

def appendAndDelete(s, t, k):
    s = str(s)
    t = str(t)
    diff = 0
    for i in range(0, min(len(s), len(t))):
        if s[i] != t[i]:
            break
    i += 1
    diff = len(s) - i + len(t) -i
    return 'Yes' if (k >= diff and (k - diff) % 2 == 0) or (len(s) + len(t) <= k) else 'No'

# endregion

# region Repeated String
# There is a string, s, of lowercase English letters that is repeated infinitely many times. Given an integer n,
# find and print the number of letter a's in the first letters of the infinite string.
# Example:
# s = 'abcac'
# n = 10
# The substring we consider is abcacabcac he first 10 characters of the infinite string.
# There are 4 occurrences of a in the substring.


def repeatedString(s, n):
    return s.count('a') * (n // len(s)) + s[:n % len(s)].count('a')
# endregion

if __name__ == '__main__':
    s = 'abcac'
    n = 10
    print(repeatedString(s, n))
