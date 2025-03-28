class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # Initialize position
        x, y = 0, 0
        
        # Process each move
        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1
        
        # Check if the robot is back at the origin
        return x == 0 and y == 0