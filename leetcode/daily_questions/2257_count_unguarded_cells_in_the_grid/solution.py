from typing import List
import numpy as np

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        """
        m x n: 0 indexed grid
        walls: 2d integer array, walls[j] = [row_j, col_j]
        guards: 2d integer array guards[i] = [row_i, col_i] 
        """
        walls_set = set(tuple(w) for w in walls) # Use set with tuples 
        guards_set = set(tuple(g) for g in guards)
        vision_set = set()
   
        for guard_row, guard_col in guards:
            # South
            for r in range(guard_row + 1, m):
                pos = (r, guard_col)
                if pos in walls_set or pos in guards_set:
                    break
                vision_set.add(pos)

            # North
            for r in range(guard_row - 1, -1, -1):
                pos = (r, guard_col)
                if pos in walls_set or pos in guards_set:
                    break
                vision_set.add(pos)

            # East
            for c in range(guard_col + 1, n):
                pos = (guard_row, c)
                if pos in walls_set or pos in guards_set:
                    break
                vision_set.add(pos)

            # West
            for c in range(guard_col - 1, -1, -1):
                pos = (guard_row, c)
                if pos in walls_set or pos in guards_set:
                    break
                vision_set.add(pos)

        unguarded = 0
        for r in range(m):
            for c in range(n):
                pos = (r,c)
                if pos not in walls_set and pos not in guards_set and pos not in vision_set:
                    unguarded += 1
        print(unguarded)
        return unguarded



def main():
    m = 4
    n = 6
    guards = [[0,0],[1,1],[2,3]]
    walls = [[0,1],[2,2],[1,4]]

    sol = Solution()

    sol.countUnguarded(m,n,guards,walls)



if __name__ == "__main__":
    main()