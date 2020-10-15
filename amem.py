#!/usr/bin/env python3
''' Amem is a python script that describes the steps to determine the parameters to be applied
for the generation of adapted meshes for electromagnetic modeling.
The model used as test case is that described by:

    Constable, S., Weiss, C.J., 2006. Mapping thin resistors and hydrocarbons
    with marine em methods: Insights from 1d modeling. Geophysics 71, G43–G51.

The meshing rules are described in our paper:

    Castillo-Reyes, O., de la Puente, J., García-Castillo, L. E., & Cela,
    J. M. (2019). Parallel 3-D marine controlled-source electromagnetic
    modelling using high-order tetrahedral Nédélec elements.
    Geophysical Journal International, 219(1), 39-65.

Based on this approach, all element sizes are constrained by the global
spacing dg. When refining the mesh at receivers positions and when embedding
the sources, local spacing dss specifies the size of the mesh according to
the distance to such regions. Furthermore, the outer boundaries are placed at
least four skin-depth away from the modelling region of interest, so that
electric fields generated in the centre of the computational domain are
sufficiently attenuated by the artificial model boundaries, in accordance
with the imposed Dirichlet boundary conditions.

Parameters:
    Frequency --> 2 Hz
    Source position [x,y,z] --> [1750.0, 1750.0, -975.0]
    Conductivity [Sediments, Oil, Sediments, Water] --> [1.0, 1.0/100.0, 1.0, 1.0/0.3] S/m
    x-dimensions --> [-1000., 4500.] m
    y-dimensions --> [0., 3500.] m
    z-dimensions --> [-3500., 0.] m

Author:  Octavio Castillo-Reyes
Contact: octavio.castillo@bsc.es
'''
import numpy as np

# --------------------------------
# --       USER PARAMETERS      --
# --------------------------------
# Frequency for modeling (Hz)
frequency = 2
# Material conductivity (S/m). This example has 4 materials (from bottom to top): [Sediments, Oil, Sediments, Water]
sigma_materials = np.array([1.0, 1.0/100.0, 1.0, 1.0/0.3], dtype=np.float)
# FEM basis order within petgem (high-order basis from 1 to 6)
p = 2     # 1,2,3,4,5,6
# Model dimensions ([min, max])
x_dimensions = np.array([-1000., 4500.], dtype=np.float)
y_dimensions = np.array([0., 3500.], dtype=np.float)
z_dimensions = np.array([-3500., 0.], dtype=np.float)

# --------------------------------
# --   CONSTANTS DEFINITION     --
# --------------------------------
# Depending on p order, we will need more or less points per skin-depth.
# Here, I use a number of points per-skin depth to guarantee 2% error
# in electromagnetic responses (This is based on the results of our last paper)
#                               p_oder_1, p_oder_2, p_oder_3, p_oder_4, p_oder_5, p_oder_6
rg = np.array([2.5382,   1.0918,   0.9433,   0.8512,   0.7847,   0.5682], dtype=np.float)
# Resolution number between 13 and 6, which argo depends on the p order
rs = np.array([13, 11, 10, 9, 8, 6], dtype=np.float)

# --------------------------------
# --  COMPUTE MESH PARAMETERS   --
# --------------------------------
# Skin-depth computation (in meters)
skin_depth = 503.*np.sqrt(1./(frequency*sigma_materials))

# Compute global mesh element size (in meters) --> whole domain
dg = np.round(np.min(skin_depth)/rg[p-1])

# Compute local mesh element size (in meters) --> near to source/receiver locations
# The element size ds must be logarithmically increased until reaching dg (this
# usually happens at a distance of 10*ds)
ds = np.round(dg/rs[p-1])

# Compute new model dimensions
boundary_extension = np.array([-dg*4. , dg*4.], dtype=np.float)
x_dimensions = x_dimensions + boundary_extension
y_dimensions = y_dimensions + boundary_extension
z_dimensions = z_dimensions + boundary_extension

# Print parameters
print('----------------------------------------------------------')
print('Basis order of FEM (p)            --> ', p)
print('Global spacing (whole domain)     --> ', dg, 'm')
print('Local spacing (source, receivers) --> ', ds, 'm')
print('Model x-dimensions (min max)      --> ', x_dimensions, 'm')
print('Model y-dimensions (min max)      --> ', y_dimensions, 'm')
print('Model z-dimensions (min max)      --> ', z_dimensions, 'm')
print('----------------------------------------------------------')
