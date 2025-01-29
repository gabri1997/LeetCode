"""
You are given an integer array nums. 
You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
"""

def jump_game(nums):

    # La somma dei numeri deve essere pari all'indice dell'ultimo elemento 
    target_index = len(nums) - 1
    current_index = 0

    while(current_index <= target_index):        
            numero_attuale = nums[current_index]
            if numero_attuale == 0 and current_index < target_index:
                  return False
            current_index += numero_attuale
            if current_index >= target_index:
                    return True
            
    return False 

if __name__ == '__main__':
    nums = [3, 2, 1, 0, 4]
    bool = jump_game(nums)
    print(bool)