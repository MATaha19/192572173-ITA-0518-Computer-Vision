from graphviz import Digraph

dot = Digraph("Q11_Concept_Map", format="png")
dot.attr(rankdir="TB", splines="ortho", nodesep="0.5", ranksep="0.8")

# Main Node
dot.node("A", "Quantization Process", shape="box",
         style="filled", fillcolor="lightblue")

# Quantization
dot.node("B", "Quantization Levels", shape="box",
         style="filled", fillcolor="lightgreen")
dot.node("B1", "2-bit (4 Levels)")
dot.node("B2", "4-bit (16 Levels)")
dot.node("B3", "8-bit (256 Levels)")
dot.node("B4", "Higher Bit Depth")

# Intensity Resolution
dot.node("C", "Intensity Resolution", shape="box",
         style="filled", fillcolor="lightyellow")
dot.node("C1", "Gray Levels")
dot.node("C2", "Color Depth")
dot.node("C3", "Brightness Accuracy")
dot.node("C4", "Smooth Intensity Variation")

# Image Quality
dot.node("D", "Image Quality", shape="box",
         style="filled", fillcolor="lightskyblue")
dot.node("D1", "Better Contrast")
dot.node("D2", "Fine Details")
dot.node("D3", "Banding Effect")
dot.node("D4", "Quantization Error")

# Image Quality Degradation
dot.node("E", "Quality Degradation", shape="box",
         style="filled", fillcolor="orange")
dot.node("E1", "Information Loss")
dot.node("E2", "Poor Visual Appearance")
dot.node("E3", "Reduced Accuracy")
dot.node("E4", "Image Artifacts")

# Computer Vision
dot.node("F", "Computer Vision Performance", shape="box",
         style="filled", fillcolor="gold")
dot.node("F1", "Feature Extraction")
dot.node("F2", "Object Detection")
dot.node("F3", "Classification")
dot.node("F4", "Recognition Accuracy")

# Literature
dot.node("L", "Literature References", shape="note",
         color="blue")
dot.node("L1", "Higher bit depth preserves image details",
         shape="note")
dot.node("L2", "Low quantization increases information loss",
         shape="note")
dot.node("L3", "Higher intensity resolution improves recognition",
         shape="note")
dot.node("L4", "Quantization directly affects Computer Vision performance",
         shape="note")

# Connections
dot.edge("A", "B")

dot.edge("B", "B1")
dot.edge("B", "B2")
dot.edge("B", "B3")
dot.edge("B", "B4")

dot.edge("B", "C")

dot.edge("C", "C1")
dot.edge("C", "C2")
dot.edge("C", "C3")
dot.edge("C", "C4")

dot.edge("C", "D")

dot.edge("D", "D1")
dot.edge("D", "D2")
dot.edge("D", "D3")
dot.edge("D", "D4")

dot.edge("D", "E")

dot.edge("E", "E1")
dot.edge("E", "E2")
dot.edge("E", "E3")
dot.edge("E", "E4")

dot.edge("E", "F")

dot.edge("F", "F1")
dot.edge("F", "F2")
dot.edge("F", "F3")
dot.edge("F", "F4")

# Literature Connections
dot.edge("L", "L1", style="dashed")
dot.edge("L", "L2", style="dashed")
dot.edge("L", "L3", style="dashed")
dot.edge("L", "L4", style="dashed")

dot.edge("L", "B", style="dotted")
dot.edge("L", "C", style="dotted")
dot.edge("L", "D", style="dotted")
dot.edge("L", "F", style="dotted")

dot.render("Q11_Concept_Map", view=True)

print("Q11 Concept Map Generated Successfully!")
