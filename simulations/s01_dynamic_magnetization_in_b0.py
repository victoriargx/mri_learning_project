"""
This program was originally developed for the MRI1 course at the Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU).
This version is maintained and documented by Victoria Rincon, with slight modifications for desktop use.

Title: Dynamics of M in B₀
Authors: Victoria Rincon, Frederik Laun, FAU, University Hospital Erlangen
Original public release: : September 2023
Original version available at:
https://glowscript.org/#/user/Frederik.Laun/folder/LectureMRI1/program/Lecture03.Dynamics-of-M-in-B0
License: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
https://creativecommons.org/licenses/by-sa/4.0/
"""

from vpython import *
# --- Web VPython (Glowscript) required version declaration ---
# Web VPython 3.2

# SCENE PARAMETERS
scene.background = color.white
window_innerWidth = 1600
window_innerHeight = 900
scene.width = window_innerWidth * 0.6
scene.height = window_innerHeight * 0.75
# --- Web VPython (Glowscript) version of scene sizing ---
# scene.width = window.innerWidth * 0.6
# scene.height = window.innerHeight * 0.92
scene.align = 'left'
scene.up = vector(0, 0, 1)
scene.forward = vector(-1, 0, 0)
scene.right = vector(0, -1, 0)
scene.lights = []
scene.ambient = color.gray(0.8)
scene.center = vector(0, 0, 10)

# FAU LOGO
# FAU_logo_width = window.innerWidth * 0.3  # Web VPython (Glowscript)
FAU_logo_width = window_innerWidth * 0.3
FAU_logo_height = FAU_logo_width / 5
scene.caption = "  <img src='https://mod.fau.eu/wp-content/uploads/FAU-logo_940x182.jpg' width='{0}' height='{1}'> \n <b>MAGNETIC RESONANCE IMAGING I</b> \n\n".format(
    FAU_logo_width, FAU_logo_height)

# COORD. SYSTEM
axis_length = scene.height / 10
axis_thickness = axis_length / 30
axis_label_height = axis_length * 0.45

COLOR_AXIS = vector(0.9, 0.9, 0.99)

x_axis = arrow(pos=vector(0, 0, 0), axis=vector(1, 0, 0), length=axis_length, shaftwidth=axis_thickness, round=True,
               color=COLOR_AXIS, opacity=1)
label(pos=vector(axis_length + axis_length * 0.05, 0.5, 0), height=axis_label_height, text='<b>x</b>', opacity=0,
      box=False, color=color.black)
x_neg_axis = cylinder(pos=vector(0, 0, 0), axis=vector(-1, 0, 0), length=axis_length, radius=axis_thickness / 2,
                      color=COLOR_AXIS, opacity=1)

y_axis = arrow(pos=vector(0, 0, 0), axis=vector(0, 1, 0), length=axis_length, shaftwidth=axis_thickness, round=True,
               color=COLOR_AXIS, opacity=1)
label(pos=vector(0.5, axis_length + axis_length * 0.05, 0), height=axis_label_height, text='<b>y</b>', opacity=0,
      box=False, color=color.black)
y_neg_axis = cylinder(pos=vector(0, 0, 0), axis=vector(0, -1, 0), length=axis_length, radius=axis_thickness / 2,
                      color=COLOR_AXIS, opacity=1)

z_axis = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 1), length=axis_length, shaftwidth=axis_thickness, round=True,
               color=COLOR_AXIS, opacity=1)
label(pos=vector(0, 0.5, axis_length + axis_length * 0.05), height=axis_label_height, text='<b>z</b>', opacity=0,
      box=False, color=color.black)
# z_neg_axis = cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, -1), length=axis_length, radius=axis_thickness/2, color=COLOR_AXIS, opacity=1)


# MAIN MAGNETIC FIELD (B0)
arrow_length = axis_length * 0.9
arrow_thickness = axis_thickness * 1.4

COLOR_B0 = vector(0, 0.5, 1)
COLOR_LABEL_B0 = vector(0, 0.35, 0.69)

arrow_B0 = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, arrow_length), shaftwidth=arrow_thickness, round=True,
                 color=COLOR_B0)
label_B0 = label(pos=vector(-5, 8, arrow_length * 0.9), height=axis_label_height, text='<b>B<sub>0</sub></b>',
                 opacity=0, box=False, color=COLOR_LABEL_B0)

# MAGNETIZATION (M)
Mo = arrow_length * 0.7
COLOR_Mo = vector(1, 0.781, 0.021)

arrow_M = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 1), length=Mo, shaftwidth=arrow_thickness, round=True,
                color=COLOR_Mo, make_trail=False)
label_M = label(pos=vector(-5, 8, arrow_M.length * 0.9), height=axis_label_height, text='<b>M</b>', opacity=0,
                box=False, color=COLOR_Mo)

# MAGNETIZATION TRAIL
COLOR_TRAIL = vector(1, 0.8, 0.4)

sphere_tip = sphere(pos=arrow_M.axis, radius=arrow_thickness * 0.15, make_trail=True, trail_type="points", interval=1,
                    retain=300, color=COLOR_TRAIL, opacity=1)
sphere_tip.trail_radius = sphere_tip.radius

# FREQUENCY LABELS
w0 = '0'
v0 = '0'
label_w0 = label(pos=vector(20, 20, 0), pixel_pos=True, height=axis_label_height * 0.75, line=False, box=False,
                 opacity=0, color=color.black, align='left', text='\u03C9<sub>0</sub> = ' + w0 + ' rad/s')
label_v0 = label(pos=vector(20, 20 + label_w0.height, 0), pixel_pos=True, height=axis_label_height * 0.75, line=False,
                 box=False, opacity=0, color=color.black, align='left', text='\u03BD<sub>0</sub> = ' + v0 + ' Hz')
label(pos=vector(20, 20 + 2 * label_v0.height, 0), pixel_pos=True, height=axis_label_height * 0.65, line=False,
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
scene.append_to_caption('  <b>DYNAMIC OF M(t) IN B<sub>0</sub></b>: \n')
scene.append_to_caption('''
   This simulation exemplifies the precession 
   of the magnetization vector (<b>M</b>) due to the 
   influence of the main magnetic field (<b>B</b><sub>0</sub>).\n''')

scene.append_to_caption('''      
   Below you can modify the strength of the main 
   magnetic field (B<sub>0</sub>), the angle between <b>M</b> and,
   z-axis and activate/deactivate the x-y view of the
   scene.\n\n\n''')


# |B0| SELECTION FUNCTION
def set_B0(s):
    reset_animation()
    wt_B0.text = '{:1.1f}'.format(s.value)


# |B0| SLIDER
scene.append_to_caption('    Strength of the main magnetic field:\n')
scene.append_to_caption('      B<sub>0</sub>: ')

slider_B0 = slider(min=0.1, max=3, value=3, length=220, bind=set_B0, right=15)
wt_B0 = wtext(text='{:1.1f}'.format(slider_B0.value))

scene.append_to_caption('T\n\n')

# STARTING POINT OF THE MAGNETIZATION FUNCTION
angle_M = 90


def set_starting_point(r):
    reset_animation()
    global angle_M
    if r.checked:
        if r.angle == 90:
            angle_M = 90
        elif r.angle == 45:
            angle_M = 45
        elif r.angle == 15:
            angle_M = 15
        elif r.angle == 5:
            angle_M = 5


# STARTING POINT OF THE MAGNETIZATION BUTTONS
scene.append_to_caption('    Angle Between <b>M</b> and z-axis:\n')
scene.append_to_caption('      ')
radio_p1 = radio(angle=5, bind=set_starting_point, checked=False, name='starting_point')
scene.append_to_caption('5°')

scene.append_to_caption('      ')
radio_p15 = radio(angle=15, bind=set_starting_point, checked=False, name='starting_point')
scene.append_to_caption('15°')

scene.append_to_caption('      ')
radio_p45 = radio(angle=45, bind=set_starting_point, checked=False, name='starting_point')
scene.append_to_caption('45°')

scene.append_to_caption('      ')
radio_p90 = radio(angle=90, bind=set_starting_point, checked=True, name='starting_point')
scene.append_to_caption('90°\n\n')


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
    same 1 second duration (B<sub>0</sub> = 3 T).\n
    by Victoria Rincon and Frederik Laun\n''')

# GRAPH
graph(width=scene.width, height=scene.width / 4, fast=False, title='<b>Evolution of M(t) in B<sub>0</sub></b>',
      xtitle='Time (ns)', ytitle='M(t)/M<sub>0</sub>', ymin=-1, ymax=1, scroll=True, xmin=0, xmax=300)
Mx = gcurve(color=color.blue, label='<i>M</i><sub>x</sub>')
My = gcurve(color=color.red, label='<i>M</i><sub>y</sub>')
Mz = gcurve(color=color.green, label='<i>M</i><sub>z</sub>')


# RESET FUNCTION
def reset_animation():
    global t, t_g
    t = 0
    t_g = 0
    Mx.delete()
    My.delete()
    Mz.delete()
    sphere_tip.clear_trail()


# ANIMATION PARAMETERS
RATEVALUE = 30  # Frames per second

SCALE_FACTOR = 3831841466
TIME_FACTOR = 7.829
FORMAT_FACTOR = 1E6

# PHYSICS CONSTANTS
GAMMA_PROTONS = 2.67513E8

# VARIABLES INITIALIZATION
t = 0
t_g = 0

# ITERATION OVER TIME
while True:

    rate(RATEVALUE)  # Limit the animation to run at a maximum of 'rate_value' frames per second
    if play:
        # Frequencies calculation
        B0 = slider_B0.value
        w0 = GAMMA_PROTONS * B0
        v0 = w0 / (2 * pi)
        w0_simulation = w0 / SCALE_FACTOR
        v0_simulation = w0_simulation / (2 * pi)

        # Formatting the variables to display on the screen
        v0_formatted = "{:.3f}".format(v0 / FORMAT_FACTOR)
        w0_formatted = "{:.1f}".format(w0)

        # Setting the behaviour of the Magnetization (M)
        arrow_M.axis = Mo * vector(cos(w0_simulation * t) * sin(radians(angle_M)),
                                   sin(w0_simulation * t) * sin(radians(angle_M)),
                                   cos(radians(angle_M)))  # Change the axis of the arrow over time
        label_M.pos = vector(arrow_M.axis.x + 5, arrow_M.axis.y + 5, arrow_M.axis.z + 3)

        # Adjusting B0 vector length according to the selected strength
        arrow_B0.length = slider_B0.value * (arrow_length / slider_B0.max)
        label_B0.pos = vector(-5, 8, arrow_B0.length * 0.9)

        # Displaying w0 and v0 on the screen
        label_w0.text = '\u03C9<sub>0</sub> = ' + w0_formatted + ' rad/s'
        label_v0.text = '\u03BD<sub>0</sub> = ' + v0_formatted + ' MHz'

        # Verification print statement
        # print('v0: ',v0,'\nv0_sim: ',v0_simulation,'\nw0: ',w0,'\nw0_sim: ',w0_simulation)

        # Adjusting trail trajectory
        sphere_tip.pos = arrow_M.axis

        # Displaying the components of the magnetization
        Mx.plot(t_g, cos(w0_simulation * t) * sin(radians(angle_M)))
        My.plot(t_g, sin(w0_simulation * t) * sin(radians(angle_M)))
        Mz.plot(t_g, cos(radians(angle_M)))

        # Time scaling for the graph
        t_g = t * TIME_FACTOR / RATEVALUE

        # time iteration
        t = t + 1


