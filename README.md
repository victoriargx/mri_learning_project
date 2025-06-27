# MRI Learning Simulations with VPython

This repository contains a collection of MRI-related simulations derived from original educational scripts developed by Frederik Laun and Victoria Rincon (University Hospital Erlangen) as part of the Magnetic Resonance Imaging 1 (MRI1) course at the Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU). These simulations have been adapted for local execution using desktop VPython.


>The current version is maintained by Victoria Rincon and aims to facilitate local desktop execution of the original simulations. It also serves as a base for continuous improvement of the existing MRI-related simulations and for the development of new ones, while remaining fully dedicated to open, non-commercial educational use.

---
## How to Run

To run these simulations, you'll need [VPython](https://vpython.org/).  
It is suggested to create a virtual environment and install VPython there using:

```bash
pip install vpython
```

- For more installation options or troubleshooting, see the official [VPython Installation Guide](https://vpython.org/presentation2018/install.html).

---
## Repository Structure

```text
mri_learning_project/
├── docs/                            # Supporting scripts and documentation files
│   └── img/                         # Images used in documentation
│
├── simulations/                     # Desktop-adapted VPython simulations
│   ├── s01_dynamic_magnetization_in_b0.py
│   ├── s02_rotating_reference_frame.py
│   ├── s03_resonant_excitation.py
│   ├── s04_off_resonant_excitation.py
│   ├── s05_coil_sensitivity_profile.py
│   ├── s06_ideal_gradient_field.py
│   └── s07_fourier_series.py
│
├── LICENSE                          # License information (CC BY-SA 4.0)
└── README.md                        # Project overview and usage
```
---
## Original Simulations

The original simulations were implemented using Web VPython on [Glowscript.org](https://www.glowscript.org/docs/VPythonDocs/index.html), allowing for interactive 3D visualization using Python-like syntax. These scripts were created for teaching concepts of magnetic resonance imaging (MRI) in a visually intuitive way and were fully web-accessible, requiring no local setup.

The full collection of original Web VPython scripts can be found [here](https://glowscript.org/#/user/Frederik.Laun/folder/LectureMRI1/), and their corresponding desktop-adapted versions included in this repository are listed in the table below.

### List of Original Simulations

| Simulation Title                    | Adapted Desktop Script (`simulations/`)                                              | Original Script (Glowscript)                                                                                                                    |
|-------------------------------------|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Dynamic of M(t) in B<sub>0</sub> | [s01_dynamic_magnetization_in_b0.py](simulations/s01_dynamic_magnetization_in_b0.py) | [Lecture03.Dynamics-of-M-in-B0](https://glowscript.org/#/user/Frederik.Laun/folder/LectureMRI1/program/Lecture03.Dynamics-of-M-in-B0)           |
| 2. Rotating Reference Frame         | [s02_rotating_reference_frame.py](simulations/s02_rotating_reference_frame.py)       | [Lecture03.Rotating-Reference-Frame](https://glowscript.org/#/user/Frederik.Laun/folder/LectureMRI1/program/Lecture03.Rotating-Reference-Frame) |
| 3. Resonant Excitation              | [s03_resonant_excitation.py](simulations/s03_resonant_excitation.py)                 | [Lecture03.Resonant-Excitation](https://glowscript.org/#/user/Frederik.Laun/folder/LectureMRI1/program/Lecture03.Resonant-Excitation)           |
| 4. Off-Resonant Excitation          | [s04_off_resonant_excitation.py](simulations/s04_off_resonant_excitation.py)         | [Lecture4.Off-Resonant-Excitation](https://glowscript.org/#/user/Frederik.Laun/folder/LectureMRI1/program/Lecture4.Off-Resonant-Excitation)     |
| 5. Coil Sensitivity Profile         | [s05_coil_sensitivity_profile.py](simulations/s05_coil_sensitivity_profile.py)       | [Lecture5.CoilSensitivityProfile](https://glowscript.org/#/user/Frederik.Laun/folder/LectureMRI1/program/Lecture5.CoilSensitivityProfile)       |
| 6. The ideal Gradient Field         | [s06_ideal_gradient_field.py](simulations/s06_ideal_gradient_field.py)                                     | [Lecture07.Gradients](https://glowscript.org/#/user/Frederik.Laun/folder/LectureMRI1/program/Lecture07.Gradients)                               |
| 7. Fourier Series                   | [s07_fourier_series.py](simulations/s07_fourier_series.py)                           | [Lecture08.FourierSeries](https://glowscript.org/#/user/Frederik.Laun/folder/LectureMRI1/program/Lecture08.FourierSeries)                       |

> ### 💡 Why Adapt to Desktop?
> 
> While the original Web VPython simulations offered great accessibility via a browser, they required an internet connection and provided limited flexibility for extension or customization.  
>  
> The desktop VPython adaptation presented in this repository allows offline use, easier code modification, and greater potential for further development.

---
## License

This repository contains adaptations of educational scripts originally developed by **Frederik Laun** and **Victoria Rincon** for the *Magnetic Resonance Imaging 1 (MRI1)* course at **Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU)**.

This repository is licensed under the **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)** license.  

> You are free to share and adapt the material, as long as you credit the original authors and share any modifications under the same license.
>
> For more information, see the [full license text](https://creativecommons.org/licenses/by-sa/4.0/).

---
## 🚧 Future Work

Several improvements and extensions are planned for future iterations of this project:
- Improve simulation stability. For instance, some simulations show rendering issues, such as visual glitches when sliders are moved too quickly, which were not noticeable in the original web-based versions.
- Code cleanup and refactoring to improved readability, modularity, and maintainability.
- Addition of explanatory documentation or user instructions.
- Add new simulations to cover additional MRI concepts.

---
##  Comments🗨️? Suggestions💡? Issues🪲? 
### ⭐Let me know!!⭐
> 
> Your input is very welcome! Help improve this project by sharing your thoughts or opening an issue.
>
[//]: # (---)

[//]: # (---)

[//]: # (> ###  Comments🗨️? Suggestions💡? Issues🪲? ⭐Let me know!!⭐)

[//]: # (> )

[//]: # (> Your input is very welcome! Help improve this project by sharing your thoughts or opening an issue.)

[//]: # (> )
