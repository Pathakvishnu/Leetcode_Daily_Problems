<h1>Problem Statement</h1>

You have n flower seeds. Every seed must be planted first before it can begin to grow, then bloom. Planting a seed takes time and so does the growth of a seed. <br/>
You are given two 0-indexed integer arrays plantTime and growTime, of length n each:<br/>

plantTime[i] is the number of full days it takes you to plant the ith seed. Every day, you can work on planting exactly one seed. You do not have to work on planting the
same seed on consecutive days, but the planting of a seed is not complete until you have worked plantTime[i] days on planting it in total.<br/>
growTime[i] is the number of full days it takes the ith seed to grow after being completely planted. After the last day of its growth, the flower blooms and 
stays bloomed forever.<br/>
From the beginning of day 0, you can plant the seeds in any order.<br/>

Return the earliest possible day where all seeds are blooming.<br/>

<h2>Example 1:</h2><br/>

![image](https://user-images.githubusercontent.com/37989419/198844086-4fa530e1-693d-4b34-8638-06d7c4ff45ea.png)<br/>

Input: plantTime = [1,4,3], growTime = [2,3,1]<br/>
Output: 9<br/>
Explanation: The grayed out pots represent planting days, colored pots represent growing days, and the flower represents the day it blooms.<br/>
One optimal way is:<br/>
On day 0, plant the 0th seed. The seed grows for 2 full days and blooms on day 3.<br/>
On days 1, 2, 3, and 4, plant the 1st seed. The seed grows for 3 full days and blooms on day 8.<br/>
On days 5, 6, and 7, plant the 2nd seed. The seed grows for 1 full day and blooms on day 9.<br/>
Thus, on day 9, all the seeds are blooming.<br/>

<h2>Constraints:</h2><br/>

n == plantTime.length == growTime.length<br/>
1 <= n <= 105<br/>
1 <= plantTime[i], growTime[i] <= 104<br/>
