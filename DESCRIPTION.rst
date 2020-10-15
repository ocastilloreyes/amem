**amem**
==========

amem (Adapted Meshes for Electromagnetic Modeling) is a python script
that describes the steps to determine the parameters to be applied
for the generation of adapted meshes for electromagnetic modeling.

The meshing rules are described in our paper:

    Castillo-Reyes, O., de la Puente, J., García-Castillo, L. E., & Cela,
    J. M. (2019). Parallel 3-D marine controlled-source electromagnetic
    modelling using high-order tetrahedral Nédélec elements.
    Geophysical Journal International, 219(1), 39-65.

Based on this approach, all element sizes are constrained by the global
spacing dg. When refining the mesh at receivers positions and when embedding
the sources, local spacing ds specifies the size of the mesh according to
the distance to such regions. Furthermore, the outer boundaries are placed at
least four skin-depth away from the modelling region of interest, so that
electric fields generated in the centre of the computational domain are
sufficiently attenuated by the artificial model boundaries, in accordance
with the imposed Dirichlet boundary conditions.

Requirements
------------

**amem** is known to run on various flavors of Linux clusters. Its requirements are:

* `Python 3 <https://www.python.org/>`__ (versions 3.5.2, 3.6.3 and 3.6.9 have been tested)
* `Numpy <http://www.numpy.org/>`__ for arrays manipulation

On Linux, consult the package manager of your preference. **amem** can be
used without any installation by running the main driver from the top-level
directory of the distribution.


Citations
---------

If **amem** been significant to a project that leads to an academic
publication, please acknowledge that fact by citing the project:

* Castillo-Reyes, O., de la Puente, J., García-Castillo, L. E., Cela, J. M. (2019).
  *Parallel 3D marine controlled-source electromagnetic modeling using high-order
  tetrahedral Nédélec elements*. Geophysical Journal International, ggz285,
  vol 219: 39-65. ISSN 0956-540X. https://doi.org/10.1093/gji/ggz285
