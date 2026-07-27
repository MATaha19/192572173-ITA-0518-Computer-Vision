from graphviz import Digraph

dot = Digraph("Q4_Concept_Map", format="png")
dot.attr(rankdir="TB", splines="ortho", nodesep="0.5", ranksep="0.8")

# Main Node
dot.node("A", "Image Acquisition Conditions", shape="box", style="filled", fillcolor="lightblue")

# Acquisition Factors
dot.node("B", "Lighting Conditions", shape="box", style="filled", fillcolor="lightgreen")
dot.node("B1", "Uniform Lighting")
dot.node("B2", "Uneven Lighting")
dot.node("B3", "Brightness")
dot.node("B4", "Shadows")

dot.node("C", "Camera Characteristics", shape="box", style="filled", fillcolor="lightgreen")
dot.node("C1", "Resolution")
dot.node("C2", "Lens Quality")
dot.node("C3", "CCD / CMOS Sensor")
dot.node("C4", "Exposure")

dot.node("D", "Environmental Conditions", shape="box", style="filled", fillcolor="lightgreen")
dot.node("D1", "Distance")
dot.node("D2", "Viewing Angle")
dot.node("D3", "Motion")
dot.node("D4", "Weather")

# Processing
dot.node("E", "Image Preprocessing", shape="box", style="filled", fillcolor="lightyellow")
dot.node("E1", "Noise Removal")
dot.node("E2", "Contrast Enhancement")
dot.node("E3", "Filtering")
dot.node("E4", "Normalization")

dot.node("F", "Feature Extraction", shape="box", style="filled", fillcolor="lightskyblue")
dot.node("F1", "Edges")
dot.node("F2", "Texture")
dot.node("F3", "Shape")
dot.node("F4", "Color")

dot.node("G", "Computer Vision Processing", shape="box", style="filled", fillcolor="orange")
dot.node("G1", "Segmentation")
dot.node("G2", "Object Detection")
dot.node("G3", "Recognition")
dot.node("G4", "Classification")

# Performance
dot.node("H", "Application Performance", shape="box", style="filled", fillcolor="gold")
dot.node("H1", "Medical Imaging")
dot.node("H2", "Autonomous Vehicles")
dot.node("H3", "Industrial Inspection")
dot.node("H4", "Agriculture")
dot.node("H5", "Surveillance")

# Literature
dot.node("L", "Literature Findings", shape="note", color="blue")
dot.node("L1", "Proper lighting improves segmentation", shape="note")
dot.node("L2", "High-resolution cameras improve feature extraction", shape="note")
dot.node("L3", "Noise reduction increases recognition accuracy", shape="note")
dot.node("L4", "Acquisition quality affects overall system performance", shape="note")

# Connections
dot.edge("A","B")
dot.edge("A","C")
dot.edge("A","D")

# Lighting
dot.edge("B","B1")
dot.edge("B","B2")
dot.edge("B","B3")
dot.edge("B","B4")

# Camera
dot.edge("C","C1")
dot.edge("C","C2")
dot.edge("C","C3")
dot.edge("C","C4")

# Environment
dot.edge("D","D1")
dot.edge("D","D2")
dot.edge("D","D3")
dot.edge("D","D4")

# Pipeline
dot.edge("B","E")
dot.edge("C","E")
dot.edge("D","E")

dot.edge("E","E1")
dot.edge("E","E2")
dot.edge("E","E3")
dot.edge("E","E4")

dot.edge("E","F")

dot.edge("F","F1")
dot.edge("F","F2")
dot.edge("F","F3")
dot.edge("F","F4")

dot.edge("F","G")

dot.edge("G","G1")
dot.edge("G","G2")
dot.edge("G","G3")
dot.edge("G","G4")

dot.edge("G","H")

dot.edge("H","H1")
dot.edge("H","H2")
dot.edge("H","H3")
dot.edge("H","H4")
dot.edge("H","H5")

# Literature
dot.edge("L","L1", style="dashed")
dot.edge("L","L2", style="dashed")
dot.edge("L","L3", style="dashed")
dot.edge("L","L4", style="dashed")

dot.edge("L","A", style="dotted")
dot.edge("L","E", style="dotted")
dot.edge("L","F", style="dotted")
dot.edge("L","H", style="dotted")

dot.render("Q4_Concept_Map", view=True)

print("Q4 Concept Map Generated Successfully!")
