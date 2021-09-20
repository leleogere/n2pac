"""
Discipline
##########
"""
from gemseo.core.discipline import MDODiscipline
from numpy import array

from h2_turbofan.turbofan_h2_function import fct_turbofan_h2


class H2TurboFan(MDODiscipline):

    TECHNOLOGICAL_VARIABLES = ["tgi","tvi","sfc","mass","drag"]
    DESIGN_VARIABLES = ["thrust","bpr","area","aspect_ratio"]

    def __init__(self):
        super(H2TurboFan, self).__init__()
        self.input_grammar.initialize_from_data_names(self.DESIGN_VARIABLES+self.TECHNOLOGICAL_VARIABLES)
        self.output_grammar.initialize_from_data_names(["mtow","fuel","coc","tofl","vapp","vz_mcl","vz_mcr","oei_path","ttc","far"])
        self.default_inputs = {'thrust': array([125000.]),'bpr':array([8.5]), 'area':array([160.]), 'aspect_ratio':array([9.5]),"tgi":array([0.3]),"tvi":array([0.845]),"drag":array([1.]),"sfc":array([1.]),"mass":array([1.])}

    def _run(self):
        design_data = {name: self.local_data[name][0] for name in self.DESIGN_VARIABLES}
        techno_data = {name: self.local_data[name][0] for name in self.TECHNOLOGICAL_VARIABLES}
        output_data = fct_turbofan_h2(techno_data, design_data, "eval")
        output_data = {name: array([value]) for name, value in output_data.items()}
        self.local_data.update(output_data)

    def plot(self):
        design_data = {name: self.local_data[name][0] for name in self.DESIGN_VARIABLES}
        techno_data = {name: self.local_data[name][0] for name in self.TECHNOLOGICAL_VARIABLES}
        fct_turbofan_h2(techno_data, design_data, "draw")

if __name__ == "__main__":
    discipline = H2TurboFan()
    print(discipline)
    print(repr(discipline))

    output_data = discipline.execute()
    print(output_data)

    input_data = {"thrust": array([110000])}
    output_data = discipline.execute(input_data)
    print(output_data)