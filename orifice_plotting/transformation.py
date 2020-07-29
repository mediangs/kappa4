from scipy.spatial.transform import Rotation as R
import numpy as np

r = R.from_quat([0, 0, np.sin(np.pi/4), np.cos(np.pi/4)])

print(r.as_dcm())
