from graphviz import Digraph

dot = Digraph("Q6_Concept_Map", format="png")
dot.attr(rankdir="TB", splines="ortho", nodesep="0.5", ranksep="0.8")

# Main Node
dot.node("A", "Digital Image Formation", shape="box", style="filled", fillcolor="lightblue")

# Scene Formation
dot.node("B", "Real-World Scene", shape="box", style="filled", fillcolor="lightgreen")
dot.node("B1", "Light Source")
dot.node("B2", "Object")
dot.node("B3", "Reflection")

# Image Acquisition
dot.node("C", "Image Acquisition", shape="box", style="filled", fillcolor="lightyellow")
dot.node("C1", "Camera Lens")
dot.node("C2", "CCD / CMOS Sensor")
dot.node("C3", "Optical Signal")

# Digital Formation
dot.node("D", "Image Formation", shape="box", style="filled", fillcolor="lightskyblue")
dot.node("D1", "Sampling")
dot.node("D2", "Pixel Grid")
dot.node("D3", "Quantization")
dot.node("D4", "Gray / RGB Levels")

# Image Quality
dot.node("E", "Image Quality", shape="box", style="filled", fillcolor="orange")
dot.node("E1", "Spatial Resolution")
dot.node("E2", "Intensity Resolution")
dot.node("E3", "Noise")
dot.node("E4", "Contrast")
dot.node("E5", "Aliasing")

# Digital Image
dot.node("F", "Digital Image", shape="box", style="filled", fillcolor="gold")
dot.node("F1", "Pixel Matrix")
dot.node("F2", "Image Storage")
dot.node("F3", "Computer Vision Input")

# Literature
dot.node("L", "Literature Insights", shape="note", color="blue")
dot.node("L1", "Proper sensing improves image accuracy", shape="note")
dot.node("L2", "Higher sampling preserves spatial details", shape="note")
dot.node("L3", "Higher quantization reduces information loss", shape="note")
dot.node("L4", "Image quality directly influences Computer Vision performance", shape="note")

# Connections
dot.edge("A","B")
dot.edge("B","B1")
dot.edge("B","B2")
dot.edge("B","B3")

dot.edge("B","C")
dot.edge("C","C1")
dot.edge("C","C2")
dot.edge("C","C3")

dot.edge("C","D")
dot.edge("D","D1")
dot.edge("D","D2")
dot.edge("D","D3")
dot.edge("D","D4")

dot.edge("D","E")
dot.edge("E","E1")
dot.edge("E","E2")
dot.edge("E","E3")
dot.edge("E","E4")
dot.edge("E","E5")

dot.edge("E","F")
dot.edge("F","F1")
dot.edge("F","F2")
dot.edge("F","F3")

# Literature
dot.edge("L","L1", style="dashed")
dot.edge("L","L2", style="dashed")
dot.edge("L","L3", style="dashed")
dot.edge("L","L4", style="dashed")

dot.edge("L","C", style="dotted")
dot.edge("L","D", style="dotted")
dot.edge("L","E", style="dotted")
dot.edge("L","F", style="dotted")

dot.render("Q6_Concept_Map", view=True)

print("Q6 Concept Map Generated Successfully!")
