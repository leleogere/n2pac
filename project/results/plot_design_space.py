"""
H2TFDesignSpace: use
####################
"""
from design_space import H2TFDesignSpace

#%%
# First,
# we instantiate a :class:`H2TFDesignSpace`:
design_space = H2TFDesignSpace()

#%%
# Then,
# we print it in a tabular way:
print(design_space)

#%%
# .. note::
#
#    In this study,
#    this design space will be used
#    both to define the lower and upper bounds of the optimization variables,
#    to provide the starting point for most of the optimization algorithms,
#    and as the input space on which to build a design of experiments.
#
# .. seealso::
#
#    Go to `this webpage <https://gemseo.readthedocs.io/en/stable/design_space.html>`_
#    for more information about design spaces
#    and to `this one  <https://gemseo.readthedocs.io/en/stable/examples/design_space/index.html>`_
#    for examples.
