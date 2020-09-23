from __future__ import division

'''
NOTE init() and show() are expected to be called only once
'''
# draw a vector
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
import numpy as np


class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)


def set_axes_equal(ax):
    '''
    https://stackoverflow.com/questions/13685386/matplotlib-equal-unit-length-with-equal-aspect-ratio-z-axis-is-not-equal-to
    Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    '''

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5 * max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])


def init(lim, grid=False):
    global ax, plt, fig
    # import
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    AXIS_COLOR = "#FFFFFF"  # white

    # create axes
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection='3d', autoscale_on=False)

    ax.set_xlim(*lim[0])
    ax.set_ylim(*lim[1])
    ax.set_zlim(*lim[2])

    mpl.rcParams['legend.fontsize'] = 12
    if not grid:
        ax.set_xlabel('').set_color(AXIS_COLOR)
        ax.set_ylabel('').set_color(AXIS_COLOR)
        ax.set_zlabel('').set_color(AXIS_COLOR)

        [i.set_color(AXIS_COLOR) for i in plt.gca().get_xticklabels()]
        [i.set_color(AXIS_COLOR) for i in plt.gca().get_yticklabels()]
        [i.set_color(AXIS_COLOR) for i in plt.gca().get_zticklabels()]

        ax.w_xaxis.line.set_color(AXIS_COLOR)
        ax.w_yaxis.line.set_color(AXIS_COLOR)
        ax.w_zaxis.line.set_color(AXIS_COLOR)

        ax.xaxis._axinfo['tick']['color'] = AXIS_COLOR
        ax.yaxis._axinfo['tick']['color'] = AXIS_COLOR
        ax.zaxis._axinfo['tick']['color'] = AXIS_COLOR

        ax.set_facecolor('white')
        # make the panes transparent
        ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        # make the grid lines transparent
        ax.xaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)
        ax.yaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)
        ax.zaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)


def text3d(text, P, color='k'):
    x, y, z = P
    ax.text(x, y, z, text, size=15, zorder=1, color=color)


def plot_arrow(p1, p2, **kwargs):
    '''
    P: a  point (x, y, z)
    NOTE for format string of marker, refer to http://matplotlib.org/api/axes_api.html?highlight=axes#matplotlib.axes.Axes.plot
    '''

    a = Arrow3D([p2[0], p1[0]], [p2[1], p1[1]], [p2[2], p1[2]], mutation_scale=20, lw=1.0, arrowstyle="-|>", **kwargs)
    ax.add_artist(a)


def plot_points_detail(P, color_style, label=None, linewidth=1.5):
    X, Y, Z = zip(*P)
    if len(color_style) > 2:
        linewidth = color_style[2]

    ax.plot(X, Y, Z, color=color_style[0], linestyle=color_style[1], label=label, linewidth=linewidth)


def plot_marker(P, color_style, markersize=4, label=None):
    X, Y, Z = zip(*P)

    if len(color_style) == 1:
        color = color_style[0]
        marker = 'o'
    if len(color_style) == 2:
        color = color_style[0]
        marker = color_style[1]
    if len(color_style) > 2:  # if marker info available
        color = color_style[0]
        marker = color_style[1]
        markersize = color_style[2]

    ax.plot(X, Y, Z, color=color, marker=marker, markersize=markersize, label=label)


def plot_points(P, marker=None, markersize=4, label=None, linewidth=1.0, ):  # org : 4, 1.0
    '''
    P: a list of points (x, y, z)

    NOTE for format string of marker, refer to
    http://matplotlib.org/api/axes_api.html?highlight=axes#matplotlib.axes.Axes.plot
    '''
    X, Y, Z = zip(*P)

    color = ''
    markerstyle = ''

    if marker and len(marker) > 2:
        color = ''.join([c for c in marker if c.isalpha()])
        markerstyle = ''.join([c for c in marker if not c.isalpha()])

    if marker != None and len(color) > 1:
        ax.plot(X, Y, Z, marker=markerstyle, color=color, markersize=markersize, label=label, linewidth=linewidth)
        # ax.plot(X, Y, Z,  color = color, markersize = markersize, label=label, linewidth=linewidth)

    elif marker != None:
        ax.plot(X, Y, Z, marker, markersize=markersize, label=label, linewidth=linewidth)
    else:
        ax.plot(X, Y, Z, label=label)

def plot_circle(center, radius, color='r', fill=False):

    #plt.plot(x, y, '.')
    circle = plt.Circle(center, radius, color='r', fill=False)
    plt.gca().add_artist(circle)

    # plt.title('Found center at ({:.2f}, {:.2f})\n'
    #           '{}% radius is {:.2f}\n'
    #           '{} / {} points within circle'.format(
    #     x0, y0, t, r0, n_within, n))
    #


def plot_surface(X, Y, Z):
    '''
    NOTE X, Y, Z should be meshgrid. Easiest way is to use numpy.
    '''
    ax.plot_surface(X, Y, Z, color='w', rstride=1, cstride=1, linewidth=0, antialiased=False)


def show():
    ax.legend()
    set_axes_equal(ax)
    plt.show()
    # st.header("""
    # # test
    # """)

    # fig = plt.figure()
    # st.plotly_chart(fig)

    # st.pyplot()
