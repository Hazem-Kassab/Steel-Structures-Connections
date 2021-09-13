from abc import abstractmethod, ABC
import pandas as pd


class Section(ABC):
    pass


class ISection(Section, ABC):
    def __init__(self, profile: str):
        file = pd.read_csv(profile[0:3] + ".txt", delimiter="\t")
        my_list = file[file["Profile"] == int(profile[3:])].values.tolist()[0]
        self.profile = profile
        self.weight = my_list[1]
        self.area = my_list[2]
        self.web_area = my_list[3]
        self.depth = my_list[4]
        self.breadth = my_list[5]
        self.web_thickness = my_list[6]
        self.flange_thickness = my_list[7]


class HEA(ISection):
    pass


class HEB(ISection):
    pass


class IPE(ISection):
    pass


class IPN(ISection):
    pass


class Pipe(Section):
    pass


class Angle(Section):
    pass


class DoubleAngle(Section):
    pass


class StarShapeAngle(Section):
    pass
