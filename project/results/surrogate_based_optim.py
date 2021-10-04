"""
1.c. Surrogate-based optimization
#################################

The surrogate-based optimization uses a surrogate discipline
to decrease the objective function
whilst ensuring the feasibility of the constraints.
"""
from gemseo.api import configure_logger, create_scenario, create_surrogate
from gemseo.core.discipline import MDODiscipline
from gemseo.mlearning.api import import_regression_model
from marilib.utils import unit

from discipline import H2TurboFan
from design_space import H2TFDesignSpace


configure_logger()

#%%
# First,
# we import the discipline taking the design variables as inputs
# and returning the objective, constraints and observables as outputs:
discipline = create_surrogate(import_regression_model("r_b_f_regression_training_set"))

#%%
# We also import the design space on which to perform the optimization:
design_space = H2TFDesignSpace()

#%%
# Then,
# we create a scenario of type "MDO" (Multidisciplinary Design Optimization)
scenario = create_scenario(
    [discipline],
    "DisciplinaryOpt",
    "mtow",
    design_space,
    scenario_type="MDO",
)

#%%
# and add the constraints to be satisfied:
scenario.add_constraint("tofl", constraint_type="ineq", value=2200)
scenario.add_constraint("vapp", constraint_type="ineq", value=unit.mps_kt(137))
scenario.add_constraint(
    "vz_mcl", constraint_type="ineq", positive=True, value=unit.mps_ftpmin(300.0)
)
scenario.add_constraint(
    "vz_mcr", constraint_type="ineq", positive=True, value=unit.mps_ftpmin(0.0)
)
scenario.add_constraint(
    "oei_path", constraint_type="ineq", positive=True, value=1.1 / 100
)
scenario.add_constraint("ttc", constraint_type="ineq", value=unit.s_min(25))
scenario.add_constraint("far", constraint_type="ineq", value=13.4)
#%%
# .. warning::
#
#    The thresholds used by the constraints are sometimes provided with usual units
#    while MARILib works with the international system of units.
#    Beware of conversion problems!


# %%
# We can also add the output variable "fuel" and "coc" as constraints,
# so that their values are stored in the optimization history:
scenario.add_constraint("fuel", "ineq", positive=True)
scenario.add_constraint("coc", "ineq", positive=True)

#%%
# Lastly,
# we solve the optimization problem by executing the scenario from:
# - the name of an optimization algorithm,
# - the maximum number of iterations,
# - possibly algorithms options passed as a dictionary indexed by `"algo_options"`:
scenario.execute({"algo": "NLOPT_COBYLA", "max_iter": 100})
H2TurboFan.print_results_from_opt_problem(scenario.formulation.opt_problem)


#%%
# Do not forget to save the optimization history:
scenario.save_optimization_history("deterministic_optimization_with_surrogate")
