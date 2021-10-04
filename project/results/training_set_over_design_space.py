"""
1.a. Training data
##################

The objective is to create a training set
made up of :math:`N` input and output samples of :class:`H2TurboFan`
over :class:`H2TFDesignSpace`,
by means of a design of experiments (DOE).
"""
from gemseo.api import configure_logger, create_scenario
from discipline import H2TurboFan
from design_space import H2TFDesignSpace

configure_logger()

#%%
# First,
# we import the discipline providing the input and output samples:
discipline = H2TurboFan()

#%%
# and the design space on which to build the DOE:
design_space = H2TFDesignSpace()

#%%
# Then,
# we define a scenario of type "DOE"
# from these objects and an output of interest, e.g. the objective "mtow":
scenario = create_scenario(
    [discipline], "DisciplinaryOpt", "mtow", design_space, scenario_type="DOE"
)

#%%
# By default,
# GEMSEO will store only the output variable "mtow"
# for the sake of space management.
# Adding an output as observable is necessary to store it:
for output in discipline.OBSERVABLES + discipline.CONSTRAINTS:
    scenario.add_observable(output)

#%%
# Lastly,
# we execute the scenario:
# - the name of a DOE algorithm,
# - the number of input and output samples,
# - possibly algorithm options passed as a dictionary indexed by `"algo_options"`:
scenario.execute({"algo": "OT_OPT_LHS", "n_samples": 30})

#%% and save the training set in an HDF5 file:
scenario.save_optimization_history("training_set.hdf5")

#%%
# .. note::
#
#    In this study,
#    this dataset will be used to create the surrogate model
#    that will replace the discipline :class:`H2TurboFan`.
#
# .. seealso::
#
#    Go to `this webpage <https://gemseo.readthedocs.io/en/stable/algorithms/doe_algos.html>`_
#    for more information about the available design of experiments
#    and to `this one  <https://gemseo.readthedocs.io/en/stable/examples/doe/index.html>`_
#    for examples.
