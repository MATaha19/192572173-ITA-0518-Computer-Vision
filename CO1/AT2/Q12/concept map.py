from graphviz import Digraph

dot = Digraph("Q12_Concept_Map", format="png")
dot.attr(rankdir="TB", splines="ortho", nodesep="0.5", ranksep="0.8")

# Main Node
dot.node("A", "Image Acquisition Conditions", shape="box",
         style="filled", fillcolor="lightblue")

# Lighting
dot.node("B", "Lighting Conditions", shape="box",
         style="filled", fillcolor="lightgreen")
dot.node("B1", "Low Lighting")
dot.node("B2", "Uneven Lighting")
dot.node("B3", "Overexposure")
dot.node("B4", "Underexposure")

# Motion
dot.node("C", "Motion Conditions", shape="box",
         style="filled", fillcolor="lightgreen")
dot.node("C1", "Camera Motion")
dot.node("C2", "Object Motion")
dot.node("C3", "Motion Speed")
dot.node("C4", "Shaking")

# Environment
dot.node("D", "Environmental Conditions", shape="box",
         style="filled", fillcolor="lightgreen")
dot.node("D1", "Fog")
dot.node("D2", "Rain")
dot.node("D3", "Dust")
dot.node("D4", "Smoke")

# Image Artifacts
dot.node("E", "Image Artifacts", shape="box",
         style="filled", fillcolor="lightskyblue")
dot.node("E1", "Blur")
dot.node("E2", "Noise")
dot.node("E3", "Shadows")
dot.node("E4", "Glare")
dot.node("E5", "Low Contrast")

# Image Quality
dot.node("F", "Image Quality", shape="box",
         style="filled", fillcolor="orange")
dot.node("F1", "Reduced Sharpness")
dot.node("F2", "Poor Visibility")
dot.node("F3", "Loss of Details")
dot.node("F4", "Distorted Features")

# Computer Vision Performance
dot.node("G", "Computer Vision Performance", shape="box",
         style="filled", fillcolor="gold")
dot.node("G1", "Feature Extraction")
dot.node("G2", "Object Detection")
dot.node("G3", "Classification")
dot.node("G4", "Recognition Accuracy")

# Literature
dot.node("L", "Literature Findings", shape="note",
         color="blue")
dot.node("L1", "Good lighting improves image quality",
         shape="note")
dot.node("L2", "Motion causes image blur",
         shape="note")
dot.node("L3", "Environmental conditions introduce artifacts",
         shape="note")
dot.node("L4", "Image artifacts reduce Computer Vision accuracy",
         shape="note")

# Connections
dot.edge("A", "B")
dot.edge("A", "C")
dot.edge("A", "D")

# Lighting
dot.edge("B", "B1")
dot.edge("B", "B2")
dot.edge("B", "B3")
dot.edge("B", "B4")

# Motion
dot.edge("C", "C1")
dot.edge("C", "C2")
dot.edge("C", "C3")
dot.edge("C", "C4")

# Environment
dot.edge("D", "D1")
dot.edge("D", "D2")
dot.edge("D", "D3")
dot.edge("D", "D4")

# Image Artifacts
dot.edge("B", "E")
dot.edge("C", "E")
dot.edge("D", "E")

dot.edge("E", "E1")
dot.edge("E", "E2")
dot.edge("E", "E3")
dot.edge("E", "E4")
dot.edge("E", "E5")

# Image Quality
dot.edge("E", "F")

dot.edge("F", "F1")
dot.edge("F", "F2")
dot.edge("F", "F3")
dot.edge("F", "F4")

# Computer Vision
dot.edge("F", "G")

dot.edge("G", "G1")
dot.edge("G", "G2")
dot.edge("G", "G3")
dot.edge("G", "G4")

# Literature
dot.edge("L", "L1", style="dashed")
dot.edge("L", "L2", style="dashed")
dot.edge("L", "L3", style="dashed")
dot.edge("L", "L4", style="dashed")

dot.edge("L", "B", style="dotted")
dot.edge("L", "C", style="dotted")
dot.edge("L", "D", style="dotted")
dot.edge("L", "E", style="dotted")
dot.edge("L", "G", style="dotted")

dot.render("Q12_Concept_Map", view=True)

print("Q12 Concept Map Generated Successfully!")
