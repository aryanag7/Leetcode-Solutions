class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        distance_1=0
   
        if start>destination:
            temp=start
            start=destination
            destination=temp
    

        
        for i in range(start,destination):
       
       
        
            distance_1=distance_1+distance[i]
    
        new_distance=0
    
        for i in range(0,len(distance)):
            new_distance=new_distance+distance[i]
        distance_2=new_distance-distance_1

        return min(distance_1,distance_2) 

        
        
