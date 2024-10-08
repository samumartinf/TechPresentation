from manim import *
from manim_slides import Slide

class DeploymentPresentation(Slide):
    def construct(self):
        # Slide: Streamlining Deployments
        self.next_slide()
        
        # Title
        title = Text("Streamlining Deployments with Docker", font_size=24, color=BLUE).to_corner(UL)
        self.play(Write(title))
        
        # Show Docker containers for Production (Blue) environment
        prod_containers = VGroup(
            *[Rectangle(width=2, height=1, color=BLUE) for _ in range(3)]
        ).arrange(RIGHT, buff=0.5).shift(UP * 2)
        
        prod_labels = VGroup(
            *[Text(f"Prod {i+1}", font_size=20).move_to(prod_containers[i].get_center()) for i in range(3)]
        )
        
        self.play(FadeIn(prod_containers), Write(prod_labels))
        
        # Show Docker containers for UAT (Green) environment
        uat_containers = VGroup(
            *[Rectangle(width=2, height=1, color=GREEN) for _ in range(3)]
        ).arrange(RIGHT, buff=0.5).shift(DOWN * 2)
        
        uat_labels = VGroup(
            *[Text(f"UAT {i+1}", font_size=20).move_to(uat_containers[i].get_center()) for i in range(3)]
        )
        
        self.play(FadeIn(uat_containers), Write(uat_labels))
        
        # Highlight Blue-Green Deployment
        bg_text = Text("StandardDeployment", font_size=24, color=YELLOW).to_corner(UR)
        self.play(Write(bg_text))
        self.wait(2)
        
        # Continuous operation indicator
        orchestrade_text = Text("Orchestrade", font_size=24, color="#D1244D").shift(LEFT * 5 + UP * 0.5)
        cog = ImageMobject("cog.png").scale(0.2).next_to(orchestrade_text, DOWN, buff=0.2)
        cog.set_color("#D1244D")  # Set the cog color to match the Orchestrade text
        self.play(FadeIn(orchestrade_text), FadeIn(cog))

        # Start rotating the cog
        cog.add_updater(lambda c: c.rotate(0.025))
        self.wait(2)  # Let the cog rotate visibly before stopping it
        
        # Transition to previous status where Orchestrade stops
        self.next_slide()
        previous_status_title = Text("Previous Status: Full Stop for Upgrades", font_size=24, color=BLUE).to_corner(UL)
        self.play(Transform(title, previous_status_title))
        
        # Stop the cog and turn Orchestrade text and cog gray
        cog.clear_updaters()
        self.play(
            orchestrade_text.animate.set_color(GRAY),
            cog.animate.set_color(GRAY),
            run_time=2
        )
        
        # Show simultaneous upgrade process
        self.next_slide()
        upgrade_title = Text("Simultaneous Upgrade Process", font_size=24, color=BLUE).to_corner(UL)
        self.play(Transform(title, upgrade_title))
        
        # Animate all UAT containers being promoted to Production simultaneously
        self.play(
            *[uat_containers[i].animate.shift(UP * 4).set_color(BLUE) for i in range(3)],
            run_time=2
        )
        
        # Restart the cog and change color back to original
        self.play(
            orchestrade_text.animate.set_color("#D1244D"),
            cog.animate.set_color("#D1244D"),
            run_time=2
        )
        cog.add_updater(lambda c: c.rotate(0.025))

        restart_text = Text("Restart OT with the new version", font_size=24, color=BLUE).to_corner(UL)
        self.play(Transform(title, restart_text))
        self.wait(2)
        

        # Clear the screen before the new approach
        self.clear()

        # The new approach with Blue-Green Deployment
        self.next_slide()
        title = Text("Streamlining Deployments with Docker", font_size=24, color=BLUE).to_corner(UL)
        self.play(Write(title))
        bg_text = Text("Blue-Green Deployment", font_size=24, color=YELLOW).to_corner(UR)
        self.play(Write(bg_text))

        # Show the new approach with Blue-Green Deployment
        prod_containers = VGroup(
            *[Rectangle(width=2, height=1, color=BLUE) for _ in range(3)]
        ).arrange(RIGHT, buff=0.5).shift(UP * 2)
        
        prod_labels = VGroup(
            *[Text(f"Prod {i+1}", font_size=20).move_to(prod_containers[i].get_center()) for i in range(3)]
        )
        
        self.play(FadeIn(prod_containers), Write(prod_labels))
        
        # Show Docker containers for UAT (Green) environment
        uat_containers = VGroup(
            *[Rectangle(width=2, height=1, color=GREEN) for _ in range(3)]
        ).arrange(RIGHT, buff=0.5).shift(DOWN * 2)
        
        uat_labels = VGroup(
            *[Text(f"UAT {i+1}", font_size=20).move_to(uat_containers[i].get_center()) for i in range(3)]
        )
        
        self.play(FadeIn(uat_containers), Write(uat_labels))
        
        # Continuous operation indicator
        orchestrade_text = Text("Orchestrade", font_size=24, color="#D1244D").shift(LEFT * 5 + UP * 0.5)
        cog = ImageMobject("cog.png").scale(0.2).next_to(orchestrade_text, DOWN, buff=0.2)
        cog.set_color("#D1244D")  # Set the cog color to match the Orchestrade text
        self.play(FadeIn(orchestrade_text), FadeIn(cog))

        # Start rotating the cog
        cog.add_updater(lambda c: c.rotate(0.025))

        mixed_bag_title = Text("Running with Mixed Versions", font_size=24, color=BLUE).to_corner(UL)
        self.play(Transform(title, mixed_bag_title))

        # Migrate one by one the containers from UAT to Production
        for i in range(3):
            self.play(
                uat_containers[i].animate.shift(UP * 4).set_color(BLUE),
                run_time=2
            )

            