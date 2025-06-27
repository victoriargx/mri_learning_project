"""
This program was originally developed for the MRI1 course at the Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU).
This version is maintained and documented by Victoria Rincon, with slight modifications for desktop use and minor fixes.

Title: Resonant Excitation
Authors: Victoria Rincon, Frederik Laun, FAU, University Hospital Erlangen
Original public release: : September 2023
Original version available at:
https://glowscript.org/#/user/Frederik.Laun/folder/LectureMRI1/program/Lecture03.Resonant-Excitation
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
scene.height = window_innerHeight * 0.7
scene.align = 'left'
scene.up = vector(0, 0, 1)
scene.forward = vector(-1, 0, 0)
scene.right = vector(0, -1, 0)
scene.lights = []
scene.ambient = color.gray(0.8)


# INITIAL CAMERA SETTINGS FUNCTION
def initial_camera_settings():
    # Parameters that change the camera view
    scene.range = 76.6866
    # scene.center = vector(0, 0, 0)
    scene.camera.pos = vector(90.8748, 93.5682, 25.0852)
    scene.camera.axis = vector(-90.8748, -93.5682, -25.0852)


initial_camera_settings()

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
label_x_axis = label(pos=vector(axis_length + axis_length * 0.05, 0.5, 0), height=axis_label_height, text='<b>x</b>',
                     opacity=0, box=False, color=color.black)
x_neg_axis = cylinder(pos=vector(0, 0, 0), axis=vector(-1, 0, 0), length=axis_length, radius=axis_thickness / 2,
                      color=COLOR_AXIS, opacity=1)

y_axis = arrow(pos=vector(0, 0, 0), axis=vector(0, 1, 0), length=axis_length, shaftwidth=axis_thickness, round=True,
               color=COLOR_AXIS, opacity=1)
label_y_axis = label(pos=vector(0.5, axis_length + axis_length * 0.05, 0), height=axis_label_height, text='<b>y</b>',
                     opacity=0, box=False, color=color.black)
y_neg_axis = cylinder(pos=vector(0, 0, 0), axis=vector(0, -1, 0), length=axis_length, radius=axis_thickness / 2,
                      color=COLOR_AXIS, opacity=1)

z_axis = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 1), length=axis_length, shaftwidth=axis_thickness, round=True,
               color=COLOR_AXIS, opacity=1)
label_z_axis = label(pos=vector(0, 0.5, axis_length + axis_length * 0.05), height=axis_label_height, text='<b>z</b>',
                     opacity=0, box=False, color=color.black)
# z_neg_axis = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, -1), length=axis_lenght,shaftwidth=axis_thickness, round=True, color=COLOR_AXIS, opacity=1)


# RFF C.S.
rff_length = axis_length
COLOR_RFF = vector(0.5, 0.5, 0.59)

x_rff = arrow(pos=vector(0, 0, 0), axis=vector(1, 0, 0), length=axis_length, shaftwidth=axis_thickness, round=True,
              color=COLOR_RFF, opacity=1, visible=False)
label_x_rff = label(pos=vector(axis_length + axis_length * 0.05, 0.5, 0), height=axis_label_height, text='<b>x\'</b>',
                    opacity=0, box=False, color=color.black, visible=False)
x_neg_rff = cylinder(pos=vector(0, 0, 0), axis=vector(-1, 0, 0), length=axis_length, radius=1, color=COLOR_RFF,
                     opacity=1, visible=False)

y_rff = arrow(pos=vector(0, 0, 0), axis=vector(0, 1, 0), length=axis_length, shaftwidth=axis_thickness, round=True,
              color=COLOR_RFF, opacity=1, visible=False)
label_y_rff = label(pos=vector(0.5, axis_length + axis_length * 0.05, 0), height=axis_label_height, text='<b>y\'</b>',
                    opacity=0, box=False, color=color.black, visible=False)
y_neg_rff = cylinder(pos=vector(0, 0, 0), axis=vector(0, -1, 0), length=axis_length, radius=1, color=COLOR_RFF,
                     opacity=1, visible=False)

z_rff = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 1), length=rff_length, shaftwidth=axis_thickness, round=True,
              color=COLOR_RFF, opacity=1, visible=False)
label_z_rff = label(pos=vector(-1, -0.5, z_rff.length * 0.95), height=axis_label_height, text='<b>z\'</b>', opacity=0,
                    box=False, color=color.black, visible=False)
# z_neg_axis = cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, -1), length=axis_length, radius=1, color=COLOR_RFF, opacity=1)


# MAIN MAGNETIC FIELD (B0)
arrow_length = axis_length * 0.9
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
label_B1plus = label(pos=vector(arrow_B1plus.length, 2, 2), height=axis_label_height,
                     text='<b>B<sub>1</sub><sup>+</sup></b>', opacity=0, box=False, color=COLOR_B1plus)

# MAGNETIZATION (M)
Mo = arrow_length * 0.7
COLOR_Mo = vector(1, 0.781, 0.021)

arrow_M = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 1), length=Mo, shaftwidth=arrow_thickness, round=True,
                color=COLOR_Mo, make_trail=False)
label_M = label(pos=vector(-5, 8, arrow_M.length * 0.9), height=axis_label_height, text='<b>M</b>', opacity=0,
                box=False, color=COLOR_Mo)

# MAGNETIZATION TRAIL
COLOR_TRAIL = vector(1, 0.8, 0.4)

sphere_tip = sphere(pos=arrow_M.axis, radius=arrow_thickness * 0.15, make_trail=True, trail_type="points", interval=0.2,
                    retain=320, color=COLOR_TRAIL, opacity=1)
sphere_tip.trail_radius = sphere_tip.radius

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
scene.append_to_caption('  <b> RESONANT EXCITATION</b>\n')
scene.append_to_caption('''
   This simulation exemplifies the precession of
   the magnetization vector (<b>M</b>) with  <b>B</b>(t) =  <b>B</b><sub>0</sub>
   + B<sub>1</sub><sup>+</sup>(t) in the World Coordinate System (WCS)
   and the Rotating Reference Frame (RRF).

   The B<sub>1</sub><sup>+</sup> field is a radiofrequency (RF) magnetic
   field that is perpendicular to the main magnetic
   field (<b>B</b><sub>0</sub>). The B<sub>1</sub><sup>+</sup> field oscillates at a specific
   resonant frequency \u03C9<sub>HF</sub> and excitates <b>M</b> under 
   the resonant condition \u03C9<sub>HF</sub> = \u03C9<sub>0</sub>.\n''')

scene.append_to_caption('''      
   Below, you can choose to visualize the excitation 
   process in either the World Coordinate System or 
   the Rotating Reference Frame. You can modify 
   the strength of the main magnetic field (<b>B</b><sub>0</sub>) and 
   the strength of the B<sub>1</sub><sup>+</sup> field. Additionally, you can 
   activate or deactivate the x-y view of the scene.\n\n''')

# COORDINATE SYSTEM SELECTION FUNCTIONS
WCS_view = True


def change_to_WSC():
    button_WCS.background = color.green
    button_RRF.background = color.white
    global WCS_view
    WCS_view = True
    gp.xtitle = 'Time (ns)'
    curve_path.visible = False
    label_curve_path.visible = False
    reset_animation()


def change_to_FFR():
    button_WCS.background = color.white
    button_RRF.background = color.green
    global WCS_view
    WCS_view = False
    gp.xtitle = 'Time (ms)'
    curve_path.visible = True
    reset_animation()


# COORDINATE SYSTEM SELECTION BUTTONS
scene.append_to_caption('    World Coordinate System:      ')
button_WCS = button(text='WCS', bind=change_to_WSC, background=color.green)

scene.append_to_caption('<p style="color:red">      In the WCS, <b>M</b> has a minor error in its behavior.</p>')

scene.append_to_caption('\n    Rotating Reference Frame:      ')
button_RRF = button(text='RRF', bind=change_to_FFR)

# |B0| SELECTION FUNCTION
B0_bs = 3


def set_strength_B0(r):
    global B0_bs
    reset_animation()
    if r.checked:
        if r.strength == 3:
            B0_bs = 3
        elif r.strength == 1.5:
            B0_bs = 1.5
        elif r.strength == 0.5:
            B0_bs = 0.5


# |B0| SELECTION BUTTONS
scene.append_to_caption('\n\n    Strength of the main magnetic field:\n')
scene.append_to_caption('      B<sub>0</sub>: ')

scene.append_to_caption('      ')
radio_B0_05 = radio(strength=0.5, bind=set_strength_B0, checked=False, name='strength_B0')
scene.append_to_caption('0.5 T')

scene.append_to_caption('      ')
radio__B0_1 = radio(strength=1.5, bind=set_strength_B0, checked=False, name='strength_B0')
scene.append_to_caption('1 T')

scene.append_to_caption('      ')
radio__B0_3 = radio(strength=3, bind=set_strength_B0, checked=True, name='strength_B0')
scene.append_to_caption('3 T\n\n')

# |B1+| SELECTION FUNCTION
B1_bs = 5E-6


def set_strength_B1(r):
    global B1_bs
    reset_animation()
    if r.checked:

        if r.strength == 5:
            B1_bs = 5E-6
        elif r.strength == 3:
            B1_bs = 3E-6
        elif r.strength == 1:
            B1_bs = 1E-6


# |B1+| SELECTION BUTTONS
scene.append_to_caption('    Strength of the B<sub>1</sub><sup>+</sup> field:\n')
scene.append_to_caption('      B<sub>1</sub><sup>+</sup>: ')

scene.append_to_caption('      ')
radio_B1_1 = radio(strength=1, bind=set_strength_B1, checked=False, name='strength_B1')
scene.append_to_caption('1 \u03BCT')

scene.append_to_caption('      ')
radio_B1_3 = radio(strength=3, bind=set_strength_B1, checked=False, name='strength_B1')
scene.append_to_caption('3  \u03BCT')

scene.append_to_caption('      ')
radio_B1_5 = radio(strength=5, bind=set_strength_B1, checked=True, name='strength_B1')
scene.append_to_caption('5  \u03BCT\n\n')

# CURVE PHASE B1+ FUNCTION
phase_path_origin = arrow_B1plus.length * 0.2


def set_curve_parameters(phase_path_angle):
    global phase_path_points
    phase_path_points = []
    # Each degree we establish a point in the curve
    for angle in range(0, phase_path_angle + 1):
        phase_path_points.append(
            vector(phase_path_origin * cos(radians(angle)), phase_path_origin * sin(radians(angle)), 0))
    curve_path.append(phase_path_points)


# CURVE PHASE B1+
COLOR_CURVE_PATH = vector(1, 0.2, 1)
curve_path = curve(color=COLOR_CURVE_PATH, radius=0.7, visible=False)

label_curve_path = label(visible=False, pos=(arrow_B1plus.length * 0.3) * vector(1, 0, 0), height=axis_label_height,
                         text='<i>\u03B8</i><sub>B1</sub>', opacity=0, box=False, color=COLOR_CURVE_PATH)


# B1+ PHASE SELECTION FUNCTION
def set_B1phase(s):
    slider_angle = round(s.value)
    wtext_B1phase.text = slider_angle
    curve_path.clear()
    set_curve_parameters(slider_angle)
    reset_animation()


# B1+ PHASE SLIDER
scene.append_to_caption('    Phase of the B<sub>1<sup></sub>+</sup> field:\n')
scene.append_to_caption('      <i>\u03B8</i><sub>B1</sub>: ')

slider_B1phase = slider(min=0, max=180, value=0, length=220, bind=set_B1phase, right=15)
wtext_B1phase = wtext(text='{:1.0f}'.format(slider_B1phase.value))

scene.append_to_caption('°\n\n')


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
    <b>Scale factor In the World Coordinate System</b>:
    1 second (s) in the simulation corresponds to
    approximately 26.31 nanoseconds (ns) in real life.\n 
    In other words, while one rotation is completed in
    0.297 s of the simulation, approximately 127,728,049
    rotations are completed in real life within the
    same 1 second duration (B<sub>0</sub> = 3 T).\n\n''')

scene.append_to_caption('''      
    <b>Scale factor In the Rotating Reference Frame</b>:
    1 second (s) in the simulation corresponds to
    approximately 0.626 miliseconds (ms) in real life.\n 
    In other words, while one rotation is completed in
    7.5 s of the simulation, approximately 212
    rotations are completed in real life within the
    same 1 second duration (B<sub>1</sub><sup>+</sup> = 5 \u03BCT).\n
    by Victoria Rincon and Frederik Laun\n\n\n''')

# GRAPH
gp = graph(width=scene.width, height=scene.width / 4, title='<b>Evolution of M(t) in B(t)</b>', xtitle='Time (ns)',
           ytitle='M(t)/M<sub>0</sub>', ymin=-1, ymax=1, scroll=True, xmin=0, xmax=300, fast=False)
Mx = gcurve(color=color.blue, label='<i>M</i><sub>x</sub>')
My = gcurve(color=color.red, label='<i>M</i><sub>y</sub>')
Mz = gcurve(color=color.green, label='<i>M</i><sub>z</sub>')


# RESET FUNCTION
def reset_animation():
    global t
    t = 0
    Mx.delete()
    My.delete()
    Mz.delete()
    sphere_tip.clear_trail()


# ANIMATION PARAMETERS
RATEVALUE = 100  # Frames per second

SCALE_FACTOR_w0 = 3831841466  # 3.8E9
SCALE_FACTOR_w1 = 159660.0611

TIME_FACTOR_WCS = 26.097  # units ns<---------
TIME_FACTOR_RRF = 0.6263  # units ms  <---------

FORMAT_FACTOR = 1000000

# PHYSICS CONSTANTS
GAMMA_PROTONS = 2.67513E8

# VARIABLES INITIALIZATION
phase_path_points = []
phase_path_points_rotating = []

t = 0
t_g = 0

# ITERATION OVER TIME
while True:

    rate(RATEVALUE)
    if play:

        B0 = B0_bs
        w0 = GAMMA_PROTONS * B0
        v0 = w0 / (2 * pi)
        w0_simulation = w0 / SCALE_FACTOR_w0
        v0_simulation = w0_simulation / (2 * pi)

        B1 = B1_bs
        w1 = GAMMA_PROTONS * B1
        v1 = w1 / (2 * pi)
        w1_simulation = w1 / SCALE_FACTOR_w1
        v1_simulation = w1_simulation / (2 * pi)

        # Resonance Case (Resonance condition)
        wHF_simulation = w0_simulation

        # Formatting the variables to display on the screen
        v0_formatted = "{:.3f}".format(v0 / FORMAT_FACTOR)
        w0_formatted = "{:.1f}".format(w0 / FORMAT_FACTOR)

        # Adjusting B1+ and B0 vectors length according to the selected strength
        arrow_B0.length = (B0_bs / 3) * arrow_length
        arrow_B1plus.length = (B1_bs / 5E-6) * (arrow_length * 0.75)

        # In the World Coordinate System (WCS)
        if WCS_view == True:

            # WCS Visualization
            x_axis.visible = True
            label_x_axis.visible = True
            x_neg_axis.visible = True
            y_axis.visible = True
            label_y_axis.visible = True
            y_neg_axis.visible = True
            z_axis.visible = True
            label_z_axis.visible = True

            # RFF C.S. Hiding
            x_rff.visible = False
            label_x_rff.visible = False
            x_neg_rff.visible = False
            y_rff.visible = False
            label_y_rff.visible = False
            y_neg_rff.visible = False
            z_rff.visible = False
            label_z_rff.visible = False

            # Setting the behaviour of the Magnetization (M) in the WCS
            # THIS BEHAVIOUR HAS TO BE MODIFIED <-------------------------------------------------------------------------------------
            arrow_M.axis = vector(Mo * sin(w0_simulation * t + radians(slider_B1phase.value)) * sin(w1_simulation * t),
                                  -Mo * cos(w0_simulation * t + radians(slider_B1phase.value)) * sin(w1_simulation * t),
                                  Mo * cos(w1_simulation * t))
            # arrow_M.axis = vector(-Mo*sin(w0_simulation*t+radians(slider_B1phase.value))*sin(w1_simulation*t), Mo*cos(w0_simulation*t-radians(slider_B1phase.value))*sin(w1_simulation*t), Mo*cos(w1_simulation*t))

            # Setting the behaviour of the B1+ field in the WCS
            arrow_B1plus.axis = vector(arrow_B1plus.length * cos(wHF_simulation * t),
                                       arrow_B1plus.length * sin(wHF_simulation * t), 0)

            # Time scaling for the graph
            t_g = t * TIME_FACTOR_WCS / RATEVALUE


        # In the Rotating Raference Frame (RRF)
        elif WCS_view == False:

            # WCS Hiding
            x_axis.visible = False
            label_x_axis.visible = False
            x_neg_axis.visible = False
            y_axis.visible = False
            label_y_axis.visible = False
            y_neg_axis.visible = False
            z_axis.visible = False
            label_z_axis.visible = False

            # RFF C.S. Visualization
            x_rff.visible = True
            label_x_rff.visible = True
            x_neg_rff.visible = True
            y_rff.visible = True
            label_y_rff.visible = True
            y_neg_rff.visible = True
            z_rff.visible = True
            label_z_rff.visible = True

            # Setting the behaviour of the Magnetization (M) in the RRF
            arrow_M.axis = vector(Mo * sin(w1_simulation * t) * sin(radians(slider_B1phase.value)),
                                  -Mo * sin(w1_simulation * t) * cos(radians(slider_B1phase.value)),
                                  Mo * cos(w1_simulation * t))

            # Setting the behaviour of the B1+ field in the RRF
            arrow_B1plus.axis = vector(arrow_B1plus.length * cos(radians(slider_B1phase.value)),
                                       arrow_B1plus.length * sin(radians(slider_B1phase.value)), 0)

            # Time scaling for the graph
            t_g = t * TIME_FACTOR_RRF / RATEVALUE

            # Curve
            if curve_path.npoints != 0:
                label_curve_path.visible = True
                data_label_curve_path_position = curve_path.point(int(len(phase_path_points) / 2))
                # print(data_label_curve_path_position)
                label_curve_path.pos = data_label_curve_path_position["pos"] * 1.4

        # Adjusting labels position
        label_B0.pos = vector(-5, 8, arrow_B0.length * 0.9)
        label_M.pos = vector(arrow_M.axis.x + 5, arrow_M.axis.y + 5, arrow_M.axis.z + 3)
        label_B1plus.pos = vector(arrow_B1plus.axis.x + 5, arrow_B1plus.axis.y + 5, arrow_B1plus.axis.z + 3)

        # Verification print statements
        # print('v0: ',v0,'     v0_sim: ',v0_simulation,'\nw0: ',w0,'     w0_sim: ',w0_simulation, '\nv1: ',v1,'     v1_sim: ',v1_simulation,'\nw1: ',w1,'     w1_sim: ',w1_simulation, '\B1: ', B1)
        # print('t: ', t, '    t_g: ', t_g)

        # Adjusting trail trayectory
        sphere_tip.pos = arrow_M.axis

        # Displaying the components of the magnetization
        Mx.plot(t_g, arrow_M.axis.x / Mo)
        My.plot(t_g, arrow_M.axis.y / Mo)
        Mz.plot(t_g, arrow_M.axis.z / Mo)

        # time iteration
        t = t + 1

