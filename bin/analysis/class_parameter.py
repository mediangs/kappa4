# -*- coding: cp949 -*-
"""
Created on 2015. 7. 13.

@author: jongki
"""


class Parameters(object):

    def __init__(self):

        #self.specimen = None

        # Stat나 Multiple draw에서 분석할 치아(specimen)의 배열
        self.specimens = []

        #self.canal_to_analysis = None

        # evaluating sections
        self.sections = []

        self.fixed_long_axis_vector = None # vector([0,0,1])


class StatParameters(Parameters):
    def __init__(self):
        Parameters.__init__(self)
        self.interval = .1  # None #.1
        self.export_to_excel = True
        self.measure_canal_width = True
        self.buccal_only = True


class ModelColorParameters(object):
    def __init__(self):
        self.canal_axis_pre = ['#aa0000', '-']
        self.canal_axis_opp = ['#aa0000', ':']
        self.canal_axis_post = [['#008400', '-'], ['#ef37ff', '-'],
                                ['#4300d3', '-'], ['#bc9e27', '-']]
        self.curve_height_axis_line = ['#0000ff', '-']
        self.crossing_point_pre = ['green', 'o', 4]
        self.crossing_point_post = ['red', 'o', 4]
        self.highlighted_body_outline = ['#214861', '-']
        self.normal_body_outline = ['#214861', '-']
        self.ch_arrow = ['k', '-']
        self.canal_outline_pre = ['#214861', '-']
        self.canal_outline_post = [['#008400', '-'], ['#ef37ff', '-'],
                                   ['#4300d3', '-'], ['#bc9e27', '-']]
        self.mindist_line_pre = ['#214861', '-']
        self.mindist_line_post = [['#008400', '-'], ['#ef37ff', '-'],
                                  ['#4300d3', '-'], ['#bc9e27', '-']]

        self.mesial_line = ['#409d26', '-']
        self.distal_line = ['#004eeb', '-']
        self.lateral_line = ['#989800', '-']
        self.mesial_concavity = ['#409d26', '.']
        self.distal_concavity = ['#004eeb', '.']


class DrawOptionParameters(Parameters):

    def __init__(self):
        Parameters.__init__(self)

        self.legend = True                   # toggle displaying legend
        self.legend_width = False            # toggle displaying canal width and area info

        self.root_outlines = True            # toggle drawing outline of root
        self.canal_outlines = True           # toggle drawing major canals
        self.all_canal_outlines = True       # toggle drawing all canals(including artifact)
        self.curve_axis = False              # toggle drawing curve axis

        self.curve_height = False            # toggle drawing Global curve
        self.curve_height_axis = True        # curve of root  canal

        self.crossing_points = True          # toggle drawing Intersection points(Mindist * root outline)
        self.transportation_arrow = True     # toggle drawing canal transportation arrow
        self.mindist_pre = False  # toggle drawing min distance, 원래최소거리구함
        self.mindist_iod = False  # toggle drawing min distance, 원래최소거리구함
        self.mindist_post = True             # toggle drawing   min distance
        self.orthogonal_line = False  # Mesial, Distal, Lateral line
        self.concavity = False  #

        self.highlight_sections = None       # [11.1] #None

        self.ransac_ellipse = False          # toggle drawing ransac ellipse

        self.export_as_wrl = False

'''
class MultipleDrawParameters(DrawParameters):
    def __init__(self):
        DrawParameters.__init__(self)
        #Parameters.__init__(self)
        self.specimens = []
'''

def test():
    dp = MultipleDrawParameters()
    dp.all_canal_outlines = True
    dp.canal_to_analysis = CONST.LINGUAL
    print(dp.canal_to_analysis)


if __name__ == '__main__':
    test()
