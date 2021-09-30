"""
Discipline
##########
"""
from gemseo.core.discipline import MDODiscipline
from marilib.utils import unit
from numpy import array

from h2_turbofan.turbofan_h2_function import fct_turbofan_h2, str_h2turbofan

class H2TurboFan(MDODiscipline):

    TECHNOLOGICAL_VARIABLES = ["tgi","tvi","sfc","mass","drag"]
    DESIGN_VARIABLES = ["thrust","bpr","area","aspect_ratio"]
    OUTPUT_VARIABLES = ["mtow","fuel","coc","tofl","vapp","vz_mcl","vz_mcr","oei_path","ttc","far"]
    DEFAULT_DESIGN_VALUES = {'thrust': array([125000.]), 'bpr': array([8.5]), 'area': array([160.]), 'aspect_ratio': array([9.5])}
    DEFAULT_TECHNOLOGICAL_VALUES = {"tgi": array([0.3]), "tvi": array([0.845]), "drag": array([1.]), "sfc": array([1.]), "mass": array([1.])}

    def __init__(self):
        super(H2TurboFan, self).__init__()
        self.input_grammar.initialize_from_data_names(self.DESIGN_VARIABLES+self.TECHNOLOGICAL_VARIABLES)
        self.output_grammar.initialize_from_data_names(self.OUTPUT_VARIABLES)
        self.default_inputs = self.DEFAULT_DESIGN_VALUES
        self.default_inputs.update(self.DEFAULT_TECHNOLOGICAL_VALUES)

    def _run(self):
        design_data = self.get_variables(self.local_data,self.DESIGN_VARIABLES)
        techno_data = self.get_variables(self.local_data, self.TECHNOLOGICAL_VARIABLES)
        output_data = fct_turbofan_h2(techno_data, design_data, "eval")
        output_data = {name: array([value]) for name, value in output_data.items()}
        self.local_data.update(output_data)

    @classmethod
    def plot_results(cls, data):
        design_data = cls.get_variables(cls.data,cls.DESIGN_VARIABLES)
        techno_data = cls.get_variables(cls.data, cls.TECHNOLOGICAL_VARIABLES)
        fct_turbofan_h2(techno_data, design_data, "draw")

    @classmethod
    def print_results(cls, data):
        design_data = cls.get_variables(data,cls.DESIGN_VARIABLES)
        techno_data = cls.get_variables(data, cls.TECHNOLOGICAL_VARIABLES)
        output_data = cls.get_variables(data, cls.OUTPUT_VARIABLES)
        print(str_h2turbofan(techno_data, design_data, output_data))

    @staticmethod
    def get_variables(data, vtype):
        return {name: data[name][0] for name in vtype}

    @classmethod
    def print_results_from_opt_problem(cls, problem):
        f_opt, x_opt, is_feas, c_opt, _ = problem.get_optimum()
        x_opt = {name: x_opt[i] for i, name in
                 enumerate(problem.design_space.variables_names)}
        y_opt = {}
        y_opt['mtow'] = f_opt
        for name, value in c_opt.items():
            if name.startswith("-"):
                y_opt[name[1:]] = -value
            else:
                y_opt[name] = value
        data = {name: array([value]) for name, value in x_opt.items()}
        data.update({name: array([value]) for name, value in y_opt.items()})
        data.update(H2TurboFan.DEFAULT_TECHNOLOGICAL_VALUES)
        data["ttc"] += unit.s_min(25)
        data["tofl"] += 2200
        data["vapp"] += unit.mps_kt(137)
        data["vz_mcl"] += unit.mps_ftpmin(300)
        data["oei_path"] += 0.011
        cls.print_results(data)

if __name__ == "__main__":
    discipline = H2TurboFan()
    print(discipline)

    print("#"*20)

    print(repr(discipline))

    print("#"*20)

    output_data = discipline.execute()
    discipline.print_results(output_data)

    print("#"*20)

    input_data = {"thrust": array([110000])}
    output_data = discipline.execute(input_data)
    discipline.print_results(output_data)
