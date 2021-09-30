"""
Optimization - Post-processing
==============================
"""
from gemseo.algos.opt_problem import OptimizationProblem

from discipline import H2TurboFan
from gemseo.api import execute_post

problem = OptimizationProblem.import_hdf("deterministic_optimization_with_marilib")
data = H2TurboFan.print_results_from_opt_problem(problem)

execute_post(problem, "OptHistoryView",save=False,show=True)