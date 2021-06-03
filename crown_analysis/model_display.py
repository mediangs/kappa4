import pyvista as pv
import numpy as np
from contact_surface import interpolated_points


def lines_from_points(points):
    """Given an array of points, make a line set"""
    poly = pv.PolyData()
    poly.points = points
    cells = np.full((len(points)-1, 3), 2, dtype=np.int_)
    cells[:, 1] = np.arange(0, len(points)-1, dtype=np.int_)
    cells[:, 2] = np.arange(1, len(points), dtype=np.int_)
    poly.lines = cells
    return poly


colors = [["ff0000", "28e5da", "0000ff"],
          ["ffff00", "c8bebe", "f79292"],
          ["fffff0", "f18c1d", "23dcaa"],
          ["d785ec", "9d5b13", "e4e0b1"],
          ["894509", "af45f5", "fff000"]]


class SetVisibilityCallback:
    """Helper callback to keep a reference to the actor being modified."""
    def __init__(self, actor):
        self.actor = actor

    def __call__(self, state):
        self.actor.SetVisibility(state)


def toggle_vis(flag):
    actor.SetVisibility(flag)


canal = pv.read("D:\Dropbox\\10.Research\\00.Ancient teeth\고대치아.STL\\1.신석기(5000년전)-4500\m25.47\canal.stl")
dentin = pv.read("D:\Dropbox\\10.Research\\00.Ancient teeth\고대치아.STL\\1.신석기(5000년전)-4500\m25.47\dentin.stl")
crown = pv.read("D:\Dropbox\\10.Research\\00.Ancient teeth\고대치아.STL\\1.신석기(5000년전)-4500\m25.47\crown.stl")
import crown_points
data = crown_points.points_info()

e = next(item for item in data if item["name"] == "4500.m25.47")
contact_pts, _ = interpolated_points(e['contact'])
cej_pts, cej_perimeter = interpolated_points(e['cej'])

size = 50
Startpos = 12

p = pv.Plotter()

actor = p.add_mesh(canal, color='green')
callback = SetVisibilityCallback(actor)
p.add_checkbox_button_widget(callback, value=True, size=50, color_on='green',
                             position=(5.0, Startpos), color_off='gray', background_color='gray')
Startpos = Startpos + size + (size//10)


actor = p.add_mesh(dentin, opacity=0.5, color='white')
callback = SetVisibilityCallback(actor)
p.add_checkbox_button_widget(callback, value=True, size=50, color_on='white',
                             position=(5.0, Startpos), color_off='gray', background_color='gray')
Startpos = Startpos + size + (size//10)

actor = p.add_mesh(crown, opacity=0.4, color='yellow')
p.add_text('Crown')
callback = SetVisibilityCallback(actor)
p.add_checkbox_button_widget(callback, value=True, size=50, color_on='yellow',
                             position=(5.0, Startpos), color_off='gray', background_color='gray')
Startpos = Startpos + size + (size//10)


p.add_mesh(lines_from_points(contact_pts), color='red')
p.add_mesh(lines_from_points(cej_pts), color='red')

cent = np.random.random(3)
direction = np.random.random(3)
p.add_arrows(cent, direction)

cpos = p.show()
