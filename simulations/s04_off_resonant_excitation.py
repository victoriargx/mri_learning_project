"""
This program was originally developed for the MRI1 course at the Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU).
This version is maintained and documented by Victoria Rincon, with slight modifications for desktop.

Title: Off-Resonant Excitation
Authors: Victoria Rincon, Frederik Laun, FAU, University Hospital Erlangen
Original public release: : September 2023
Original version available at:
https://glowscript.org/#/user/Frederik.Laun/folder/LectureMRI1/program/Lecture4.Off-Resonant-Excitation
License: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
https://creativecommons.org/licenses/by-sa/4.0/
"""

from vpython import *
# --- Web VPython (Glowscript) required version declaration ---
# Web VPython 3.2

# SCENE PARAMETERS
scene.background = color.white
window_innerWidth = 1000
window_innerHeight = 800
scene.width = window_innerWidth * 0.6
scene.height = window_innerHeight * 0.9
scene.align = 'left'
scene.up = vector(0, 0, 1)
scene.forward = vector(-1, 0, 0)
scene.right = vector(0, -1, 0)
scene.lights = []
scene.ambient = color.gray(0.8)


# INITIAL CAMERA SETTINGS FUNCTION
def initial_camera_settings():
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
axis_headwidth = 2 * axis_thickness
axis_headlength = 3 * axis_thickness
axis_label_height = axis_length * 0.45

# WORLD C.S.
COLOR_AXIS = vector(0.9, 0.9, 0.99)

x_axis = arrow(pos=vector(0, 0, 0), axis=vector(1, 0, 0), length=axis_length, shaftwidth=axis_thickness,
               headwidth=axis_headwidth, headlength=axis_headlength, round=True, color=COLOR_AXIS, opacity=1)
label_x_axis = label(pos=vector(axis_length + axis_length * 0.05, 0.5, 0), height=axis_label_height, text='<b>x</b>',
                     opacity=0, box=False, color=color.black)
x_neg_axis = cylinder(pos=vector(0, 0, 0), axis=vector(-1, 0, 0), length=axis_length, radius=axis_thickness / 2,
                      color=COLOR_AXIS, opacity=1)

y_axis = arrow(pos=vector(0, 0, 0), axis=vector(0, 1, 0), length=axis_length, shaftwidth=axis_thickness,
               headwidth=axis_headwidth, headlength=axis_headlength, round=True, color=COLOR_AXIS, opacity=1)
label_y_axis = label(pos=vector(0.5, axis_length + axis_length * 0.05, 0), height=axis_label_height, text='<b>y</b>',
                     opacity=0, box=False, color=color.black)
y_neg_axis = cylinder(pos=vector(0, 0, 0), axis=vector(0, -1, 0), length=axis_length, radius=axis_thickness / 2,
                      color=COLOR_AXIS, opacity=1)

z_axis = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 1), length=axis_length, shaftwidth=axis_thickness,
               headwidth=axis_headwidth, headlength=axis_headlength, round=True, color=COLOR_AXIS, opacity=1)
label_z_axis = label(pos=vector(0, 0.5, axis_length + axis_length * 0.05), height=axis_label_height, text='<b>z</b>',
                     opacity=0, box=False, color=color.black)
# z_neg_axis = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, -1), length=axis_lenght,shaftwidth=axis_thickness, round=True, color=COLOR_AXIS, opacity=1)


# RFF C.S.
rff_length = axis_length
COLOR_RFF = vector(0.5, 0.5, 0.59)

x_rff = arrow(pos=vector(0, 0, 0), axis=vector(1, 0, 0), length=axis_length, shaftwidth=axis_thickness,
              headwidth=axis_headwidth, headlength=axis_headlength, round=True, color=COLOR_RFF, opacity=1,
              visible=False)
label_x_rff = label(pos=vector(axis_length + axis_length * 0.05, 0.5, 0), height=axis_label_height, text='<b>x\'</b>',
                    opacity=0, box=False, color=color.black, visible=False)
x_neg_rff = cylinder(pos=vector(0, 0, 0), axis=vector(-1, 0, 0), length=axis_length, radius=1, color=COLOR_RFF,
                     opacity=1, visible=False)

y_rff = arrow(pos=vector(0, 0, 0), axis=vector(0, 1, 0), length=axis_length, shaftwidth=axis_thickness,
              headwidth=axis_headwidth, headlength=axis_headlength, round=True, color=COLOR_RFF, opacity=1,
              visible=False)
label_y_rff = label(pos=vector(0.5, axis_length + axis_length * 0.05, 0), height=axis_label_height, text='<b>y\'</b>',
                    opacity=0, box=False, color=color.black, visible=False)
y_neg_rff = cylinder(pos=vector(0, 0, 0), axis=vector(0, -1, 0), length=axis_length, radius=1, color=COLOR_RFF,
                     opacity=1, visible=False)

z_rff = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 1), length=rff_length, shaftwidth=axis_thickness,
              headwidth=axis_headwidth, headlength=axis_headlength, round=True, color=COLOR_RFF, opacity=1,
              visible=False)
label_z_rff = label(pos=vector(-1, -0.5, z_rff.length * 0.95), height=axis_label_height, text='<b>z\'</b>', opacity=0,
                    box=False, color=color.black, visible=False)
# z_neg_axis = cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, -1), length=axis_length, radius=1, color=COLOR_RFF, opacity=1)


# MAIN MAGNETIC FIELD (B0)
arrow_length = axis_length * 0.9
arrow_thickness = axis_thickness * 1.4

COLOR_B0 = vector(0, 0.5, 1)
COLOR_LABEL_B0 = vector(0, 0.35, 0.69)

arrow_B0 = arrow(visible=True, pos=vector(0, 0, 0), axis=vector(0, 0, arrow_length), shaftwidth=arrow_thickness,
                 headwidth=axis_headwidth, headlength=axis_headlength, round=True, color=COLOR_B0)
label_B0 = label(visible=True, pos=vector(-5, 8, arrow_length * 0.9), height=axis_label_height,
                 text='<b>B<sub>0</sub></b>', opacity=0, box=False, color=COLOR_LABEL_B0)

# B1+ Field
COLOR_B1plus = vector(0.1, 0.6, 0.1)
arrow_B1plus = arrow(pos=vector(0, 0, 0), axis=vector(arrow_length * 0.75, 0, 0), shaftwidth=arrow_thickness,
                     headwidth=axis_headwidth, headlength=axis_headlength, round=True, color=COLOR_B1plus)
label_B1plus = label(pos=vector(arrow_B1plus.axis.x + 5, arrow_B1plus.axis.y + 5, arrow_B1plus.axis.z + 6),
                     height=axis_label_height, text='<b>B<sub>1</sub><sup>+</sup></b>', opacity=0, box=False,
                     color=COLOR_B1plus)

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
scene.append_to_caption('  <b> OFF-RESONANT EXCITATION</b>\n')
scene.append_to_caption('''
   by Victoria Rincon and Frederik Laun\n
   This simulation exemplifies the precession of
   the magnetization vector (<b>M</b>) with  <b>B</b><sub>eff</sub>(t) =  <b>B</b>(t)
   - <b>\u03A9</b>/\u0263 in the World Coordinate System (WCS)
   and the Rotating Reference Frame (RRF), in
   the Off-resonant case \u03C9<sub>HF</sub> \u2260 \u03C9<sub>0</sub> = \u03A9 .\n''')

scene.append_to_caption('''      
   Below, you can choose to visualize the excitation 
   process in either the World Coordinate System or 
   the Rotating Reference Frame. You can modify 
   the strength of the main magnetic field (<b>B</b><sub>0</sub>) and 
   the strength of the <b>B</b><sub>1</sub><sup>+</sup> field. Additionally, you can 
   activate or deactivate the x-y view of the scene.\n''')

# |B0| BUTTON SELECTION
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


# |B1+| BUTTON SELECTION
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


# OFF-RESONANCE BUTTON SELECTION
off_resonance_bs = 10E-6  # ppm


def set_off_resonance(r):
    global off_resonance_bs
    reset_animation()
    if r.checked:
        if r.ppm == -5:
            off_resonance_bs = -5E-6
        elif r.ppm == 1:
            off_resonance_bs = 1E-6
        elif r.ppm == 10:
            off_resonance_bs = 10E-6


# PHYSICS CONSTANT
GAMMA_PROTONS = 2.67513E8

# Z COMPONENT OF THE EFFECTIVE FIELD
COLOR_Zc_Beff = vector(0.4, 0.8, 1)
COLOR_LABEL_Zc_Beff = vector(0.4, 0.8, 1)

wHF = (1 + off_resonance_bs) * (GAMMA_PROTONS * B0_bs)
strength_Zc_Beff = abs(B0_bs - wHF / GAMMA_PROTONS)

arrow_Zc_Beff = arrow(visible=False, pos=vector(0, 0, 0),
                      axis=vector(0, 0, round(strength_Zc_Beff / B1_bs, 2) * arrow_B1plus.length),
                      shaftwidth=arrow_thickness, headwidth=axis_headwidth, headlength=axis_headlength, round=True,
                      color=COLOR_Zc_Beff)
label_Zc_Beff = label(visible=False, pos=vector(-10, 20, arrow_Zc_Beff.length * 0.9), height=axis_label_height * 0.8,
                      text='<b>B<sub>0</sub> - \u03C9<sub>HF</sub>/\u03B3</b>', opacity=0, box=False,
                      color=COLOR_LABEL_Zc_Beff)

# Verification print statements
# print(wHF/GAMMA_PROTONS)
# print(strength_Zc_Beff)


# EFFECTIVE FIELD (Beff)
COLOR_Beff = vector(0, 0.7, 1)
COLOR_LABEL_Beff = vector(0, 0.7, 1)

arrow_Beff = arrow(visible=False, pos=vector(0, 0, 0), axis=vector(arrow_B1plus.axis.x, 0, arrow_Zc_Beff.axis.z),
                   shaftwidth=arrow_thickness, headwidth=axis_headwidth, headlength=axis_headlength, round=True,
                   color=COLOR_Beff)
label_Beff = label(visible=False, pos=vector(-5, 8, arrow_length * 0.9), height=axis_label_height * 0.8,
                   text='<b>B<sub>eff</sub></b>', opacity=0, box=False, color=COLOR_LABEL_Beff)

# MAGNETIZATION (M)
Mo = arrow_length * 0.7
COLOR_Mo = vector(1, 0.781, 0.021)

arrow_M = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 1), length=Mo, shaftwidth=arrow_thickness,
                headwidth=axis_headwidth, headlength=axis_headlength, round=True, color=COLOR_Mo, make_trail=False)
label_M = label(pos=vector(-5, 8, arrow_M.length * 0.9), height=axis_label_height, text='<b>M</b>', opacity=0,
                box=False, color=COLOR_Mo)

# MAGNETIZATION TRAIL
COLOR_TRAIL = vector(1, 0.8, 0.4)

sphere_tip = sphere(pos=arrow_M.axis, radius=arrow_thickness * 0.15, make_trail=True, trail_type="points", interval=0.2,
                    retain=320, color=COLOR_TRAIL, opacity=1)
sphere_tip.trail_radius = sphere_tip.radius

# COORDINATE SYSTEM SELECTION FUNCTIONS
WCS_view = True


def change_to_WSC():
    button_WCS.background = color.green
    button_RRF.background = color.white
    global WCS_view, Mo
    Mo = arrow_length * 0.7
    WCS_view = True
    arrow_B0.visible = True
    label_B0.visible = True
    arrow_Beff.visible = False
    label_Beff.visible = False
    arrow_Zc_Beff.visible = False
    label_Zc_Beff.visible = False
    initial_camera_settings()
    gp.xtitle = 'Time (ns)'
    reset_animation()


def change_to_FFR():
    button_WCS.background = color.white
    button_RRF.background = color.green
    global WCS_view
    WCS_view = False
    arrow_B0.visible = False
    label_B0.visible = False
    arrow_Beff.visible = True
    label_Beff.visible = True
    arrow_Zc_Beff.visible = True
    label_Zc_Beff.visible = True
    # Camera settings for the RRF
    scene.range = 226.26338
    scene.camera.pos = vector(-0.753934, 305.516, 87.3495)
    scene.camera.axis = vector(-0.311108, -391.194, 23.4999)
    gp.xtitle = 'Time (ms)'
    reset_animation()


# COORDINATE SYSTEM SELECTION BUTTONS
scene.append_to_caption('    World Coordinate System:      ')
button_WCS = button(text='WCS', bind=change_to_WSC, background=color.green)

scene.append_to_caption('<p style="color:red">      In the WCS, <b>M</b> has a minor error in its behavior.</p>')

scene.append_to_caption('\n    Rotating Reference Frame:      ')
button_RRF = button(text='RRF', bind=change_to_FFR)

# |B0| SELECTION BUTTONS
scene.append_to_caption('\n\n    Strength of the main magnetic field:\n')
scene.append_to_caption('      B<sub>0</sub>: ')

scene.append_to_caption('      ')
radio_B0_05 = radio(strength=0.5, bind=set_strength_B0, checked=False, name='strength_B0')
scene.append_to_caption('0.5 T')

scene.append_to_caption('      ')
radio__B0_1 = radio(strength=1.5, bind=set_strength_B0, checked=False, name='strength_B0')
scene.append_to_caption('1.5 T')

scene.append_to_caption('      ')
radio__B0_3 = radio(strength=3, bind=set_strength_B0, checked=True, name='strength_B0')
scene.append_to_caption('3 T\n\n')

# |B1+| SELECTION BUTTONS
scene.append_to_caption('    Strength of the  <b>B</b><sub>1</sub><sup>+</sup> field:\n')
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

# OFF-RESONANCE SELECTION BUTTONS
scene.append_to_caption('    Off-resonance:\n')
scene.append_to_caption('      ')

scene.append_to_caption('      ')
radio_offresonance_minus1 = radio(ppm=-5, bind=set_off_resonance, checked=False, name='off_resonance')
scene.append_to_caption('-5 ppm')

scene.append_to_caption('      ')
radio_offresonance_1 = radio(ppm=1, bind=set_off_resonance, checked=False, name='off_resonance')
scene.append_to_caption('1 ppm')

scene.append_to_caption('      ')
radio_offresonance_10 = radio(ppm=10, bind=set_off_resonance, checked=True, name='off_resonance')
scene.append_to_caption('10 ppm\n\n')

# ANGLE LABEL
theta = '0'
label_theta = label(pos=vector(20, 20, 0), pixel_pos=True, height=axis_label_height * 0.75, line=False, box=False,
                    opacity=0, color=color.black, align='left', text='\u03B8 = ' + theta + '°')
label(pos=vector(20, 20 + 2 * label_theta.height, 0), pixel_pos=True, height=axis_label_height * 0.65, line=False,
      box=False, opacity=0, color=color.black, align='left',
      text='<b>Angle between e\'<sub>z</sub> and B<sub>eff</sub>:</b>')


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

SCALE_FACTOR_w0 = 3.8E9
SCALE_FACTOR_w1 = 159660.6579

TIME_FACTOR_WCS = 26.097  # units ns<---------
TIME_FACTOR_RRF = 0.6263  # units ms  <---------

FORMAT_FACTOR = 1000000

# VARIABLES INITIALIZATION
arrow_Zc_Beff_max_length = arrow_Zc_Beff.length

t = 0
t_g = 0

# ITERATION OVER TIME
while True:

    rate(RATEVALUE)
    if play:

        # Frequencies calculation
        B0 = B0_bs
        w0 = GAMMA_PROTONS * B0
        v0 = w0 / (2 * pi)
        w0_simulation = (w0 / SCALE_FACTOR_w0)
        v0_simulation = w0_simulation / (2 * pi)

        off_resonance = off_resonance_bs
        wHF = (1 + off_resonance) * w0
        wHF_simulation = off_resonance * w0_simulation

        B1 = B1_bs
        w1 = GAMMA_PROTONS * B1
        v1 = w1 / (2 * pi)
        w1_simulation = (w1 / SCALE_FACTOR_w1)
        v1_simulation = w1_simulation / (2 * pi)

        delta_wHF = w0 - wHF
        weff = sqrt(pow(abs(delta_wHF), 2) + pow(w1, 2))

        # Formatting the variables to display on the screen
        v0_formatted = "{:.3f}".format(v0 / FORMAT_FACTOR)
        w0_formatted = "{:.1f}".format(w0 / FORMAT_FACTOR)

        # Adjusting B1+ and B0 vectors length according to the selected strength
        arrow_B0.length = (B0_bs / 3) * arrow_length
        arrow_B1plus.length = (B1_bs / 5E-6) * (arrow_length * 0.75)

        # Adjusting z-component of the effective field
        strength_Zc_Beff = abs(delta_wHF) / GAMMA_PROTONS
        arrow_Zc_Beff.length = round((strength_Zc_Beff / B1_bs) * arrow_B1plus.length, 2)

        # Adjusting Theta
        theta = acos(abs(delta_wHF) / weff)
        theta_degrees = "{:.2f}".format(degrees(theta))
        label_theta.text = '\u03B8 = ' + theta_degrees + '°'

        # Verification print statement
        # print('wHF: ', wHF, '\nRadians: ',theta,'Degrees:', degrees(theta))

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
            arrow_M.axis = vector(-Mo * sin(w0_simulation * t) * sin(w1_simulation * t),
                                  Mo * cos(w0_simulation * t) * sin(w1_simulation * t), Mo * cos(w1_simulation * t))

            # Setting the behaviour of the B1+ field in the WCS
            arrow_B1plus.axis = vector(arrow_B1plus.length * cos(wHF_simulation * t),
                                       arrow_B1plus.length * sin(wHF_simulation * t), 0)
            label_B1plus.height = axis_label_height
            label_B1plus.pos = vector(arrow_B1plus.axis.x + 5, arrow_B1plus.axis.y + 5, arrow_B1plus.axis.z + 6)

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

            z_rff.length = arrow_Zc_Beff.length + arrow_Zc_Beff.length * 0.1
            label_z_rff.pos = vector(z_rff.axis.x, z_rff.axis.y, z_rff.axis.z + 6)

            # Setting the behaviour of the B1+ field in the RRF
            arrow_B1plus.axis = vector(arrow_B1plus.length, 0, 0)
            label_B1plus.height = axis_label_height * 0.8
            label_B1plus.pos = vector(arrow_B1plus.axis.x + 5, arrow_B1plus.axis.y + 5, arrow_B1plus.axis.z + 6)

            arrow_Beff.axis = vector(arrow_B1plus.axis.x, 0, arrow_B1plus.length / tan(theta))
            label_Beff.pos = vector(arrow_Beff.axis.x + 8, arrow_Beff.axis.y + 5, arrow_Beff.axis.z + 8)

            arrow_Zc_Beff.axis = vector(0, 0, arrow_Zc_Beff.length)
            label_Zc_Beff.pos = vector(-10, 30, arrow_Zc_Beff.length * 0.9)

            MX = cos(w0_simulation * t) * sin(theta)
            MY = sin(w0_simulation * t) * sin(theta)
            MZ = cos(theta)

            Mo = arrow_Beff.length * 0.7
            arrow_M.axis = Mo * vector(MX * cos(theta) + MZ * sin(theta), sin(w0_simulation * t) * sin(theta),
                                       -MX * sin(theta) + MZ * cos(theta))

            # Time scaling for the graph
            t_g = t * TIME_FACTOR_RRF / RATEVALUE

        # Adjusting labels position
        label_B0.pos = vector(-5, 8, arrow_B0.length * 0.9)
        label_M.pos = vector(arrow_M.axis.x + 5, arrow_M.axis.y + 5, arrow_M.axis.z + 3)

        # Verification print statements
        # print('v0: ',v0,'     v0_sim: ',v0_simulation,'\nw0: ',w0,'     w0_sim: ',w0_simulation, '\nv1: ',v1,'     v1_sim: ',v1_simulation,'\nw1: ',w1,'     w1_sim: ',w1_simulation, '\B1: ', B1)
        # print('Beff_zc: ',arrow_B1plus.length/tan(theta), '   arrow_Zc_Beff_length: ',arrow_Zc_Beff.length)

        # Adjusting trail trayectory
        sphere_tip.pos = arrow_M.axis

        # Displaying the components of the magnetization
        Mx.plot(t_g, arrow_M.axis.x / Mo)
        My.plot(t_g, arrow_M.axis.y / Mo)
        Mz.plot(t_g, arrow_M.axis.z / Mo)

        # time iteration
        t = t + 1

