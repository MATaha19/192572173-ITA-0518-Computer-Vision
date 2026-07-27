from graphviz import Digraph

dot = Digraph("Q10_Concept_Map", format="png")
dot.attr(rankdir="TB", splines="ortho", nodesep="0.5", ranksep="0.8")

# Main Node
dot.node("A", "Sampling", shape="box",
         style="filled", fillcolor="lightblue")

# Sampling
dot.node("B", "Sampling Rate", shape="box",
         style="filled", fillcolor="lightgreen")
dot.node("B1", "High Sampling Rate")
dot.node("B2", "Low Sampling Rate")

# Nyquist Theorem
dot.node("C", "Nyquist Sampling Theorem", shape="box",
         style="filled", fillcolor="lightyellow")
dot.node("C1", "Sampling ≥ 2 × Highest Frequency")
dot.node("C2", "Prevents Information Loss")

# Aliasing
dot.node("D", "Aliasing", shape="box",
         style="filled", fillcolor="lightskyblue")
dot.node("D1", "Jagged Edges")
dot.node("D2", "Moiré Pattern")
dot.node("D3", "False Patterns")
dot.node("D4", "Loss of Fine Details")

# Image Distortion
dot.node("E", "Image Distortion", shape="box",
         style="filled", fillcolor="orange")
dot.node("E1", "Blur")
dot.node("E2", "Artifacts")
dot.node("E3", "Reduced Image Quality")
dot.node("E4", "Incorrect Representation")

# Computer Vision
dot.node("F", "Computer Vision Performance", shape="box",
         style="filled", fillcolor="gold")
dot.node("F1", "Poor Feature Extraction")
dot.node("F2", "Recognition Errors")
dot.node("F3", "Reduced Detection Accuracy")
dot.node("F4", "Incorrect Decision Making")

# Literature
dot.node("L", "Theoretical Insights", shape="note",
         color="blue")
dot.node("L1", "Nyquist theorem minimizes aliasing",
         shape="note")
dot.node("L2", "Higher sampling preserves image details",
         shape="note")
dot.node("L3", "Aliasing reduces Computer Vision accuracy",
         shape="note")
dot.node("L4", "Proper sampling improves image quality",
         shape="note")

# Connections
dot.edge("A", "B")

dot.edge("B", "B1")
dot.edge("B", "B2")

dot.edge("B", "C")

dot.edge("C", "C1")
dot.edge("C", "C2")

dot.edge("C", "D")
dot.edge("B2", "D")

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

dot.edge("L", "C", style="dotted")
dot.edge("L", "D", style="dotted")
dot.edge("L", "E", style="dotted")
dot.edge("L", "F", style="dotted")

dot.render("Q10_Concept_Map", view=True)

print("Q10 Concept Map Generated Successfully!")
