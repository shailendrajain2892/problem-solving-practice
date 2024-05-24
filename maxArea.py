def maxArea(height):
    ans = []
    for i,n in enumerate(height):
        for j,m in enumerate(height[i+1:]):
            area=1
            if m > n:
                area = n*(j+1)
            else:
                temp=m
                area = temp*(j+1)
            ans.append(area)
    return max(ans)

def maxAreaO(height):
    low=0
    high=len(height)-1
    max_area = 0
    while low < high: 
        # calculate width
        width = high - low 

        # calculate height - 
        # we can only consider only min height as we can't slant 
        hght = min(height[low], height[high])

        # calculate aread based on above height and width
        current_area = hght*width

        # track the max area
        max_area = max(current_area, max_area)

        if height[low] < height[high]:
            low+=1
        else:
            high-=1
    return max_area
        
height1= [1,2,3,4,5,6,7,8,9]
height2 = [1,1]
print(maxAreaO(height1))