class Solution:
    def findComplement(self, num: int) -> int:
        # Determine the number of bits required to represent num
        bit_length = num.bit_length()
        
        # Create a mask with all bits set to 1 of the same length as num
        mask = (1 << bit_length) - 1
        
        # Calculate the complement by flipping the bits
        complement = num ^ mask
        
        return complement