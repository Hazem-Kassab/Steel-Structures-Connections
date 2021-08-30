from section import Section
from bolt import Bolt


class ExtendedMomentConnection:
    def __init__(self, beam: Section, column: Section, haunch_length, extended: bool, end_plate_thickness,
                 bolt_rows_outside, bolt_rows_inside, yield_strength):
        self.beam = beam
        self.column = column
        self.haunch_length = haunch_length
        self.extended = extended
        self.yield_strength = yield_strength

    def __calc_design_moment(self, shear):
        plastic_moment = 1.1 * 1.5 * self.yield_strength * self.beam.plastic_section_modulus_x
        plastic_hinge_distance = min(self.beam.depth/2, self.beam.breadth * 3)
        design_moment = plastic_moment + plastic_hinge_distance * shear
        return design_moment
