# Minimum Amount of Damage Dealt to Bob
import math
class Solution:
    def answer(self, power, damage, health):
        n = len(damage)
        threat = []
        
        # Calculate threat level for each enemy: (time_to_kill / damage[i])
        for i in range(n):
            time_to_kill = math.ceil(health[i] / power)
            threat.append((time_to_kill / damage[i], i))
            
        
        # # Sort enemies by threat level in ascending order
        threat.sort()
        # return threat
        
        totalDamage = 0
        cumulativeDamage = sum(damage)
        
        for i in range(n):
            idx = threat[i][1]
            time_to_kill = math.ceil(health[idx] / power)
            
            # Add the damage dealt by all enemies during the time it takes to kill the current one
            totalDamage += cumulativeDamage * time_to_kill
            
            # After this enemy is killed, subtract its damage from the cumulative damage
            cumulativeDamage -= damage[idx]
        
        return totalDamage
        
        
        
        
result =  Solution().answer(4, [1,2,3,4],  [4,5,6,8])

print(result)