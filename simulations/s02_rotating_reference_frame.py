"""
This program was originally developed for the MRI1 course at the Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU).
This version is maintained and documented by Victoria Rincon, with slight modifications for desktop use and minor fixes.

Title: Rotating Reference Frame
Authors: Victoria Rincon, Frederik Laun, FAU, University Hospital Erlangen
Original public release: : September 2023
Original version available at:
hhttps://glowscript.org/#/user/Frederik.Laun/folder/LectureMRI1/program/Lecture03.Rotating-Reference-Frame
License: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
https://creativecommons.org/licenses/by-sa/4.0/
"""

from vpython import *
# --- Web VPython (Glowscript) required version declaration ---
# Web VPython 3.2


# SCENE PARAMETERS
scene.background = color.white
window_innerWidth = 1000
window_innerHeight = 600
scene.width = window_innerWidth
scene.height = window_innerHeight
scene.align = 'left'
scene.up = vector(0, 0, 1)
scene.forward = vector(-1, 0, 0)
scene.right = vector(0, -1, 0)
scene.lights = []
scene.ambient = color.gray(0.8)
scene.center = vector(0, 0, 10)

# FAU LOGO
FAU_logo_width = window_innerWidth * 0.35
FAU_logo_height = FAU_logo_width / 5
scene.caption = "  <img src='https://mod.fau.eu/wp-content/uploads/FAU-logo_940x182.jpg' width='{0}' height='{1}'> \n <b>MAGNETIC RESONANCE IMAGING I</b> \n\n".format(
    FAU_logo_width, FAU_logo_height)

# COORD. SYSTEMS GENERAL PARAMETERS
axis_length = scene.height / 10
axis_thickness = axis_length / 30
axis_label_height = axis_length * 0.45

# WORLD C.S.
COLOR_AXIS = vector(0.9, 0.9, 0.99)

x_axis = arrow(pos=vector(0, 0, 0), axis=vector(1, 0, 0), length=axis_length, shaftwidth=axis_thickness, round=True,
               color=COLOR_AXIS, opacity=1)
label(pos=vector(axis_length + axis_length * 0.05, 0.5, 0), height=axis_label_height, text='<b>x</b>', opacity=0,
      box=False, color=color.black)
x_neg_axis = cylinder(pos=vector(0, 0, 0), axis=vector(-1, 0, 0), length=axis_length, radius=1, color=COLOR_AXIS,
                      opacity=1)

y_axis = arrow(pos=vector(0, 0, 0), axis=vector(0, 1, 0), length=axis_length, shaftwidth=axis_thickness, round=True,
               color=COLOR_AXIS, opacity=1)
label(pos=vector(0.5, axis_length + axis_length * 0.05, 0), height=axis_label_height, text='<b>y</b>', opacity=0,
      box=False, color=color.black)
y_neg_axis = cylinder(pos=vector(0, 0, 0), axis=vector(0, -1, 0), length=axis_length, radius=1, color=COLOR_AXIS,
                      opacity=1)

z_axis = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 1), length=axis_length, shaftwidth=axis_thickness, round=True,
               color=COLOR_AXIS, opacity=1)
label(pos=vector(0, 0.5, axis_length + axis_length * 0.05), height=axis_label_height, text='<b>z</b>', opacity=0,
      box=False, color=color.black)
# z_neg_axis = cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, -1), length=axis_length, radius=1, color=COLOR_AXIS, opacity=1)


# RRF C.S.
rrf_length = axis_length * 0.95
COLOR_RRF = vector(0.5, 0.5, 0.59)

x_rrf = arrow(pos=vector(0, 0, 0), axis=vector(1, 0, 0), length=axis_length, shaftwidth=axis_thickness, round=True,
              color=COLOR_RRF, opacity=1)
label_x_rrf = label(pos=vector(axis_length + axis_length * 0.05, 0.5, 0), height=axis_label_height, text='<b>x\'</b>',
                    opacity=0, box=False, color=color.black)
x_neg_rrf = cylinder(pos=vector(0, 0, 0), axis=vector(-1, 0, 0), length=axis_length, radius=1, color=COLOR_RRF,
                     opacity=1)

y_rrf = arrow(pos=vector(0, 0, 0), axis=vector(0, 1, 0), length=axis_length, shaftwidth=axis_thickness, round=True,
              color=COLOR_RRF, opacity=1)
label_y_rrf = label(pos=vector(0.5, axis_length + axis_length * 0.05, 0), height=axis_label_height, text='<b>y\'</b>',
                    opacity=0, box=False, color=color.black)
y_neg_rrf = cylinder(pos=vector(0, 0, 0), axis=vector(0, -1, 0), length=axis_length, radius=1, color=COLOR_RRF,
                     opacity=1)

z_rrf = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 1), length=rrf_length, shaftwidth=axis_thickness, round=True,
              color=COLOR_RRF, opacity=1)
label_z_rrf = label(pos=vector(-1, -0.5, z_rrf.length * 0.95), height=axis_label_height, text='<b>z\'</b>', opacity=0,
                    box=False, color=color.black)
# z_neg_axis = cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, -1), length=axis_length, radius=1, color=COLOR_RRF, opacity=1)


# MAIN MAGNETIC FIELD (B0)
arrow_length = axis_length * 0.8
arrow_thickness = axis_thickness * 1.4

COLOR_B0 = vector(0, 0.5, 1)
COLOR_LABEL_B0 = vector(0, 0.35, 0.69)

arrow_B0 = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, arrow_length), shaftwidth=arrow_thickness, round=True,
                 color=COLOR_B0)
label_B0 = label(pos=vector(-5, 8, arrow_length * 0.9), height=axis_label_height, text='<b>B<sub>0</sub></b>',
                 opacity=0, box=False, color=COLOR_LABEL_B0)

# B1+ Field
COLOR_B1plus = vector(0.1, 0.6, 0.1)
arrow_B1plus = arrow(pos=vector(0, 0, 0), axis=vector(arrow_length * 0.7, 0, 0), shaftwidth=arrow_thickness, round=True,
                     color=COLOR_B1plus)
label_B1plus = label(pos=vector(arrow_B1plus.length, 2, 2), height=axis_label_height, text='<b>B<sub>1</sub>+</b>',
                     opacity=0, box=False, color=COLOR_B1plus)

# FREQUENCY LABELS
w0 = '0'
wHF = w0
omega = w0
label_wHF = label(pos=vector(20, 20, 0), pixel_pos=True, height=axis_label_height * 0.75, line=False, box=False,
                  opacity=0, color=color.black, align='left', text='\u03C9<sub>HF</sub> = ' + wHF + ' rad/s')
label_omega = label(pos=vector(20, 20 + label_wHF.height, 0), pixel_pos=True, height=axis_label_height * 0.75,
                    line=False, box=False, opacity=0, color=color.black, align='left',
                    text='\u03A9 = ' + omega + ' rad/s')
label_w0 = label(pos=vector(20, 20 + 2 * label_wHF.height, 0), pixel_pos=True, height=axis_label_height * 0.75,
                 line=False, box=False, opacity=0, color=color.black, align='left',
                 text='\u03C9<sub>0</sub> = ' + w0 + ' rad/s')
label(pos=vector(20, 20 + 3 * label_wHF.height, 0), pixel_pos=True, height=axis_label_height * 0.65, line=False,
      box=False, opacity=0, color=color.black, align='left', text='<b>Real values:</b>')

# PLAY FUNCTION
play = False


def run_play(b):
    global play
    play = not play
    if play:
        b.text = "Pause"
    else:
        b.text = "Play"


# PLAY BUTTON
button(text="Play", pos=scene.title_anchor, bind=run_play)

# PROGRAM DESCRIPTION
scene.append_to_caption('  <b>THE ROTATING REFERENCE FRAME (RRF)</b>: \n')
scene.append_to_caption('''
   This simulation exemplifies the behaviour 
   of the Rotating Reference Frame (RRF) 
   with respect to the World Coordinate 
   System (WCS).

   The RRF rotates with angular frequency \u03A9 
   and the B<sub>1<sup>+</sub></sup> field with angular frequency \u03C9<sub>HF</sub>. 
   Under resonant condition \u03C9<sub>HF</sub> = \u03C9<sub>0</sub> = \u03A9, but
   in the off resonant case \u03C9<sub>HF</sub> \u2260 \u03C9<sub>0</sub> = \u03A9. \n''')

scene.append_to_caption('''      
   Below you can modify the strength of the 
   main magnetic field (B<sub>0</sub>) and activate or 
   deactivate the x-y view of the scene.\n\n\n''')


# |Bo| SLIDER FUNCTION
def set_B0(s):
    wt_B0.text = '{:1.1f}'.format(s.value)
    #c.delete()


# |Bo| SLIDER
scene.append_to_caption('    Strength of the main magnetic field:\n')
scene.append_to_caption('      B<sub>0</sub>: ')

slider_B0 = slider(min=0.1, max=3, value=3, length=220, bind=set_B0, right=15)
wt_B0 = wtext(text='{:1.1f}'.format(slider_B0.value))

scene.append_to_caption('T\n\n')

# CURVE PHASE B1+ FUNCTION
phase_path_radious = 1


def set_curve_parameters(phase_path_angle):
    phase_path_radious = arrow_B1plus.length * 0.4
    global phase_path_points
    phase_path_points = []
    for angle in range(0, phase_path_angle + 1):
        phase_path_points.append(
            vector(phase_path_radious * cos(radians(angle)), phase_path_radious * sin(radians(angle)), 0))
    curve_path.append(phase_path_points)


# B1+ PHASE SLIDER FUNCTION
def set_B1phase(s):
    slider_angle = round(s.value)
    # wtext_B1phase.text = '{:1.1f}'.format(s.value)
    wtext_B1phase.text = slider_angle
    curve_path.clear()

    # curve_path.delete
    set_curve_parameters(slider_angle)
    reset_animation()


# B1+ PHASE SLIDER
scene.append_to_caption('    Phase of the B<sub>1<sup>+</sub></sup> field:\n')
scene.append_to_caption('      <i>\u03B8</i><sub>B1</sub>: ')

slider_B1phase = slider(min=0, max=180, value=0, length=220, bind=set_B1phase, right=15)
wtext_B1phase = wtext(text='{:1.1f}'.format(slider_B1phase.value))

scene.append_to_caption('°\n\n')

# CURVE PHASE B1+
COLOR_CURVE_PATH = vector(1, 0.2, 1)
curve_path = curve(color=COLOR_CURVE_PATH, radius=1)

label_curve_path = label(visible=False, pos=(arrow_B1plus.length * 0.4) * vector(1, 0, 0), height=axis_label_height,
                         text='<i>\u03B8</i><sub>B1</sub>', opacity=0, box=False, color=COLOR_CURVE_PATH)


# X-Y VIEW FUNCTION
def change_view():
    global x_y_view
    if x_y_view:
        scene.up = vector(0, 0, 1)
        scene.forward = vector(-1, 0, 0)
        scene.right = vector(0, -1, 0)
        scene.userspin = True
        button_x_y.background = color.white
        x_y_view = False
    else:
        scene.center = vector(0, 0, 0)
        scene.up = vector(0, 1, 0)  # Set up direction
        scene.forward = vector(0, 0, -1)
        scene.userspin = False
        button_x_y.background = color.green
        x_y_view = True


# X-Y VIEW BUTTON
scene.append_to_caption('    X-Y view activation:      ')
button_x_y = button(text='X-Y View', bind=change_view)
x_y_view = False

# SCALE FACTOR DESCRIPTION
scene.append_to_caption('\n')
scene.append_to_caption('''      
    <b>Scale factor</b>:
    1 second (s) in the simulation corresponds to
    approximately 7.8 nanoseconds (ns) in real life.\n 
    In other words, while one rotation is completed in
    1 s of the simulation, approximately 127,728,049
    rotations are completed in real life within the
    same 1 second duration (B<sub>0</sub> = 3 T).\n\n\n''')


# RESET FUNCTION
def reset_animation():
    global t
    t = 0


# ANIMATION PARAMETERS
RATEVALUE = 30

SCALE_FACTOR = 3831841466

# PHYSICS CONSTANTS
GAMMA_PROTONS = 2.67513E8

# VARIABLES INITIALIZATION
phase_path_points = []
phase_path_points_rotating = []
t = 0

# ITERATION OVER TIME
while True:

    rate(RATEVALUE)
    if play:

        # Frequencies calculation
        B0 = round(slider_B0.value, 1)
        B1phase = slider_B1phase.value
        phase_path_angle = slider_B1phase.value

        w0 = GAMMA_PROTONS * B0
        v0 = w0 / (2 * pi)
        omega = w0
        wHF = w0

        w0_simulation = w0 / SCALE_FACTOR
        v0_simulation = w0_simulation / (2 * pi)
        wHF_simulation = w0_simulation
        omega_simulation = w0_simulation

        # Formatting the variables
        w0_formatted = "{:.1f}".format(w0)
        wHF_formatted = "{:.1f}".format(wHF)
        omega_formatted = "{:.1f}".format(omega)

        # Displaying frequencies on the screen
        label_w0.text = '\u03C9<sub>0</sub> = ' + w0_formatted + ' rad/s'
        label_wHF.text = '\u03C9<sub>HF</sub> = ' + wHF_formatted + ' rad/s'
        label_omega.text = '\u03A9 = ' + omega_formatted + ' rad/s'

        # Setting the behaviour of the RRF
        x_rrf.axis = vector(axis_length * cos(omega_simulation * t), axis_length * sin(omega_simulation * t),
                            0)  # Change the axis of the arrow over time
        x_neg_rrf.axis = vector(-axis_length * cos(omega_simulation * t), -axis_length * sin(omega_simulation * t), 0)
        label_x_rrf.pos = vector(x_rrf.axis.x + 5, x_rrf.axis.y + 5, x_rrf.axis.z + 3)

        y_rrf.axis = vector(-axis_length * sin(omega_simulation * t), axis_length * cos(omega_simulation * t), 0)
        y_neg_rrf.axis = vector(axis_length * sin(omega_simulation * t), -axis_length * cos(omega_simulation * t), 0)
        label_y_rrf.pos = vector(y_rrf.axis.x + 5, y_rrf.axis.y + 5, y_rrf.axis.z + 3)

        # Adjusting Bo vector length according to the selected strength
        arrow_B0.length = slider_B0.value * (arrow_length / slider_B0.max)
        label_B0.pos = vector(-5, 8, arrow_B0.length * 0.9)

        # Setting the behaviour of the B1+ field
        arrow_B1plus.axis = arrow_B1plus.length * vector(
            cos(radians(B1phase)) * cos(wHF_simulation * t) - sin(radians(B1phase)) * sin(wHF_simulation * t),
            sin(radians(B1phase)) * cos(wHF_simulation * t) + cos(radians(B1phase)) * sin(wHF_simulation * t), 0)
        label_B1plus.pos = vector(arrow_B1plus.axis.x + 5, arrow_B1plus.axis.y + 5, arrow_B1plus.axis.z + 3)

        # Setting the curve that represent the phase of the B1+ field
        for N in range(0, len(phase_path_points)):
            curve_path.modify(N, pos=vector(
                phase_path_points[N].x * cos(wHF_simulation * t) - phase_path_points[N].y * sin(wHF_simulation * t),
                phase_path_points[N].x * sin(wHF_simulation * t) + phase_path_points[N].y * cos(wHF_simulation * t), 0))

        if curve_path.npoints != 0:
            label_curve_path.visible = True
            data_label_curve_path_position = curve_path.point(int(len(phase_path_points) / 2))
            # print(data_label_curve_path_position)
            label_curve_path.pos = data_label_curve_path_position["pos"] * 1.4

        # time iteration
        t = t + 1

