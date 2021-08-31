class Solution(object):
    def minSessions(self, tasks, sessionTime):
        """
        :type tasks: List[int]
        :type sessionTime: int
        :rtype: int
        """
        tasks.sort()
        count = 0

        while len(tasks)>0:
            # we start with the biggest and keep eliminating
            currentTask = tasks.pop()
            currentTaskList = [currentTask]
            sessionLeft = sessionTime - currentTask
            i = len(tasks)
            while sessionLeft>0 and i>0:
                i -= 1
                if sessionLeft >= tasks[i]:
                    newTask = tasks.pop(i)
                    sessionLeft -= newTask
                    currentTaskList.append(newTask)
            count += 1
            print(currentTaskList)

        return count

# this doesn't work 

s = Solution()
tasks = [2,3,3,4,4,4,5,6,7,10]
sessionTime = 12
# answer should be 2
print(s.minSessions(tasks, sessionTime))