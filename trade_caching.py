from manim import *
from manim_slides import Slide

class TradeCachingPresentation(Slide):
    def construct(self):
        # Slide: Trade Caching Challenge
        self.next_slide()
        
        # Create multiple OrchServer instances
        orch_servers = VGroup(
            *[Rectangle(width=3, height=1, color=BLUE) for _ in range(3)]
        ).arrange(DOWN, buff=0.5).shift(LEFT * 3)
        
        labels = VGroup(
            *[Text(f"OrchServer {i+1}", font_size=24).move_to(orch_servers[i].get_center()) for i in range(3)]
        )
        
        # Show OrchServer instances
        self.play(FadeIn(orch_servers), Write(labels))
        
        # Add trade cache text inline with each OrchServer
        trade_caches = VGroup(
            *[Text("80GB Trade Cache", font_size=20, color=GRAY).next_to(orch_servers[i], RIGHT, buff=0.5) for i in range(3)]
        )
        self.play(Write(trade_caches))
        
        # Highlight the challenge
        challenge_text = Text("Trade Caching Challenge", font_size=24, color=RED).to_corner(UL)
        self.play(Write(challenge_text))
        self.wait(2)
        
        # Transition to solution
        self.next_slide()
        solution_text = Text("Centralized Trade Cache Solution", font_size=24, color=GREEN).to_corner(UL)
        self.play(Transform(challenge_text, solution_text))
        
        # Animate trade caches moving to centralized cache
        centralized_cache = Rectangle(width=4, height=2, color=GREEN).shift(RIGHT * 4)
        cache_label = Text("Centralized Trade Cache", font_size=24).next_to(centralized_cache, UP, buff=0.3)
        self.play(FadeIn(centralized_cache), Write(cache_label))
        
        # Move trade caches to centralized cache
        for trade_cache in trade_caches:
            self.play(trade_cache.animate.move_to(centralized_cache.get_center()), run_time=1)
        
        # Connect OrchServers to centralized cache
        connections = VGroup(
            *[Arrow(orch_servers[i].get_right(), centralized_cache.get_left(), buff=0.1, color=GREEN) for i in range(3)]
        )
        for arrow in connections:
            self.play(GrowArrow(arrow))
        
        # Finalize
        self.wait(2)
