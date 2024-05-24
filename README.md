# problem-solving-practice

# Container With Most Water

This repository contains a Python implementation of the "Container With Most Water" problem. The goal is to find two lines that, together with the x-axis, form a container that holds the maximum amount of water.

## Problem Description

Given an integer array `height` of length `n`, where `height[i]` represents the height of a vertical line at position `i`, find two lines that form a container, along with the x-axis, such that the container contains the most water.

## Solution Approach

The solution uses a two-pointer approach to find the maximum area efficiently in O(n) time complexity. 

### Intuition Behind the Two-Pointer Approach

1. **Initialize Two Pointers**: Start with one pointer at the beginning (`left = 0`) and one at the end (`right = n - 1`) of the array.
2. **Calculate Area**: Compute the area formed by the lines at the `left` and `right` pointers.
3. **Update Maximum Area**: Keep track of the maximum area encountered.
4. **Move Pointers**: Move the pointer pointing to the shorter line inward to potentially find a taller line that can form a larger area.
5. **Repeat Until Pointers Meet**: Continue this process until the two pointers meet.

## Code

```python
def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    
    while left < right:
        # Calculate the width and height of the container
        width = right - left
        h = min(height[left], height[right])
        
        # Calculate the current area
        current_area = width * h
        
        # Update the maximum area
        max_area = max(max_area, current_area)
        
        # Move the pointers
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

# Example usage
if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print("The maximum amount of water a container can store:", maxArea(height))
