import queue
# 
# 拓扑排序的思想解决
# 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        record = [0] * numCourses
        select_node = []

        for i in range(len(prerequisites)):
            id_prev, id_next = prerequisites[i]
            record[id_prev] += 1
            graph[id_next].append(id_prev)
        
        search_queue = queue.Queue()
        for i in range(numCourses):
            if record[i] == 0:
                search_queue.put(i)
                select_node.append(i)
        
        while not search_queue.empty():
            idx = search_queue.get()
            for id in graph[idx]:
                record[id] -= 1
                if record[id] == 0:
                    search_queue.put(id)
                    select_node.append(id)
        
        if len(select_node) == numCourses:
            return True
        
        return False