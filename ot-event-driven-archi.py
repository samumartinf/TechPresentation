from manim import *
from manim_slides import Slide

class EventDrivenArchitecture(Slide):
    runtimeSpeed = 1.5
    def construct(self):
        # Set background color to dark gray instead of black
        self.camera.background_color = rgb_to_color((0.1, 0.1, 0.1))
        
        # Create title
        title = Text("Event Driven Architecture", color=WHITE, font_size=35)
        title.to_edge(UP + LEFT * 0.5, buff=0.5)
        
        # Create real-time indicator
        rt_box = Rectangle(height=0.4, width=1.8, color=GREEN, fill_opacity=0.2)
        rt_text = Text("REAL TIME", color=GREEN, font_size=20)
        rt_group = VGroup(rt_box, rt_text).arrange(ORIGIN, buff=0).to_edge(UP + RIGHT, buff=0.5)
        
        # Show title and real-time indicator with glow effect
        glow = rt_box.copy()
        glow.set_fill(GREEN, opacity=0.2)
        glow.set_stroke(GREEN, opacity=0.2)
        
        self.play(
            FadeIn(title),
            FadeIn(rt_group),
        )
        
        # Add subtle glow animation
        self.play(
            glow.animate.scale(1.3).set_opacity(0),
            rate_func=there_and_back,
            run_time=1
        )
        self.next_slide()

        self.play(FadeOut(glow))
        
        # Create Orchestrade main system
        orchestrade = Rectangle(height=3, width=4, color=RED_C, fill_opacity=0.1)
        orchestrade_label = Text("Orchestrade", color=RED_C, font_size=48).next_to(orchestrade, UP, buff=0.3)
        main_system = VGroup(orchestrade, orchestrade_label).move_to(LEFT * 4)
        
        # Initial animation
        self.play(Create(main_system), run_time=0.8)
        self.next_slide()
        
        # Create trade object
        trade = Square(side_length=0.5, color=BLUE, fill_opacity=0.1)
        trade_label = Text("Trade", font_size=24).next_to(trade, UP, buff=0.2)
        trade_group = VGroup(trade, trade_label).move_to(LEFT * 7)
        
        # Animate trade entering the system - faster animation
        self.play(FadeIn(trade_group), run_time=1/self.runtimeSpeed)
        self.play(
            trade_group.animate.move_to(orchestrade.get_center() + LEFT * 1),
            run_time=1/self.runtimeSpeed
        )
        self.next_slide()
        
        # Create envelope with faster animation
        envelope_points = [
            (-0.3, 0, 0),      # bottom left
            (0.3, 0, 0),       # bottom right
            (0.3, 0.4, 0),     # top right
            (-0.3, 0.4, 0),    # top left
            (-0.3, 0, 0),      # back to start to close the polygon
        ]

        envelope_top_points = [
            (-0.25, 0.4, 0),    # top left
            (0.25, 0.4, 0),     # top right
            (0, 0.2, 0),     # top middle point (flap)
            (-0.25, 0.4, 0),    # top left to close the polygon
        ]
        envelope = Polygon(*envelope_points, color=BLUE, fill_opacity=0.1)
        envelope_top = Polygon(*envelope_top_points, color=BLUE, fill_opacity=0.1)
        envelope_label = Text("Trade\nMessage", font_size=16, color=BLUE).next_to(envelope, UP, buff=0.1)
        message = VGroup(envelope, envelope_top, envelope_label).scale(1.3).move_to(orchestrade.get_center() + RIGHT * 0.5)
        
        # Animate message creation - faster
        self.play(Create(message), run_time=1/self.runtimeSpeed)
        self.next_slide()
        
        # Create RabbitMQ
        queue_box = Rectangle(height=3, width=2.5, color=GREEN, fill_opacity=0.1)
        queue_label = Text("RabbitMQ", color=GREEN, font_size=36).next_to(queue_box, UP, buff=0.3)
        queue_system = VGroup(queue_box, queue_label).move_to(RIGHT * 0)
        
        # Show RabbitMQ - faster
        self.play(Create(queue_system), run_time=1/self.runtimeSpeed)
        
        # Animate message going to RabbitMQ - faster with streak effect
        streak = message.copy().set_opacity(0.3)
        self.add(streak)
        self.play(
            message.animate.move_to(queue_box.get_center()),
            streak.animate.move_to(queue_box.get_center()).set_opacity(0),
            run_time=1/self.runtimeSpeed
        )
        self.remove(streak)
        self.next_slide()
        
        # Create duplicate message
        message_copy1 = message.copy()
        message_copy2 = message.copy()
        
        # Create consumers with larger boxes
        ot_service = Rectangle(height=2, width=2.5, color=RED_C, fill_opacity=0.1)
        ot_label = Text("OT Service", font_size=24, color=RED_C).next_to(ot_service, RIGHT, buff=0.4)
        ot_group = VGroup(ot_service, ot_label).move_to(RIGHT * 4 + UP * 2)
        
        custom_service = Rectangle(height=2, width=2.5, color=ORANGE, fill_opacity=0.1)
        custom_label = Text("Custom\n Service", font_size=24, color=ORANGE).next_to(custom_service, RIGHT, buff=0.4)
        custom_group = VGroup(custom_service, custom_label).move_to(RIGHT * 4 + DOWN * 2)
        
        # Show consumers - faster
        self.play(
            Create(ot_group),
            Create(custom_group),
            run_time=1/self.runtimeSpeed
        )
        
        # Animate message duplication and delivery - faster with streak effects
        streak1 = message_copy1.copy().set_opacity(0.3)
        streak2 = message_copy2.copy().set_opacity(0.3)
        self.add(streak1, streak2)
        
        self.play(
            message_copy1.animate.move_to(ot_service.get_center()),
            streak1.animate.move_to(ot_service.get_center()).set_opacity(0),
            run_time=1/self.runtimeSpeed
        )
        self.play(
            message_copy2.animate.move_to(custom_service.get_center()),
            streak2.animate.move_to(custom_service.get_center()).set_opacity(0),
            run_time=1/self.runtimeSpeed
        )
        self.remove(streak1, streak2)
        self.next_slide()
        
        # Final state
        self.wait(1)
