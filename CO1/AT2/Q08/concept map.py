from graphviz import Digraph

dot = Digraph("Q8_Concept_Map", format="png")
dot.attr(rankdir="TB", splines="ortho", nodesep="0.5", ranksep="0.8")

# Main Node
dot.node("A", "Spatial Resolution", shape="box", style="filled", fillcolor="lightblue")

# Factors Affecting Spatial Resolution
dot.node("B", "Factors Affecting Spatial Resolution", shape="box", style="filled", fillcolor="lightgreen")
dot.node("B1", "Sampling Rate")
dot.node("B2", "Pixel Density")
dot.node("B3", "Sensor Resolution")
dot.node("B4", "Image Size")

# Image Quality
dot.node("C", "Image Quality", shape="box", style="filled", fillcolor="lightyellow")
dot.node("C1", "Sharpness")
dot.node("C2", "Fine Details")
dot.node("C3", "Aliasing")
dot.node("C4", "Blur")

# Application Requirements
dot.node("D", "Application Requirements", shape="box", style="filled", fillcolor="lightskyblue")
dot.node("D1", "Medical Imaging")
dot.node("D2", "Satellite Imaging")
dot.node("D3", "Autonomous Vehicles")
dot.node("D4", "Face Recognition")
dot.node("D5", "Industrial Inspection")

# Performance
dot.node("E", "System Performance", shape="box", style="filled", fillcolor="orange")
dot.node("E1", "High Accuracy")
dot.node("E2", "Reliable Detection")
dot.node("E3", "Improved Decision Making")

# Literature
dot.node("L", "Literature Evidence", shape="note", color="blue")
dot.node("L1", "Higher sampling improves spatial detail", shape="note")
dot.node("L2", "Greater pixel density increases image quality", shape="note")
dot.node("L3", "Application determines required resolution", shape="note")
dot.node("L4", "Proper spatial resolution improves Computer Vision performance", shape="note")

# Connections
dot.edge("A","B")

dot.edge("B","B1")
dot.edge("B","B2")
dot.edge("B","B3")
dot.edge("B","B4")

dot.edge("B","C")

dot.edge("C","C1")
dot.edge("C","C2")
dot.edge("C","C3")
dot.edge("C","C4")

dot.edge("C","D")

dot.edge("D","D1")
dot.edge("D","D2")
dot.edge("D","D3")
dot.edge("D","D4")
dot.edge("D","D5")

dot.edge("D","E")

dot.edge("E","E1")
dot.edge("E","E2")
dot.edge("E","E3")

# Literature Connections
dot.edge("L","L1", style="dashed")
dot.edge("L","L2", style="dashed")
dot.edge("L","L3", style="dashed")
dot.edge("L","L4", style="dashed")

dot.edge("L","B", style="dotted")
dot.edge("L","C", style="dotted")
dot.edge("L","D", style="dotted")
dot.edge("L","E", style="dotted")

dot.render("Q8_Concept_Map", view=True)

print("Q8 Concept Map Generated Successfully!")
