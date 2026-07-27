from graphviz import Digraph

dot = Digraph("Q14_Concept_Map", format="png")
dot.attr(rankdir="TB", splines="ortho", nodesep="0.5", ranksep="0.8")

# Main Node
dot.node("A", "Image Quality Parameters", shape="box",
         style="filled", fillcolor="lightblue")

# Resolution
dot.node("B", "Resolution", shape="box",
         style="filled", fillcolor="lightgreen")
dot.node("B1", "Spatial Resolution")
dot.node("B2", "Pixel Density")
dot.node("B3", "Sampling Rate")

# Noise
dot.node("C", "Noise", shape="box",
         style="filled", fillcolor="lightgreen")
dot.node("C1", "Thermal Noise")
dot.node("C2", "Shot Noise")
dot.node("C3", "Electronic Noise")

# Contrast
dot.node("D", "Contrast", shape="box",
         style="filled", fillcolor="lightgreen")
dot.node("D1", "Brightness Difference")
dot.node("D2", "Dynamic Range")
dot.node("D3", "Histogram")

# Image Quality
dot.node("E", "Overall Image Quality", shape="box",
         style="filled", fillcolor="lightyellow")
dot.node("E1", "Sharpness")
dot.node("E2", "Visibility")
dot.node("E3", "Detail Preservation")
dot.node("E4", "Signal-to-Noise Ratio")

# Computer Vision
dot.node("F", "Computer Vision Performance", shape="box",
         style="filled", fillcolor="lightskyblue")
dot.node("F1", "Feature Extraction")
dot.node("F2", "Segmentation")
dot.node("F3", "Object Detection")
dot.node("F4", "Classification")
dot.node("F5", "Recognition Accuracy")

# Applications
dot.node("G", "System Performance", shape="box",
         style="filled", fillcolor="orange")
dot.node("G1", "Medical Imaging")
dot.node("G2", "Autonomous Vehicles")
dot.node("G3", "Face Recognition")
dot.node("G4", "Industrial Inspection")
dot.node("G5", "Surveillance")

# Literature
dot.node("L", "Literature Perspectives", shape="note",
         color="blue")
dot.node("L1", "Higher resolution improves feature extraction",
         shape="note")
dot.node("L2", "Noise decreases recognition accuracy",
         shape="note")
dot.node("L3", "Good contrast improves segmentation",
         shape="note")
dot.node("L4", "Balanced image quality improves overall system performance",
         shape="note")

# Connections
dot.edge("A", "B")
dot.edge("A", "C")
dot.edge("A", "D")

# Resolution
dot.edge("B", "B1")
dot.edge("B", "B2")
dot.edge("B", "B3")

# Noise
dot.edge("C", "C1")
dot.edge("C", "C2")
dot.edge("C", "C3")

# Contrast
dot.edge("D", "D1")
dot.edge("D", "D2")
dot.edge("D", "D3")

# Image Quality
dot.edge("B", "E")
dot.edge("C", "E")
dot.edge("D", "E")

dot.edge("E", "E1")
dot.edge("E", "E2")
dot.edge("E", "E3")
dot.edge("E", "E4")

# Computer Vision
dot.edge("E", "F")

dot.edge("F", "F1")
dot.edge("F", "F2")
dot.edge("F", "F3")
dot.edge("F", "F4")
dot.edge("F", "F5")

# Applications
dot.edge("F", "G")

dot.edge("G", "G1")
dot.edge("G", "G2")
dot.edge("G", "G3")
dot.edge("G", "G4")
dot.edge("G", "G5")

# Literature
dot.edge("L", "L1", style="dashed")
dot.edge("L", "L2", style="dashed")
dot.edge("L", "L3", style="dashed")
dot.edge("L", "L4", style="dashed")

dot.edge("L", "B", style="dotted")
dot.edge("L", "C", style="dotted")
dot.edge("L", "D", style="dotted")
dot.edge("L", "E", style="dotted")
dot.edge("L", "F", style="dotted")
dot.edge("L", "G", style="dotted")

dot.render("Q14_Concept_Map", view=True)

print("Q14 Concept Map Generated Successfully!")
