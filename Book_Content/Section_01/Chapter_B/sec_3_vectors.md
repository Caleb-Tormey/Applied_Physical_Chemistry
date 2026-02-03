## Vectors
It isn't just enough to say something is moving at a certain rate; we must also talk about in what direction. Given a coordinate system, we can define essential physical properties like velocity and acceleration based on these principles. This is the point of a vector. Unlike a simple numerical value, a vector contains information about both its magnitude (how much) and its direction (where).

In our previous discussions on Cylindrical and Spherical coordinates, we used values like $r, \theta, \text{ and } \phi$ to define a point in space. A vector is effectively the "arrow" that points from the origin $(0,0,0)$ to that specific point, or between any two points in that space.

### Scalars vs. Vectors
To understand vectors, we must distinguish them from **scalars**.

- Scalar: A quantity described strictly by a single value (magnitude).

    * Example: Speed is a scalar. If a car is traveling at 60 mph, you know its speed, but you don't know where it is going.

- Vector: A quantity described by both magnitude and direction.

    * Example: Velocity is a vector. If a car is traveling at 60 mph North, you have its velocity.

In chemistry, temperature ($T$) and mass ($m$) are scalars, while the dipole moment ($\vec{\mu}$) of a molecule or the force ($\vec{F}$) applied during a molecular collision are vectors.
:::{code-cell} python
:tags: ["remove-input"]
# --- START: Required for every block that imports from _ext ---
import sys
import os
from IPython.display import display, HTML

# Adjust the path based on file depth
try:
    cwd = os.getcwd()
    # e.g., use ("..", "..") for a file 2 levels deep.
    project_root = os.path.abspath(os.path.join(cwd, "..", "..", ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
except Exception as e:
    print(f"Error setting project path: {e}")

from _ext.interactive_qa import QuestionBlock
# --- END: Required for every block ---
questions = QuestionBlock()
questions.add_question(
    question_id="sec-01-ch-B-q04",
    question_text="Why is it insufficient to describe the momentum of a gas particle using only a scalar value? What physical information would be missing? "
)
display(HTML(questions.render()))
:::
### Vector Notation
n textbooks, vectors are typically identified by boldface type ($\mathbf{V}$) or by a small arrow placed above the letter ($\vec{V}$).

In a Cartesian coordinate system, we represent a vector by breaking it down into its "shadows" or projections along the axes. We use unit vectors ($\hat{i}, \hat{j}, \hat{k}$) to represent a length of "1" in the $x, y, \text{ and } z$ directions respectively. This allows us to write any vector as a sum of these components:

$$\vec{V} = V_x\hat{i} + V_y\hat{j} + V_z\hat{k}$$

Where $V_x, V_y, \text{ and } V_z$ are the components of the vector.

### Calculating Magnitude: The Geomeotry of Space
The magnitude of the vector is simply its length. To calculate this, we rely on the geometry of right triangles and the Pythagorean theorem.
#### The 2D Case
If we look at a vector in a 2D plane ($x$ and $y$), the vector itself forms the hypotenuse of a right triangle, where the $x$-component and $y$-component are the two legs.

$$|\vec{V}| = \sqrt{V_x^2 + V_y^2}$$

#### The 3D Case and Euclidean Distance

When we move into three dimensions, this logic extends into what we call Euclidean distance. Whether we are in Cartesian, Cylindrical, or Spherical space, the total length from the origin to the tip of the vector is found by:

$$|\vec{V}| = \sqrt{V_x^2 + V_y^2 + V_z^2}$$

This magnitude represents the "absolute value" of the vector. This is why the magnitude of a velocity vector is simply the speed of the object.
:::{code-cell} python
:tags: ["remove-input"]
# --- START: Required for every block that imports from _ext ---
import sys
import os
from IPython.display import display, HTML

# Adjust the path based on file depth
try:
    cwd = os.getcwd()
    # e.g., use ("..", "..") for a file 2 levels deep.
    project_root = os.path.abspath(os.path.join(cwd, "..", "..", ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
except Exception as e:
    print(f"Error setting project path: {e}")

from _ext.interactive_qa import QuestionBlock
# --- END: Required for every block ---
questions = QuestionBlock()
questions.add_question(
    question_id="sec-01-ch-B-q05",
    question_text="If you have a 2D vector and you double the length of its $x$-component while keeping the $y$-component the same, does the total magnitude of the vector double? Explain why or why not using the geometry of space."
)
display(HTML(questions.render()))
:::
### Interactive Vector Explorer

Adjust the sliders below to change the $x$ and $y$ components of the vector. Observe how the red and green component vectors add up to create the blue resultant vector, and how the magnitude is calculated.

:::{include} interactive_code/vectors.md
:::
**You will notice the magnitude of the vector equation is similar to how we found distances between two points. How are they related?**
### Mathematical operations with vectors
One of the most powerful aspects of vectors is that they can be combined to describe complex motions or forces. In physical chemistry, we often need to add vectors together—for example, when calculating the total dipole moment of a molecule by summing the bond dipoles of individual chemical bonds.

#### Vector Addition (Component-wise)
Mathematically, adding two vectors is straightforward if they are in Cartesian form. You simply add the corresponding components together. If we have $\vec{A} = A_x\hat{i} + A_y\hat{j}$ and $\vec{B} = B_x\hat{i} + B_y\hat{j}$, the resultant vector $\vec{R}$ is:

$$\vec{R} = \vec{A} + \vec{B} = (A_x + B_x)\hat{i} + (A_y + B_y)\hat{j}$$

#### Vector Subtraction
Subtraction is treated as adding a negative vector. To subtract $\vec{B}$ from $\vec{A}$, you simply flip the direction of $\vec{B}$ and add it to $\vec{A}$:

$$\vec{R} = \vec{A} - \vec{B} = (A_x - B_x)\hat{i} + (A_y - B_y)\hat{j}$$

#### Visual Addition: The Head-to-Tail Method
While the math is simple, the visual representation is key to understanding physical systems. To add two vectors visually, we use the Head-to-Tail method:

1. Draw vector $\vec{A}$ starting from the origin.

2. Draw vector $\vec{B}$ starting from the head (the tip) of vector $\vec{A}$.

3. The resultant vector $\vec{R}$ is the arrow drawn from the tail of the first vector to the head of the last vector.

#### Interactive Vector Addition Explorer

Adjust the components of Vector $\vec{A}$ (Red) and Vector $\vec{B}$ (Green). The widget shows the Head-to-Tail addition. The Resultant Vector $\vec{R}$ (Blue) shows the final sum.
:::{include} interactive_code/vector_addition.md
:::