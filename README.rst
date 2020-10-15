----

.. image:: https://readthedocs.org/projects/emg3d/badge/?version=latest
   :target: https://github.com/ocastilloreyes/amem/
   :alt: Documentation Status
.. image:: https://img.shields.io/github/v/release/ocastilloreyes/amem
   :target: https://github.com/ocastilloreyes/amem/releases
   :alt: GitHub release (latest by date)
.. image:: https://img.shields.io/static/v1?label=Ubuntu&logo=Ubuntu&logoColor=white&message=support&color=success
   :target: https://ubuntu.com/
   :alt: Ubuntu support
.. image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg
   :target: https://opensource.org/licenses/BSD-3-Clause
   :alt: amem-license


Adapted Meshes for Electromagnetic Modeling
-------------------------------------------
**amem** (Adapted Meshes for Electromagnetic Modeling) is a python script
that describes the steps to determine the parameters to be applied
for the generation of adapted meshes for electromagnetic modeling.

Based on this approach, all element sizes are constrained by the global
spacing dg. When refining the mesh at receivers positions and when embedding
the sources, local spacing ds specifies the size of the mesh according to
the distance to such regions. Furthermore, the outer boundaries are placed at
least four skin-depth away from the modelling region of interest, so that
electric fields generated in the centre of the computational domain are
sufficiently attenuated by the artificial model boundaries, in accordance
with the imposed Dirichlet boundary conditions.

Requests and contributions are welcome.

Dependencies
------------

-  Python\_ (versions 3.5.2, 3.6.3, 3.6.9, 3.12.0 have been tested).

-  A recent NumPy\_ release.

Citation
--------
If you publish results for which you used **amem**, please give credit by citing
`Castillo-Reyes, O. et al. (2019) <https://doi.org/10.1093/gji/ggz285>`_:

  Castillo-Reyes, O., de la Puente, J., García-Castillo, L. E., Cela, J.M. (2019).
  *Parallel 3-D marine controlled-source electromagnetic modelling using high-order
  tetrahedral Nédélec elements*. Geophysical Journal International, Volume 219,
  Issue 1, October 2019, Pages 39–65, https://doi.org/10.1093/gji/ggz285


License
-------
**amem** is developed as open-source under BSD-3 license at Computer Applications
in Science & Engineering of the Barcelona Supercomputing Center - Centro Nacional
de Supercomputación. Please, see the CONDITIONS OF USE described in the LICENSE.rst file.
