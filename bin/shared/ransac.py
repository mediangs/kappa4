'''
https://github.com/ahojnnes/numpy-snippets/blob/master/ransac.py

http://dvitonis.net/blog/2014/09/10/fitting-ellipse-ransac-python/
'''


import math

import cv2
# coding: utf-8
import numpy as np

class EllipseFit(object):
    """
    (h,k) - ellipse center in x,y
    a, b - halves of major and minor semiaxes (major and minor radii)
    tau - ellipse counter-clockwise rotation angle in radians

    Ellipse is specified in parametric way:
    x(t) = h + cos(tau)[a cos(t)] - sin(tau)[b sin(t)]
    y(t) = k + sin(tau)[a cos(t)] + cos(tau)[b sin(t)]
    0 <= t <= 2pi

    Also in conic way:
    Ax^2 + Bxy +Cy^2 + Dx + Ey + F = 0

    Conversion from parametric to conic:
    c = cos(tau)
    s = sin(tau)
    A = (bc)^2 + (as)^2
    B = -2cs(a^2 - b^2)
    C = (bs)^2 + (ac)^2
    D = -2Ah - kB
    E = -2Ck - hB
    F = -(ab)^2 + Ah^2 + Bhk + Ck^2

    Residual:
    R = SUM(i=1,n) (Axi^2 + Bxiyi +Cyi^2 + Dxi + Eyi + F)^2

    http://en.wikipedia.org/wiki/Ellipse
    http://www.cs.cornell.edu/cv/OtherPdf/Ellipse.pdf
    """

    def fit(self, data):
        ellipse = cv2.fitEllipse(data)
        return ellipse

    def residuals(self, model, data):
        (h, k), (a2, b2), degrees = model

        a = a2 / 2.0
        b = b2 / 2.0
        tau = degrees * math.pi / 180

        c = math.cos(tau)
        s = math.sin(tau)
        A = (b * c) ** 2 + (a * s) ** 2
        B = -2 * c * s * (a ** 2 - b ** 2)
        C = (b * s) ** 2 + (a * c) ** 2
        D = -2 * A * h - k * B
        E = -2 * C * k - h * B
        F = -(a * b) ** 2 + A * (h ** 2) + B * h * k + C * (k ** 2)

        xi = data[:, 0]
        yi = data[:, 1]
        variance = np.var(xi)
        R = abs(A * (xi ** 2) + B * xi * yi + C * (yi ** 2) + D * xi + E * yi + F) / variance

        return R

    def is_degenerate(self, sample):
        return False


class LinearLeastSquares2D(object):

    '''
    2D linear least squares using the hesse normal form:
        d = x*sin(theta) + y*cos(theta)
    which allows you to have vertical lines.
    '''

    def fit(self, data):
        data_mean = data.mean(axis=0)
        x0, y0 = data_mean
        if data.shape[0] > 2: # over determined
            u, v, w = np.linalg.svd(data-data_mean)
            vec = w[0]
            theta = math.atan2(vec[0], vec[1])
        elif data.shape[0] == 2: # well determined
            theta = math.atan2(data[1,0]-data[0,0], data[1,1]-data[0,1])
        theta = (theta + math.pi * 5 / 2) % (2*math.pi)
        d = x0*math.sin(theta) + y0*math.cos(theta)
        return d, theta

    def residuals(self, model, data):
        d, theta = model
        dfit = data[:,0]*math.sin(theta) + data[:,1]*math.cos(theta)
        return np.abs(d-dfit)

    def is_degenerate(self, sample):
        return False


def ransac(data, model_class, min_samples, threshold, max_trials=1000):
    '''
    Fits a model to data with the RANSAC algorithm.
    :param data: numpy.ndarray
        data set to which the model is fitted, must be of shape NxD where
        N is the number of data points and D the dimensionality of the data
    :param model_class: object
        object with the following methods implemented:
         * fit(data): return the computed model
         * residuals(model, data): return residuals for each data point
         * is_degenerate(sample): return boolean value if sample choice is
            degenerate
        see LinearLeastSquares2D class for a sample implementation
    :param min_samples: int
        the minimum number of data points to fit a model
    :param threshold: int or float
        maximum distance for a data point to count as an inlier
    :param max_trials: int, optional
        maximum number of iterations for random sample selection, default 1000
    :returns: tuple
        best model returned by model_class.fit, best inlier indices
    '''

    best_model = None
    best_inlier_num = 0
    best_inliers = None
    data_idx = np.arange(data.shape[0])
    for _ in xrange(max_trials):
        # org
        #sample = data[np.random.randint(0, data.shape[0], 2)]
        # modified by jongki
        sample = data[np.random.randint(0, data.shape[0], min_samples)]

        if model_class.is_degenerate(sample):
            continue
        sample_model = model_class.fit(sample)
        sample_model_residua = model_class.residuals(sample_model, data)
        sample_model_inliers = data_idx[sample_model_residua<threshold]
        inlier_num = sample_model_inliers.shape[0]
        if inlier_num > best_inlier_num:
            best_inlier_num = inlier_num
            best_inliers = sample_model_inliers
    if best_inliers is not None:
        best_model = model_class.fit(data[best_inliers])
    return best_model, best_inliers

def test_linear_square():
    x = np.mgrid[-5:5:200j]
    y = np.mgrid[3:10:200j]
    data = np.vstack((x.ravel(), y.ravel())).T
    data += np.random.normal(size=data.shape)

    # generate some faulty data
    data[0,:] = (3, 20)
    data[1,:] = (4, 21)
    data[2,:] = (5, 22)
    data[3,:] = (5, 24)
    data[4,:] = (-2, -24)
    data[5,:] = (-3, -23)

    model, inliers = ransac(data, LinearLeastSquares2D(), 2, 2)

    #: plot working
    import pylab

    pylab.plot(data[:,0], data[:,1], '.r', label='outliers')
    pylab.plot(data[inliers][:,0], data[inliers][:,1], '.b', label='inliers')

    x = np.arange(-7, 8)
    dr, thetar = model
    y_ransac = (dr - x*math.sin(thetar)) / math.cos(thetar)
    ds, thetas = LinearLeastSquares2D().fit(data)
    y_simple = (ds - x*math.sin(thetas)) / math.cos(thetas)
    pylab.plot(x, y_simple, '-r', label='least-squares solution of all points')
    pylab.plot(x, y_ransac, '-b', label='RANSAC solution')

    pylab.legend(loc=4)
    pylab.show()
    

def test_my_ellipse():

    import point_data as p
    from rotate import get_rotated_points
    
    #data_3d = get_rotated_points(p.c, p.n, p.P0)
    #data = (data_3d[:,:2]).astype(np.float32) # data type should be float32 or int32
    
    data = (get_rotated_points(p.c, p.n, p.P0)[:,:2]).astype(np.float32) # data type should be float32 or int32

    for i in range(1):
        model, inliers = ransac(data, EllipseFit(), min_samples = 14, threshold = .03 ,max_trials=500)
    ellipse = cv2.fitEllipse(data)

    from pylab import figure
    from matplotlib.patches import Ellipse

    e = Ellipse(ellipse[0], width=ellipse[1][0], height=ellipse[1][1], angle=ellipse[-1])
    e_ransac = Ellipse(model[0], width=model[1][0], height=model[1][1], angle=model[-1])

    #: plot working
    import pylab

    fig = figure()
    ax = fig.add_subplot(111, aspect='equal')
    ax.plot(data[:, 0], data[:, 1], '.r', label='outliers')
    ax.plot(data[inliers][:, 0], data[inliers][:, 1], '.b', label='inliers')
    ax.add_artist(e)
    e.set_alpha(0.5)
    e.set_color('r')
    ax.add_artist(e_ransac)
    e_ransac.set_alpha(0.5)

    pylab.gca().invert_yaxis()
    pylab.legend(loc=4)
    pylab.show()

    
def test_ellipse():
    data = cont
    for i in range(1):
        model, inliers = ransac(data, EllipseFit(),20,500,max_trials=100)

    ellipse = cv2.fitEllipse(data)


    from pylab import figure
    from matplotlib.patches import Ellipse


    e = Ellipse(ellipse[0], width=ellipse[1][0], height=ellipse[1][1], angle=ellipse[-1])
    e_ransac = Ellipse(model[0], width=model[1][0], height=model[1][1], angle=model[-1])


    #: plot working
    import pylab

    fig = figure()
    ax = fig.add_subplot(111, aspect='equal')
    ax.plot(data[:, 0], data[:, 1], '.r', label='outliers')
    ax.plot(data[inliers][:, 0], data[inliers][:, 1], '.b', label='inliers')
    ax.add_artist(e)
    e.set_alpha(0.5)
    e.set_color('r')
    ax.add_artist(e_ransac)
    e_ransac.set_alpha(0.5)

    pylab.gca().invert_yaxis()
    pylab.legend(loc=4)
    pylab.show()


# region contour
cont = np.array([[294, 196], [295, 195], [296, 196], [297, 195], [298, 195], [299, 195], [300, 195], [301, 195],
                    [302, 195], [303, 196], [304, 196], [305, 197], [305, 198], [305, 199], [305, 198], [305, 197],
                    [306, 196], [307, 196], [308, 195], [309, 195], [310, 195], [311, 195], [312, 196], [313, 196],
                    [314, 197], [315, 196], [316, 196], [317, 196], [318, 196], [319, 196], [320, 196], [321, 197],
                    [322, 197], [323, 197], [324, 198], [325, 198], [326, 198], [327, 199], [328, 199], [329, 199],
                    [330, 199], [331, 200], [332, 200], [333, 201], [333, 202], [334, 201], [335, 201], [336, 202],
                    [337, 202], [338, 203], [339, 203], [340, 204], [341, 205], [341, 206], [341, 207], [341, 208],
                    [342, 207], [343, 207], [344, 206], [345, 207], [346, 207], [347, 208], [348, 207], [349, 208],
                    [350, 208], [351, 209], [351, 210], [352, 211], [353, 211], [354, 212], [354, 213], [354, 214],
                    [354, 215], [355, 214], [356, 214], [357, 214], [358, 215], [359, 215], [360, 216], [361, 217],
                    [361, 218], [362, 219], [363, 219], [364, 220], [364, 221], [365, 222], [366, 222], [367, 223],
                    [368, 224], [369, 225], [369, 226], [370, 227], [371, 228], [371, 229], [372, 230], [373, 231],
                    [373, 232], [373, 233], [374, 234], [375, 235], [375, 236], [375, 237], [374, 238], [375, 238],
                    [376, 239], [377, 240], [378, 241], [379, 242], [379, 243], [379, 244], [379, 245], [379, 246],
                    [379, 247], [378, 248], [377, 248], [378, 248], [379, 249], [380, 249], [381, 250], [382, 251],
                    [382, 252], [382, 253], [382, 254], [382, 255], [382, 256], [382, 257], [382, 258], [381, 259],
                    [382, 260], [382, 261], [382, 262], [381, 263], [381, 264], [380, 265], [381, 265], [382, 266],
                    [382, 267], [382, 268], [382, 269], [382, 270], [382, 271], [381, 272], [380, 273], [379, 273],
                    [378, 274], [377, 274], [376, 273], [376, 274], [376, 275], [377, 275], [378, 276], [378, 277],
                    [378, 278], [379, 279], [379, 280], [379, 281], [379, 282], [378, 283], [377, 283], [376, 284],
                    [375, 285], [375, 286], [375, 287], [375, 288], [375, 289], [374, 290], [373, 291], [373, 292],
                    [373, 293], [373, 294], [372, 295], [371, 295], [370, 296], [370, 297], [369, 298], [368, 298],
                    [368, 299], [367, 300], [367, 301], [366, 302], [365, 302], [364, 303], [363, 304], [362, 304],
                    [362, 305], [362, 306], [361, 307], [360, 307], [359, 308], [358, 308], [357, 308], [357, 309],
                    [356, 310], [355, 310], [355, 311], [354, 312], [354, 313], [353, 314], [352, 314], [351, 315],
                    [350, 315], [349, 314], [348, 314], [347, 315], [346, 315], [345, 315], [344, 314], [343, 314],
                    [342, 313], [342, 312], [342, 311], [342, 310], [342, 309], [341, 309], [340, 308], [340, 307],
                    [340, 306], [341, 305], [340, 306], [339, 306], [338, 305], [337, 306], [336, 305], [335, 305],
                    [334, 304], [334, 303], [334, 302], [335, 301], [335, 300], [335, 299], [335, 298], [334, 299],
                    [333, 299], [332, 300], [331, 299], [330, 300], [329, 300], [328, 301], [327, 301], [326, 300],
                    [325, 300], [324, 301], [323, 302], [323, 303], [322, 304], [321, 304], [320, 305], [319, 304],
                    [318, 304], [317, 303], [317, 304], [316, 305], [315, 305], [314, 306], [315, 307], [315, 308],
                    [315, 309], [314, 310], [313, 310], [314, 310], [315, 311], [315, 312], [315, 313], [314, 314],
                    [315, 314], [316, 315], [316, 316], [316, 317], [316, 318], [316, 319], [316, 320], [317, 320],
                    [318, 321], [318, 322], [319, 322], [320, 323], [320, 324], [320, 325], [319, 326], [318, 326],
                    [318, 327], [317, 328], [316, 328], [315, 329], [314, 329], [313, 330], [312, 330], [311, 330],
                    [310, 329], [309, 330], [308, 330], [307, 329], [306, 329], [305, 328], [304, 328], [303, 327],
                    [302, 328], [301, 328], [300, 328], [299, 328], [298, 327], [297, 328], [296, 328], [295, 327],
                    [294, 328], [293, 327], [292, 327], [291, 326], [290, 326], [289, 325], [288, 326], [287, 326],
                    [286, 326], [285, 325], [284, 325], [283, 324], [282, 325], [281, 325], [280, 324], [279, 324],
                    [278, 323], [277, 323], [276, 323], [275, 323], [274, 322], [273, 322], [272, 321], [271, 320],
                    [270, 320], [269, 319], [269, 318], [268, 317], [267, 317], [266, 317], [265, 316], [264, 316],
                    [263, 315], [263, 314], [262, 314], [261, 313], [260, 312], [259, 312], [258, 312], [257, 311],
                    [256, 311], [255, 310], [255, 309], [254, 308], [253, 307], [252, 306], [252, 305], [251, 304],
                    [250, 303], [249, 302], [249, 301], [249, 300], [248, 300], [247, 299], [246, 298], [246, 297],
                    [245, 296], [245, 295], [245, 294], [244, 293], [243, 292], [243, 291], [243, 290], [242, 290],
                    [241, 289], [241, 288], [240, 287], [240, 286], [240, 285], [239, 284], [239, 283], [239, 282],
                    [238, 281], [238, 280], [237, 280], [236, 279], [236, 278], [236, 277], [236, 276], [236, 275],
                    [236, 274], [235, 273], [235, 272], [235, 271], [235, 270], [235, 269], [235, 268], [234, 267],
                    [234, 266], [234, 265], [234, 264], [234, 263], [234, 262], [234, 261], [234, 260], [234, 259],
                    [235, 258], [236, 258], [235, 258], [234, 257], [234, 256], [234, 255], [234, 254], [234, 253],
                    [235, 252], [234, 251], [234, 250], [234, 249], [234, 248], [235, 247], [235, 246], [235, 245],
                    [235, 244], [235, 243], [235, 242], [236, 241], [237, 241], [237, 240], [237, 239], [238, 238],
                    [238, 237], [238, 236], [238, 235], [239, 234], [239, 233], [240, 232], [240, 231], [240, 230],
                    [240, 229], [241, 228], [242, 227], [243, 226], [244, 226], [245, 225], [245, 224], [245, 223],
                    [245, 222], [246, 221], [247, 221], [248, 220], [249, 220], [250, 221], [250, 220], [250, 219],
                    [250, 218], [251, 217], [252, 217], [252, 216], [253, 215], [254, 214], [255, 214], [255, 213],
                    [256, 212], [256, 211], [257, 210], [258, 209], [259, 208], [260, 208], [261, 207], [262, 207],
                    [263, 206], [264, 206], [265, 205], [266, 205], [267, 204], [268, 204], [268, 203], [269, 202],
                    [270, 202], [271, 201], [272, 202], [273, 201], [274, 201], [275, 200], [276, 200], [277, 199],
                    [278, 199], [279, 198], [280, 198], [281, 197], [282, 197], [283, 197], [284, 198], [285, 197],
                    [286, 197], [287, 196], [288, 196], [289, 196], [290, 196], [291, 197], [292, 196], [293, 196]])
# endregion    

if __name__ == '__main__':
    #test_linear_square()
    #test_ellipse()
    test_my_ellipse()