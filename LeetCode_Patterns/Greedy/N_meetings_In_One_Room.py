'''

Difficulty: EasyAccuracy: 45.3%Submissions: 233K+Points: 2
There is one meeting room in a firm. There are n meetings in the form of (start[i], end[i]) where start[i] is start time of meeting i and end[i] is finish time of meeting i.
What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting room at a particular time? Return the maximum number of meetings that can be held in the meeting room.

 

Note: Start time of one chosen meeting can't be equal to the end time of the other chosen meeting.


Examples :

Input: n = 6, start[] = {1,3,0,5,8,5}, end[] =  {2,4,6,7,9,9}
Output: 4
Explanation: Maximum four meetings can be held with given start and end timings. The meetings are - (1, 2),(3, 4), (5,7) and (8,9)
Input: n = 3, start[] = {10, 12, 20}, end[] = {20, 25, 30}
Output: 1
Explanation: Only one meetings can be held with given start and end timings.
Expected Time Complexity : O(n*Logn)
Expected Auxilliary Space : O(n)


Constraints:
1 ≤ n ≤ 105
0 ≤ start[i] < end[i] ≤ 105

Seen this question in a real interview before ?
Yes
No
Company Tags

'''
class Data:
    def __init__(self,start=None,end=None):
        self.start = start
        self.end = end

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        arr = [Data(start[i], end[i]) for i in range(n)]  # Creating Data objects
        arr = sorted(arr, key=lambda x: x.end)  # Sorting Data objects by end time

        count = 1
        prevTime = arr[0].end

        for i in range(1, n):
            if arr[i].start > prevTime:
                count += 1
                prevTime = arr[i].end

        return count