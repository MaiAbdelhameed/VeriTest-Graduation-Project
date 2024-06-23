from z3 import *

# Create three boolean variables
x = Bool('x')
y = Bool('y')
z = Bool('z')

# Create a Z3 solver
solver = Solver()

# Add the constraint that at least one of x, y, or z must be True
solver.add(Or(x, y, z))


# If a solution is found, retrieve the model
model = solver.model()
# Print the values of x, y, z that satisfy the constraint
print("Solution found:")
print("x =", model[x])
print("y =", model[y])
print("z =", model[z])
