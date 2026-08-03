from problems.models import Problem

Problem.objects.all().delete()

# ==========================================

# EASY PROBLEMS (1 to 40)

# ==========================================

Problem.objects.create( title="Two Sum", description="""Given an array of
integers nums and an integer target, return indices of the two numbers such that
they add up to target. You may assume that each input would have exactly one
solution, and you may not use the same element twice. You can return the answer
in any order.""", difficulty="Easy", input_format="""The first line contains N,
the size of the array, and the target integer T. The second line contains N
space-separated integers.""", output_format="""Print two space-separated
integers representing the indices of the two numbers.""", constraints="""2 <= N
<= 10^4 -10^9 <= nums[i] <= 10^9 -10^9 <= T <= 10^9""", examples="""Input: 4 9
2 7 11 15

Output: 0 1""" )

Problem.objects.create( title="Valid Parentheses", description="""Given a string
s containing just the characters '(', ')', '{', '}', '[' and ']', determine if
the input string is valid. An input string is valid if open brackets are closed
by the same type of brackets, and open brackets are closed in the correct
order.""", difficulty="Easy", input_format="""A single line containing the
string s.""", output_format="""Print "true" if the string is valid, or "false"
otherwise.""", constraints="""1 <= s.length <= 10^4 s consists of parentheses
characters only.""", examples="""Input: ()[]{}

Output: true""" )

Problem.objects.create( title="Merge Sorted Array", description="""You are given
two integer arrays nums1 and nums2, sorted in non-decreasing order, and two
integers m and n, representing the number of elements in nums1 and nums2
respectively. Merge nums1 and nums2 into a single array sorted in non-decreasing
order.""", difficulty="Easy", input_format="""The first line contains m and n.
The second line contains m sorted integers (elements of nums1). The third line
contains n sorted integers (elements of nums2).""", output_format="""Print the
merged sorted array of size m + n as space-separated integers.""",
constraints="""0 <= m, n <= 1000 1 <= m + n <= 2000 -10^9 <= nums1[i], nums2[j]
<= 10^9""", examples="""Input: 3 3 1 2 3 2 5 6

Output: 1 2 2 3 5 6""" )

Problem.objects.create( title="Best Time to Buy and Sell Stock",
description="""You are given an array prices where prices[i] is the price of a
given stock on the ith day. You want to maximize your profit by choosing a
single day to buy one stock and choosing a different day in the future to sell
that stock. Return the maximum profit you can achieve from this transaction. If
you cannot achieve any profit, return 0.""", difficulty="Easy",
input_format="""The first line contains N, the number of days. The second line
contains N space-separated integers representing the daily stock prices.""",
output_format="""Print a single integer representing the maximum possible
profit.""", constraints="""1 <= N <= 10^5 0 <= prices[i] <= 10^4""",
examples="""Input: 6 7 1 5 3 6 4

Output: 5""" )

Problem.objects.create( title="Valid Palindrome", description="""A phrase is a
palindrome if, after converting all uppercase letters into lowercase letters and
removing all non-alphanumeric characters, it reads the same forward and
backward. Alphanumeric characters include letters and numbers. Given a string s,
return true if it is a palindrome, or false otherwise.""", difficulty="Easy",
input_format="""A single line containing the string s.""",
output_format="""Print "true" if the string is a palindrome, and "false"
otherwise.""", constraints="""1 <= s.length <= 2 * 10^5 s consists only of
printable ASCII characters.""", examples="""Input: A man, a plan, a canal:
Panama

Output: true""" )

Problem.objects.create( title="Invert Binary Tree", description="""Given the
root of a binary tree represented as an array in level-order format, invert the
tree (mirror its structure) and return its level-order representation.""",
difficulty="Easy", input_format="""The first line contains N, the number of
nodes in the binary tree. The second line contains N space-separated integers
representing the level-order traversal of the tree (use -1 to denote a null
node).""", output_format="""Print the level-order traversal of the inverted tree
as space-separated integers (omit trailing nulls).""", constraints="""0 <= N
<= 1000 -100 <= Node.val <= 100""", examples="""Input: 7 4 2 7 1 3 6 9

Output: 4 7 2 9 6 3 1""" )

Problem.objects.create( title="Binary Search", description="""Given an array of
integers nums which is sorted in ascending order, and an integer target, write a
function to search target in nums. If target exists, then return its index.
Otherwise, return -1.""", difficulty="Easy", input_format="""The first line
contains N, the size of the array, and the target value T. The second line
contains N space-separated sorted integers.""", output_format="""Print
the 0-based index of T in the array, or -1 if T is not present.""",
constraints="""1 <= N <= 10^4 -10^4 < nums[i], target < 10^4 All the integers in
nums are unique.""", examples="""Input: 6 9 -1 0 3 5 9 12

Output: 4""" )

Problem.objects.create( title="Flood Fill", description="""An image is
represented by an m x n integer grid image where image[i][j] represents the
pixel value of the image. You are also given three integers sr, sc, and color.
You should perform a flood fill on the image starting from the pixel
image[sr][sc]. To perform a flood fill, consider the starting pixel, plus any
pixels connected 4-directionally to the starting pixel of the same color as the
starting pixel, plus any pixels connected 4-directionally to those pixels (also
with the same color), and so on. Replace the color of all of the aforementioned
pixels with color.""", difficulty="Easy", input_format="""The first line
contains two integers M and N, representing the rows and columns. The next M
lines contain N space-separated integers each, representing the grid. The last
line contains three integers: sr, sc, and the new color.""",
output_format="""Print the modified grid of size M x N.""", constraints="""1 <=
M, N <= 50 0 <= image[i][j], color < 2^16 0 <= sr < M, 0 <= sc < N""",
examples="""Input: 3 3 1 1 1 1 1 0 1 0 1 1 1 2

Output: 2 2 2 2 2 0 2 0 1""" )

Problem.objects.create( title="Maximum Subarray", description="""Given an
integer array nums, find the subarray with the largest sum, and return its
sum.""", difficulty="Easy", input_format="""The first line contains N, the size
of the array. The second line contains N space-separated integers.""",
output_format="""Print a single integer representing the maximum subarray
sum.""", constraints="""1 <= N <= 10^5 -10^4 <= nums[i] <= 10^4""",
examples="""Input: 9 -2 1 -3 4 -1 2 1 -5 4

Output: 6""" )

Problem.objects.create( title="LCA of a BST", description="""Given a binary
search tree (BST), find the lowest common ancestor (LCA) node of two given nodes
in the BST.""", difficulty="Easy", input_format="""The first line contains N,
the number of nodes in the BST. The second line contains N space-separated
integers in level-order representing the BST (use -1 for null). The third line
contains two integers representing the values of nodes p and q.""",
output_format="""Print the value of the Lowest Common Ancestor node.""",
constraints="""2 <= N <= 10^5 -10^9 <= Node.val <= 10^9 All Node.val are unique.
p and q exist in the BST.""", examples="""Input: 6 6 2 8 0 4 7 9 2 8

Output: 6""" )

Problem.objects.create( title="Balanced Binary Tree", description="""Given a
binary tree, determine if it is height-balanced. A height-balanced binary tree
is defined as a binary tree in which the depth of the two subtrees of every node
never differs by more than one.""", difficulty="Easy", input_format="""The first
line contains N, the number of nodes. The second line contains N space-separated
integers in level-order (use -1 for null).""", output_format="""Print "true" if
the tree is height-balanced, or "false" otherwise.""", constraints="""0 <= N
<= 5000 -10^4 <= Node.val <= 10^4""", examples="""Input: 7 3 9 20 -1 -1 15 7

Output: true""" )

Problem.objects.create( title="Linked List Cycle Detection",
description="""Given head, the head of a linked list, determine if the linked
list has a cycle in it. There is a cycle in a linked list if there is some node
in the list that can be reached again by continuously following the next
pointer.""", difficulty="Easy", input_format="""The first line contains N, the
number of nodes, and P, the 0-based index of the node that the tail points to
(or -1 if there is no cycle). The second line contains N space-separated
integers representing the list node values.""", output_format="""Print "true" if
a cycle exists, and "false" otherwise.""", constraints="""0 <= N <= 10^4 -10^5
<= Node.val <= 10^5 -1 <= P < N""", examples="""Input: 4 1 3 2 0 -4

Output: true""" )

Problem.objects.create( title="Implement Queue using Stacks",
description="""Implement a first-in-first-out (FIFO) queue using only two
stacks. The implemented queue should support all the functions of a normal queue
(push, pop, peek, and empty).""", difficulty="Easy", input_format="""The first
line contains Q, the number of queries. The next Q lines contain commands: "push
x", "pop", "peek", or "empty".""", output_format="""For each "pop" and "peek"
command, print the returned integer. For "empty", print "true" or "false".""",
constraints="""1 <= Q <= 100 1 <= x <= 9 All operations are valid (no pop/peek
on empty queue).""", examples="""Input: 5 push 1 push 2 peek pop empty

Output: 1 1 false""" )

Problem.objects.create( title="First Bad Version", description="""You are a
product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check. Since
each version is developed based on the previous version, all the versions after
a bad version are also bad. Suppose you have n versions [1, 2, ..., n] and you
want to find out the first bad one, which causes all the following ones to be
bad. You are given an API isBadVersion(version) which returns whether version is
bad. Implement a function to find the first bad version with minimum API
calls.""", difficulty="Easy", input_format="""The first line contains N, the
total number of versions, and B, the first bad version.""",
output_format="""Print the integer index of the first bad version.""",
constraints="""1 <= B <= N <= 2^31 - 1""", examples="""Input: 5 4

Output: 4""" )

Problem.objects.create( title="Ransom Note", description="""Given two strings
ransomNote and magazine, return true if ransomNote can be constructed by using
the letters from magazine and false otherwise. Each letter in magazine can only
be used once in ransomNote.""", difficulty="Easy", input_format="""The first
line contains the string ransomNote. The second line contains the string
magazine.""", output_format="""Print "true" if the ransom note can be
constructed, or "false" otherwise.""", constraints="""1 <= ransomNote.length,
magazine.length <= 10^5 ransomNote and magazine consist of lowercase English
letters.""", examples="""Input: aa aab

Output: true""" )

Problem.objects.create( title="Climbing Stairs", description="""You are climbing
a staircase. It takes n steps to reach the top. Each time you can either climb 1
or 2 steps. In how many distinct ways can you climb to the top?""",
difficulty="Easy", input_format="""A single integer N.""",
output_format="""Print the number of distinct ways to climb to the top.""",
constraints="""1 <= N <= 45""", examples="""Input: 3

Output: 3""" )

Problem.objects.create( title="Reverse Linked List", description="""Given the
head of a singly linked list, reverse the list, and return the reversed
list.""", difficulty="Easy", input_format="""The first line contains N, the
number of nodes in the linked list. The second line contains N space-separated
integers.""", output_format="""Print the reversed linked list values as
space-separated integers.""", constraints="""0 <= N <= 5000 -5000 <= Node.val
<= 5000""", examples="""Input: 5 1 2 3 4 5

Output: 5 4 3 2 1""" )

Problem.objects.create( title="Majority Element", description="""Given an array
nums of size n, return the majority element. The majority element is the element
that appears more than floor(n / 2) times. You may assume that the majority
element always exists in the array.""", difficulty="Easy", input_format="""The
first line contains N. The second line contains N space-separated integers.""",
output_format="""Print the majority element.""", constraints="""1 <= N <= 5
* 10^4 -10^9 <= nums[i] <= 10^9""", examples="""Input: 7 2 2 1 1 1 2 2

Output: 2""" )

Problem.objects.create( title="Add Binary", description="""Given two binary
strings a and b, return their sum as a binary string.""", difficulty="Easy",
input_format="""The first line contains binary string a. The second line
contains binary string b.""", output_format="""Print the sum of the two binary
strings.""", constraints="""1 <= a.length, b.length <= 10^4 a and b consist only
of '0' or '1' characters without leading zeros except the number 0 itself.""",
examples="""Input: 1010 1011

Output: 10101""" )

Problem.objects.create( title="Diameter of Binary Tree", description="""Given
the root of a binary tree, return the length of the diameter of the tree. The
diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.""",
difficulty="Easy", input_format="""The first line contains N, the number of
nodes. The second line contains N space-separated integers in level-order
representation.""", output_format="""Print the integer representing the tree's
diameter.""", constraints="""1 <= N <= 10^4 -100 <= Node.val <= 100""",
examples="""Input: 5 1 2 3 4 5

Output: 3""" )

Problem.objects.create( title="Middle of the Linked List", description="""Given
the head of a singly linked list, return the middle node of the linked list. If
there are two middle nodes, return the second middle node.""",
difficulty="Easy", input_format="""The first line contains N, the number of
nodes. The second line contains N space-separated integers representing node
values.""", output_format="""Print the node values starting from the middle node
to the end of the list.""", constraints="""1 <= N <= 100 1 <= Node.val
<= 100""", examples="""Input: 6 1 2 3 4 5 6

Output: 4 5 6""" )

Problem.objects.create( title="Maximum Depth of Binary Tree",
description="""Given the root of a binary tree, return its maximum depth. A
binary tree's maximum depth is the number of nodes along the longest path from
the root node down to the farthest leaf node.""", difficulty="Easy",
input_format="""The first line contains N, the number of nodes. The second line
contains N space-separated integers in level-order.""", output_format="""Print
the maximum depth.""", constraints="""0 <= N <= 10^4 -100 <= Node.val <= 100""",
examples="""Input: 5 3 9 20 -1 -1 15 7

Output: 3""" )

Problem.objects.create( title="Contains Duplicate", description="""Given an
integer array nums, return true if any value appears at least twice in the
array, and return false if every element is distinct.""", difficulty="Easy",
input_format="""The first line contains N, the size of the array. The second
line contains N space-separated integers.""", output_format="""Print "true" if
duplicates exist, and "false" otherwise.""", constraints="""1 <= N <= 10^5 -10^9
<= nums[i] <= 10^9""", examples="""Input: 4 1 2 3 1

Output: true""" )

Problem.objects.create( title="Meeting Rooms", description="""Given an array of
meeting time intervals where intervals[i] = [start_i, end_i], determine if a
person could attend all meetings.""", difficulty="Easy", input_format="""The
first line contains N, the number of intervals. The next N lines contain two
space-separated integers representing the start and end of each meeting.""",
output_format="""Print "true" if the person can attend all meetings, or "false"
otherwise.""", constraints="""0 <= N <= 10^4 0 <= start_i < end_i <= 10^6""",
examples="""Input: 3 0 30 5 10 15 20

Output: false""" )

Problem.objects.create( title="Roman to Integer", description="""Roman numerals
are represented by seven different symbols: I, V, X, L, C, D and M. Given a
roman numeral, convert it to an integer.""", difficulty="Easy",
input_format="""A single line containing the Roman numeral s.""",
output_format="""Print the corresponding integer value.""", constraints="""1 <=
s.length <= 15 s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D',
'M').""", examples="""Input: LVIII

Output: 58""" )

Problem.objects.create( title="Backspace String Compare", description="""Given
two strings s and t, return true if they are equal when both are typed into
empty text editors. '#' means a backspace character. Note that after backspacing
an empty text, the text will continue empty.""", difficulty="Easy",
input_format="""The first line contains string s. The second line contains
string t.""", output_format="""Print "true" if they are equal, or "false"
otherwise.""", constraints="""1 <= s.length, t.length <= 200 s and t contain
lowercase letters and '#' characters.""", examples="""Input: ab#c ad#c

Output: true""" )

Problem.objects.create( title="Counting Bits", description="""Given an integer
n, return an array of length n + 1 such that for each i (0 <= i <= n), ans[i] is
the number of 1's in the binary representation of i.""", difficulty="Easy",
input_format="""A single integer N.""", output_format="""Print N + 1
space-separated integers representing the bit counts.""", constraints="""0 <= N
<= 10^5""", examples="""Input: 5

Output: 0 1 1 2 1 2""" )

Problem.objects.create( title="Same Tree", description="""Given the roots of two
binary trees p and q, write a function to check if they are the same or not. Two
binary trees are considered the same if they are structurally identical, and the
nodes have the same value.""", difficulty="Easy", input_format="""The first line
contains N and M, the node counts of trees p and q. The second line contains N
elements of p in level-order. The third line contains M elements of q in
level-order.""", output_format="""Print "true" if the trees are identical, or
"false" otherwise.""", constraints="""0 <= N, M <= 100 -10^4 <= Node.val
<= 10^4""", examples="""Input: 3 3 1 2 3 1 2 3

Output: true""" )

Problem.objects.create( title="Number of 1 Bits", description="""Write a
function that takes an unsigned integer and returns the number of '1' bits it
has (also known as the Hamming weight).""", difficulty="Easy", input_format="""A
single positive integer N.""", output_format="""Print the count of '1' bits in
its binary representation.""", constraints="""1 <= N <= 2^31 - 1""",
examples="""Input: 11

Output: 3""" )

Problem.objects.create( title="Single Number", description="""Given a non-empty
array of integers nums, every element appears twice except for one. Find that
single one. You must implement a solution with a linear runtime complexity and
use only constant extra space.""", difficulty="Easy", input_format="""The first
line contains N, the size of the array. The second line contains N
space-separated integers.""", output_format="""Print the single integer.""",
constraints="""1 <= N <= 3 * 10^4 -3 * 10^4 <= nums[i] <= 3 * 10^4 Each element
in the array appears twice except for one.""", examples="""Input: 5 4 1 2 1 2

Output: 4""" )

Problem.objects.create( title="Palindrome Linked List", description="""Given the
head of a singly linked list, return true if it is a palindrome or false
otherwise.""", difficulty="Easy", input_format="""The first line contains N, the
number of nodes. The second line contains N space-separated integers
representing the list node values.""", output_format="""Print "true" if the list
is a palindrome, and "false" otherwise.""", constraints="""1 <= N <= 10^5 0 <=
Node.val <= 9""", examples="""Input: 4 1 2 2 1

Output: true""" )

Problem.objects.create( title="Move Zeroes", description="""Given an integer
array nums, move all 0's to the end of it while maintaining the relative order
of the non-zero elements. Note that you must do this in-place without making a
copy of the array.""", difficulty="Easy", input_format="""The first line
contains N, the size of the array. The second line contains N space-separated
integers.""", output_format="""Print the modified array as space-separated
integers.""", constraints="""1 <= N <= 10^4 -2^31 <= nums[i] <= 2^31 - 1""",
examples="""Input: 5 0 1 0 3 12

Output: 1 3 12 0 0""" )

Problem.objects.create( title="Symmetric Tree", description="""Given the root of
a binary tree, check whether it is a mirror of itself (i.e., symmetric around
its center).""", difficulty="Easy", input_format="""The first line contains N,
the number of nodes. The second line contains N space-separated integers in
level-order (use -1 for null).""", output_format="""Print "true" if the tree is
symmetric, or "false" otherwise.""", constraints="""1 <= N <= 1000 -100 <=
Node.val <= 100""", examples="""Input: 7 1 2 2 3 4 4 3

Output: true""" )

Problem.objects.create( title="Missing Number", description="""Given an array
nums containing n distinct numbers in the range [0, n], return the only number
in the range that is missing from the array.""", difficulty="Easy",
input_format="""The first line contains N, the size of the array. The second
line contains N space-separated integers.""", output_format="""Print the missing
number.""", constraints="""1 <= N <= 10^4 0 <= nums[i] <= N All elements of nums
are unique.""", examples="""Input: 3 3 0 1

Output: 2""" )

Problem.objects.create( title="Reverse String", description="""Write a function
that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra
memory.""", difficulty="Easy", input_format="""The first line contains N, the
length of the string. The second line contains N space-separated characters.""",
output_format="""Print the reversed string characters separated by space.""",
constraints="""1 <= N <= 10^5 s[i] is a printable ASCII character.""",
examples="""Input: 5 h e l l o

Output: o l l e h""" )

Problem.objects.create( title="Intersection of Two Arrays", description="""Given
two integer arrays nums1 and nums2, return an array of their intersection. Each
element in the result must be unique and you may return the result in any
order.""", difficulty="Easy", input_format="""The first line contains sizes N
and M. The second line contains N space-separated integers. The third line
contains M space-separated integers.""", output_format="""Print the unique
intersecting elements as space-separated integers (sorted in ascending
order).""", constraints="""1 <= N, M <= 1000 0 <= nums1[i], nums2[i] <= 1000""",
examples="""Input: 4 5 1 2 2 1 2 2 3 4 5

Output: 2""" )

Problem.objects.create( title="Squares of a Sorted Array", description="""Given
an integer array nums sorted in non-decreasing order, return an array of the
squares of each number sorted in non-decreasing order.""", difficulty="Easy",
input_format="""The first line contains N, the size of the array. The second
line contains N space-separated integers sorted in non-decreasing order.""",
output_format="""Print N space-separated integers representing the sorted
squares.""", constraints="""1 <= N <= 10^4 -10^4 <= nums[i] <= 10^4""",
examples="""Input: 5 -4 -1 0 3 10

Output: 0 1 9 16 100""" )

Problem.objects.create( title="Fizz Buzz", description="""Given an integer n,
return a string array answer (1-indexed) where: answer[i] == "FizzBuzz" if i is
divisible by 3 and 5. answer[i] == "Fizz" if i is divisible by 3. answer[i] ==
"Buzz" if i is divisible by 5. answer[i] == i (as a string) if none of the above
conditions are true.""", difficulty="Easy", input_format="""A single integer
N.""", output_format="""Print N lines, where line i represents the answer[i]
value.""", constraints="""1 <= N <= 10^4""", examples="""Input: 15

Output: 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz""" )

Problem.objects.create( title="Valid Anagram", description="""Given two strings
s and t, return true if t is an anagram of s, and false otherwise. An Anagram is
a word or phrase formed by rearranging the letters of a different word or
phrase, typically using all the original letters exactly once.""",
difficulty="Easy", input_format="""The first line contains string s. The second
line contains string t.""", output_format="""Print "true" if they are anagrams,
or "false" otherwise.""", constraints="""1 <= s.length, t.length <= 5 * 10^4 s
and t consist of lowercase English letters.""", examples="""Input: anagram
nagaram

Output: true""" )

Problem.objects.create( title="Prefix Sum Query", description="""Given an
integer array nums, handle multiple queries of the following type: Calculate the
sum of the elements of nums between indices left and right inclusive where left
<= right.""", difficulty="Easy", input_format="""The first line contains N, the
size of the array, and Q, the number of queries. The second line contains N
space-separated integers. The next Q lines each contain two space-separated
integers representing left and right.""", output_format="""For each query, print
the sum on a new line.""", constraints="""1 <= N, Q <= 10^5 -10^9 <= nums[i]
<= 10^9 0 <= left <= right < N""", examples="""Input: 6 3 -2 0 3 -5 2 -1 0 2 2 5
0 5

Output: 1 -1 -3""" )

# ==========================================

# MEDIUM PROBLEMS (41 to 80)

# ==========================================

Problem.objects.create( title="3Sum", description="""Given an integer array
nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i !=
k, and j != k, and nums[i] + nums[j] + nums[k] == 0. Notice that the solution
set must not contain duplicate triplets.""", difficulty="Medium",
input_format="""The first line contains N, the size of the array. The second
line contains N space-separated integers.""", output_format="""Print each unique
triplet on a new line, sorted both inside the triplet and across triplets.""",
constraints="""3 <= N <= 3000 -10^5 <= nums[i] <= 10^5""", examples="""Input: 6
-1 0 1 2 -1 -4

Output: -1 -1 2 -1 0 1""" )

Problem.objects.create( title="Longest Substring Without Repeating Characters",
description="""Given a string s, find the length of the longest substring
without repeating characters.""", difficulty="Medium", input_format="""A single
line containing the string s.""", output_format="""Print the length of the
longest substring.""", constraints="""0 <= s.length <= 5 * 10^4 s consists of
English letters, digits, symbols and spaces.""", examples="""Input: abcabcbb

Output: 3""" )

Problem.objects.create( title="Container With Most Water", description="""You
are given an integer array height of length n. There are n vertical lines drawn
such that the two endpoints of the ith line are (i, 0) and (i, height[i]). Find
two lines that together with the x-axis form a container, such that the
container contains the most water. Return the maximum amount of water a
container can store.""", difficulty="Medium", input_format="""The first line
contains N, the number of lines. The second line contains N space-separated
integers representing the heights.""", output_format="""Print the maximum water
volume as an integer.""", constraints="""2 <= N <= 10^5 0 <= height[i]
<= 10^4""", examples="""Input: 9 1 8 6 2 5 4 8 3 7

Output: 49""" )

Problem.objects.create( title="Longest Repeating Character Replacement",
description="""You are given a string s and an integer k. You can choose any
character of the string and change it to any other uppercase English character.
You can perform this operation at most k times. Return the length of the longest
substring containing the same letter you can get after performing the above
operations.""", difficulty="Medium", input_format="""The first line contains
string s. The second line contains integer k.""", output_format="""Print the
length of the longest valid substring.""", constraints="""1 <= s.length <= 10^5
0 <= k <= s.length s consists of uppercase English letters.""",
examples="""Input: AABABBA 1

Output: 4""" )

Problem.objects.create( title="Find All Anagrams in a String",
description="""Given two strings s and p, return an array of all the start
indices of p's anagrams in s. You may return the answer in any order.""",
difficulty="Medium", input_format="""The first line contains the string s. The
second line contains the string p.""", output_format="""Print the starting
indices of anagrams as space-separated integers in ascending order.""",
constraints="""1 <= s.length, p.length <= 3 * 10^4 s and p consist of lowercase
English letters.""", examples="""Input: cbaebabacd abc

Output: 0 6""" )

Problem.objects.create( title="Minimum Size Subarray Sum", description="""Given
an array of positive integers nums and a positive integer target, return the
minimal length of a subarray whose sum is greater than or equal to target. If
there is no such subarray, return 0 instead.""", difficulty="Medium",
input_format="""The first line contains N and the target T. The second line
contains N space-separated positive integers.""", output_format="""Print the
minimal length of a subarray.""", constraints="""1 <= N <= 10^5 1 <= target
<= 10^9 1 <= nums[i] <= 10^4""", examples="""Input: 6 7 2 3 1 2 4 3

Output: 2""" )

Problem.objects.create( title="Product of Array Except Self",
description="""Given an integer array nums, return an array answer such that
answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
integer. You must write an algorithm that runs in O(n) time and without using
the division operation.""", difficulty="Medium", input_format="""The first line
contains N, the size of the array. The second line contains N space-separated
integers.""", output_format="""Print N space-separated integers representing the
output array.""", constraints="""2 <= N <= 10^5 -30 <= nums[i] <= 30""",
examples="""Input: 4 1 2 3 4

Output: 24 12 8 6""" )

Problem.objects.create( title="Group Anagrams", description="""Given an array of
strings strs, group the anagrams together. You can return the answer in any
order. An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly
once.""", difficulty="Medium", input_format="""The first line contains N, the
number of strings. The next N lines each contain a single string.""",
output_format="""Print each group of anagrams on a new line (with words inside
the group sorted and space-separated). Sort the lines alphabetically by their
first word.""", constraints="""1 <= N <= 10^4 0 <= strs[i].length <= 100 strs[i]
consists of lowercase English letters.""", examples="""Input: 6 eat tea tan ate
nat bat

Output: ate eat tea bat nat tan""" )

Problem.objects.create( title="Top K Frequent Elements", description="""Given an
integer array nums and an integer k, return the k most frequent elements. You
may return the answer in any order.""", difficulty="Medium", input_format="""The
first line contains N and K. The second line contains N space-separated
integers.""", output_format="""Print the K most frequent elements as
space-separated integers in ascending order.""", constraints="""1 <= N <= 10^5 1
<= K <= number of unique elements -10^4 <= nums[i] <= 10^4""",
examples="""Input: 6 2 1 1 1 2 2 3

Output: 1 2""" )

Problem.objects.create( title="Sort Colors", description="""Given an array nums
with n objects colored red, white, or blue, sort them in-place so that objects
of the same color are adjacent, with the colors in the order red, white, and
blue. We will use the integers 0, 1, and 2 to represent the color red, white,
and blue, respectively.""", difficulty="Medium", input_format="""The first line
contains N, the size of the array. The second line contains N space-separated
integers (only containing 0, 1, or 2).""", output_format="""Print the sorted
array as space-separated integers.""", constraints="""1 <= N <= 300 nums[i] is
either 0, 1, or 2.""", examples="""Input: 6 2 0 2 1 1 0

Output: 0 0 1 1 2 2""" )

Problem.objects.create( title="Search in Rotated Sorted Array",
description="""There is an integer array nums sorted in ascending order (with
distinct values). Prior to being passed to your function, nums is possibly
rotated at an unknown pivot index k (1 <= k < nums.length). Given the array nums
after the possible rotation and an integer target, return the index of target if
it is in nums, or -1 if it is not in nums.""", difficulty="Medium",
input_format="""The first line contains N and the target value T. The second
line contains N space-separated integers representing the rotated array.""",
output_format="""Print the index of T, or -1 if it is not found.""",
constraints="""1 <= N <= 5000 -10^4 <= nums[i], T <= 10^4 All values in the
array are unique.""", examples="""Input: 7 0 4 5 6 7 0 1 2

Output: 4""" )

Problem.objects.create( title="Find Minimum in Rotated Sorted Array",
description="""Suppose an array of length n sorted in ascending order is rotated
between 1 and n times. Find the minimum element of this array.""",
difficulty="Medium", input_format="""The first line contains N, the size of the
array. The second line contains N space-separated integers.""",
output_format="""Print the minimum element in the array.""", constraints="""1 <=
N <= 5000 -10^4 <= nums[i] <= 10^4 All elements of nums are unique.""",
examples="""Input: 5 3 4 5 1 2

Output: 1""" )

Problem.objects.create( title="Kth Largest Element in an Array",
description="""Given an integer array nums and an integer k, return the kth
largest element in the array. Note that it is the kth largest element in the
sorted order, not the kth distinct element.""", difficulty="Medium",
input_format="""The first line contains N and K. The second line contains N
space-separated integers.""", output_format="""Print the Kth largest
element.""", constraints="""1 <= K <= N <= 10^5 -10^4 <= nums[i] <= 10^4""",
examples="""Input: 6 2 3 2 1 5 6 4

Output: 5""" )

Problem.objects.create( title="Merge Intervals", description="""Given an array
of intervals where intervals[i] = [start_i, end_i], merge all overlapping
intervals, and return an array of the non-overlapping intervals that cover all
the intervals in the input.""", difficulty="Medium", input_format="""The first
line contains N, the number of intervals. The next N lines contain two
space-separated integers representing start and end times.""",
output_format="""Print each merged interval on a new line as space-separated
integers, sorted by start time.""", constraints="""1 <= N <= 10^4 0 <= start_i
<= end_i <= 10^4""", examples="""Input: 4 1 3 2 6 8 10 15 18

Output: 1 6 8 10 15 18""" )

Problem.objects.create( title="Insert Interval", description="""You are given an
array of non-overlapping intervals where intervals[i] = [start_i, end_i] sorted
in ascending order by start_i. You are also given a newInterval = [start, end]
that represents the start and end of another interval. Insert newInterval into
intervals such that intervals is still sorted in ascending order by start_i and
intervals still does not have any overlapping intervals.""",
difficulty="Medium", input_format="""The first line contains N, the number of
existing intervals. The next N lines contain two space-separated integers. The
last line contains two space-separated integers for the new interval.""",
output_format="""Print each final interval on a new line.""", constraints="""0
<= N <= 10^4 0 <= start_i <= end_i <= 10^5 0 <= start <= end <= 10^5""",
examples="""Input: 2 1 3 6 9 2 5

Output: 1 5 6 9""" )

Problem.objects.create( title="Non-overlapping Intervals", description="""Given
an array of intervals intervals where intervals[i] = [start_i, end_i], return
the minimum number of intervals you need to remove to make the rest of the
intervals non-overlapping.""", difficulty="Medium", input_format="""The first
line contains N, the number of intervals. The next N lines contain two
space-separated integers each.""", output_format="""Print the minimum number of
intervals to remove.""", constraints="""1 <= N <= 10^5 -5 * 10^4 <= start_i <
end_i <= 5 * 10^4""", examples="""Input: 4 1 2 2 3 3 4 1 3

Output: 1""" )

Problem.objects.create( title="Reorder List", description="""You are given the
head of a singly linked list. Reorder the list to be on the following form: L0
-> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ... You may not modify the values in the
list's nodes. Only nodes themselves may be changed.""", difficulty="Medium",
input_format="""The first line contains N, the number of nodes. The second line
contains N space-separated integers representing the list.""",
output_format="""Print the reordered list as space-separated integers.""",
constraints="""1 <= N <= 5 * 10^4 1 <= Node.val <= 1000""", examples="""Input: 4
1 2 3 4

Output: 1 4 2 3""" )

Problem.objects.create( title="Remove Nth Node From End of List",
description="""Given the head of a linked list, remove the nth node from the end
of the list and return its head.""", difficulty="Medium", input_format="""The
first line contains N, the number of nodes, and K, the node index to remove from
the end. The second line contains N space-separated integers.""",
output_format="""Print the modified list as space-separated integers.""",
constraints="""1 <= N <= 30 1 <= K <= N 0 <= Node.val <= 100""",
examples="""Input: 5 2 1 2 3 4 5

Output: 1 2 3 5""" )

Problem.objects.create( title="Copy List with Random Pointer", description="""A
linked list of length n is given such that each node contains an additional
random pointer, which could point to any node in the list, or null. Construct a
deep copy of the list.""", difficulty="Medium", input_format="""The first line
contains N, the number of nodes. The second line contains N space-separated
integers representing the values. The third line contains N space-separated
integers representing the 0-based index of each node's random pointer (or -1 if
null).""", output_format="""Print the copied list's values and their random
indices formatted as 'val(rand_index)' separated by spaces.""", constraints="""0
<= N <= 1000 -10^4 <= Node.val <= 10^4""", examples="""Input: 3 1 2 3 2 0 -1

Output: 1(2) 2(0) 3(-1)""" )

Problem.objects.create( title="Binary Tree Level Order Traversal",
description="""Given the root of a binary tree, return the level order traversal
of its nodes' values. (i.e., from left to right, level by level).""",
difficulty="Medium", input_format="""The first line contains N, the number of
nodes. The second line contains N space-separated integers in level-order (use
-1 for null).""", output_format="""Print each level's values on a new line as
space-separated integers.""", constraints="""0 <= N <= 2000 -1000 <= Node.val
<= 1000""", examples="""Input: 7 3 9 20 -1 -1 15 7

Output: 3 9 20 15 7""" )

Problem.objects.create( title="Construct Binary Tree from Preorder and Inorder Traversal", description="""Given two integer arrays preorder and inorder where
preorder is the preorder traversal of a binary tree and inorder is the inorder
traversal of the same tree, construct and return the binary tree's level-order
representation.""", difficulty="Medium", input_format="""The first line contains
N, the number of nodes. The second line contains N space-separated integers of
preorder traversal. The third line contains N space-separated integers of
inorder traversal.""", output_format="""Print the level-order traversal of the
constructed tree (omitting trailing nulls).""", constraints="""1 <= N <= 3000
-3000 <= preorder[i], inorder[i] <= 3000 preorder and inorder consist of unique
values.""", examples="""Input: 5 3 9 20 15 7 9 3 15 20 7

Output: 3 9 20 -1 -1 15 7""" )

Problem.objects.create( title="Validate Binary Search Tree",
description="""Given the root of a binary tree, determine if it is a valid
binary search tree (BST).""", difficulty="Medium", input_format="""The first
line contains N, the number of nodes. The second line contains N space-separated
integers in level-order (use -1 for null).""", output_format="""Print "true" if
the tree is a valid BST, or "false" otherwise.""", constraints="""1 <= N <= 10^4
-2^31 <= Node.val <= 2^31 - 1""", examples="""Input: 3 2 1 3

Output: true""" )

Problem.objects.create( title="Kth Smallest Element in a BST",
description="""Given the root of a binary search tree, and an integer k, return
the kth smallest value (1-indexed) of all the values of the nodes in the
tree.""", difficulty="Medium", input_format="""The first line contains N and K.
The second line contains N space-separated BST elements in level-order.""",
output_format="""Print the Kth smallest element.""", constraints="""1 <= K <= N
<= 10^4 0 <= Node.val <= 10^4""", examples="""Input: 6 3 5 3 6 2 4 -1 -1

Output: 4""" )

Problem.objects.create( title="Lowest Common Ancestor of a Binary Tree",
description="""Given a binary tree, find the lowest common ancestor (LCA) of two
given nodes in the tree. According to the definition of LCA on Wikipedia: "The
lowest common ancestor is defined between two nodes p and q as the lowest node
in T that has both p and q as descendants." """, difficulty="Medium",
input_format="""The first line contains N. The second line contains N
space-separated integers in level-order. The third line contains the two target
node values.""", output_format="""Print the LCA node value.""", constraints="""2
<= N <= 10^5 -10^9 <= Node.val <= 10^9 All Node.val are unique.""",
examples="""Input: 7 3 5 1 6 2 0 8 5 1

Output: 3""" )

Problem.objects.create( title="Implement Trie (Prefix Tree)", description="""A
trie (pronounced as "try") or prefix tree is a tree data structure used to
efficiently store and retrieve keys in a dataset of strings. Implement a trie
with insert, search, and startsWith methods.""", difficulty="Medium",
input_format="""The first line contains Q, the number of operations. The next Q
lines contain commands: "insert word", "search word", or "startsWith
prefix".""", output_format="""For "search" and "startsWith" commands, print
"true" or "false".""", constraints="""1 <= Q <= 1000 word and prefix consist of
lowercase English letters only.""", examples="""Input: 5 insert apple search
apple search app startsWith app insert app

Output: true false true""" )

Problem.objects.create( title="Course Schedule", description="""There are a
total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates
that you must take course bi first if you want to take course ai. Return true if
you can finish all courses. Otherwise, return false.""", difficulty="Medium",
input_format="""The first line contains V, the number of courses, and E, the
number of dependency pairs. The next E lines each contain two integers ai and
bi.""", output_format="""Print "true" if you can complete all courses, and
"false" otherwise.""", constraints="""1 <= V <= 2000 0 <= E <= 5000""",
examples="""Input: 2 1 1 0

Output: true""" )

Problem.objects.create( title="Number of Islands", description="""Given an m x
n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands. An island is surrounded by water and is formed by
connecting adjacent lands horizontally or vertically.""", difficulty="Medium",
input_format="""The first line contains M and N, the grid dimensions. The next M
lines each contain N characters ('0' or '1').""", output_format="""Print the
total count of islands.""", constraints="""1 <= M, N <= 300""",
examples="""Input: 4 5 11110 11010 11000 00000

Output: 1""" )

Problem.objects.create( title="Clone Graph", description="""Given a reference of
a node in a connected undirected graph, return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its
neighbors.""", difficulty="Medium", input_format="""The first line contains N,
the number of nodes, and M, the number of undirected edges. The next M lines
each contain two space-separated integers representing an edge.""",
output_format="""Print the adjacency list of the cloned graph. Each node's
neighbors should be printed in sorted order.""", constraints="""0 <= N <= 100 1
<= Node.val <= N""", examples="""Input: 4 4 1 2 2 3 3 4 4 1

Output: 1: 2 4 2: 1 3 3: 2 4 4: 1 3""" )

Problem.objects.create( title="Pacific Atlantic Water Flow",
description="""There is an m x n rectangular island that borders both the
Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left
and top edges, and the Atlantic Ocean touches the island's right and bottom
edges. Water can flow in 4 directions to neighboring cells of equal or lower
height. Find the grid coordinates from which water can flow to both oceans.""",
difficulty="Medium", input_format="""The first line contains M and N. The next M
lines contain N space-separated integers representing the height of each
cell.""", output_format="""Print the coordinates [r, c] that can reach both
oceans, sorted lexicographically.""", constraints="""1 <= M, N <= 200 0 <=
heights[r][c] <= 10^5""", examples="""Input: 5 5 1 2 2 3 5 3 2 3 4 4 2 4 5 3 1
6 7 1 4 5 5 1 1 2 4

Output: 0 4 1 3 1 4 2 2 3 0 3 1 4 0""" )

Problem.objects.create( title="Rotting Oranges", description="""You are given an
m x n grid where each cell can have one of three values: 0 representing empty, 1
representing fresh orange, or 2 representing rotten orange. Every minute, any
fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh
orange. If this is impossible, return -1.""", difficulty="Medium",
input_format="""The first line contains M and N. The next M lines contain N
space-separated integers (0, 1, or 2).""", output_format="""Print the minimum
minutes required, or -1.""", constraints="""1 <= M, N <= 10 grid[i][j] is 0, 1,
or 2.""", examples="""Input: 3 3 2 1 1 1 1 0 0 1 1

Output: 4""" )

Problem.objects.create( title="Number of Connected Components",
description="""You have a graph of n nodes. You are given an integer n and an
array edges where edges[i] = [ai, bi] indicates that there is an edge between ai
and bi in the graph. Return the number of connected components in the graph.""",
difficulty="Medium", input_format="""The first line contains N and E (number of
nodes and edges). The next E lines each contain two integers ai and bi.""",
output_format="""Print the total number of connected components.""",
constraints="""1 <= N <= 2000 0 <= E <= 5000""", examples="""Input: 5 3 0 1 1 2
3 4

Output: 2""" )

Problem.objects.create( title="Graph Valid Tree", description="""You have a
graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list
of undirected edges. Write a function to check whether these edges make up a
valid tree.""", difficulty="Medium", input_format="""The first line contains N
and E. The next E lines each contain two space-separated integers.""",
output_format="""Print "true" if the graph is a valid tree, and "false"
otherwise.""", constraints="""1 <= N <= 2000 0 <= E <= 5000""",
examples="""Input: 5 4 0 1 0 2 0 3 1 4

Output: true""" )

Problem.objects.create( title="House Robber", description="""You are a
professional robber planning to rob houses along a street. Each house has a
certain amount of money stashed, the only constraint stopping you from robbing
each of them is that adjacent houses have security systems connected and it will
automatically contact the police if two adjacent houses were broken into on the
same night. Return the maximum amount of money you can rob tonight without
alerting the police.""", difficulty="Medium", input_format="""The first line
contains N, the number of houses. The second line contains N space-separated
integers.""", output_format="""Print the maximum money that can be stolen.""",
constraints="""1 <= N <= 100 0 <= nums[i] <= 400""", examples="""Input: 4
1 2 3 1

Output: 4""" )

Problem.objects.create( title="Longest Increasing Subsequence",
description="""Given an integer array nums, return the length of the longest
strictly increasing subsequence.""", difficulty="Medium", input_format="""The
first line contains N, the size of the array. The second line contains N
space-separated integers.""", output_format="""Print the length of the longest
increasing subsequence.""", constraints="""1 <= N <= 2500 -10^4 <= nums[i]
<= 10^4""", examples="""Input: 8 10 9 2 5 3 7 101 18

Output: 4""" )

Problem.objects.create( title="Longest Common Subsequence", description="""Given
two strings text1 and text2, return the length of their longest common
subsequence. If there is no common subsequence, return 0.""",
difficulty="Medium", input_format="""The first line contains string text1. The
second line contains string text2.""", output_format="""Print the length of the
longest common subsequence.""", constraints="""1 <= text1.length, text2.length
<= 1000 text1 and text2 consist of lowercase English characters.""",
examples="""Input: abcde ace

Output: 3""" )

Problem.objects.create( title="Coin Change", description="""You are given an
integer array coins representing coins of different denominations and an integer
amount representing a total amount of money. Return the fewest number of coins
that you need to make up that amount. If that amount of money cannot be made up
by any combination of the coins, return -1.""", difficulty="Medium",
input_format="""The first line contains N (number of coin types) and T (target
amount). The second line contains N space-separated integers representing the
coins.""", output_format="""Print the minimum number of coins, or -1.""",
constraints="""1 <= N <= 12 1 <= coins[i] <= 2^31 - 1 0 <= T <= 10^4""",
examples="""Input: 3 11 1 2 5

Output: 3""" )

Problem.objects.create( title="Word Break", description="""Given a string s and
a dictionary of strings wordDict, return true if s can be segmented into a
space-separated sequence of one or more dictionary words.""",
difficulty="Medium", input_format="""The first line contains the target string
s. The second line contains N, the number of words in the dictionary. The next N
lines each contain a word.""", output_format="""Print "true" if the word can be
broken into dictionary words, or "false" otherwise.""", constraints="""1 <=
s.length <= 300 1 <= N <= 1000 1 <= wordDict[i].length <= 20""",
examples="""Input: leetcode 2 leet code

Output: true""" )

Problem.objects.create( title="Combination Sum", description="""Given an array
of distinct integers candidates and a target integer target, return a list of
all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.""", difficulty="Medium",
input_format="""The first line contains N and the target value T. The second
line contains N space-separated candidate integers.""", output_format="""Print
each unique combination on a new line (with numbers space-separated and sorted).
Sort the combinations lexicographically.""", constraints="""1 <= N <= 30 1 <=
candidates[i] <= 200 1 <= T <= 500""", examples="""Input: 4 7 2 3 6 7

Output: 2 2 3 7""" )

Problem.objects.create( title="Permutations", description="""Given an array nums
of distinct integers, return all the possible permutations. You can return the
answer in any order.""", difficulty="Medium", input_format="""The first line
contains N, the number of elements. The second line contains N space-separated
distinct integers.""", output_format="""Print each permutation on a new line as
space-separated integers. The output should be sorted lexicographically.""",
constraints="""1 <= N <= 6 -10 <= nums[i] <= 10""", examples="""Input: 3 1 2 3

Output: 1 2 3 1 3 2 2 1 3 2 3 1 3 1 2 3 2 1""" )

Problem.objects.create( title="Subsets", description="""Given an integer array
nums of unique elements, return all possible subsets (the power set). The
solution set must not contain duplicate subsets. Return the solution in any
order.""", difficulty="Medium", input_format="""The first line contains N. The
second line contains N space-separated integers.""", output_format="""Print each
subset on a new line as space-separated integers. The subsets should be sorted
internally, and the collection of subsets should be printed sorted
lexicographically.""", constraints="""1 <= N <= 10 -10 <= nums[i] <= 10""",
examples="""Input: 3 1 2 3

Output:

1 1 2 1 2 3 1 3 2 2 3 3""" )

# ==========================================

# HARD PROBLEMS (81 to 100)

# ==========================================

Problem.objects.create( title="Median of Two Sorted Arrays",
description="""Given two sorted arrays nums1 and nums2 of size m and n
respectively, return the median of the two sorted arrays. The run time
complexity should be O(log (m+n)).""", difficulty="Hard", input_format="""The
first line contains m and n. The second line contains m space-separated sorted
integers. The third line contains n space-separated sorted integers.""",
output_format="""Print the median as a float (exactly 1 decimal place).""",
constraints="""0 <= m, n <= 1000 1 <= m + n <= 2000 -10^6 <= nums1[i], nums2[j]
<= 10^6""", examples="""Input: 2 1 1 3 2

Output: 2.0""" )

Problem.objects.create( title="Longest Valid Parentheses", description="""Given
a string containing just the characters '(' and ')', find the length of the
longest valid (well-formed) parentheses substring.""", difficulty="Hard",
input_format="""A single line containing the string s.""",
output_format="""Print the length of the longest valid parentheses
substring.""", constraints="""0 <= s.length <= 3 * 10^4 s consists of '(' and
')' only.""", examples="""Input: )()())

Output: 4""" )

Problem.objects.create( title="Edit Distance", description="""Given two strings
word1 and word2, return the minimum number of operations required to convert
word1 to word2. You have the following three operations permitted on a word:
Insert a character, Delete a character, Replace a character.""",
difficulty="Hard", input_format="""The first line contains string word1. The
second line contains string word2.""", output_format="""Print the minimum edit
distance as an integer.""", constraints="""0 <= word1.length, word2.length
<= 500 word1 and word2 consist of lowercase English letters.""",
examples="""Input: horse ros

Output: 3""" )

Problem.objects.create( title="Merge k Sorted Lists", description="""You are
given an array of k linked-lists lists, each linked-list is sorted in ascending
order. Merge all the linked-lists into one sorted linked-list and return it.""",
difficulty="Hard", input_format="""The first line contains K, the number of
lists. The next K lines each start with N (size of the list) followed by N
sorted integers.""", output_format="""Print the merged sorted list as
space-separated integers.""", constraints="""0 <= K <= 10^4 0 <= N <= 500 -10^4
<= Node.val <= 10^4""", examples="""Input: 3 3 1 4 5 3 1 3 4 2 2 6

Output: 1 1 2 3 4 4 5 6""" )

Problem.objects.create( title="Sliding Window Maximum", description="""You are
given an array of integers nums, there is a sliding window of size k which is
moving from the very left of the array to the very right. You can only see the k
numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.""", difficulty="Hard", input_format="""The first
line contains N and K. The second line contains N space-separated integers.""",
output_format="""Print the sliding window maximums as space-separated
integers.""", constraints="""1 <= N <= 10^5 1 <= K <= N -10^4 <= nums[i]
<= 10^4""", examples="""Input: 8 3 1 3 -1 -3 5 3 6 7

Output: 3 3 5 5 6 7""" )

Problem.objects.create( title="Minimum Window Substring", description="""Given
two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included
in the window. If there is no such substring, return the empty string.""",
difficulty="Hard", input_format="""The first line contains string s. The second
line contains string t.""", output_format="""Print the minimum window
substring.""", constraints="""1 <= s.length, t.length <= 10^5 s and t consist of
uppercase and lowercase English letters.""", examples="""Input: ADOBECODEBANC
ABC

Output: BANC""" )

Problem.objects.create( title="Binary Tree Maximum Path Sum", description="""A
path in a binary tree is a sequence of nodes where each pair of adjacent nodes
in the sequence has an edge connecting them. A node can only appear in the
sequence at most once. Note that the path does not need to pass through the
root. The path sum of a path is the sum of the node's values in the path. Given
the root of a binary tree, return the maximum path sum of any non-empty
path.""", difficulty="Hard", input_format="""The first line contains N, the
number of nodes. The second line contains N space-separated integers in
level-order (use -1001 for null).""", output_format="""Print the maximum path
sum.""", constraints="""1 <= N <= 3 * 10^4 -1000 <= Node.val <= 1000""",
examples="""Input: 5 -10 9 20 -1001 -1001 15 7

Output: 42""" )

Problem.objects.create( title="Serialize and Deserialize Binary Tree",
description="""Serialization is the process of converting a data structure or
object into a sequence of bits so that it can be stored in a file or memory
buffer. Design an algorithm to serialize and deserialize a binary tree. There is
no restriction on how your serialization/deserialization algorithm should
work.""", difficulty="Hard", input_format="""The first line contains N, the
number of nodes. The second line contains N space-separated integers in
level-order (use -1 for null).""", output_format="""Print the level-order
representation after performing serialization and deserialization (omitting
trailing nulls).""", constraints="""0 <= N <= 10000 -1000 <= Node.val
<= 1000""", examples="""Input: 5 1 2 3 -1 -1 4 5

Output: 1 2 3 -1 -1 4 5""" )