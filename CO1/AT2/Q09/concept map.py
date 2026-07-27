from graphviz import Digraph

dot = Digraph("Q9_Concept_Map", format="png")
dot.attr(rankdir="TB", splines="ortho", nodesep="0.5", ranksep="0.8")

# Main Node
dot.node("A", "Image Sensing Mechanisms", shape="box",
         style="filled", fillcolor="lightblue")

# Sensing Mechanisms
dot.node("B", "Image Sensors", shape="box",
         style="filled", fillcolor="lightgreen")
dot.node("B1", "CCD Sensor")
dot.node("B2", "CMOS Sensor")
dot.node("B3", "Camera Lens")
dot.node("B4", "Optical Signal")

# Sensor Characteristics
dot.node("C", "Sensor Characteristics", shape="box",
         style="filled", fillcolor="lightyellow")
dot.node("C1", "Sensitivity")
dot.node("C2", "Resolution")
dot.node("C3", "Dynamic Range")
dot.node("C4", "Response Time")

# Noise Generation
dot.node("D", "Noise Generation", shape="box",
         style="filled", fillcolor="lightskyblue")
dot.node("D1", "Thermal Noise")
dot.node("D2", "Shot Noise")
dot.node("D3", "Electronic Noise")
dot.node("D4", "Environmental Noise")

# Acquisition Quality
dot.node("E", "Image Acquisition Quality", shape="box",
         style="filled", fillcolor="orange")
dot.node("E1", "Sharpness")
dot.node("E2", "Contrast")
dot.node("E3", "Brightness")
dot.node("E4", "Signal-to-Noise Ratio")

# Computer Vision
dot.node("F", "Computer Vision Performance", shape="box",
         style="filled", fillcolor="gold")
dot.node("F1", "Feature Extraction")
dot.node("F2", "Object Detection")
dot.node("F3", "Recognition Accuracy")
dot.node("F4", "Decision Making")

# Literature
dot.node("L", "Literature Perspectives", shape="note",
         color="blue")
dot.node("L1", "High-quality sensors improve acquisition accuracy",
         shape="note")
dot.node("L2", "Noise reduces recognition performance",
         shape="note")
dot.node("L3", "Higher dynamic range captures more details",
         shape="note")
dot.node("L4", "Better sensing enhances Computer Vision reliability",
         shape="note")

# Connections
dot.edge("A", "B")

dot.edge("B", "B1")
dot.edge("B", "B2")
dot.edge("B", "B3")
dot.edge("B", "B4")

dot.edge("B", "C")

dot.edge("C", "C1")
dot.edge("C", "C2")
dot.edge("C", "C3")
dot.edge("C", "C4")

dot.edge("C", "D")

dot.edge("D", "D1")
dot.edge("D", "D2")
dot.edge("D", "D3")
dot.edge("D", "D4")

dot.edge("D", "E")

dot.edge("E", "E1")
dot.edge("E", "E2")
dot.edge("E", "E3")
dot.edge("E", "E4")

dot.edge("E", "F")

dot.edge("F", "F1")
dot.edge("F", "F2")
dot.edge("F", "F3")
dot.edge("F", "F4")

# Literature Connections
dot.edge("L", "L1", style="dashed")
dot.edge("L", "L2", style="dashed")
dot.edge("L", "L3", style="dashed")
dot.edge("L", "L4", style="dashed")

dot.edge("L", "B", style="dotted")
dot.edge("L", "C", style="dotted")
dot.edge("L", "D", style="dotted")
dot.edge("L", "E", style="dotted")
dot.edge("L", "F", style="dotted")

dot.render("Q9_Concept_Map", view=True)

print("Q9 Concept Map Generated Successfully!")
