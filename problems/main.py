
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

import math
from typing import List


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
            left = 0 if str_n_sq[0:len(
                str_n_sq) - d] == '' else int(str_n_sq[0:len(str_n_sq) - d])

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
    # here divide by 2 is to make sure we don't repeat cases again.
    for i in range(1, k // 2 + 1):
        if i != k - i:
            count += max(rem_lst[i], rem_lst[k-i])
        else:
            # case to handle scenarios where value sum = k.
            count += 1 if rem_lst[i] > 0 else 0

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
    diff = len(s) - i + len(t) - i
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

# region Magic numbers


def formingMagicSquare(s):
    total_sum = []
    all_magic_sq = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    ]

    for mg in all_magic_sq:
        sum = 0
        for mg_row, input_row in zip(mg, s):
            for sample_mg_no, input_no in zip(mg_row, input_row):
                sum += abs(sample_mg_no - input_no)
        total_sum += [sum]

    return min(total_sum)

# endregion

# region Encyrption


# Complete the encryption function below.


def encryption(s):
    s = s.replace(' ', '')
    l = len(s)
    row = math.floor(math.sqrt(l))
    col = math.ceil(math.sqrt(l))

    # invalid condition
    if row * col < l:
        if row < col:
            row = row + 1
        elif row == col:
            col = col + 1

    row_idx = 0
    input_rows = []
    output = ''

    while row_idx < row:
        col_idx = 0
        rows = []
        while col_idx < col:
            col_gap = row_idx * col
            rows += [s[col_idx + col_gap]
                     ] if (col_idx + col_gap) < len(s) else ''
            col_idx += 1
        row_idx += 1
        input_rows += [rows]
    col_list = []

    # transpose array
    for i in range(len(input_rows[0])):
        row = []
        for item in input_rows:
            row.append(item[i] if i < len(item) else '')
        col_list.append(row)

    for val in col_list:
        output += ''.join(val)
        output += ' '

    return output


# endregion

# Breaking the palindrome:
#
# Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.
#
# Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.
#
# A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.

# Input: palindrome = "abccba"
# Output: "aaccba"
# Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
# Of all the ways, "aaccba" is the lexicographically smallest.
def breakPalindrome(input):
    input_len = int(len(input))

    if input_len <= 1:
        return ''

    for idx in range(0, int(input_len/2)):
        if input[idx] != 'a':
            return input[0: idx] + 'a' + input[idx+1:]
    return input[0: input_len-1] + 'b'
# endregion

# region Minium Window Substring
#
# Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".
#
# Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.
#
# Example 1:
#
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
#
# Example 2:
#
# Input: s = "a", t = "a"
# Output: "a"
#


def get_min_window(s, t):
    if s == t:
        return s

    left, right = 0, 0

    # if t not in s[left, right]:


# endregion


# region synup interview question
# You are climbing a staircase. It takes n steps to reach to the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Eg.
# Input: 3
# Output: 3
#
#
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
# 4
# 1 1 1 1
# 2 2
# 1 2 1
# 2 1 1
# 1 1 2


# worst case complexity of 2^n
def ways_to_climb_using_recursion(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return ways_to_climb_using_recursion(n-1) + ways_to_climb_using_recursion(n-2)


# using dynamic programming
# tabulation
def ways_to_climb_using_dp_tabulation(n):
    sum = [0, 1, 2]
    res = 0
    for i in range(3, n+1):
        res = sum[i-1] + sum[i-2]
        sum += [res]
    return res

# memoization:


def ways_to_climb_using_dp_memoization(n, lookup):
    if n <= 1:
        lookup[n] = 1

    if lookup[n] is None:
        lookup[n] = ways_to_climb_using_dp_memoization(
            n-1, lookup) + ways_to_climb_using_dp_memoization(n - 2, lookup)

    return lookup[n]
# endregion

# region Python LinkedList


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DoublyListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_list_item(self, item):
        if not isinstance(item, Node):
            item = Node(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item  # this is using the Node's next property

        self.tail = item

    def remove_list_item(self, item):
        previous_node = None
        current_node = self.head
        while current_node is not None:
            if current_node.data == item:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                    return
            previous_node = current_node
            current_node = current_node.next

    def list_length(self):
        count = 0
        current_node = self.head

        while current_node is not None:
            count += 1
            current_node = current_node.next

        return count

    def list_items(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_list_item(self, item):
        if not isinstance(item, Node):
            item = Node(item)

        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail

        self.tail = item

    def remove_list_item(self, item):
        current_node = self.head
        while current_node is not None:
            previous_node = current_node.prev
            next_node = current_node.next
            if current_node.data == item:
                if previous_node is not None:
                    previous_node.next = next_node
                    if next_node is not None:
                        next_node.prev = previous_node
                else:
                    self.head = next_node
                    if next_node is not None:
                        next_node.prev = None
                    return
            current_node = current_node.next

    def list_length(self):
        count = 0
        current_node = self.head

        while current_node is not None:
            count += 1
            current_node = current_node.next

        return count

    def list_items(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
# driver program
#  linked_list = SinglyLinkedList()
#     linked_list.add_list_item(10)
#     linked_list.add_list_item(11)
#     linked_list.add_list_item(12)
#     linked_list.add_list_item(13)
#     linked_list.add_list_item(14)
#     linked_list.list_items()
#     linked_list.remove_list_item(13)
#     print('doom')
#     linked_list.list_items()
#     print(linked_list.list_length())
# endregion


# region Hare and Tortoise algo for finding cyclic dependency in linked list
# TODO

def hare_and_tortoise_algo():
    pass

# endregion

# region Maximum Streak
# A project manager wants to look at employee attendance data. Given that m employees are working on the project,
# and the manager has the record of the employees present on n days of the project, help him find the maximum number
# of consecutive days on which all employees were present and working on the project.
# As an example there are m = 3 employees and n = 5 workdays to analyze.
# The attendance data strings, data = [YYY, YYY, YNN, YYN, YYN].
# There are only two days at the beginning of the period , where all worker are present.
# Using zero indexing for employees, employees 1 and 2 are absent on the third day, and employee 2 is also out on the forth and fifth days.
# The maximum streak occurs at the beginning and is 2 days long.
# Function Description Complete the maxStrak function in the editor below. The function must return an integer denoting the maximum number of consecutive days where all the employees of the project are present.
# maxStreak has the following parameters: m: an integer denoting the number of employees working on the project. data: an array of n strings, where the value of each element data[i] is a string where data[i][j] denotes the j-th employee is present on the i-th day.
# Constraints
# 1 <= m <= 10
# 1 <= n <= 100000
# Each data[i][j] belongs {"Y", "N"}
# Sample Input 0:
# 2
# 2
# YN
# NN
# Sample Output 0:
# 0
# Sample Input 1:
# 3
# 1
# NYY
# Sample output 1:
# 0


def maxStreak(m, n, data):
    count = 0
    res = 0
    for k in data:
        if all(c == 'Y' for c in k):
            count += 1
        else:
            res = max(res, count)
            count = 0
    return max(count, res)
# endregion
# region
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Example 3:

# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000

# Example 4:

# Input: nums1 = [], nums2 = [1]
# Output: 1.00000

# Example 5:

# Input: nums1 = [2], nums2 = []
# Output: 2.00000

# complexity ?? TODO
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    m = len(nums1)
    n = len(nums2)
    median = 0
    if m == 1 and n == 0:
        median = nums1[0]
    elif m == 0 and n == 1:
        median = nums2[0]
    else:
        final_list = nums1 + nums2
        c = len(final_list)
        index = c // 2
        if c % 2:
            median = sorted(final_list)[index]
        else:
            median = sum(sorted(final_list)[index-1:index+1]) / 2
    return median
# endregion


# region

# Find Numbers with Even Number of Digits
# Given an array nums of integers, return how many of them contain an even number of digits. 
# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.

def findEvenNumberOfDigits(nums: List[int]) -> int:
    count = 0
    for num in nums:
        length = 0
        while num:
            num = num // 10
            length += 1
        if length % 2 == 0:
            count += 1
    return count

def findEvenNumberOfDigits2(nums: List[int]) -> int:
    count = 0
    return sum([len(str(num)) % 2 ==0 for num in nums])

# endregion 

# region 

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].


def sortedSquares(nums: List[int]) -> List[int]:
    res = [num * num for num in nums]
    res.sort(reverse=False)
    return res

def sortedSquares2(nums: List[int]) -> List[int]:
    return [num * num for num in nums].sort(reverse=False)

# endregion

# region 

# Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written.

# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

def duplicateZeros(arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        n = len(arr)
        while i < n -1:
            if arr[i] == 0:
                print(arr[:i+1]+ [0] + arr[i+1: n-1])
                print(arr[:])
                arr[:] = arr[:i+1]+ [0] + arr[i+1: n-1]
                i +=1
            i +=1
        print(arr)

      

# endregion 


# region 
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.
# e.g1: Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

# e.g2: Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    nums1[:] = nums1[:m] + nums2[:n]
    nums1.sort(reverse=False)
    print(nums1)
        
# endregion

# region RemoveElement
# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2]
def removeElement(nums: List[int], val: int) -> int:
    nums[:] = [num for num in nums if num != val]
    return len(nums)

# endregion


if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    n = 3
    nums2 = [2,5,6]
    merge(nums1, m, nums2, n)
