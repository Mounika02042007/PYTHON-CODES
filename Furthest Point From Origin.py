class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        count=0
        blank=0
        for i in range(0,len(moves)):
            if(moves[i]=="L"):
                count-=1
            elif(moves[i]=="R"):
                count+=1
            else:
                blank+=1
        return abs(count)+blank
