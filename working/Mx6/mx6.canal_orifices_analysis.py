import data_mx6 as data_set
from constant import CONST
from canal_orifice_analysis import draw_landmarks_relation, export_landmarks_relation

specimens = data_set.specimens[:]
#export_landmarks_relation(specimens)
draw_landmarks_relation(specimens, orifice_origin=CONST.MB, orifice_on_xaxis=CONST.P, grid=False)
