# vectorise
A Python package that implements and represents basic functionalities of Vectors.

It is also available on [PyPI](https://pypi.org/project/vectorise/)

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
## Quick Guide
***Please Read till the End***
- Import the Package using `import vectorise as vr`
- `vr.Vector` creates a vector object.
    - By Default it creates a null vector.
    - It is ***Mutable*** i.e after its creation the vector object can be changed by `<Vector object>.[x, y, z] = value`.
- Direction Ratios of a Vector can be retrieved by the following methods :-
    - `<Vector object>.x` returns the direction ratio on the X-axis unit vector **i**.
    - `<Vector object>.y` returns the direction ratio on the Y-axis unit vector **j**.
    - `<Vector object>.z` returns the direction ratio on the Z-axis unit vector **k**.
    - `<Vector object>.directionRatios()` returns a **tuple** of the direction ratios of **i**, **j**, **k** respectively.
- `<Vector object>.directionCosines()` returns a **tuple** of the direction cosines of **i**, **j**, **k** respectively.
- `<Vector object>.directionAngles()` returns a **tuple** of the direction angles of **i**, **j**, **k** respectively.
- `<Vector object>.magnitude()` returns the magnitude of the Vector.
- `<Vector object>.toUnit()` converts the given Vector to unit vector and returns it.
- **All the Arithmetic Operations**, except **Multiplication**; can be done using their usual symbols.
- `<Vector object>.dot(<Vector object>)` returns the **Dot Product** of the given 2 Vectors, which would be a **Scalar** i.e either an **integer** or a **floating point number**.
- `<Vector object>.cross(<Vector object>)` returns the **Cross Product** of the given 2 Vectors, which would be another instance of Vector.
- `<Vector object>.makesAngleWith(<Vector object>)` returns the **angle** between the given 2 Vectors.
- `<Vector object>.projectionOn(<Vector object>)` returns the projection of the self Vector over the Vector passed in.
- `<Vector object>.projectionVectorOn(<Vector object>)` returns the projection Vector of the self Vector over the Vector passed in.

***Please Note :- All the Angles Returned are in DEGREES, NOT IN RADIANS; so as to make calculations and understandability effortless.***
***Have Fun Learning!!!***

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
