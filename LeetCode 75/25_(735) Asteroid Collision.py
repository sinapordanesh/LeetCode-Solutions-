class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
                continue
            
            previous = stack.pop()
            
            if asteroid*previous > 0:
                stack.append(previous)
                stack.append(asteroid)
                continue
            else:
                winner, withdraw = None, None
                while asteroid*previous < 0:
                    if abs(asteroid) < abs(previous):
                        winner = previous
                        break
                    elif abs(asteroid) > abs(previous):
                        previous = stack.pop()
                        # winner = None
                    else:
                        withdraw = 1
                        break

                if winner:
                    stack.append(winner)
                elif withdraw:
                    continue
                else:
                    stack.append(previous)
                    stack.appen(asteroid)

        return stack