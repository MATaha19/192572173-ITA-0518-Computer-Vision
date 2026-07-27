from graphviz import Digraph

dot = Digraph("Q3_Concept_Map", format="png")
dot.attr(rankdir="TB", splines="ortho", nodesep="0.5", ranksep="0.8")

# Main Node
dot.node("A", "Image Resolution & Intensity Levels", shape="box", style="filled", fillcolor="lightblue")

# Resolution
dot.node("B", "Spatial Resolution", shape="box", style="filled", fillcolor="lightgreen")
dot.node("B1", "Pixel Density")
dot.node("B2", "Image Size")
dot.node("B3", "Sampling Rate")

# Intensity
dot.node("C", "Intensity Resolution", shape="box", style="filled", fillcolor="lightgreen")
dot.node("C1", "Bit Depth")
dot.node("C2", "Gray Levels")
dot.node("C3", "Color Depth")

# Image Quality
dot.node("D", "Image Quality", shape="box", style="filled", fillcolor="lightyellow")
dot.node("D1", "Sharpness")
dot.node("D2", "Contrast")
dot.node("D3", "Noise")
dot.node("D4", "Detail Preservation")

# Usability
dot.node("E", "Image Usability", shape="box", style="filled", fillcolor="lightskyblue")
dot.node("E1", "Medical Imaging")
dot.node("E2", "Remote Sensing")
dot.node("E3", "Face Recognition")
dot.node("E4", "Autonomous Vehicles")
dot.node("E5", "Industrial Inspection")

# Cause-Effect
dot.node("F", "Cause–Effect Relationships", shape="box", style="filled", fillcolor="lightpink")
dot.node("F1", "Higher Sampling → Better Detail")
dot.node("F2", "Higher Bit Depth → Better Contrast")
dot.node("F3", "Low Resolution → Information Loss")
dot.node("F4", "Low Intensity Levels → Quantization Error")
dot.node("F5", "Noise → Reduced Accuracy")

# Literature
dot.node("L", "Literature Evidence", shape="note", color="blue")
dot.node("L1", "Higher spatial resolution improves feature extraction", shape="note")
dot.node("L2", "Higher bit depth preserves image information", shape="note")
dot.node("L3", "Proper sampling reduces aliasing", shape="note")
dot.node("L4", "Image quality directly affects CV accuracy", shape="note")

# Connections
dot.edge("A","B")
dot.edge("A","C")

dot.edge("B","B1")
dot.edge("B","B2")
dot.edge("B","B3")

dot.edge("C","C1")
dot.edge("C","C2")
dot.edge("C","C3")

dot.edge("B","D")
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

dot.edge("D","F")

dot.edge("F","F1")
dot.edge("F","F2")
dot.edge("F","F3")
dot.edge("F","F4")
dot.edge("F","F5")

dot.edge("L","L1", style="dashed")
dot.edge("L","L2", style="dashed")
dot.edge("L","L3", style="dashed")
dot.edge("L","L4", style="dashed")

dot.edge("L","B", style="dotted")
dot.edge("L","C", style="dotted")
dot.edge("L","D", style="dotted")
dot.edge("L","E", style="dotted")

dot.render("Q3_Concept_Map", view=True)

print("Q3 Concept Map Generated Successfully!")
