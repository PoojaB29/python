#Created by Pooja
#On 22 Feb 2020
#The program explains the implementation of dictionary in python.
def mystery(l,v):
  if len(l) == 0:
    return (v)
  else:
    return (mystery(l[:-1],l[-1]+v))
a=mystery([22,14,19,65,82,55],1)
print(a)
print(type(a))

triples = [ (x,y,z) for x in range(2,4) for y in range(2,5) for z in range(5,7) if 2*x*y > 3*z ]
print(triples)

runs = {"Test":{"Rahul":[90,14,35],"Kohli":[3,103,73,42],"Pujara":[53,15,133,8]},"ODI":{"Sharma":[37,99],"Kohli":[63,47]}}
runs["ODI"]["Rahul"].append([74])
runs["ODI"]["Rahul"].extend([74])
disruns["ODI"]["Rahul"][0]=74
runs["ODI"]["Rahul"]=[74]

actor={}
actor["Star Wars"] = ["Rey","Ridley"]
actor["Star Wars, Rey"] = "Ridley"
actor[["Star Wars", "Rey"]] = "Ridley"
actor[("Star Wars", "Rey")] = "Ridley"
