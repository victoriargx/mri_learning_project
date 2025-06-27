"""
This program was originally developed for the MRI1 course at the Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU).
This version is maintained and documented by Victoria Rincon, with slight modifications for desktop.

Title: Fourier Series
Authors: Victoria Rincon, Frederik Laun, FAU, University Hospital Erlangen
Original public release: : Summer 2024
Original version available at:
https://glowscript.org/#/user/Frederik.Laun/folder/LectureMRI1/program/Lecture08.FourierSeries
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
scene.height = window_innerWidth * 0.07
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
FAU_logo_width = window_innerWidth * 0.35
FAU_logo_height = FAU_logo_width / 5
scene.caption = "  <img src='https://mod.fau.eu/wp-content/uploads/FAU-logo_940x182.jpg' width='{0}' height='{1}'> \n <b>MAGNETIC RESONANCE IMAGING I</b> \n\n".format(
    FAU_logo_width, FAU_logo_height)

gp_fx = graph(width=window_innerWidth * 0.6, height=window_innerHeight * 0.6 / 2, title='<b>f(x)</b>', xtitle='x [mm]',
              ytitle='f(x)', scroll=False, fast=False, align='left')
fx = gcurve(color=color.blue, label='<i>f(x)</i>', graph=gp_fx)
sN = gcurve(color=color.orange, label='<i>s<sub>N</sub>(x)</i>', graph=gp_fx)

gp_cn = graph(width=window_innerWidth * 0.6, height=window_innerHeight * 0.6 / 2, title='<b>c<sub>n</sub></b>',
              xtitle='n', ytitle='c<sub>n</sub>', scroll=False, fast=False, align='left')
cn = gdots(color=color.red, label='<i>Im(c<sub>n</sub>)</i>', graph=gp_cn)
cn_bars = gvbars(delta=0.05, color=color.red, graph=gp_cn)

'''
However, due to the Gibbs phenomenon, oscillations near 
    discontinuities may still appear. These oscialtions do not 
    disappear completely, even when increasing N, but the overall 
    approximation improves as more terms are added.
'''

# PROGRAM DESCRIPTION
scene.append_to_caption('  <b>FOURIER SERIES</b> \n')
scene.append_to_caption('''
    This simulation illustrates the approximation of a function f(x)
    using its Fourier series expansion. The function is periodic over 
    the interval [-L/2, L/2], and the Fourier series reconstructs the 
    original function by summing only sinusoidal components, as 
    the function is odd. The more N terms included in the series, 
    the more accurate the approximation of f(x).

    The first graph displays both, the original function and the 
    Fourier series approximation for a selected f(x) and number of 
    terms N. 

    The second graph displays the Fourier coefficients <b>c<sub>n</sub></b> of the 
    series, which represent the amplitude of each sinusoidal 
    component in the Fourier expansion. As N increases, the 
    magnitudes of the coefficients gradually decrease, reflecting
    the diminishing contribution of higher-frequency components
    to the overall approximation.
    \n''')

scene.append_to_caption('''      
   <b>Simulation Interaction:</b>
    Below, you can selected the function f(x) and the number
    of terms (N) to use for the Fourier series approximation.
    \n''')

# Fourier Series Parameters
L = 5  # Length of the interval


# Define f(x) = x
def f_x(x):
    return x / L


# Define f(x) = sign(x)
def f_sign(x):
    return 1 if x >= 0 else -1


def fourier_series_sign(x, N):
    S_N = 0
    for n in range(1, N + 1, 2):  # Solo términos impares
        S_N += (4 / (n * pi)) * sin(n * x)
    return S_N


def fourier_series_x(x, N):
    sum_terms = 0
    for n in range(1, N + 1):
        cn = cn_x(n)
        # Real Part: cn * cos(2 * pi * n * x / L)
        sum_terms += cn * sin(2 * pi * n * x / L) * (-1)
    return sum_terms


def set_function(r):
    x_min = -2.5
    x_max = 2.5
    num_points = 1000
    step_size = (x_max - x_min) / (num_points - 1)

    # Clean up the graphs
    fx.delete()
    sN.delete()
    cn.delete()
    cn_bars.delete()

    if r.example == 'A':
        for i in range(num_points):
            # f(x)
            x = x_min + i * step_size
            y = f_sign(x)
            fx.plot(x, y)

            # Fourier Series
            sN.plot(x, fourier_series_sign(x, slider_n.value))


    elif r.example == 'B':
        L = 5  # mm
        for i in range(num_points):
            x = x_min + i * step_size
            y = x / L
            fx.plot(x, y)

            # Fourier Series
            sN.plot(x, fourier_series_x(x, slider_n.value))

    set_n(slider_n)


def cn_sign(n):
    if n == 0:
        return 0  # El coeficiente para n = 0 se define como 0
    else:
        Im = (1 - pow(-1, n)) / (n * pi) * (-1)
        return Im


def cn_x(n):
    if n == 0:
        return 0  # The coefficient for n = 0 is zero in this case
    else:
        return (1 / (1 * n * pi)) * pow(-1, (n + 1)) * (-1)


# Function selection radiobuttons
scene.append_to_caption('    Function selection:\n')
scene.append_to_caption('      ')
radio_sign = radio(example='A', bind=set_function, text='f(x) = sign(x)', checked=False, name='function')
scene.append_to_caption('\n      ')
radio_x = radio(example='B', bind=set_function, text='f(x) = x/L', checked=False, name='function')


# scene.append_to_caption('\n      ')


def set_n(s):
    coefficients_Im = []
    n_values = arange(-s.value, s.value + 1)

    # Clean Previous Graphs
    sN.delete()
    cn.delete()
    cn_bars.delete()

    if radio_sign.checked:
        for n in n_values:
            coefficients_Im.append(cn_sign(n))
        paired_values = list(zip(n_values, coefficients_Im))
        cn.plot(paired_values)
        cn_bars.plot(paired_values)
        wtext_n.text = s.value

        x_min = -2.5
        x_max = 2.5
        num_points = 1000
        step_size = (x_max - x_min) / (num_points - 1)

        sN.delete()  # Limpiar gráfica anterior
        for i in range(num_points):
            # f(x)
            x = x_min + i * step_size

            # Fourier Series
            sN.plot(x, fourier_series_sign(x, slider_n.value))

    elif radio_x.checked:
        for n in n_values:
            coefficients_Im.append(cn_x(n))
        paired_values = list(zip(n_values, coefficients_Im))
        cn.plot(paired_values)
        cn_bars.plot(paired_values)
        wtext_n.text = s.value

        x_min = -2.5
        x_max = 2.5
        num_points = 1000
        step_size = (x_max - x_min) / (num_points - 1)

        sN.delete()  # Limpiar gráfica anterior
        for i in range(num_points):
            # f(x)
            x = x_min + i * step_size

            # Fourier Series
            sN.plot(x, fourier_series_x(x, slider_n.value))


# Slider for number of coefficients
scene.append_to_caption('\n\n    Number of Terms:\n')
scene.append_to_caption('      N:')
slider_n = slider(min=1, max=20, value=1, length=220, bind=set_n, right=15, step=1,
                  disabled=False, text='0')
wtext_n = wtext(text=slider_n.value)

# --- VPython desktop rendering loop (required for local execution) ---
# Keeps the 3D scene alive and updates the animation at 30 FPS
while True:
    rate(30)


