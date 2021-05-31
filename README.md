# vectorise
A Python package that implements and represents basic functionalities of Vectors.
It is also available on [PyPI](https:pypi.org/)

## Installation in Python
***Note \:- Requires Python Version 3.x***

**If there are 2 or more versions of Python installed in your system (which mostly occurs in UNIX/Linux systems) then please run _any one_ of the commands in the BASH/ZSH Shell \:-**
```bash
$ pip3 install vectorise

$ python3 -m pip install vectorise
```

**If there is only Python 3.x installed in your system like in Windows systems then please run _any one_ of commands in the Command Prompt \:-**
```cmd
>pip install vectorise

>python -m pip install vectorise
```

## A Sample Implementation
```python3
from vectorise import Vector

v1 = Vector(-3, 4, 5)
v2 = Vector(21, -54, -101)
v3 = Vector(-3, 4, 5)

print("V1 :", v1, "\nV2 :", v2, "\nV3 :", v3)

print("\nV1 == V2 :", v1 == v2)
print("V1 == V3 :", v1 == v3)

print("\nDirection Angles of V1 :", v1.directionAngles())
print("Direction Angles of V2 :", v2.directionAngles())

print("\nDirection Ratios of V1 :", v1.directionRatios())
print("Direction Ratios of V2 :", v2.directionRatios())

print("\nDirection Cosines of V1 :", v1.directionCosines())
print("Direction Cosines of V2 :", v2.directionCosines())

print("\n|V1| :", v1.magnitude(), "\n|V2| :", v2.magnitude())

print("\nUnit Vector of V1 :", v1.toUnit(), "\nUnit Vector of V2 :", v2.toUnit())

print("\nV1 + V2 :", v1+v2)
print("V1 - V2 :", v1-v2)

print("\nV1 * 2 :", v1*2)
print("V2 * 3 :", v2*3)

print("\nV1 . V2 :",  v1.dot(v2))
print("V1 X V2 :", v1.cross(v2))
print("V2 X V1 :", v2.cross(v1))

print("\nAngle between V1 and V2 :", v1.makesAngleWith(v2))

print("\nProjection Vector of V1 on V2 :", v1.projectionVectorOn(v2))
print("Projection Vector of V2 on V1 :", v2.projectionVectorOn(v1))

print("\nProjection of V1 on V2 :", v1.projectionOn(v2))
print("Projection of V2 on V1 :", v2.projectionOn(v1))
```
