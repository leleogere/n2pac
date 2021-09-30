"""
Optimization
============
"""
from gemseo.api import configure_logger, create_scenario
from marilib.utils import unit

from discipline import H2TurboFan
from design_space import H2TFDesignSpace


configure_logger()

scenario = create_scenario(
    [H2TurboFan()],
    "DisciplinaryOpt",
    "mtow",
    H2TFDesignSpace(),
    scenario_type="MDO",
)
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
scenario.add_constraint("fuel", constraint_type="ineq", positive=True)
scenario.add_constraint("coc", constraint_type="ineq", positive=True)
scenario.execute({"algo": "NLOPT_COBYLA", "max_iter": 30})
scenario.save_optimization_history("deterministic_optimization_with_marilib")