"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. 
You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. 
If there exists a solution, it is guaranteed to be unique.
"""

def canCompleteCircuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    total_cost = sum(cost)
    total_gas = sum(gas)

    if total_cost < total_gas:
        print('Non è possibile completare il percorso')
        return -1

    start_index = 0
    tank = 0

    for i in range(len(gas)):
        tank += gas[i] - cost[i]

        # Controllo di avere benzina
        if tank < 0:
            start_index = i + 1
            tank = 0

    return start_index

if __name__ == '__main__':
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    canCompleteCircuit(gas, cost)