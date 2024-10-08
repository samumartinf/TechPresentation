from manim import *
from manim_slides import Slide

# class TechRoadmapPresentation(Slide):
#     def construct(self):
#         # Slide 1: Title
#         self.next_slide()
#         title = Text("Orchestrade Technology Roadmap")
#         self.play(Write(title))
#         self.wait()

#         # Slide 2: Current Architecture Overview
#         self.next_slide()
#         current_architecture = Text("Current Architecture Overview")
#         self.play(Transform(title, current_architecture))
#         self.wait()

#         # Slide 3: Serialization Challenge Visualization
#         self.next_slide()
#         challenge = Text("Serialization Challenge Visualization")
#         self.play(Transform(title, challenge))
#         self.wait()

#         # Add more slides following the same pattern
#         # ...

#         # Final Slide: Roadmap Summary
#         self.next_slide()
#         summary = Text("Roadmap Summary")
#         self.play(Transform(title, summary))
#         self.wait()

class ProtoBufVisualization(Slide):
    def construct(self):
        # Slide: Serialization Challenge Visualization
        self.next_slide()
        
        # Create service A and B with adjusted size
        service_a = Rectangle(width=3.5, height=2.5, color=BLUE).shift(LEFT * 3)
        service_b = Rectangle(width=3.5, height=2.5, color=GREEN).shift(RIGHT * 3)
        label_a = Text("Service A\n(Version 1.0)", font_size=28).next_to(service_a, UP, buff=0.5)
        label_b = Text("Service B\n(Version 1.1)", font_size=28).next_to(service_b, UP, buff=0.5)
        
        # Add hints about DLL version differences
        hint_a = Text("Using DLLs: v1.0", font_size=20).next_to(service_a, DOWN, buff=0.5)
        hint_b = Text("Using DLLs: v1.1", font_size=20).next_to(service_b, DOWN, buff=0.5)
        
        self.play(Write(label_a), Write(label_b), Write(hint_a), Write(hint_b))
        
        # Show services
        self.play(FadeIn(service_a), FadeIn(service_b), Write(label_a), Write(label_b))
        
        # Show communication line
        line = Arrow(service_a.get_right(), service_b.get_left(), buff=0.1)
        self.play(GrowArrow(line))
        
        # Highlight serialization challenge
        challenge_text = Text("Serialization Challenge", font_size=24, color=RED).next_to(line, UP, buff=0.5)
        self.play(Write(challenge_text))
        self.wait(2)
        
        # Transition to solution
        self.next_slide()
        solution_text = Text("Multiple ProtoBuf Serializers", font_size=24, color=YELLOW).next_to(line, UP, buff=0.5)
        self.play(Transform(challenge_text, solution_text))
        
        # Indicate seamless communication
        seamless_line = Arrow(service_a.get_right(), service_b.get_left(), buff=0.1, color=YELLOW)
        self.play(Transform(line, seamless_line))
        
        # Finalize
        self.wait(2)
