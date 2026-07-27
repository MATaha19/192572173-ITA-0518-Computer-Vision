from graphviz import Digraph

dot = Digraph("Q15_Concept_Map", format="png")
dot.attr(rankdir="TB", splines="ortho", nodesep="0.5", ranksep="0.8")

# Main Node
dot.node("A", "Image Formation Models", shape="box",
         style="filled", fillcolor="lightblue")

# Theoretical Models
dot.node("B", "Theoretical Models", shape="box",
         style="filled", fillcolor="lightgreen")
dot.node("B1", "Pinhole Camera Model")
dot.node("B2", "Perspective Projection")
dot.node("B3", "Illumination Model")
dot.node("B4", "Geometric Transformation")

# Image Acquisition
dot.node("C", "Image Acquisition", shape="box",
         style="filled", fillcolor="lightyellow")
dot.node("C1", "Camera Lens")
dot.node("C2", "CCD / CMOS Sensor")
dot.node("C3", "Image Capture")
dot.node("C4", "Digital Image")

# Image Processing
dot.node("D", "Image Processing", shape="box",
         style="filled", fillcolor="lightskyblue")
dot.node("D1", "Noise Removal")
dot.node("D2", "Image Enhancement")
dot.node("D3", "Segmentation")
dot.node("D4", "Feature Extraction")

# Computer Vision Applications
dot.node("E", "Computer Vision Applications", shape="box",
         style="filled", fillcolor="orange")
dot.node("E1", "Medical Imaging")
dot.node("E2", "Autonomous Vehicles")
dot.node("E3", "Face Recognition")
dot.node("E4", "Industrial Inspection")
dot.node("E5", "Agriculture")
dot.node("E6", "Surveillance")

# System Performance
dot.node("F", "Practical System Performance", shape="box",
         style="filled", fillcolor="gold")
dot.node("F1", "Detection Accuracy")
dot.node("F2", "Recognition Accuracy")
dot.node("F3", "Processing Speed")
dot.node("F4", "Reliability")
dot.node("F5", "Real-Time Decision Making")

# Literature
dot.node("L", "Literature Insights", shape="note",
         color="blue")
dot.node("L1", "Accurate camera models improve calibration",
         shape="note")
dot.node("L2", "Illumination models improve image interpretation",
         shape="note")
dot.node("L3", "Feature extraction depends on image formation quality",
         shape="note")
dot.node("L4", "Better image formation enhances Computer Vision performance",
         shape="note")

# Connections
dot.edge("A", "B")

# Theoretical Models
dot.edge("B", "B1")
dot.edge("B", "B2")
dot.edge("B", "B3")
dot.edge("B", "B4")

# Acquisition
dot.edge("B", "C")

dot.edge("C", "C1")
dot.edge("C", "C2")
dot.edge("C", "C3")
dot.edge("C", "C4")

# Processing
dot.edge("C", "D")

dot.edge("D", "D1")
dot.edge("D", "D2")
dot.edge("D", "D3")
dot.edge("D", "D4")

# Applications
dot.edge("D", "E")

dot.edge("E", "E1")
dot.edge("E", "E2")
dot.edge("E", "E3")
dot.edge("E", "E4")
dot.edge("E", "E5")
dot.edge("E", "E6")

# Performance
dot.edge("E", "F")

dot.edge("F", "F1")
dot.edge("F", "F2")
dot.edge("F", "F3")
dot.edge("F", "F4")
dot.edge("F", "F5")

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

dot.render("Q15_Concept_Map", view=True)

print("Q15 Concept Map Generated Successfully!")
