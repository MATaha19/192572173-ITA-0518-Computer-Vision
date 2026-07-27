from graphviz import Digraph

dot = Digraph("Q2_Concept_Map", format="png")
dot.attr(rankdir="TB", splines="ortho", nodesep="0.5", ranksep="0.8")

# Main Pipeline
dot.node("A", "Real-World Environment", shape="box", style="filled", fillcolor="lightblue")
dot.node("B", "Image Acquisition", shape="box", style="filled", fillcolor="lightgreen")
dot.node("C", "Image Preprocessing", shape="box", style="filled", fillcolor="lightyellow")
dot.node("D", "Feature Extraction", shape="box", style="filled", fillcolor="lightgreen")
dot.node("E", "Feature Selection", shape="box")
dot.node("F", "Computer Vision Processing", shape="box", style="filled", fillcolor="lightskyblue")
dot.node("G", "Decision Making", shape="box", style="filled", fillcolor="lightpink")
dot.node("H", "Meaningful Output", shape="box", style="filled", fillcolor="gold")

# Acquisition
dot.node("B1", "Camera")
dot.node("B2", "Sensor")
dot.node("B3", "Lighting")
dot.node("B4", "Scene Capture")

# Preprocessing
dot.node("C1", "Noise Removal")
dot.node("C2", "Contrast Enhancement")
dot.node("C3", "Normalization")
dot.node("C4", "Filtering")

# Features
dot.node("D1", "Edges")
dot.node("D2", "Corners")
dot.node("D3", "Texture")
dot.node("D4", "Shape")
dot.node("D5", "Color")

# Vision Tasks
dot.node("F1", "Segmentation")
dot.node("F2", "Object Detection")
dot.node("F3", "Recognition")
dot.node("F4", "Classification")
dot.node("F5", "Tracking")

# Applications
dot.node("H1", "Medical Imaging")
dot.node("H2", "Autonomous Vehicles")
dot.node("H3", "Face Recognition")
dot.node("H4", "Agriculture")
dot.node("H5", "Industrial Inspection")
dot.node("H6", "Surveillance")

# Literature
dot.node("L", "Literature Connections", shape="note", color="blue")
dot.node("L1", "High-quality preprocessing improves accuracy", shape="note")
dot.node("L2", "Robust features improve recognition", shape="note")
dot.node("L3", "Efficient algorithms improve performance", shape="note")
dot.node("L4", "Better vision systems produce reliable outputs", shape="note")

# Main Flow
dot.edges([
    ("A","B"),
    ("B","C"),
    ("C","D"),
    ("D","E"),
    ("E","F"),
    ("F","G"),
    ("G","H")
])

# Acquisition
dot.edge("B","B1")
dot.edge("B","B2")
dot.edge("B","B3")
dot.edge("B","B4")

# Preprocessing
dot.edge("C","C1")
dot.edge("C","C2")
dot.edge("C","C3")
dot.edge("C","C4")

# Features
dot.edge("D","D1")
dot.edge("D","D2")
dot.edge("D","D3")
dot.edge("D","D4")
dot.edge("D","D5")

# Vision Tasks
dot.edge("F","F1")
dot.edge("F","F2")
dot.edge("F","F3")
dot.edge("F","F4")
dot.edge("F","F5")

# Applications
dot.edge("H","H1")
dot.edge("H","H2")
dot.edge("H","H3")
dot.edge("H","H4")
dot.edge("H","H5")
dot.edge("H","H6")

# Literature
dot.edge("L","L1", style="dashed")
dot.edge("L","L2", style="dashed")
dot.edge("L","L3", style="dashed")
dot.edge("L","L4", style="dashed")

dot.edge("L","B", style="dotted")
dot.edge("L","C", style="dotted")
dot.edge("L","D", style="dotted")
dot.edge("L","F", style="dotted")
dot.edge("L","H", style="dotted")

dot.render("Q2_Concept_Map", view=True)

print("Q2 Concept Map Generated Successfully!")
