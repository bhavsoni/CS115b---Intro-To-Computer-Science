from cs import *

Inf = float("inf")
FiveCities = ["A", "B", "C", "D", "E"]
FiveDists = {("A", "A"):0, ("A", "B"):1, ("A", "C"):3, ("A", "D"):7, ("A", "E"):Inf,
             ("B", "A"):Inf, ("B", "B"):0, ("B", "C"):42, ("B", "D"):6, ("B", "E"):27,
             ("C", "A"):Inf, ("C", "B"):Inf, ("C", "C"):0, ("C", "D"):2, ("C", "E"):13,
             ("D", "A"):Inf, ("D", "B"):Inf, ("D", "C"):Inf, ("D", "D"):0, ("D", "E"):5,
             ("E", "A"):Inf, ("E", "B"):Inf, ("E", "C"):Inf, ("E", "D"):Inf, ("E", "E"):0
            }           

def shortestPath(Cities,Dists):
    if Cities == [] or len(Cities) == 1:
        return 0
    if len(Cities) == 2:
        return Dists[(Cities[0],Cities[1])]
    else:
        useIt = shortestPath(Cities[1:],Dists) + Dists[(Cities[0],Cities[1])]
        loseIt = shortestPath([Cities[0]]+Cities[2:],Dists)
        return min(useIt,loseIt)

def findShortestPath(Cities,Dists):
    if Cities == [] or len(Cities) == 1:
        return [0,[]]
    if len(Cities) == 2:
        return [Dists[(Cities[0],Cities[1])],Cities]
    else:
        useIt = findShortestPath(Cities[1:],Dists)
        useIt[0] = useIt[0] + Dists[(Cities[0],Cities[1])]
        useIt[1] = [Cities[0]] + useIt[1] 
        loseIt = findShortestPath([Cities[0]]+Cities[2:],Dists)
        if useIt[0] < loseIt[0]:
            return useIt
        return loseIt

print(findShortestPath(FiveCities, FiveDists))
print()
print(shortestPath(FiveCities, FiveDists))
print()
print(shortestPath(["C", "D", "E"], FiveDists))
print()
print(shortestPath(["E"], FiveDists))

