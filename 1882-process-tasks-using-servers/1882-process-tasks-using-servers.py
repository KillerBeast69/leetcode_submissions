class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        avail = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(avail)
        unavail = []
        res = [0] * len(tasks)
        t = 0

        for i in range(len(tasks)):
            t = max(t, i)

            if len(avail) == 0:
                t = unavail[0][0]
            while unavail and t >= unavail[0][0]:
                timefree, weight, index = heapq.heappop(unavail)
                heapq.heappush(avail, (weight, index))

            weight, index = heapq.heappop(avail)
            res[i] = index

            heapq.heappush(unavail, (tasks[i] + t, weight, index))

        return res

            