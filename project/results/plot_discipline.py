"""
H2TurboFan: use
###############
"""
from numpy import array
from discipline import H2TurboFan

#%%
# First,
# we instantiate a :class:`H2TurboFan`:
discipline = H2TurboFan()

#%%
# Then,
# we look at its name:
print(discipline)

#%%
# and at its input and output variables:
print(repr(discipline))

#%%
# Thirdly,
# we execute it with all default values:
output_data = discipline.execute()

#%%
# and print the results:
discipline.print_results(output_data)

#%%
# Lastly,
# we can change the value of some input variables,
# e.g. the thrust,
input_data = {"thrust": array([110000])}
output_data = discipline.execute(input_data)

#%%
# and print the results:
discipline.print_results(output_data)

#%%
# .. note::
#
#    In this study,
#    this discipline will be used
#    both:
#
#    - to get a rough idea of the optima and output uncertainties,
#    - to provide input and output samples to build the surrogate models.
#
# .. seealso::
#
#    Go to `this webpage <https://gemseo.readthedocs.io/en/stable/discipline.html>`_
#    for more information about design spaces
#    and to `this one  <https://gemseo.readthedocs.io/en/stable/examples/discipline/index.html>`_
#    for examples.
