from graphviz import Digraph

dot = Digraph("Q5_Concept_Map", format="png")
dot.attr(rankdir="TB", splines="ortho", nodesep="0.5", ranksep="0.8")

# Main Node
dot.node("A", "Computer Vision System Capabilities",
         shape="box", style="filled", fillcolor="lightblue")

# Hardware
dot.node("B", "Hardware Capabilities",
         shape="box", style="filled", fillcolor="lightgreen")
dot.node("B1", "CPU")
dot.node("B2", "GPU")
dot.node("B3", "Memory")
dot.node("B4", "Camera")
dot.node("B5", "Image Sensor")

# Software
dot.node("C", "Software Capabilities",
         shape="box", style="filled", fillcolor="lightgreen")
dot.node("C1", "Image Processing")
dot.node("C2", "Machine Learning")
dot.node("C3", "Deep Learning")
dot.node("C4", "Feature Extraction")
dot.node("C5", "Object Detection")

# Data
dot.node("D", "Data Capabilities",
         shape="box", style="filled", fillcolor="lightyellow")
dot.node("D1", "Dataset Size")
dot.node("D2", "Image Quality")
dot.node("D3", "Annotation")
dot.node("D4", "Data Diversity")

# Performance
dot.node("E", "Performance Metrics",
         shape="box", style="filled", fillcolor="lightskyblue")
dot.node("E1", "Accuracy")
dot.node("E2", "Speed")
dot.node("E3", "Robustness")
dot.node("E4", "Scalability")
dot.node("E5", "Real-Time Processing")

# Vision Applications
dot.node("F", "Vision-Based Applications",
         shape="box", style="filled", fillcolor="orange")
dot.node("F1", "Medical Imaging")
dot.node("F2", "Autonomous Vehicles")
dot.node("F3", "Face Recognition")
dot.node("F4", "Industrial Automation")
dot.node("F5", "Agriculture")
dot.node("F6", "Surveillance")
dot.node("F7", "Robotics")

# Effectiveness
dot.node("G", "Application Effectiveness",
         shape="box", style="filled", fillcolor="gold")
dot.node("G1", "Reliable Decisions")
dot.node("G2", "Automation")
dot.node("G3", "High Accuracy")
dot.node("G4", "Reduced Human Error")
dot.node("G5", "Improved Safety")

# Literature
dot.node("L", "Literature Perspectives",
         shape="note", color="blue")
dot.node("L1", "Powerful hardware improves inference speed",
         shape="note")
dot.node("L2", "High-quality datasets improve accuracy",
         shape="note")
dot.node("L3", "Efficient algorithms increase robustness",
         shape="note")
dot.node("L4", "Real-time processing improves application performance",
         shape="note")
dot.node("L5", "Integrated hardware and software enhance system capability",
         shape="note")

# Connections
dot.edge("A","B")
dot.edge("A","C")
dot.edge("A","D")
dot.edge("A","E")

# Hardware
dot.edge("B","B1")
dot.edge("B","B2")
dot.edge("B","B3")
dot.edge("B","B4")
dot.edge("B","B5")

# Software
dot.edge("C","C1")
dot.edge("C","C2")
dot.edge("C","C3")
dot.edge("C","C4")
dot.edge("C","C5")

# Data
dot.edge("D","D1")
dot.edge("D","D2")
dot.edge("D","D3")
dot.edge("D","D4")

# Performance
dot.edge("E","E1")
dot.edge("E","E2")
dot.edge("E","E3")
dot.edge("E","E4")
dot.edge("E","E5")

# System → Applications
dot.edge("B","F")
dot.edge("C","F")
dot.edge("D","F")
dot.edge("E","F")

# Applications
dot.edge("F","F1")
dot.edge("F","F2")
dot.edge("F","F3")
dot.edge("F","F4")
dot.edge("F","F5")
dot.edge("F","F6")
dot.edge("F","F7")

# Effectiveness
dot.edge("F","G")
dot.edge("G","G1")
dot.edge("G","G2")
dot.edge("G","G3")
dot.edge("G","G4")
dot.edge("G","G5")

# Literature
dot.edge("L","L1", style="dashed")
dot.edge("L","L2", style="dashed")
dot.edge("L","L3", style="dashed")
dot.edge("L","L4", style="dashed")
dot.edge("L","L5", style="dashed")

dot.edge("L","A", style="dotted")
dot.edge("L","F", style="dotted")
dot.edge("L","G", style="dotted")

dot.render("Q5_Concept_Map", view=True)

print("Q5 Concept Map Generated Successfully!")
