from graphviz import Digraph

dot = Digraph("Q13_Concept_Map", format="png")
dot.attr(rankdir="TB", splines="ortho", nodesep="0.5", ranksep="0.8")

# Main Node
dot.node("A", "Analog Scene to Digital Image", shape="box",
         style="filled", fillcolor="lightblue")

# Physical World
dot.node("B", "Real-World Scene", shape="box",
         style="filled", fillcolor="lightgreen")
dot.node("B1", "Light Source")
dot.node("B2", "Object")
dot.node("B3", "Reflection")

# Optical System
dot.node("C", "Optical System", shape="box",
         style="filled", fillcolor="lightyellow")
dot.node("C1", "Camera Lens")
dot.node("C2", "Focus")
dot.node("C3", "Exposure")

# Image Sensor
dot.node("D", "Image Sensor", shape="box",
         style="filled", fillcolor="lightskyblue")
dot.node("D1", "CCD")
dot.node("D2", "CMOS")
dot.node("D3", "Analog Signal")

# Digitization
dot.node("E", "Digitization Process", shape="box",
         style="filled", fillcolor="orange")
dot.node("E1", "Sampling")
dot.node("E2", "Quantization")
dot.node("E3", "Encoding")

# Digital Representation
dot.node("F", "Digital Image Representation", shape="box",
         style="filled", fillcolor="gold")
dot.node("F1", "Pixel Matrix")
dot.node("F2", "Gray / RGB Values")
dot.node("F3", "Binary Data")

# Computer Processing
dot.node("G", "Computer Vision Processing", shape="box",
         style="filled", fillcolor="lightpink")
dot.node("G1", "Image Preprocessing")
dot.node("G2", "Feature Extraction")
dot.node("G3", "Object Detection")
dot.node("G4", "Recognition")

# Applications
dot.node("H", "Applications", shape="box",
         style="filled", fillcolor="lightcyan")
dot.node("H1", "Medical Imaging")
dot.node("H2", "Autonomous Vehicles")
dot.node("H3", "Face Recognition")
dot.node("H4", "Surveillance")

# Literature
dot.node("L", "Literature Insights", shape="note",
         color="blue")
dot.node("L1", "Light reflection forms the optical image",
         shape="note")
dot.node("L2", "Sampling converts spatial information",
         shape="note")
dot.node("L3", "Quantization converts intensity values",
         shape="note")
dot.node("L4", "Digital representation enables Computer Vision",
         shape="note")

# Main Flow
dot.edge("A", "B")
dot.edge("B", "B1")
dot.edge("B", "B2")
dot.edge("B", "B3")

dot.edge("B", "C")
dot.edge("C", "C1")
dot.edge("C", "C2")
dot.edge("C", "C3")

dot.edge("C", "D")
dot.edge("D", "D1")
dot.edge("D", "D2")
dot.edge("D", "D3")

dot.edge("D", "E")
dot.edge("E", "E1")
dot.edge("E", "E2")
dot.edge("E", "E3")

dot.edge("E", "F")
dot.edge("F", "F1")
dot.edge("F", "F2")
dot.edge("F", "F3")

dot.edge("F", "G")
dot.edge("G", "G1")
dot.edge("G", "G2")
dot.edge("G", "G3")
dot.edge("G", "G4")

dot.edge("G", "H")
dot.edge("H", "H1")
dot.edge("H", "H2")
dot.edge("H", "H3")
dot.edge("H", "H4")

# Literature
dot.edge("L", "L1", style="dashed")
dot.edge("L", "L2", style="dashed")
dot.edge("L", "L3", style="dashed")
dot.edge("L", "L4", style="dashed")

dot.edge("L", "B", style="dotted")
dot.edge("L", "D", style="dotted")
dot.edge("L", "E", style="dotted")
dot.edge("L", "F", style="dotted")
dot.edge("L", "G", style="dotted")

dot.render("Q13_Concept_Map", view=True)

print("Q13 Concept Map Generated Successfully!")
