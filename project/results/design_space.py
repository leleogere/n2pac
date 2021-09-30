"""
Design space
############
"""
from gemseo.algos.design_space import DesignSpace


class H2TFDesignSpace(DesignSpace):
    def __init__(self):
        super(H2TFDesignSpace, self).__init__()
        self.add_variable("thrust", l_b=100000, u_b=150000, value=125000)
        self.add_variable("bpr", l_b=5, u_b=12, value=8.5)
        self.add_variable("area", l_b=120, u_b=200, value=160)
        self.add_variable("aspect_ratio", l_b=7, u_b=12, value=9.5)


if __name__ == "__main__":
    print(H2TFDesignSpace())
