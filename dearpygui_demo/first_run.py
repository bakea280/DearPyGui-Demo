# Gives three missing angles of triangle when three sides of triangles are inputted

import dearpygui.dearpygui as dpg
from math import sin, asin, acos, degrees, pi

dpg.create_context()

side_a_id = dpg.generate_uuid()
side_b_id = dpg.generate_uuid()
side_c_id = dpg.generate_uuid()
output_id = dpg.generate_uuid()

def solve_triangle(a, b, c):
    try:
        A = acos((b**2 + c**2 - a**2)/(2 * b * c))
        B = asin(b * sin(A) / a)
        C = pi - A - B
        return f"A = {round(degrees(A), 2)}° ; B = {round(degrees(B), 2)}° ; C = {round(degrees(C), 2)}°"
    except:
        return "Not a triangle"

def callback():
    a = dpg.get_value(side_a_id)
    b = dpg.get_value(side_b_id)
    c = dpg.get_value(side_c_id)
    output = solve_triangle(a, b, c)
    dpg.set_value(output_id, output)

dpg.create_viewport(title='Triangle Solver', width=300, height=170)

with dpg.window(label="Triangle Solver", width=270):
    dpg.add_text("Input three sides")
    dpg.add_input_float(label="a", width=150, tag=side_a_id, min_value=0, min_clamped=True)
    dpg.add_input_float(label="b", width=150, tag=side_b_id, min_value=0, min_clamped=True)
    dpg.add_input_float(label="c", width=150, tag=side_c_id, min_value=0, min_clamped=True)
    dpg.add_button(label="Solve", callback=callback)
    dpg.add_text("", tag=output_id)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()