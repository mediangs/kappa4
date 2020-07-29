
# named tuple

from collections import namedtuple

CanalDimension = namedtuple('CanalDimension', 'p1 p2 width')
DentinThickness = namedtuple('DentinThickness', 'p_body p_canal thickness angle')
FileMovement = namedtuple('FileMovement', 'vector angle distance')
