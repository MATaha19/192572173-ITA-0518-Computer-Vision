from graphviz import Digraph

dot = Digraph("Q1_Concept_Map", format="png")
dot.attr(rankdir="TB", splines="ortho", nodesep="0.5", ranksep="0.8")

# Main Pipeline
dot.node("A", "Real-World Scene", shape="box", style="filled", fillcolor="lightblue")
dot.node("B", "Light Source", shape="box")
dot.node("C", "Object Reflection", shape="box")
dot.node("D", "Camera Lens", shape="box")
dot.node("E", "Image Sensor\n(CCD / CMOS)", shape="box")
dot.node("F", "Image Acquisition", shape="box", style="filled", fillcolor="lightgreen")
dot.node("G", "Image Formation", shape="box")
dot.node("H", "Sampling", shape="box")
dot.node("I", "Pixel Grid Formation", shape="box")
dot.node("J", "Quantization", shape="box")
dot.node("K", "Intensity Levels\n(Gray/RGB)", shape="box")
dot.node("L", "Digital Image Representation", shape="box", style="filled", fillcolor="orange")

# Preprocessing
dot.node("M", "Image Preprocessing", shape="box", style="filled", fillcolor="lightyellow")
dot.node("N1", "Noise Reduction")
dot.node("N2", "Contrast Enhancement")
dot.node("N3", "Histogram Equalization")
dot.node("N4", "Normalization")

# Feature Extraction
dot.node("O", "Feature Extraction", shape="box", style="filled", fillcolor="lightgreen")
dot.node("P1", "Edges")
dot.node("P2", "Corners")
dot.node("P3", "Texture")
dot.node("P4", "Shape")
dot.node("P5", "Color Features")

# CV
dot.node("Q", "Computer Vision Analysis", shape="box", style="filled", fillcolor="lightskyblue")
dot.node("R1", "Segmentation")
dot.node("R2", "Object Detection")
dot.node("R3", "Recognition")
dot.node("R4", "Classification")
dot.node("R5", "Tracking")

dot.node("S", "Decision Making", shape="box", style="filled", fillcolor="lightpink")

dot.node("T", "Applications", shape="box", style="filled", fillcolor="gold")
dot.node("T1", "Medical Imaging")
dot.node("T2", "Autonomous Vehicles")
dot.node("T3", "Face Recognition")
dot.node("T4", "Industrial Inspection")
dot.node("T5", "Agriculture")
dot.node("T6", "Surveillance")

# Literature
dot.node("U", "Literature Insights", shape="note", color="blue")
dot.node("U1", "High-quality acquisition\nimproves accuracy", shape="note")
dot.node("U2", "Proper sampling\nreduces aliasing", shape="note")
dot.node("U3", "Higher quantization\npreserves detail", shape="note")
dot.node("U4", "Preprocessing improves\nfeature extraction", shape="note")
dot.node("U5", "Reliable image representation\nimproves decision making", shape="note")

# Connections
dot.edges([
    ("A","B"),
    ("B","C"),
    ("C","D"),
    ("D","E"),
    ("E","F"),
    ("F","G"),
    ("G","H"),
    ("H","I"),
    ("I","J"),
    ("J","K"),
    ("K","L"),
    ("L","M"),
    ("M","O"),
    ("O","Q"),
    ("Q","S"),
    ("S","T")
])

# Preprocessing
dot.edge("M","N1")
dot.edge("M","N2")
dot.edge("M","N3")
dot.edge("M","N4")

# Feature Extraction
dot.edge("O","P1")
dot.edge("O","P2")
dot.edge("O","P3")
dot.edge("O","P4")
dot.edge("O","P5")

# Computer Vision
dot.edge("Q","R1")
dot.edge("Q","R2")
dot.edge("Q","R3")
dot.edge("Q","R4")
dot.edge("Q","R5")

# Applications
dot.edge("T","T1")
dot.edge("T","T2")
dot.edge("T","T3")
dot.edge("T","T4")
dot.edge("T","T5")
dot.edge("T","T6")

# Literature
dot.edge("U","U1", style="dashed")
dot.edge("U","U2", style="dashed")
dot.edge("U","U3", style="dashed")
dot.edge("U","U4", style="dashed")
dot.edge("U","U5", style="dashed")

dot.edge("U","F", style="dotted")
dot.edge("U","H", style="dotted")
dot.edge("U","J", style="dotted")
dot.edge("U","M", style="dotted")
dot.edge("U","S", style="dotted")

dot.render("Q1_Concept_Map", view=True)

print("Concept Map Generated Successfully!")
