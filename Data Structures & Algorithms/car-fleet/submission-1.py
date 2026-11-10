class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        PandS = []
        for i in range(len(position)):
            PandS.append((position[i], speed[i]))
        PandS.sort(key=lambda x: x[0], reverse=True)
        # stack = []
        num_fleet = 0
        slowest_time = -1
        for car in PandS:
            time_to_reach = (target - car[0])/car[1]
            if time_to_reach > slowest_time:
                num_fleet += 1
                slowest_time = time_to_reach
        return num_fleet