from manim import *

class robotDemo(Scene):
    def construct(self):
        # Robot scan the first AprilTag and says "I see AprilTag 0"
        robot = ImageMobject("robot.png")
        robot.height = 2
        robot.width = 2
        robot.move_to(LEFT * 3)
        self.play(FadeIn(robot))
        self.wait(1)
        self.play(robot.animate.move_to(LEFT * 2))
        self.wait(1)