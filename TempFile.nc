%
(Roland nc Post Processor Ver1 - By Benjamin Solar)

(G-CODE GENERATED BY FLATCAM v8.993 - www.flatcam.org - Version Date: 2020/06/05)

(Name: DrillExample)
(Type: G-code from Excellon)
(Units: MM)

(Created on Tuesday, 13 December 2022 at 03:15)

(This preprocessor is the default preprocessor used by FlatCAM.)
(It is made to work with MACH3 compatible motion controllers.)


(TOOLS DIAMETER: )
(Tool: 1 -> Dia: 1.0)
(Tool: 2 -> Dia: 1.52)

(FEEDRATE Z: )
(Tool: 1 -> Feedrate: 300.0)
(Tool: 2 -> Feedrate: 300.0)

(FEEDRATE RAPIDS: )
(Tool: 1 -> Feedrate Rapids: 1500)
(Tool: 2 -> Feedrate Rapids: 1500)

(Z_CUT: )
(Tool: 1 -> Z_Cut: -2.5)
(Tool: 2 -> Z_Cut: -2.5)

(Tools Offset: )
(Tool: 1 -> Offset Z: -0.0)
(Tool: 2 -> Offset Z: -0.0)

(Z_MOVE: )
(Tool: 1 -> Z_Move: 2.0)
(Tool: 2 -> Z_Move: 2.0)

(Z Toolchange: 15.0 mm)
(X,Y Toolchange: 0.0000, 0.0000 mm)
(Z Start: None mm)
(Z End: 2.0 mm)
(Steps per circle: 64)
(Preprocessor Excellon: default)

(X range:    1.8784 ...   18.6384  mm)
(Y range:    1.4596 ...   31.1676  mm)

(Spindle Speed: 9000.0 RPM)
G21
G90
G94



G01 F300.00

M05
G00 Z15.0000
G00 X0.0000 Y0.0000                
(MSG, Change to Tool Dia = 1.0000 ||| Total drills for tool T1 = 4)
!NR
G00 Z2.0000

M03 S9000
G00 X6.4484 Y1.9596
G01 Z-2.5000
G01 Z0
G00 Z2.0000
G00 X8.9884 Y1.9596
G01 Z-2.5000
G01 Z0
G00 Z2.0000
G00 X11.5284 Y1.9596
G01 Z-2.5000
G01 Z0
G00 Z2.0000
G00 X14.0684 Y1.9596
G01 Z-2.5000
G01 Z0
G00 Z2.0000
G01 F300.00

M05
G00 Z15.0000
G00 X0.0000 Y0.0000                
(MSG, Change to Tool Dia = 1.5200 ||| Total drills for tool T2 = 4)
!NR
G00 Z2.0000

M03 S9000
G00 X2.6384 Y30.4076
G01 Z-2.5000
G01 Z0
G00 Z2.0000
G00 X7.7184 Y30.4076
G01 Z-2.5000
G01 Z0
G00 Z2.0000
G00 X12.7984 Y30.4076
G01 Z-2.5000
G01 Z0
G00 Z2.0000
G00 X17.8784 Y30.4076
G01 Z-2.5000
G01 Z0
G00 Z2.0000
M05
G00 Z2.00

G00 Z15.0000
G00 X0.0000 Y0.0000
M02
%