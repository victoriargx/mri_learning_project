"""
This program was originally developed for the MRI1 course at the Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU).
This version is maintained and documented by Victoria Rincon, with slight modifications for desktop.

Title: The ideal Gradient Field
Authors: Victoria Rincon, Frederik Laun, FAU, University Hospital Erlangen
Original public release: : Summer 2024
Original version available at:
https://glowscript.org/#/user/Frederik.Laun/folder/LectureMRI1/program/Lecture07.Gradients
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
scene.width = window_innerWidth * 0.5
scene.height = window_innerHeight * 1.52

scene.align = 'left'
scene.up = vector(0, 1, 0)  # Set up direction
scene.forward = vector(1, 0, 0)
# scene.center = vector(-4.5, -0, 1.99839)
# scene.range = 11
scene.userspin = False  # Default Y-Z view
scene.lights = []
scene.ambient = color.gray(0.8)
scene.resizable = False

# FAU LOGO
FAU_logo_width = window_innerWidth * 0.39
FAU_logo_height = FAU_logo_width / 5
scene.caption = " <img src='https://mod.fau.eu/wp-content/uploads/FAU-logo_940x182.jpg' width='{0}' height='{1}'> \n <b>MAGNETIC RESONANCE IMAGING I</b> \n\n".format(
    FAU_logo_width, FAU_logo_height)

# WORLD COORD. SYSTEM
# General Parameters
axis_length = 6
axis_thickness = axis_length / 75
axis_label_height = axis_length * 3
LABEL_HEIGHT = axis_length * 1.2
COLOR_AXIS = vector(0.9, 0.9, 0.99)

# Axes
x_axis = arrow(pos=vector(0, 0, 0), axis=vector(1, 0, 0), shaftwidth=axis_thickness, length=axis_length, round=True,
               color=COLOR_AXIS, opacity=1, pickable=False)
label(pos=vector(x_axis.length, 0, 0), xoffset=5, yoffset=5, height=axis_label_height, text='<b>x</b>', opacity=0,
      line=False, box=False, color=color.black)
x_neg_axis = cylinder(pos=vector(0, 0, 0), axis=vector(-1, 0, 0), length=axis_length, radius=axis_thickness / 2,
                      color=COLOR_AXIS, opacity=1, pickable=False)

y_axis = arrow(pos=vector(0, 0, 0), axis=vector(0, 1, 0), length=axis_length, shaftwidth=axis_thickness, round=True,
               color=COLOR_AXIS, opacity=1, pickable=False)
label(pos=vector(0, y_axis.length, 0), xoffset=5, yoffset=5, height=axis_label_height, text='<b>y</b>', opacity=0,
      line=False, box=False, color=color.black)
y_neg_axis = cylinder(pos=vector(0, 0, 0), axis=vector(0, -1, 0), length=axis_length, radius=axis_thickness / 2,
                      color=COLOR_AXIS, opacity=1, pickable=False)

z_axis = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 1), length=1.5 * axis_length, shaftwidth=axis_thickness,
               round=True, color=COLOR_AXIS, opacity=1)
label_z_axis = label(pos=vector(0, 0, z_axis.length), xoffset=5, yoffset=5, height=axis_label_height, text='<b>z</b>',
                     opacity=0, line=False, box=False, color=color.black)
z_neg_axis = cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, -1), length=1.5 * axis_length, radius=axis_thickness / 2,
                      color=COLOR_AXIS, opacity=1, pickable=False)

# SCANNER REPRESENTATION
scanner_length = 16
cylinder_scanner = cylinder(pos=vec(0, 0, -scanner_length / 2), opacity=0.25, axis=vec(0, 0, scanner_length),
                            radius=axis_length * 0.8, color=color.white)

# Conventions (Default settings)
COLOR_LABEL_GRADIENTS = vector(0, 0.7, 1)
COLOR_ISOLINES = color.black
label_gradient_field = label(pos=vector(0, axis_length * 1.6, axis_length * 1.6), pixel_pos=False,
                             height=axis_label_height, line=False, box=False, opacity=0, color=COLOR_LABEL_GRADIENTS,
                             align='right', text='<b>B</b><sub>G,ideal</sub>(<b>r</b>)')
label_isolines = label(pos=label_gradient_field.pos - vector(0, 1.5, 0), pixel_pos=False, height=axis_label_height,
                       line=False, box=False, opacity=0, color=COLOR_ISOLINES, align='right', text='Iso-lines')
arrow_label_gradient = arrow(pos=label_gradient_field.pos - vector(0, 0, 4), axis=vector(0, 0, -1),
                             color=COLOR_LABEL_GRADIENTS, round=True)
cylinder_label_isolines = cylinder(pos=label_isolines.pos - vector(0, 0, 4), axis=vector(0, 0, -1), radius=0.05,
                                   color=COLOR_ISOLINES)


# DELETE GRADIENT OBJECTS
def delete_objects(object_list_item):
    for value_element in object_list_item:
        value_element.visible = False
    object_list_item.clear()


# SET GRADIENTS <------------------------------------------------------------------------------------------------------
# Dictonaries to store gradient information
gradients_object_dict = {'x': None, 'y': None, 'z': None}  # dictionary
gradients_length_dict = {'x': [0, 0, 0, 0, 0], 'y': [0, 0, 0, 0, 0], 'z': [0, 0, 0, 0, 0]}  # dictionary

# Gradient features
arrows_thickness = axis_thickness * 1.4
sphere_radio = 0.075
COLOR_SENSITIVITY_VECTOR = vec(0, 0.62, 0.9)
COLOR_GRADIENTS = vector(0, 0.7, 1)

# Lists to store the gradient objects that represent the gradient field in XZ, YZ and XY planes
gradients_xzPlane_list = []
gradients_yzPlane_list = []
gradients_xyPlane_list = []

# Lists to store isolines per Plane
isolines_xzPlane_list = []
isolines_yzPlane_list = []
isolines_xyPlane_list = []

# List to store the gradient objects that represent the gradient field in the volumne
gradients_volume_list = []

current_gradient = None

# Coordinates in each axis where gradients are displayed
coord_x = list(range(-4, 5, 2))  # e.g. coord_x: [-4, -2, 0, 2, 4]
coord_y = list(range(-4, 5, 2))
coord_z = list(range(-8, 9, 4))  # e.g. coord_y: [-8, -4, 0, 4, 8]


# Sliders Function
def set_sliders(s):
    global gradients_object_dict, gradients_length_dict, current_gradient
    global gradients_xyPlane_list, gradients_xzPlane_list, gradients_yzPlane_list
    global coord_x, coord_y, coord_z

    # Need it for Set plots
    current_gradient = s.gradient

    # Cleaning "gradients_object_dict[s.gradient]":
    # If there is already a value for the "s.gradient" key, it is deleted it,
    # Most likely because a new gradient value (Gx, Gy or Gz) was selected using the sliders.
    if gradients_object_dict[s.gradient] is not None:
        delete_objects(gradients_object_dict[s.gradient])

    # CONDITIONALS TO SET THE POSITION OF THE "MAIN" GRADIENT ("arrow_01") IN EACH AXIS
    # For "Gz":
    if s.gradient == 'z':
        wtext_Gz.text = '{:1.1f}'.format(s.value)
        z_i = 4
        y_i = 0
        x_i = 0

    # For "Gy":
    elif s.gradient == 'y':
        wtext_Gy.text = '{:1.1f}'.format(s.value)
        z_i = 0
        y_i = 2
        x_i = 0

    # For "Gx":
    elif s.gradient == 'x':
        wtext_Gx.text = '{:1.1f}'.format(s.value)
        z_i = 0
        y_i = 0
        x_i = 2

    else:
        print('CONDITION NOT INCLUDED')

    # 3D objects that represent the gradients over the "s.gradient" axis
    arrow_01 = arrow(pos=vector(x_i, y_i, z_i), axis=vector(0, 0, 1) * s.value / s.max, shaftwidth=arrows_thickness,
                     round=True, color=COLOR_GRADIENTS, opacity=1, pickable=False, visible=False)
    arrow_02 = arrow(pos=arrow_01.pos * 2, axis=arrow_01.axis * 2, shaftwidth=arrows_thickness, round=True,
                     color=COLOR_GRADIENTS, opacity=1, pickable=False, visible=False)
    arrow_neg01 = arrow(pos=arrow_01.pos * -1, axis=arrow_01.axis * -1, shaftwidth=arrows_thickness, round=True,
                        color=COLOR_GRADIENTS, opacity=1, pickable=False, visible=False)
    arrow_neg02 = arrow(pos=arrow_01.pos * -2, axis=arrow_01.axis * -2, shaftwidth=arrows_thickness, round=True,
                        color=COLOR_GRADIENTS, opacity=1, pickable=False, visible=False)
    sphere_center = sphere(pos=vector(0, 0, 0), radius=sphere_radio, color=COLOR_GRADIENTS, pickable=False)

    # Assigning an array with the gradient objects for the corresponding axes to the "s.gradient" key
    gradients_object_dict[s.gradient] = [arrow_neg02, arrow_neg01, sphere_center, arrow_01, arrow_02]

    # Assigning an array with the length of the gradient objects to "gradients_length_dict[s.gradient]"
    dict_vector = [-arrow_neg02.length, -arrow_neg01.length, 0, arrow_01.length, arrow_02.length]
    s_value_sign = sign(s.value)
    gradients_length_dict[s.gradient] = [dict_element * s_value_sign for dict_element in dict_vector]
    # e.g.  GX = 40 mT/m then s.value = 40/ s.gradient = 'x' / gradients_length_dict['x'] = [-2, -1, 0, 1, 2]

    # CONDITIONALS FOR SELECTING PLOT VISUALIZATION MODE (AXIS, PLANE OR VOLUME)
    # For "Axis":<----------------------
    if radio_axis.checked == True:
        # Calling Functon
        set_plot_axis(radio_axis, from_plot=False)

    # For "Plane":<----------------------
    elif radio_plane.checked == True:
        # Cleaning gradient plane lists:
        if gradients_xyPlane_list != []:
            delete_objects(gradients_xyPlane_list)
        if gradients_xzPlane_list != []:
            delete_objects(gradients_xzPlane_list)
        if gradients_yzPlane_list != []:
            delete_objects(gradients_yzPlane_list)

        # Cleaning isolines lists per plane:
        if isolines_xyPlane_list != []:
            delete_objects(isolines_xyPlane_list)
        if isolines_xzPlane_list != []:
            delete_objects(isolines_xzPlane_list)
        if isolines_yzPlane_list != []:
            delete_objects(isolines_yzPlane_list)

        # Calling Functon
        set_plot_plane(radio_plane)

    # For Volume: <----------------------
    elif radio_volume.checked == True:
        if gradients_volume_list != []:
            delete_objects(gradients_volume_list)

        # Calling Functon
        set_plot_volume(radio_volume)


# PROGRAM DESCRIPTION
scene.append_to_caption('  <b>THE IDEAL LINEAR GRADIENT FIELD \n')
scene.append_to_caption('''
    This simulation exemplifies an ideal gradient field that points along 
    the z-direction: 

        <b>B</b><sub>G,ideal</sub>(<b>r</b>) = (<b>G</b>\u00B7<b>r</b>) <b>e</b><sub>z</sub>

    Where: 
            <b>G</b> = (G<sub>x</sub>, G<sub>y</sub>, G<sub>z</sub>)<sup>T</sup> 
            <b>r</b> = (x, y, z)<sup>T</sup> 
    So:
        <b>B</b><sub>G,ideal</sub>(<b>r</b>)= (0, 0, G<sub>x</sub>\u00B7x + G<sub>y</sub>\u00B7y + G<sub>z</sub>\u00B7z)<sup>T</sup> 

    The gradient field (depicted by the arrows) creates a linear variation 
    in the magnetic field across space:

        <b>B</b>(r) = (B<sub>o</sub> + <b>G</b>\u00B7<b>r</b>) <b>e</b><sub>z</sub>

    This variation adds a spatial dependence to the magnetic field, 
    which in turn makes the Larmor angular frequency (the rate at which
    magnetization precess in the magnetic field) vary with position. 
    This means that the magnetization at different locations has different 
    Larmor angular frequencies.

        \u03C9(<b>r</b>) = \u03B3\u00B7B(<b>r</b>) = \u03B3\u00B7 (B<sub>o</sub> + <b>G</b>\u00B7<b>r</b>)\n''')

scene.append_to_caption('''      
   <b>Simulation Interaction:</b>
    Below, you can adjust the strength of the gradient field. You can choose
    to view the gradients along an axis, in a plane, or throughout the entire 
    scanner. In plane mode, you can also enable the option to display 
    iso-lines. Additionally, you can switch the camera view between different 
    planes or use a free view mode to rotate the scene.
    \n''')

# GRADIENTS
scene.append_to_caption('    Strength of the gradients:\n')
scene.append_to_caption('      ')
# checkbox_Gx = checkbox(gradient='x', bind=set_gradient_scene, checked=False, text='gradient_x')

scene.append_to_caption('G<sub>x</sub>:')
slider_Gx = slider(gradient='x', min=-40, max=40, value=0, length=220, bind=set_sliders, right=15, step=10,
                   disabled=False, text='0')
wtext_Gx = wtext(text=slider_Gx.value)
scene.append_to_caption('mT/m \n\n')

scene.append_to_caption('      ')
# checkbox_Gy = checkbox(gradient='y', bind=set_gradient_scene, checked=False, text='gradient_y\n')
scene.append_to_caption('G<sub>y</sub>:')
slider_Gy = slider(gradient='y', min=-40, max=40, value=0, length=220, bind=set_sliders, right=15, step=10,
                   disabled=False, text='0')
wtext_Gy = wtext(text=slider_Gy.value)
scene.append_to_caption('mT/m \n\n')

scene.append_to_caption('      ')
# checkbox_Gz = checkbox(gradient='z', bind=set_gradient_scene, checked=False, text='gradient_z\n\n')
scene.append_to_caption('G<sub>z</sub>:')
slider_Gz = slider(gradient='z', min=-40, max=40, value=0, length=220, bind=set_sliders, right=15, step=10,
                   disabled=False, text='0')
wtext_Gz = wtext(text=slider_Gz.value)
scene.append_to_caption('mT/m \n\n')


# SET PLOTS <---------------------------------------------------------------------------------------------------------
def set_plot_axis(r, from_plot=True):
    global gradients_object_dict, current_gradient
    global gradients_xyPlane_list, gradients_xzPlane_list, gradients_yzPlane_list
    global gradients_volume_list

    # Deactivating and Disabling Iso-lines button
    button_isolines.activated = False
    button_isolines.background = color.white
    button_isolines.disabled = True

    # Cleaning gradient plane lists:
    if gradients_xyPlane_list != []:
        delete_objects(gradients_xyPlane_list)
    if gradients_xzPlane_list != []:
        delete_objects(gradients_xzPlane_list)
    if gradients_yzPlane_list != []:
        delete_objects(gradients_yzPlane_list)
    if gradients_volume_list != []:
        delete_objects(gradients_volume_list)

    # Cleaning isolines lists per plane:
    if isolines_xyPlane_list != []:
        delete_objects(isolines_xyPlane_list)
    if isolines_xzPlane_list != []:
        delete_objects(isolines_xzPlane_list)
    if isolines_yzPlane_list != []:
        delete_objects(isolines_yzPlane_list)

    if from_plot is True:
        for key in gradients_object_dict:
            if gradients_object_dict[key] is None:
                pass
            else:
                for element in gradients_object_dict[key]:
                    element.visible = True
    else:
        for element in gradients_object_dict[current_gradient]:
            element.visible = True


def set_plot_plane(r):
    global gradients_volume_list, gradients_length_dict, coord_x, coord_y, coord_z
    global gradients_xyPlane_list, gradients_xzPlane_list, gradients_yzPlane_list
    global isolines_xyPlane_list, isolines_xzPlane_list, isolines_yzPlane_list

    if gradients_volume_list != []:
        delete_objects(gradients_volume_list)

    # Enabling Iso-lines button
    button_isolines.disabled = False

    # CONDITIONALS BASED ON CURRENT SLIDERS CONFIGURATION
    # For "Gx": OFF, "Gy": OFF and "Gz": OFF
    if (gradients_length_dict['x'] == [0, 0, 0, 0, 0]) and (gradients_length_dict['y'] == [0, 0, 0, 0, 0]) and (
            gradients_length_dict['z'] == [0, 0, 0, 0, 0]):
        pass

    # For "Gx": ON, "Gy": ON and "Gz": OFF  --> Plane X-Y
    elif (gradients_length_dict['x'] != [0, 0, 0, 0, 0]) and (gradients_length_dict['y'] != [0, 0, 0, 0, 0]) and (
            gradients_length_dict['z'] == [0, 0, 0, 0, 0]):
        matrix_arrow_values = []
        positions_dict = {}
        for idx, x in enumerate(coord_x):
            row = []
            for idy, y in enumerate(coord_y):
                if (x, y) in [(-4, -4), (4, 4), (-4, 4), (4, -4)]:
                    continue
                else:
                    object_opacity = 1

                    arrow_value = gradients_length_dict['x'][idx] + gradients_length_dict['y'][idy]
                    row.append(arrow_value)
                    if arrow_value == 0:
                        gradients_xyPlane_list.append(
                            sphere(pos=vector(x, y, 0), radius=sphere_radio, color=COLOR_GRADIENTS,
                                   opacity=object_opacity, pickable=False))
                    else:
                        gradients_xyPlane_list.append(
                            arrow(pos=vector(x, y, 0), axis=vector(0, 0, 1), length=arrow_value,
                                  shaftwidth=arrows_thickness, round=True, color=COLOR_GRADIENTS,
                                  opacity=object_opacity, pickable=False))

                    # Needed for Iso-lines: "positions_dict"
                    # Adding new gradient object lenght as key to "positions_dict"
                    if arrow_value not in positions_dict:
                        positions_dict[arrow_value] = []

                    # Filling "positions_dict" dictionary
                    positions_dict[arrow_value].append(
                        vector(x, y, 0))  # e.g. 1.5:[vector(-4, -2, 0), vector(-2, -4, 0)]

                # Validation Matrix
                matrix_arrow_values.append(row)

            # Validation Matrix Adjusted
            transposed_matrix = [[row[i] for row in matrix_arrow_values] for i in range(len(matrix_arrow_values[0]))]
            adjusted_matrix = transposed_matrix[::-1]

            '''
            print('positions_dict: \n', positions_dict)
            print('adjusted_matrix: \n', adjusted_matrix)
            '''

            # Calling function for Iso-lines generation
            # Plane X-Y
            horizontal_axis = 'y'
            vertical_axis = 'x'
            generate_isolines(positions_dict, horizontal_axis, vertical_axis, isolines_xyPlane_list)

            # Conditional to display isolines when sliders are changed and "button_isolines" is activated
            if button_isolines.activated == True:
                # Showing isolines objects per plane:
                if isolines_xyPlane_list != []:
                    for value_element in isolines_xyPlane_list:
                        value_element.visible = True
                if isolines_xzPlane_list != []:
                    for value_element in isolines_xzPlane_list:
                        value_element.visible = True
                if isolines_yzPlane_list != []:
                    for value_element in isolines_yzPlane_list:
                        value_element.visible = True

    # For "Gx": OFF, "Gy": ON and "Gz": ON --> Plane Y-Z
    elif (gradients_length_dict['x'] == [0, 0, 0, 0, 0]) and (
            (gradients_length_dict['y'] != [0, 0, 0, 0, 0]) or (gradients_length_dict['z'] != [0, 0, 0, 0, 0])):
        matrix_arrow_values = []  ################### maybe up once, inside current function
        positions_dict = {}  ################### maybe up once
        for idz, z in enumerate(coord_z):
            row = []
            for idy, y in enumerate(coord_y):
                arrow_value = gradients_length_dict['y'][idy] + gradients_length_dict['z'][idz]
                # print('Value', arrow_value)
                if arrow_value == 0:
                    gradients_yzPlane_list.append(
                        sphere(pos=vector(0, y, z), radius=sphere_radio, color=COLOR_GRADIENTS, pickable=False))
                else:
                    gradients_yzPlane_list.append(
                        arrow(pos=vector(0, y, z), axis=vector(0, 0, 1), length=arrow_value,
                              shaftwidth=arrows_thickness, round=True, color=COLOR_GRADIENTS, opacity=1,
                              pickable=False))

                # Needed for Iso-lines: "positions_dict"
                # Adding new gradient object lenght as key to "positions_dict"
                if arrow_value not in positions_dict:
                    positions_dict[arrow_value] = []

                # Filling "positions_dict" dictionary
                positions_dict[arrow_value].append(
                    vector(0, y, z))  # e.g. 1.5:[vector(-4, -2, 0), vector(-2, -4, 0)]

                # Validation Matrix
            matrix_arrow_values.append(row)

        # Validation Matrix Adjusted
        transposed_matrix = [[row[i] for row in matrix_arrow_values] for i in
                             range(len(matrix_arrow_values[0]))]
        adjusted_matrix = transposed_matrix[::-1]
        '''
        print('positions_dict: \n', positions_dict)
        print('adjusted_matrix: \n', adjusted_matrix)
        '''

        # Calling function for Iso-lines generation
        # Plane Y-Z
        horizontal_axis = 'z'
        vertical_axis = 'y'
        generate_isolines(positions_dict, horizontal_axis, vertical_axis, isolines_yzPlane_list)

        # Conditional to display isolines when sliders are changed and "button_isolines" is activated
        if button_isolines.activated == True:
            # Showing isolines objects per plane:
            if isolines_xyPlane_list != []:
                for value_element in isolines_xyPlane_list:
                    value_element.visible = True
            if isolines_xzPlane_list != []:
                for value_element in isolines_xzPlane_list:
                    value_element.visible = True
            if isolines_yzPlane_list != []:
                for value_element in isolines_yzPlane_list:
                    value_element.visible = True

    # For "Gx": ON, "Gy": ON and "Gz": ON
    elif (gradients_length_dict['x'] != [0, 0, 0, 0, 0]) and (gradients_length_dict['y'] != [0, 0, 0, 0, 0]) and (
            gradients_length_dict['z'] != [0, 0, 0, 0, 0]):

        # disabling Iso-lines button
        button_isolines.disabled = True

        for idz, z in enumerate(coord_z):
            for idx, x in enumerate(coord_x):
                if z == 0 or x == 0:
                    object_opacity = 1
                else:
                    object_opacity = 0.2

                arrow_value = gradients_length_dict['x'][idx] + gradients_length_dict['z'][idz]
                if arrow_value == 0:
                    gradients_xzPlane_list.append(
                        sphere(pos=vector(x, 0, z), radius=sphere_radio, color=COLOR_GRADIENTS, opacity=object_opacity,
                               pickable=False))
                else:
                    gradients_xzPlane_list.append(
                        arrow(pos=vector(x, 0, z), axis=vector(0, 0, 1), length=arrow_value,
                              shaftwidth=arrows_thickness, round=True, color=COLOR_GRADIENTS, opacity=object_opacity,
                              pickable=False))

            for idy, y in enumerate(coord_y):
                if z == 0 or y == 0:
                    object_opacity = 1
                else:
                    object_opacity = 0.2
                arrow_value = gradients_length_dict['y'][idy] + gradients_length_dict['z'][idz]
                if arrow_value == 0:
                    gradients_yzPlane_list.append(
                        sphere(pos=vector(0, y, z), radius=sphere_radio, color=COLOR_GRADIENTS, opacity=object_opacity,
                               pickable=False))
                else:
                    gradients_yzPlane_list.append(
                        arrow(pos=vector(0, y, z), axis=vector(0, 0, 1), length=arrow_value,
                              shaftwidth=arrows_thickness, round=True, color=COLOR_GRADIENTS, opacity=object_opacity,
                              pickable=False))

        for idx, x in enumerate(coord_x):
            for idy, y in enumerate(coord_y):
                if (x, y) in [(-4, -4), (4, 4), (-4, 4), (4, -4)]:
                    continue
                else:
                    if x == 0 or y == 0:
                        object_opacity = 1
                    else:
                        object_opacity = 0.2

                    arrow_value = gradients_length_dict['x'][idx] + gradients_length_dict['y'][idy]
                    if arrow_value == 0:
                        gradients_xyPlane_list.append(
                            sphere(pos=vector(x, y, 0), radius=sphere_radio, color=COLOR_GRADIENTS,
                                   opacity=object_opacity, pickable=False))
                    else:
                        gradients_xyPlane_list.append(
                            arrow(pos=vector(x, y, 0), axis=vector(0, 0, 1), length=arrow_value,
                                  shaftwidth=arrows_thickness, round=True, color=COLOR_GRADIENTS,
                                  opacity=object_opacity,
                                  pickable=False))

    # For "Gx": ON and implicitly "Gy": OFF and "Gz": OFF or ON --> Plane X-Z
    elif (gradients_length_dict['x'] != [0, 0, 0, 0, 0]):
        matrix_arrow_values = []
        positions_dict = {}
        # positions_dict.keys() -->  List of current gradient object lengths
        # positions_dict.values() --> positions where one can find those gradient objects with those lengths

        # Loop to position gradient objects in the XZ plane
        for idz, z in enumerate(coord_z):
            row = []
            for idx, x in enumerate(coord_x):
                arrow_value = gradients_length_dict['x'][idx] + gradients_length_dict['z'][idz]
                row.append(arrow_value)
                if arrow_value == 0:
                    gradients_xzPlane_list.append(
                        sphere(pos=vector(x, 0, z), radius=sphere_radio, color=COLOR_GRADIENTS, pickable=False))
                else:
                    gradients_xzPlane_list.append(
                        arrow(pos=vector(x, 0, z), axis=vector(0, 0, 1), length=arrow_value,
                              shaftwidth=arrows_thickness, round=True, color=COLOR_GRADIENTS, opacity=1,
                              pickable=False))

                # Needed for Iso-lines:
                # Adding new gradient object lenght as key to "positions_dict"
                if arrow_value not in positions_dict:
                    positions_dict[arrow_value] = []

                # Filling "positions_dict" dictionary
                positions_dict[arrow_value].append(
                    vector(x, 0, z))  # e.g. -1.5: [vector(-2, 0, -8), vector(-4, 0, 8)]

            # Validation Matrix
            matrix_arrow_values.append(row)

        # Validation Matrix Adjusted
        transposed_matrix = [[row[i] for row in matrix_arrow_values] for i in range(len(matrix_arrow_values[0]))]
        adjusted_matrix = transposed_matrix[::-1]
        '''
        print('positions_dict: \n', positions_dict)
        print('adjusted_matrix: \n', adjusted_matrix)
        '''

        # Calling function for Iso-lines generation
        # Plane X-Z
        horizontal_axis = 'z'
        vertical_axis = 'x'
        generate_isolines(positions_dict, horizontal_axis, vertical_axis, isolines_xzPlane_list)

        # Conditional to display isolines when sliders are changed and "button_isolines" is activated
        if button_isolines.activated == True:
            # Showing isolines objects per plane:
            if isolines_xyPlane_list != []:
                for value_element in isolines_xyPlane_list:
                    value_element.visible = True
            if isolines_xzPlane_list != []:
                for value_element in isolines_xzPlane_list:
                    value_element.visible = True
            if isolines_yzPlane_list != []:
                for value_element in isolines_yzPlane_list:
                    value_element.visible = True


    # In case no all posible slider configurations were covered
    else:
        print("CONDITION NOT INCLUDED/SLIDERS FUNCTION/PLANE")


def set_plot_volume(r):
    global gradients_volume_list, gradients_length_dict, coord_x, coord_y, coord_z
    global gradients_xyPlane_list, gradients_xzPlane_list, gradients_yzPlane_list

    # Deactivating and Disabling Iso-lines button
    button_isolines.activated = False
    button_isolines.background = color.white
    button_isolines.disabled = True

    # Cleaning gradient plane lists:
    if gradients_xyPlane_list != []:
        delete_objects(gradients_xyPlane_list)
    if gradients_xzPlane_list != []:
        delete_objects(gradients_xzPlane_list)
    if gradients_yzPlane_list != []:
        delete_objects(gradients_yzPlane_list)

    # Cleaning isolines lists per plane:
    if isolines_xyPlane_list != []:
        delete_objects(isolines_xyPlane_list)
    if isolines_xzPlane_list != []:
        delete_objects(isolines_xzPlane_list)
    if isolines_yzPlane_list != []:
        delete_objects(isolines_yzPlane_list)

    for idz, z in enumerate(coord_z):
        for idy, y in enumerate(coord_y):
            for idx, x in enumerate(coord_x):
                if (x, y) in [(-4, -4), (4, 4), (-4, 4), (4, -4)]:
                    continue
                else:
                    if (x == 0 and y == 0) or (x == 0 and z == 0) or (y == 0 and z == 0):
                        object_opacity = 1
                    else:
                        object_opacity = 0.2

                    arrow_value = gradients_length_dict['x'][idx] + gradients_length_dict['y'][idy] + \
                                  gradients_length_dict['z'][idz]
                    if arrow_value == 0:
                        gradients_volume_list.append(
                            sphere(pos=vector(x, y, z), radius=0.11, color=COLOR_GRADIENTS, opacity=object_opacity,
                                   pickable=False))
                    else:
                        gradients_volume_list.append(
                            arrow(pos=vector(x, y, z), axis=vector(0, 0, 1), length=arrow_value,
                                  shaftwidth=arrows_thickness, round=True, color=COLOR_GRADIENTS,
                                  opacity=object_opacity, pickable=False))


def generate_isolines(positions_dict, horizontal_axis, vertical_axis, isolines_plane_list):
    # Setting Horizontal lower and upper bounds
    if horizontal_axis == 'y':
        horizontal_lower_bound = coord_y[0]  # e.g. -4
        horizontal_upper_bound = coord_y[-1]  # e.g. 4
    elif horizontal_axis == 'z':
        horizontal_lower_bound = coord_z[0]  # e.g. -8
        horizontal_upper_bound = coord_z[-1]  # # e.g. 8

    vertical_lower_bound = coord_y[0]  # or =coord_x[0] (both are the same)
    vertical_upper_bound = coord_y[-1]

    initial_pos = vector(0, 0, 0)
    final_pos = vector(0, 0, 0)

    # Loop for Iso-Lines Generation
    for a_value, positions in positions_dict.items():
        # Evaluating if each "a_value" (i.e. object_lenght) is at least twice to draw the iso-line

        if len(positions) > 1:
            # Validation
            # print(a_value, 'positions: ', positions)

            # Conditionals according to the position of the initial and final position of that "a_value"
            # Case 1: where the initial and final position are at the scaner limits.
            # if positions[0].z == -8 and positions[-1].z == 8:
            if (getattr(positions[0], horizontal_axis) == horizontal_lower_bound and getattr(positions[-1],
                                                                                             horizontal_axis) == horizontal_upper_bound) or (
                    getattr(positions[0], vertical_axis) == vertical_lower_bound and getattr(positions[-1],
                                                                                             vertical_axis) == vertical_upper_bound):
                isolines_plane_list.append(
                    cylinder(pos=positions[0], axis=positions[-1] - positions[0], radius=0.05, color=COLOR_ISOLINES,
                             visible=False))

            # Case 2: where the initial position is NOT at the scaner limits but the final position is.
            # elif positions[0].z != -8 and positions[-1].z == 8:
            elif getattr(positions[0], horizontal_axis) != horizontal_lower_bound and getattr(positions[-1],
                                                                                              horizontal_axis) == horizontal_upper_bound:
                slope = (getattr(positions[-1], vertical_axis) - getattr(positions[0], vertical_axis)) / (
                        getattr(positions[-1], horizontal_axis) - getattr(positions[0], horizontal_axis))
                b = getattr(positions[0], vertical_axis) - slope * getattr(positions[0], horizontal_axis)
                initial_vertical = slope * horizontal_lower_bound + b

                if initial_vertical > 0 and initial_vertical >= vertical_upper_bound:
                    initial_horizontal = (vertical_upper_bound - b) / slope
                    # initial_pos = vector(vertical_upper_bound, 0, initial_z) ###########
                    setattr(initial_pos, horizontal_axis, initial_horizontal)
                    setattr(initial_pos, vertical_axis, vertical_upper_bound)

                elif initial_vertical < 0 and initial_vertical <= vertical_lower_bound:
                    initial_horizontal = (vertical_lower_bound - b) / slope
                    # initial_pos = vector(vertical_lower_bound, 0, initial_z)  ###########
                    setattr(initial_pos, horizontal_axis, initial_horizontal)
                    setattr(initial_pos, vertical_axis, vertical_lower_bound)

                else:
                    # initial_pos = vector(initial_x, 0, -8) ##########
                    setattr(initial_pos, horizontal_axis, horizontal_lower_bound)
                    setattr(initial_pos, vertical_axis, initial_vertical)

                isolines_plane_list.append(
                    cylinder(pos=initial_pos, axis=positions[-1] - initial_pos, radius=0.05, color=COLOR_ISOLINES,
                             visible=False))

            # Case 3: where the initial position is at the scaner limits but the final position is NOT.
            # elif positions[0].z == -8 and positions[-1].z != 8:
            elif getattr(positions[0], horizontal_axis) == horizontal_lower_bound and getattr(positions[-1],
                                                                                              horizontal_axis) != horizontal_upper_bound:

                slope = (getattr(positions[-1], vertical_axis) - getattr(positions[0], vertical_axis)) / (
                        getattr(positions[-1], horizontal_axis) - getattr(positions[0], horizontal_axis))
                b = getattr(positions[0], vertical_axis) - slope * getattr(positions[0], horizontal_axis)
                final_vertical = slope * horizontal_upper_bound + b

                if final_vertical < 0 and final_vertical <= vertical_lower_bound:
                    final_horizontal = (vertical_lower_bound - b) / slope
                    # final_pos = vector(vertical_lower_bound, 0, final_horizontal)
                    setattr(final_pos, horizontal_axis, final_horizontal)
                    setattr(final_pos, vertical_axis, vertical_lower_bound)

                elif final_vertical > 0 and final_vertical >= vertical_upper_bound:
                    final_horizontal = (vertical_upper_bound - b) / slope
                    # final_pos = vector(vertical_upper_bound, 0, final_horizontal)
                    setattr(final_pos, horizontal_axis, final_horizontal)
                    setattr(final_pos, vertical_axis, vertical_upper_bound)

                else:
                    # final_pos = vector(final_vertical, 0, 8)
                    setattr(final_pos, horizontal_axis, horizontal_upper_bound)
                    setattr(final_pos, vertical_axis, final_vertical)

                isolines_plane_list.append(
                    cylinder(pos=positions[0], axis=final_pos - positions[0], radius=0.05, color=COLOR_ISOLINES,
                             visible=False))

            # Case 4: where the initial and final position are NOT at the scaner limits.
            else:
                slope = (getattr(positions[-1], vertical_axis) - getattr(positions[0], vertical_axis)) / (
                        getattr(positions[-1], horizontal_axis) - getattr(positions[0], horizontal_axis))
                b = getattr(positions[0], vertical_axis) - slope * getattr(positions[0], horizontal_axis)
                initial_vertical = slope * horizontal_lower_bound + b
                final_vertical = slope * horizontal_upper_bound + b
                # initial_x = slope * -8 + b
                # final_x = slope * 8 + b

                if initial_vertical > 0 and initial_vertical >= vertical_upper_bound:
                    initial_horizontal = (vertical_upper_bound - b) / slope
                    # initial_pos = vector(vertical_upper_bound, 0, initial_z)
                    setattr(initial_pos, horizontal_axis, initial_horizontal)
                    setattr(initial_pos, vertical_axis, vertical_upper_bound)

                elif initial_vertical < 0 and initial_vertical <= vertical_lower_bound:
                    initial_horizontal = (vertical_lower_bound - b) / slope
                    # initial_pos = vector(vertical_lower_bound, 0, initial_z)
                    setattr(initial_pos, horizontal_axis, initial_horizontal)
                    setattr(initial_pos, vertical_axis, vertical_lower_bound)

                else:
                    # initial_pos = vector(initial_x, 0, -8)
                    setattr(initial_pos, horizontal_axis, horizontal_lower_bound)
                    setattr(initial_pos, vertical_axis, initial_vertical)

                if final_vertical < 0 and final_vertical <= vertical_lower_bound:
                    final_horizontal = (vertical_lower_bound - b) / slope
                    # final_pos = vector(vertical_lower_bound, 0, final_horizontal)
                    setattr(final_pos, horizontal_axis, final_horizontal)
                    setattr(final_pos, vertical_axis, vertical_lower_bound)

                elif final_vertical > 0 and final_vertical >= vertical_upper_bound:
                    final_horizontal = (vertical_upper_bound - b) / slope
                    # final_pos = vector(vertical_upper_bound, 0, final_horizontal)
                    setattr(final_pos, horizontal_axis, final_horizontal)
                    setattr(final_pos, vertical_axis, vertical_upper_bound)

                else:
                    # final_pos = vector(final_vertical, 0, 8)
                    setattr(final_pos, horizontal_axis, horizontal_upper_bound)
                    setattr(final_pos, vertical_axis, final_vertical)

                isolines_plane_list.append(
                    cylinder(pos=initial_pos, axis=final_pos - initial_pos, radius=0.05, color=COLOR_ISOLINES,
                             visible=False))


def visualize_isolines():
    global isolines_xyPlane_list, isolines_xzPlane_list, isolines_yzPlane_list

    # If I press the button and it was on --> Turn off
    if button_isolines.activated:
        # Changing Button parameters
        button_isolines.background = color.white
        button_isolines.activated = False

        # Hidding isolines objects per plane:
        if isolines_xyPlane_list != []:
            for value_element in isolines_xyPlane_list:
                value_element.visible = False
        if isolines_xzPlane_list != []:
            for value_element in isolines_xzPlane_list:
                value_element.visible = False
        if isolines_yzPlane_list != []:
            for value_element in isolines_yzPlane_list:
                value_element.visible = False

    # If I press the button and it was off --> Turn on
    else:
        # Changing Button parameters
        button_isolines.background = color.green
        button_isolines.activated = True

        # Showing isolines objects per plane:
        if isolines_xyPlane_list != []:
            for value_element in isolines_xyPlane_list:
                value_element.visible = True
        if isolines_xzPlane_list != []:
            for value_element in isolines_xzPlane_list:
                value_element.visible = True
        if isolines_yzPlane_list != []:
            for value_element in isolines_yzPlane_list:
                value_element.visible = True


# PLOT in:
scene.append_to_caption('    Plot in:\n')
scene.append_to_caption('      ')
radio_axis = radio(bind=set_plot_axis, text='Axis', checked=True, name='plot', from_plot=True)

scene.append_to_caption('\n      ')
radio_plane = radio(bind=set_plot_plane, text='Plane', checked=False, name='plot')

scene.append_to_caption('      ')
button_isolines = button(bind=visualize_isolines, text='Show Iso-lines', background=color.white, disabled=True,
                         activated=False)

scene.append_to_caption('\n      ')
radio_volume = radio(bind=set_plot_volume, text='Volume', checked=False, name='plot')


# VIEWS FUNCTION
def set_views(r):
    if r.text == 'Y-Z':
        scene.up = vector(0, 1, 0)  # Set up direction
        scene.forward = vector(1, 0, 0)
        scene.userspin = False
        label_gradient_field.pos = vector(0, axis_length * 1.6, axis_length * 1.6)
        label_isolines.pos = label_gradient_field.pos - vector(0, 1.5, 0)
        arrow_label_gradient.pos = label_gradient_field.pos - vector(0, 0, 4)
        cylinder_label_isolines.pos = label_isolines.pos - vector(0, 0, 4)
        arrow_label_gradient.axis = vector(0, 0, -1)
        cylinder_label_isolines.axis = vector(0, 0, -1)

    elif r.text == 'X-Z':
        scene.up = vector(1, 0, 0)  # Set up direction
        scene.forward = vector(0, -1, 0)
        scene.userspin = False
        label_gradient_field.pos = vector(axis_length * 1.6, 0, axis_length * 1.6)
        label_isolines.pos = label_gradient_field.pos - vector(1.5, 0, 0)
        arrow_label_gradient.pos = label_gradient_field.pos - vector(0, 0, 4)
        cylinder_label_isolines.pos = label_isolines.pos - vector(0, 0, 4)
        arrow_label_gradient.axis = vector(0, 0, -1)
        cylinder_label_isolines.axis = vector(0, 0, -1)

    elif r.text == 'X-Y':
        scene.up = vector(1, 0, 0)  # Set up direction
        scene.forward = vector(0, 0, 1)
        scene.userspin = False
        label_gradient_field.pos = vector(axis_length * 1.6, axis_length * 1.6, 0)
        label_isolines.pos = label_gradient_field.pos - vector(1.5, 0, 0)
        arrow_label_gradient.pos = label_gradient_field.pos - vector(0, 4, 0)
        cylinder_label_isolines.pos = label_isolines.pos - vector(0, 4, 0)
        arrow_label_gradient.axis = vector(0, -1, 0)
        cylinder_label_isolines.axis = vector(0, -1, 0)

    elif r.text == 'Free rotation':
        scene.userspin = True


# VIEWS
scene.append_to_caption('\n\n    Activated views:\n')
scene.append_to_caption('      ')
radio(bind=set_views, text='Y-Z', checked=True, name='views')
scene.append_to_caption('      ')
radio(bind=set_views, text='X-Z', checked=False, name='views')
scene.append_to_caption('      ')
radio(bind=set_views, text='X-Y', checked=False, name='views')
scene.append_to_caption('\n      ')
radio(bind=set_views, text='Free rotation', checked=False, name='views')

# --- VPython desktop rendering loop (required for local execution) ---
# Keeps the 3D scene alive and updates the animation at 30 FPS
while True:
    rate(30)
