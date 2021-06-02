# find all pairs that sum to a specific value lab

def pairs_that_sum(array, v):
	# TODO
	return []


def display_results(pairs,v):
    print(f"The pairs that sum to {v} are: ")
    for i in range(len(pairs)):
        print(pairs[i][0] + " and " + pairs[i][1])


array = [7,15,2,95,31,-46,-84,-10,88,55,66,-25,15,-36,-15,21,71,-37,-69,1,-13,
         -88,-24,100,60,1,-17,43,0,70,-25,83,-60,-40,58,82,-70,-8,89,31,-93,-62,
         27,-87,-6,80,2,-55,46,96,43,-37,-34,-27,-96,58,20,35,-40,67,-96,48,-54,
         -60,-67,-31,93,79,33,74,30,-53,88,-41,-78,-92,35,39,-37,-14,60,-39,85,
         69,-90,-56,-74,98,-74,-21,84,-56,-83,-22,35,1,-21,90,40,2]


v = 42
pairs = pairs_that_sum(array, v)
display_results(pairs,v)
