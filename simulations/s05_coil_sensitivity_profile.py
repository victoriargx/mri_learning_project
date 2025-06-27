"""
This program was originally developed for the MRI1 course at the Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU).
This version is maintained and documented by Victoria Rincon, with slight modifications for desktop use and minor fixes.

Title: Coil Sensitivity Profile
Authors: Victoria Rincon, Frederik Laun, FAU, University Hospital Erlangen
Original public release: : Summer 2024
Original version available at:
https://glowscript.org/#/user/Frederik.Laun/folder/LectureMRI1/program/Lecture5.CoilSensitivityProfile
License: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
https://creativecommons.org/licenses/by-sa/4.0/
"""

from vpython import *
# --- Web VPython (Glowscript) required version declaration ---
# Web VPython 3.2

# SCENE PARAMETERS
scene.background = color.white
scene.foreground = color.black
window_innerWidth = 1000
window_innerHeight = 800
scene.width = window_innerWidth * 0.6
scene.height = window_innerHeight * 0.7
scene.align = 'left'
scene.up = vector(0, 1, 0)  # Set up direction
scene.forward = vector(0, 0, -1)
scene.center = vector(-4.5, -0, 1.99839)
scene.range = 11
scene.userspin = False
scene.lights = []
scene.ambient = color.gray(0.8)

# FAU LOGO
FAU_logo_width = window_innerWidth * 0.35
FAU_logo_height = FAU_logo_width / 5
scene.caption = "  <img src='https://mod.fau.eu/wp-content/uploads/FAU-logo_940x182.jpg' width='{0}' height='{1}'> \n <b>MAGNETIC RESONANCE IMAGING I</b> \n\n".format(
    FAU_logo_width, FAU_logo_height)

# WORLD COORD. SYSTEM
# General Parameters
axis_length = 8
axis_thickness = axis_length / 55
axis_label_height = axis_length * 2
LABEL_HEIGHT = axis_length * 1.5
COLOR_AXIS = vector(0.9, 0.9, 0.99)
RESTRICTED_RADIUS = 5

# Axes
y_axis = arrow(pos=vector(0, 0, 0), axis=vector(0, 1, 0), length=axis_length, shaftwidth=axis_thickness, round=True,
               color=COLOR_AXIS, opacity=1, pickable=False)
label(pos=vector(0, y_axis.length, 0), xoffset=5, yoffset=5, height=axis_label_height, text='<b>y</b>', opacity=0,
      line=False, box=False, color=color.black)
y_neg_axis = cylinder(pos=vector(0, 0, 0), axis=vector(0, -1, 0), length=axis_length, radius=axis_thickness / 2,
                      color=COLOR_AXIS, opacity=1, pickable=False)

x_axis = arrow(pos=vector(0, 0, 0), axis=vector(1, 0, 0), length=RESTRICTED_RADIUS, shaftwidth=axis_thickness,
               round=True, color=COLOR_AXIS, opacity=1, pickable=False)
label(pos=vector(x_axis.length, 0, 0), xoffset=5, yoffset=5, height=axis_label_height, text='<b>x</b>', opacity=0,
      line=False, box=False, color=color.black)
x_neg_axis = cylinder(pos=vector(0, 0, 0), axis=vector(-1, 0, 0), length=2 * axis_length, radius=axis_thickness / 2,
                      color=COLOR_AXIS, opacity=1, pickable=False)

# FREQUENCY LABELS
wo = '0'
vo = '0'
label_wo = label(pos=vector(20, 20, 0), pixel_pos=True, height=LABEL_HEIGHT, line=False, box=False, opacity=0,
                 color=color.black, align='left', text='\u03C9<sub>0</sub> = ' + wo + ' rad/s')
label_vo = label(pos=vector(20, 20 + label_wo.height, 0), pixel_pos=True, height=LABEL_HEIGHT, line=False, box=False,
                 opacity=0, color=color.black, align='left', text='\u03BD<sub>0</sub> = ' + vo + ' Hz')
label(pos=vector(20, 20 + 2 * label_vo.height, 0), pixel_pos=True, height=LABEL_HEIGHT, line=False, box=False,
      opacity=0, color=color.black, align='left', text='<b>Real values:</b>')

# DIPOLE
# Spin
arrow_thickness = axis_thickness * 2
COLOR_Mo = vector(1, 0.781, 0.021)
arrow_dipole = arrow(pos=vec(0, -0, 0), axis=vec(1, 0, 0), length=axis_length * 0.15, shaftwidth=arrow_thickness * 0.5,
                     color=COLOR_Mo, round=True, visible=True)

# Field Lines over x-y plane
ring_thickness = arrow_thickness * 0.2
ring_basis_length = arrow_dipole.length / 3

ring_dipole_y_10 = ring(pos=arrow_dipole.pos + vec(arrow_dipole.length / 2, ring_basis_length / 2, 0),
                        axis=vec(0, 0, 1), size=vec(ring_thickness, ring_basis_length, ring_basis_length * 3),
                        color=color.green)
ring_dipole_y_11 = ring(pos=vec(ring_dipole_y_10.pos.x, ring_dipole_y_10.pos.y * 2, 0), axis=vec(0, 0, 1),
                        size=vec(ring_thickness, ring_dipole_y_10.size.y * 2, ring_dipole_y_10.size.z * 2),
                        color=color.green)
ring_dipole_y_20 = ring(pos=arrow_dipole.pos + vec(arrow_dipole.length / 2, -ring_basis_length / 2, 0),
                        axis=vec(0, 0, 1), size=vec(ring_thickness, ring_basis_length, ring_basis_length * 3),
                        color=color.green)
ring_dipole_y_21 = ring(pos=vec(ring_dipole_y_20.pos.x, ring_dipole_y_20.pos.y * 2, 0), axis=vec(0, 0, 1),
                        size=vec(ring_thickness, ring_dipole_y_20.size.y * 2, ring_dipole_y_20.size.z * 2),
                        color=color.green)

# Dipole Model integration
dipole_scale_factor = 0.7
sphere_dipole_center = sphere(pos=vector(arrow_dipole.pos.x + arrow_dipole.length / 2, arrow_dipole.pos.y, 0),
                              radius=1.5 * 0.05 / dipole_scale_factor, color=color.red)
dipole = compound(
    [arrow_dipole, ring_dipole_y_10, ring_dipole_y_11, ring_dipole_y_20, ring_dipole_y_21, sphere_dipole_center],
    visible=False)

# Dipole Model sizing
dipole.size = dipole.size * dipole_scale_factor

# COIL
coil = ring(pos=vec(0, 0, 0), axis=vec(1, 0, 0), radius=1, thickness=axis_thickness / 2, color=color.black,
            pickable=False)

# SURFACE VECTOR
COLOR_S = vec(0.2, 0.2, 0.2)
arrow_S = arrow(pos=vector(0, 0, 0), axis=vector(-1, 0, 0), length=x_neg_axis.length * 0.1,
                shaftwidth=x_neg_axis.radius * 3.2, round=True, color=COLOR_S, opacity=1, pickable=False)
label_S = label(pos=vector(-arrow_S.length, 0, 0), xoffset=2, yoffset=6, height=axis_label_height, text='<b>S</b>',
                opacity=0, line=False, box=False, color=COLOR_S)


# DIPOLE BOX CLASS
# Creates the frame containing the dipoles to grap and drag.
class DipoleBox:
    def __init__(self):
        self.center = vec(-x_neg_axis.length * 1.2, y_axis.length * 0.94, 0)
        self.icon = dipole.clone(pos=self.center, visible=True)
        self.frame = curve(pos=[vec(-self.icon.size.x, self.icon.size.y, 0), vec(self.icon.size.x, self.icon.size.y, 0),
                                vec(self.icon.size.x, -self.icon.size.y, 0),
                                vec(-self.icon.size.x, -self.icon.size.y, 0),
                                vec(-self.icon.size.x, self.icon.size.y, 0)], origin=self.icon.pos, color=color.black,
                           pickable=False)
        self.frame.size = self.frame.size * 0.7
        self.frame.radius = ring_thickness * 0.7
        self.inframe = box(pos=self.icon.pos,
                           size=vec(1.4 * self.icon.size.x, 1.4 * self.icon.size.y, self.frame.radius),
                           color=color.cyan, opacity=0.5, visible=False, pickable=False)

    def visible(self, vis):
        self.icon.visible = vis

    def inbox(self, point):
        # if point in self.inframe:
        if (self.inframe.pos.x - self.inframe.size.x / 2) <= point.x <= (
                self.inframe.pos.x + self.inframe.size.x / 2) and \
                (self.inframe.pos.y - self.inframe.size.y / 2) <= point.y <= (
                self.inframe.pos.y + self.inframe.size.y / 2) and \
                (self.inframe.pos.z - self.inframe.size.z / 2) <= point.z <= (
                self.inframe.pos.z + self.inframe.size.z / 2):
            return True
        else:
            return False


# CREATE DIPOLE LIST FUNCTION
dipole_list = []


def create_dipole_list(newpos):
    global dipole_list
    dipole_list.append(dipole.clone(pos=vector(newpos.x, newpos.y, 0)))


# 'mousedown' = mouse button pressed --> execute grap() function

# GRAB OBJECT (DIPOLE) FUNCTION
def grab(object):
    global drag, dragpos, pick
    if not play:
        m = scene.mouse
        p = m.pick

        if p in [PosBox.icon]:  # <------ Grap and drag dipole from the frame
            if p is PosBox.icon:
                PosBox.visible(False)

            create_dipole_list(m.pos)
            pick = dipole_list[-1]
            drag = GRABBED_OBJECT
            dragpos = vector(m.pos.x, m.pos.y, 0)

        elif p:  # <------ Grap and drag an existing dipole from the grid
            pick = p
            drag = GRABBED_OBJECT
            # dragpos = m.pos
            dragpos = vector(m.pos.x, m.pos.y, 0)

        # MOVE OBJECT (DIPOLE) FUNCTION


GRABBED_OBJECT = 1
scene.bind('mousedown', grab)


def move(object):
    global drag, dragpos, pick, RESTRICTED_RADIUS
    if not drag: return
    m = scene.mouse
    if m.pos == dragpos:
        return
    if pick:
        # pick.pos = vector(m.pos.x, m.pos.y, 0)

        # GRID RESTRICTION
        new_x = max(-21, min(m.pos.x, 5))
        # NOTE: -16 is the grid limit in the x-axis but we should be able to move the grabbed dipole to the frame to delete it.
        new_y = max(-8, min(m.pos.y, 8))

        # CIRCULAR RESTRICTION CLOSE TO ORIGIN
        if new_x ** 2 + new_y ** 2 <= RESTRICTED_RADIUS ** 2:
            angle = atan2(new_y, new_x)  # Calculate the angle with respect to the origin
            new_x = RESTRICTED_RADIUS * cos(angle)  # Adjust x to the circunference
            new_y = RESTRICTED_RADIUS * sin(angle)  # Adjust y to the circunference

        pick.pos = vector(new_x, new_y, 0)
    # dragpos = m.pos
    dragpos = vector(m.pos.x, m.pos.y, 0)  # <-------------------------------

scene.bind('mousemove', move)

# DROP OBJECT (DIPOLE) FUNCTION
def drop(object):
    global drag, dragpos, pick
    m = scene.mouse
    if drag == GRABBED_OBJECT:
        # if PosBox.inbox(m.pos): # dropped back into storage box
        if PosBox.inbox(pick.pos):  # dropped back into storage box
            dipole_list.remove(pick)
            pick.visible = False
            pick = None
        else:
            #  Adjust position to grid range
            pick.pos.x = max(-16, min(pick.pos.x, 5))
            pick.pos.y = max(-8, min(pick.pos.y, 8))

        if constrain:
            pick.pos = vector(round(pick.pos.x), round(pick.pos.y), round(pick.pos.z))
        drag = None
        PosBox.visible(True)

        pick = None  # dropped the source at a new location
        dragpos = None

scene.bind('mouseup', drop)

# CREATE DIPOLE LABELLING ON GRID FUNCTION
label_list = []  # for dipoles


def create_label_list():
    global dipole_list, label_list
    for i, obj in enumerate(dipole_list):
        label_list.append(
            label(pos=obj.pos, xoffset=2, yoffset=8, height=axis_label_height, text=f'<b>r<sub>{i}</sub></b>',
                  opacity=0, line=False, box=False, color=color.black))


# CALCULATION OF THE SENSITIVITY CONTRIBUTION FUNCTION AND CANVAS VISUALIZATION
# Title "Dipoles Position" in the canvas
label_positions = label(pos=vector(20, scene.height * 0.75, 0), pixel_pos=True, height=LABEL_HEIGHT, line=False,
                        box=False, opacity=0, color=color.black, align='left', text='<b>Dipoles Position:</b>',
                        visible=False)
# Title "Dipoles Sensitivity" in the canvas
label_sensitivities = label(pos=vector(scene.width * 0.76, scene.height * 0.75, 0), pixel_pos=True, height=LABEL_HEIGHT,
                            line=False, box=False, opacity=0, color=color.black, align='left',
                            text='<b>Dipoles Sensitivity:</b>', visible=False)

# Lists Initialization
r_list = []
c_list = []
label_r_list = []  # Canvas Label List Position (r)
label_c_list = []  # Canvas Label List Sensitivity
label_sensitivity_vector = []
sensivity_arrow_list = []


# Calculation of the Sensitivity contribution function
def calculate_sensitivity_contribution():
    global dipole_list, r_list, CONSTANT_PART, wo_simulation, sensitivity_all_contributions, label_r_list, label_c_list
    COLOR_SENSITIVITY_VECTOR = vec(0, 0.62, 0.9)

    if len(dipole_list) != 0:
        sensitivity_all_contributions = vec(0, 0, 0)
        step_labels = 20  # CONSTANT TO IMPLEMENT
        for i, obj in enumerate(dipole_list):
            x_r = round(obj.pos.x, 1)
            y_r = round(obj.pos.y, 1)

            r = sqrt(x_r ** 2 + y_r ** 2)
            sensitivity = (-CONSTANT_PART / r ** 5) * vector(3 * (x_r ** 2) - r ** 2, 3 * (x_r) * (y_r),
                                                             3 * (x_r) * (obj.pos.z))
            rounded_sensitivity = vec(round(sensitivity.x, 5), round(sensitivity.y, 5), round(sensitivity.z, 5))

            r_list.append(r)
            c_list.append(rounded_sensitivity)

            # print("sensitivity ",i,": ", sensitivity)
            # print(rounded_sensitivity)
            # print("|c",i,"|: ", sqrt(sensitivity.x**2+sensitivity.y**2+sensitivity.z**2))

            sensitivity_all_contributions = sensitivity_all_contributions + rounded_sensitivity

            label_r_list.append(
                label(pos=vector(label_positions.pos.x, label_positions.pos.y - 20 * (i + 1), 0), pixel_pos=True,
                      height=LABEL_HEIGHT, line=False, box=False, opacity=0, color=color.black, align='left',
                      text=f'<b>r<sub>{i}</sub></b> = ({x_r}, {y_r}, {obj.pos.z})<sup>T</sup>', visible=True))
            label_c_list.append(
                label(pos=vector(label_sensitivities.pos.x, label_sensitivities.pos.y - 20 * (i + 1), 0),
                      pixel_pos=True, height=LABEL_HEIGHT, line=False, box=False, opacity=0, color=color.black,
                      align='left',
                      text=f'<b>c<sub>{i}</sub></b> = ({rounded_sensitivity.x}, {rounded_sensitivity.y}, {rounded_sensitivity.z})<sup>T</sup>',
                      visible=True))

            # VECTOR VISUALIZATION
            A = 0.48139
            B = 151.6826
            magnitude = sqrt(sensitivity.x ** 2 + sensitivity.y ** 2)
            scale = exp(B * magnitude)
            scaled_sensitivity = vector(rounded_sensitivity.x * (scale / magnitude),
                                        rounded_sensitivity.y * (scale / magnitude), 0)
            # print("scaled_sensitivity: ", scaled_sensitivity)
            sensivity_arrow_list.append(arrow(pos=vector(x_r, y_r, obj.pos.z),
                                              axis=vector(scaled_sensitivity.x, scaled_sensitivity.y,
                                                          scaled_sensitivity.z), shaftwidth=axis_thickness, round=True,
                                              color=COLOR_SENSITIVITY_VECTOR, opacity=1, pickable=False))
            index_sensivity_arrow_list = len(sensivity_arrow_list) - 1
            if scaled_sensitivity.y < 0:
                yoffset_label_sensitivity_vector = -3
            else:
                yoffset_label_sensitivity_vector = 3
            label_sensitivity_vector.append(
                label(pos=obj.pos + scaled_sensitivity, xoffset=2, yoffset=yoffset_label_sensitivity_vector,
                      height=axis_label_height, text=f'<b>c(r<sub>{index_sensivity_arrow_list}</sub>)</b>', opacity=0,
                      line=False, box=False, color=COLOR_SENSITIVITY_VECTOR))
        # print("sensitivity_all_contributions", sensitivity_all_contributions)


# DELETE LABEL LIST TYPE FUNCTION
def delete_label_list_type(label_list_type):
    """
    # LISTS WITH LABEL OBJECTS THAT WE HAVE (Label list type):
    # 1. label_list --> r0, r1, etc. that accompany the dipoles on the grid
    # 2. label_r_list --> for the position vector of each dipole: r0, r1, etc., on the canvas
    # 3. label_c_list --> for the sensitivity vector of each dipole: c0, c1, c2, etc., on the canvas
    # 4. label_sensitivity_vector --> for the vector arrow of the sensitivity.
    """
    for lbl_object in label_list_type:
        lbl_object.visible = False
        lbl_object.text = ''
    label_list_type.clear()


# DELETE LABEL LIST TYPE FUNCTION
def delete_sensivity_arrow_list(arrow_list):
    for arrow_object in arrow_list:
        arrow_object.visible = False
    arrow_list.clear()


# SET CONSNTRAINT FUNCTION
constrain = False


def setconstrain(object):
    global constrain
    constrain = object.checked


# PLAY FUNCTION
play = False


def run_play(b):
    global play, label_list, label_r_list, label_c_list, r_list, c_list, t, t_g, sensivity_arrow_list
    play = not play
    if play:
        b.text = "Pause"
        create_label_list()
        calculate_sensitivity_contribution()
        label_positions.visible = True
        label_sensitivities.visible = True


    else:
        b.text = "Play"
        label_positions.visible = False  # Title
        label_sensitivities.visible = False  # Title
        delete_label_list_type(label_list)
        delete_label_list_type(label_r_list)
        delete_label_list_type(label_c_list)
        delete_label_list_type(label_sensitivity_vector)
        r_list.clear()
        c_list.clear()
        delete_sensivity_arrow_list(sensivity_arrow_list)
        t = 0
        t_g = 0
        mflux_graph.delete()
        emf_graph.delete()


# GRID CLASS
class Grid:
    def __init__(self):
        global RESTRICTED_RADIUS
        self.grid_points = []
        #print(f"-x_neg_axis.length = {int(-x_neg_axis.length)}")
        #print(f"-x_neg_axis.length = {y_axis.length + 1}")
        for x in range(int(-x_neg_axis.length), int(x_axis.length + 1)):
            for y in range(int(-y_neg_axis.length), int(y_axis.length + 1)):
                # self.grid_points.append(sphere(pos=vector(x,y,0), radius=0.05, color=color.black, pickable=False))
                if x ** 2 + y ** 2 <= RESTRICTED_RADIUS ** 2:
                    self.grid_points.append(
                        sphere(pos=vector(x, y, 0), radius=0.05, color=color.white, pickable=False, visible=False))
                else:
                    self.grid_points.append(sphere(pos=vector(x, y, 0), radius=0.05, color=color.black, pickable=False))

    def visible(self, vis):
        for s in self.grid_points:
            s.visible = vis


# PLAY BUTTON
button(text="Play", pos=scene.title_anchor, bind=run_play)

# PROGRAM DESCRIPTION
scene.append_to_caption('  <b>COIL SENSITIVITY PROFILE \n')
scene.append_to_caption('''
   This simulation exemplifies the derived coil sensitivity profile 
   <b>c(r)</b> from <i>Example 2: "small coil far away from point source"</i>,
   showcasing the relationship between magnetic flux \u03A6(t) and
   induced electromotive force (emf).

   The Coil sensitivity profile <b>c(r)</b> describes how well the coil 
   can capture signals at position <b>r</b>=(x, y, z).
   The spatial dependency of the coil’s sensitivity is defined 
   indirectly via the following equation of the magnetic flux:
        \u03A6(t) = \u222B d<b>r</b><sup>3</sup> \u00B7 <b>c(r)</b> \u00B7 <b>M(r,t)</b> 

   Therefore, <b>c(r)</b> is described as:''')
scene.append_to_caption('''
        <b>c<sub></sub>(r)</b> &asymp; - (&mu;<sub>0</sub>S/4&pi;r<sub></sub><sup>5</sup>)  \u00B7 (3x<sub></sub><sup>2</sup>-r<sub0</sub><sup>2</sup>, 3x<sub></sub>y<sub></sub>, 3x<sub></sub>z<sub></sub>)<sup>T</sup>''')
scene.append_to_caption('''   
        Where: 
            \u00B7 &mu;<sub>0</sub>: Vacuum Permeability
            \u00B7 S: Number of windings of the core \n\n''')
scene.append_to_caption('''   Such that <b>c(r)</b> drops cubically with distance <b>r</b>. \n''')
scene.append_to_caption('''   
   Additionally, Faraday's law of induction further connects \u03A6(t) 
   to the induced electromotive force (emf) in the coil. 
   According to Faraday's law: 
        emf = d\u03A6(t) / dt\n\n''')
scene.append_to_caption('''      
   <b>Simulation Interaction:</b>
   Before running the simulation (using the play button), place
   some dipoles on the grid. You can drag and drop the dipoles 
   from the black frame to the grid, and delete them by 
   dragging them back to the frame. Additionally, below you 
   can modify the strength of the main magnetic field (B<sub>0</sub>).\n\n\n''')


# |Bo| SELECTION FUNCTION
def set_Bo(s):
    reset_animation()
    wt_Bo.text = '{:1.1f}'.format(s.value)


# |Bo| SLIDER
scene.append_to_caption('    Strength of the main magnetic field:\n')
scene.append_to_caption('      B<sub>0</sub>: ')

slider_Bo = slider(min=0.1, max=3, value=3, length=220, bind=set_Bo, right=15)
wt_Bo = wtext(text='{:1.1f}'.format(slider_Bo.value))

scene.append_to_caption('T\n\n')

# SCALE FACTOR DESCRIPTION
# scene.append_to_caption('\n')
scene.append_to_caption('''      
    <b>Scale factor</b>:
    1 second (s) in the simulation corresponds to approximately 
    7.8 nanoseconds (ns) in real life.\n 
    In other words, while one rotation is completed in 1 s of 
    the simulation, approximately 127,728,049 rotations are 
    completed in real life within the same 1 second duration 
    (B<sub>0</sub> = 3 T).\n\n\n''')

# GRAPHS
graph_1 = graph(width=scene.width / 2, height=scene.width / 6, fast=False, title='<b>Magnetic Flux \u03A6(t)</b>',
                xtitle='Time (ns)', ymin=-0.1, ymax=0.1, scroll=True, xmin=0, xmax=300, align='left')
mflux_graph = gcurve(color=color.blue, label='<i>\u03A6(t)</i>', graph=graph_1)
graph_2 = graph(width=scene.width / 2, height=scene.width / 6, fast=False, title='<b>Electromotive Force (emf)</b>',
                xtitle='Time (ns)', ymin=-10000000, ymax=10000000, scroll=True, xmin=0, xmax=300, align='left')
emf_graph = gcurve(color=color.red, label='<i>emf</i>', graph=graph_2)


# RESET FUNCTION
def reset_animation():
    global t
    t = 0


# SCENE CREATION
# Creating the Grid
Grid()
# Creating Dipole Frame/Box
PosBox = DipoleBox()

# VARIABLES INITIALIZATION
drag = None
dragpos = None
pick = None

sensitivity_all_contributions = vec(0, 0, 0)
Mo = 1

# ANIMATION PARAMETERS
RATEVALUE = 30  # Frames per second

SCALE_FACTOR = 3831841466
TIME_FACTOR = 7.829
FORMAT_FACTOR = 1E6

# PHYSICS/WORLD CONSTANTS
GAMMA_PROTONS = 2.67513E8
VACUUM_PERMEABILITY = 4 * pi * 1E-7
COIL_SURFACE = 1E7

# CONSTANT_PART= (VACUUM_PERMEABILITY * COIL_SURFACE)/(4*pi)
CONSTANT_PART = 1  # For simplification

# TIME INITIALIZATION
t = 0
t_g = 0

# ITERATION OVER TIME
while True:

    rate(RATEVALUE)  # Limit the animation to run at a maximum of 'rate_value' frames per second
    if play:

        # Frequencies calculation
        Bo = slider_Bo.value
        wo = GAMMA_PROTONS * Bo
        vo = wo / (2 * pi)

        wo_simulation = wo / SCALE_FACTOR
        vo_simulation = wo_simulation / (2 * pi)

        # Formatting the variables
        wo_formatted = "{:.1f}".format(wo)
        vo_formatted = "{:.3f}".format(vo / FORMAT_FACTOR)

        # Displaying frequencies on the screen
        label_wo.text = '\u03C9<sub>0</sub> = ' + wo_formatted + ' rad/s'
        label_vo.text = '\u03BD<sub>0</sub> = ' + vo_formatted + ' MHz'

        # Rotation of the Dipoles
        if len(dipole_list) != 0:
            for i, obj in enumerate(dipole_list):
                obj.axis = vector(dipole.size.x * cos(wo_simulation * t), dipole.size.y * sin(wo_simulation * t), 0)

        # Definition of the magnetization vector (Dipole Spin)
        Magnetization_vector = Mo * vector(cos(wo_simulation * t), sin(wo_simulation * t), 0)

        # Calculation of the Magnetic Flux
        magnetic_flux = dot(Magnetization_vector, sensitivity_all_contributions)
        # print("magnetic_flux: ", magnetic_flux)
        mflux_graph.plot(t_g, magnetic_flux)

        # Calculation of the Electromotive Force
        emf = -Mo * dot(vector(-sin(wo_simulation * t) * wo, cos(wo_simulation * t) * wo, 0),
                        sensitivity_all_contributions)
        emf_graph.plot(t_g, emf)

        # Time scaling for the graphs
        t_g = t * TIME_FACTOR / RATEVALUE

        # time iteration
        t = t + 1
