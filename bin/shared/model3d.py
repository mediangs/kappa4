from __future__ import division

'''
NOTE init() and show() are expected to be called only once
'''

import plotly.graph_objects as go
magnification_ratio = 1


def init(lim, grid=False):
    global fig
    fig = go.Figure()


def plot_arrow(p1, p2, **kwargs):
    '''
    P: a  point (x, y, z)
    NOTE for format string of marker, refer to http://matplotlib.org/api/axes_api.html?highlight=axes#matplotlib.axes.Axes.plot
    '''
    
    a = Arrow3D([p2[0], p1[0]], [p2[1], p1[1]], [p2[2], p1[2]], mutation_scale=20, lw=1.0, arrowstyle="-|>", **kwargs)
    ax.add_artist(a)


def convert_linestyle(style):
    # plotlystyles ='dash dot dashdot'
    if style == ':':
        return 'dash'
    elif style == '.':
        return 'dot'
    elif style == '*':
        return 'x'
    elif style == 'o':
        return 'circle'
    else:
        return 'circle'


def plot_points_detail(P, color_style, label=None, linewidth=2):
    """

    :param P:
    :param color_style: ['#FFFFFF', '-', 2] # [color, style, line width]
    :param label:
    :param linewidth:
    :return:
    """
    X, Y, Z = zip(*P)
    X = [e / magnification_ratio for e in X]
    Y = [e / magnification_ratio for e in Y]
    Z = [e / magnification_ratio for e in Z]
    if len(color_style) > 2:
        linewidth = color_style[2]

    showlegend = True if label else False
    fig.add_trace(go.Scatter3d(x=X, y=Y, z=Z, mode='lines', name=label, showlegend=showlegend,
                               line=dict(color=color_style[0], width=linewidth)))


def plot_marker(P, color_style, markersize=2, label=None):
    try:
        X, Y, Z = zip(*P)
        X = [e / magnification_ratio for e in X]
        Y = [e / magnification_ratio for e in Y]
        Z = [e / magnification_ratio for e in Z]

        if len(color_style) == 1:
            color = color_style[0]
            marker = 'circle'
        if len(color_style) == 2:
            color = color_style[0]
            marker = convert_linestyle(color_style[1])
        if len(color_style) > 2: # if marker info available
            color = color_style[0]
            marker = convert_linestyle(color_style[1])
            markersize = color_style[2]

        showlegend = True if label else False
        fig.add_trace(go.Scatter3d(x=X, y=Y, z=Z, mode='markers', marker_symbol=marker,
                                   name=label, showlegend=showlegend,
                                   marker=dict(size=markersize, color=color)))
    except:
        print('plot_marker exception')


def plot_points(P, marker=None, markersize=2, label=None, linewidth = 1.0): # org : 4, 1.0
    '''
    P: a list of points (x, y, z)
    
    NOTE for format string of marker, refer to 
    http://matplotlib.org/api/axes_api.html?highlight=axes#matplotlib.axes.Axes.plot
    '''
    X, Y, Z = zip(*P)
    X = [e / magnification_ratio for e in X]
    Y = [e / magnification_ratio for e in Y]
    Z = [e / magnification_ratio for e in Z]

    color = ''
    markerstyle = ''
    showlegend = True if label else False


    if marker and len(marker) > 2:
        color = ''.join([c for c in marker if c.isalpha()])
        markerstyle = ''.join([c for c in marker if not c.isalpha()])
    
    if marker != None and len(color) > 1:
        fig.add_trace(go.Scatter3d(x=X, y=Y, z=Z, mode='lines', name=label, showlegend=showlegend,
                                   line=dict(color=color, width=linewidth)))
        #ax.plot(X, Y, Z, marker = markerstyle, color = color, markersize = markersize, label=label, linewidth=linewidth)

    elif marker != None:
        fig.add_trace(go.Scatter3d(x=X, y=Y, z=Z, mode='lines', name=label, showlegend=showlegend,
                                   line=dict(width=linewidth)))
        #ax.plot(X, Y, Z, marker, markersize = markersize, label=label, linewidth=linewidth)
    else:
        fig.add_trace(go.Scatter3d(x=X, y=Y, z=Z, mode='lines', name=label, showlegend=showlegend))
        #ax.plot(X, Y, Z, label=label)


def plot_surface(X, Y, Z):
    '''
    NOTE X, Y, Z should be meshgrid. Easiest way is to use numpy.
    '''
    ax.plot_surface(X, Y, Z, color ='w', rstride=1, cstride=1, linewidth=0, alpha=0.5, antialiased=False)


def update_layout(axes_visible=True):
    fig.update_layout(
        scene=dict(xaxis_title='', yaxis_title='', zaxis_title='',
                   aspectmode='data',
                   aspectratio=dict(x=1, y=1, z=0.95),
                   xaxis=dict(showspikes=False, showgrid=True, zeroline=True, showline=True, visible=axes_visible, ),
                   yaxis=dict(showspikes=False, showgrid=True, zeroline=True, showline=False, visible=axes_visible, ),
                   zaxis=dict(showspikes=False, showgrid=True, zeroline=True, showline=False, visible=axes_visible, )),
        hovermode=False,
        scene_dragmode='orbit',
        uirevision='dataset',
        width=1000, margin=dict(r=20, b=10, l=10, t=10))


def model3d_drawer_fig(axes_visible=True):
    update_layout(axes_visible)
    return fig

def show():
    update_layout()
    fig.show()

    #fig = plt.figure()
    #st.plotly_chart(fig)

