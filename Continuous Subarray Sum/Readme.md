<h1>Problem Statement</h1>
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.<br>

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.<br>

 

<h2>Example 1:</h2>

Input: nums = [23,2,4,6,7], k = 6<br>
Output: true<br>
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.<br>

<h2>Example 2:</h2>

Input: nums = [23,2,6,4,7], k = 6<br>
Output: true<br>
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.<br>
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.<br>

<h2>Example 3:</h2>

Input: nums = [23,2,6,4,7], k = 13<br>
Output: false<br>
 

<h2>Constraints:</h2>

1 <= nums.length <= 105 <br>
0 <= nums[i] <= 109 <br>
0 <= sum(nums[i]) <= 231 - 1 <br>
1 <= k <= 231 - 1<br>
