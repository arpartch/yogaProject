#!/usr/bin/env python3
poses = ["Down dog", "Child's Pose", "Upward facing dog", "Crow Pose"]
poses2 = ["Down dog", "Upward facing dog", "Child's Pose", "Crow Pose"]
# print just the first element of the list (Down Dog)
print (poses[0])
#static directly accesses numeric postions in the array, fastest but inflexible 
def get_dogs_static(poses):
	print (poses[0], poses[2])
    #loop with if conditionally  adds items to a new array
    #fast and flexible but long
def get_dogs_loop (poses):
    new_dogs = []
    for pose in poses:
        if pose.endswith("dog"):
            new_dogs.append(pose)
    return new_dogs
    #list comprehesion with if returns a reduced array
    #fast, flexible, and short
def transform(thing):
    return "start" + thing.upper() + "end"
def get_dogs_comprehension (poses):
    return [transform(pose) for pose in poses if pose.endswith("dog")]
    #recursive reducer fast, most flexible, and confusing

def get_dogs (poses):
	# print just the elements of the list containing the word "dog"
	print (poses[0], poses[2])
print(get_dogs_comprehension(poses))
print(get_dogs_comprehension(poses2))

# add "Bridge Pose" to the list
# poses.append("Bridge Pose")
# print poses

# remove the items from the list containing the word "dog"
def no_dogs_loop(poses):
    no_dogs = []
    for pose in poses:
        if not pose.endswith("dog"):
            no_dogs.append(pose)
    return no_dogs
print(no_dogs_loop(poses))

# is there a way to do this in a single line?

# make every item in the list all caps
poses = [element.upper() for element in poses]
# print poses

#why do my brackets show? 

#red green refractor: a way of thinking about programing
	#red is create a falsifyable statement and prove that is false
    #green is make the statement true 
    #refactor is explore all the ways you can think of where it could be true but also (generic | fast | small | robust | obvious)
    


