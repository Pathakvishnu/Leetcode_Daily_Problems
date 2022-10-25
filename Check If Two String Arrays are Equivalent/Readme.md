<h2>Problem Statement</h2>
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.<br>

A string is represented by an array if the array elements concatenated in order forms the string.<br>

 

<h3>Example 1:</h3>

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]<br/>
Output: true<br/>
Explanation:<br/>
word1 represents string "ab" + "c" -> "abc"<br/>
word2 represents string "a" + "bc" -> "abc"<br/>
The strings are the same, so return true.<br/>

<h3>Example 2:</h3>
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]<br/>
Output: false<br/>

<h3>Example 3:</h3>
Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]<br/>
Output: true<br/>

 

<h3>Constraints:</h3>

1 <= word1.length, word2.length <= 103<br/>
1 <= word1[i].length, word2[i].length <= 103<br/>
1 <= sum(word1[i].length), sum(word2[i].length) <= 103<br/>
word1[i] and word2[i] consist of lowercase letters.<br/>

