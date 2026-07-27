from graphviz import Digraph

dot = Digraph("Q7_Concept_Map", format="png")
dot.attr(rankdir="TB", splines="ortho", nodesep="0.5", ranksep="0.8")

# Main Node
dot.node("A", "Computer Vision", shape="box", style="filled", fillcolor="lightblue")

# Levels
dot.node("B", "Low-Level Processing", shape="box", style="filled", fillcolor="lightgreen")
dot.node("C", "Mid-Level Analysis", shape="box", style="filled", fillcolor="lightyellow")
dot.node("D", "High-Level Interpretation", shape="box", style="filled", fillcolor="lightskyblue")

# Low-Level
dot.node("B1", "Image Acquisition")
dot.node("B2", "Noise Removal")
dot.node("B3", "Image Enhancement")
dot.node("B4", "Filtering")

# Mid-Level
dot.node("C1", "Segmentation")
dot.node("C2", "Edge Detection")
dot.node("C3", "Feature Extraction")
dot.node("C4", "Object Representation")

# High-Level
dot.node("D1", "Object Recognition")
dot.node("D2", "Scene Understanding")
dot.node("D3", "Classification")
dot.node("D4", "Decision Making")

# Applications
dot.node("E", "Applications", shape="box", style="filled", fillcolor="orange")
dot.node("E1", "Medical Imaging")
dot.node("E2", "Autonomous Vehicles")
dot.node("E3", "Face Recognition")
dot.node("E4", "Robotics")
dot.node("E5", "Surveillance")

# Literature
dot.node("L", "Literature Examples", shape="note", color="blue")
dot.node("L1", "Low-level processing improves image quality", shape="note")
dot.node("L2", "Mid-level analysis extracts meaningful features", shape="note")
dot.node("L3", "High-level interpretation enables intelligent decisions", shape="note")
dot.node("L4", "Hierarchical processing improves Computer Vision accuracy", shape="note")

# Main Flow
dot.edge("A","B")
dot.edge("B","C")
dot.edge("C","D")
dot.edge("D","E")

# Low-Level Branches
dot.edge("B","B1")
dot.edge("B","B2")
dot.edge("B","B3")
dot.edge("B","B4")

# Mid-Level Branches
dot.edge("C","C1")
dot.edge("C","C2")
dot.edge("C","C3")
dot.edge("C","C4")

# High-Level Branches
dot.edge("D","D1")
dot.edge("D","D2")
dot.edge("D","D3")
dot.edge("D","D4")

# Applications
dot.edge("E","E1")
dot.edge("E","E2")
dot.edge("E","E3")
dot.edge("E","E4")
dot.edge("E","E5")

# Literature
dot.edge("L","L1", style="dashed")
dot.edge("L","L2", style="dashed")
dot.edge("L","L3", style="dashed")
dot.edge("L","L4", style="dashed")

dot.edge("L","B", style="dotted")
dot.edge("L","C", style="dotted")
dot.edge("L","D", style="dotted")

dot.render("Q7_Concept_Map", view=True)

print("Q7 Concept Map Generated Successfully!")
