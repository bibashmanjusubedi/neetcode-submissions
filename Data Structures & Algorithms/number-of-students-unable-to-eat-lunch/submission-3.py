class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
     # if students= [ 1,1,0,1] , cnt will be Counter({1:3, 0:1}) ## cnt is a dictionary
     # if sandwich type matches with preferrred student sandwich type
     # decresase the students count
     # decrease the sandwich type that matches count
     # if we dont break endless cycle or infinite loop will happen

     # return the remaining count
        res = len(students)
        cnt = Counter(students)
        for sandwich in sandwiches:
            if cnt[sandwich] > 0:
                res = res - 1
                cnt[sandwich] = cnt[sandwich] -1
            else:
                break

        return res
