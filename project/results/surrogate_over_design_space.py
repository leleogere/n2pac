"""
1.b. Surrogate model
####################

The objective is to create a surrogate model of the discipline :class:`H2TurboFan`
over the design space :class:`H2TFDesignSpace`
from the training set obtained over the design space.
"""
from gemseo.algos.opt_problem import OptimizationProblem
from gemseo.api import create_surrogate
from gemseo.mlearning.qual_measure.r2_measure import R2Measure
from numpy import array
from discipline import H2TurboFan

#%%
# First,
# we import the results:
opt_problem = OptimizationProblem.import_hdf("training_set.hdf5")

#%%
# that we can convert into a :class:`Dataset`:
dataset = opt_problem.export_to_dataset("training_set", opt_naming=False)
print(dataset)
dataset.plot("ScatterMatrix")

#%%
# itself convertible into a pandas dataframe:
dataframe = dataset.export_to_dataframe()
print(dataframe)
print(dataframe.describe())

#%%
# .. seealso::
#
#    Go to `this webpage <https://gemseo.readthedocs.io/en/stable/examples/dataset/index.html>`_
#    for examples about datasets.

#%%
# Then,
# we create a surrogate model,
# inheriting from `MDODiscipline` and so usable in place of :class:`H2TurboFan`
# from a technical point of view (but pay attention to its fitting quality!):
surrogate = create_surrogate("RBFRegression", data=dataset)
print(repr(surrogate))

#%%
# For example,
# you can evaluate this surrogate discipline
# with the default values of the design variables:
output_data = surrogate.execute()
output_data.update(H2TurboFan.DEFAULT_TECHNOLOGICAL_VALUES)
H2TurboFan.print_results(output_data)

#%%
# or with new values for some design variables:
output_data = surrogate.execute({"thrust": array([100000])})
output_data.update(H2TurboFan.DEFAULT_TECHNOLOGICAL_VALUES)
H2TurboFan.print_results(output_data)

#%%
# The quality of this surrogate model can be evaluated with the :math:`R^2` coefficient
# by accessing the wrapped regression model:
quality = R2Measure(surrogate.regression_model) # you can also use RMSEMeasure
learning_r2 = quality.evaluate_learn()
cv_r2 = quality.evaluate_kfolds()
print("Learning R2 = ",{name: round(learning_r2[i],3) for i, name in enumerate(surrogate.regression_model.output_names)})
print("CV R2 = ", {name: round(cv_r2[i],3) for i, name in enumerate(surrogate.regression_model.output_names)})

#%%
# Lastly,
# do not forget to save this surrogate discipline:
output_directory = surrogate.regression_model.save(save_learning_set=True)
print(output_directory)

#%%
# .. note::
#
#    To load this surrogate discipline in another script,
#    use :
#
#    .. code::
#
#       surrogate = MDODiscipline.deserialize("surrogate_discipline.pkl")
#
# .. seealso::
#
#    Go to `this webpage <https://gemseo.readthedocs.io/en/stable/algorithms/surrogate_algos.html>`_
#    for more information about the available surrogate models
#    and to `this one  <https://gemseo.readthedocs.io/en/stable/examples/surrogate/index.html>`_
#    and `this one <https://gemseo.readthedocs.io/en/stable/examples/mlearning/index.html#regression-model>`_
#    for examples.
