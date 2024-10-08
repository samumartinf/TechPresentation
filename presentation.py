from manim import *
from manim_slides import Slide

class ProtoBufVisualization(Slide):
    def construct(self):
        # Slide: Serialization Challenge Visualization
        self.next_slide()
        
        # Create service A and B with adjusted size
        service_a = Rectangle(width=3.5, height=2.5, color=BLUE).shift(LEFT * 3)
        service_b = Rectangle(width=3.5, height=2.5, color=GREEN).shift(RIGHT * 3)
        label_a = Text("Service A", font_size=28).next_to(service_a, UP, buff=0.5)
        label_b = Text("Service B", font_size=28).next_to(service_b, UP, buff=0.5)
        
        # Show services
        self.play(FadeIn(service_a), FadeIn(service_b), Write(label_a), Write(label_b))
        
        # Add version text below services
        version_a = Text("Version 1.0.1", font_size=20, color=GRAY).next_to(service_a, DOWN, buff=0.3)
        version_b = Text("Version 1.0.2", font_size=20, color=GRAY).next_to(service_b, DOWN, buff=0.3)
        self.play(Write(version_a), Write(version_b))
        
        # Show communication line
        line = Arrow(service_a.get_right(), service_b.get_left(), buff=0.1)
        self.play(GrowArrow(line))
        
        # Highlight serialization challenge
        challenge_text = Text("Serialization Challenge", font_size=24, color=RED).to_corner(UL)
        self.play(Write(challenge_text))
        self.wait(2)
        
        # Animate object passing from Service A to Service B
        object_circle = Circle(radius=0.2, fill_color=WHITE, fill_opacity=1, color=BLUE).move_to(service_a.get_center())
        self.play(FadeIn(object_circle))
        self.play(object_circle.animate.move_to(service_b.get_center()), run_time=2)
        self.play(object_circle.animate.set_fill(RED), run_time=1)
        self.wait(1)
        
        # Transition to solution
        self.next_slide()
        solution_text = Text("Multiple ProtoBuf Serializers", font_size=24, color=GREEN).to_corner(UL)
        self.play(Transform(challenge_text, solution_text))
        
        # Remove the old line and object
        self.play(FadeOut(line), FadeOut(object_circle))
        
        # Show new green arrows for multiple ProtoBuf serializers
        arrow1 = Arrow(service_a.get_right(), service_b.get_left(), buff=0.1, color=GREEN).shift(UP * 0.2)
        arrow2 = Arrow(service_a.get_right(), service_b.get_left(), buff=0.1, color=GREEN).shift(DOWN * 0.2)
        self.play(GrowArrow(arrow1), GrowArrow(arrow2))
        
        # Animate new object passing from Service A to Service B
        new_object_circle = Circle(radius=0.2, fill_color=WHITE, fill_opacity=1, color=BLUE).move_to(service_a.get_center())
        self.play(FadeIn(new_object_circle))
        self.play(new_object_circle.animate.move_to(service_b.get_center()), run_time=2)
        self.play(new_object_circle.animate.set_fill(GREEN).set_color(GREEN), run_time=1)
        # Finalize
        self.wait(2)
