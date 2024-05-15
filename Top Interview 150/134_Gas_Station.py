class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total_tank, current_tank = 0, 0
        starting_station = 0
        
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]
            
            # If the current tank is negative, reset the starting station
            if current_tank < 0:
                starting_station = i + 1
                current_tank = 0
        
        return starting_station if total_tank >= 0 else -1
    ########################################
    #smart version: it is proofed that:
    # if sum of the gas provided is greater than or equal
    # to the sum of the cost to travel between the stations
    # then there is a solution for sure
    class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        idx = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                idx = i + 1
        return idx