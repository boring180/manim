from manim import *

# Global constants

# Functions
def gaussian(x, mu, sigma):
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

def uniform(x, a, b):
    return 1 / (b - a) if a <= x <= b else 0 

class EKF(Scene):
    def construct(self):
        
        # Number line and axis
        belAxis = Axes(x_range=[0, 12], 
        y_range=[0, 1], 
        y_axis_config={"tip_width": 0.1, "tip_height": 0.1}, 
        y_length=2,
        x_axis_config={"tip_width": 0.1, "tip_height": 0.1},
        x_length=10
        )
        belAxisLabel = belAxis.get_axis_labels(
            Tex("x").scale(0.7), Text("bel(x)").scale(0.45)
        )
        
        
        measureAxis = Axes(x_range=[0, 12], 
        y_range=[0, 1], 
        y_axis_config={"tip_width": 0.1, "tip_height": 0.1}, 
        y_length=2,
        x_axis_config={"tip_width": 0.1, "tip_height": 0.1},
        x_length=10
        )
        measureAxisLabel = measureAxis.get_axis_labels(
            Tex("x").scale(0.7), Text("p(z | x)").scale(0.45)
        )
        
        l = NumberLine(x_range=[0, 12], include_numbers=False, include_tip=False, length=10)
        
        # Robot image
        robot = ImageMobject("robot.png")
        robot.height = 2
        robot.width = 2
        
        # init belief
        belAxisGroup = VGroup(belAxis, belAxisLabel)
        a = 0
        b = 10
        bel0 = belAxis.plot(lambda x: uniform(x, a, b), color=BLUE, x_range=[0, 10])
        
        # The first measurement
        meaAxis = VGroup(measureAxis, measureAxisLabel)
        mu = 1
        sigma = 1
        gaussianDistributionTag1 = measureAxis.plot(lambda x: gaussian(x, mu, sigma), color=RED, x_range=[0, 10])
        
        # After the first measurement
        mu = 1
        sigma = 0.75
        bel1 = measureAxis.plot(lambda x: gaussian(x, mu, sigma), color=RED, x_range=[0, 10])
        
        # The first update
        mu = 3
        sigma = 1
        bel2_hat = measureAxis.plot(lambda x: gaussian(x, mu, sigma), color=RED, x_range=[0, 10])
        
        # We imagine the world coordinate as a 1D number line, we are placing our robot on the line
        self.play(Create(l), runtime = 2)
        self.wait(2)
        
        # With no prior informtion, we have no idea about the robot's pose
        # self.add(robot)
        # In probability theory, this is called a uniform distribution
        initStateText = Text("Initial State")
        initStateText.to_corner(UL)
        self.add(initStateText)
        self.play(ReplacementTransform(l, belAxisGroup), runtime = 2)
        self.play(Create(bel0), runtime = 2)
        self.wait(2)
        
        # After a measurement, we have a better idea about the robot's pose
        # TODO: Make the animation smoother
        firstMeasurementText = Text("First Measurement")
        firstMeasurementText.to_corner(UL)
        self.replace(initStateText, firstMeasurementText)
        self.play(AnimationGroup(belAxisGroup.animate.shift(DOWN * 1.5), 
                                bel0.animate.shift(DOWN * 1.5)), 
                                runtime = 2)
        meaAxis.shift(UP * 1.5)
        gaussianDistributionTag1.shift(UP * 1.5)
        self.play(Create(meaAxis), runtime = 2)
        self.play(Create(gaussianDistributionTag1), runtime = 2)
        self.wait(2)
        
        # With the proir data, we can calculate the posterior distribution
        self.play(AnimationGroup(FadeTransform(bel0, bel1, stretch=False),
                                belAxisGroup.animate.shift(UP * 1.5),
                                FadeTransform(meaAxis, bel1, stretch=False),
                                FadeTransform(gaussianDistributionTag1, bel1, stretch=True),
                                ),runtime = 2)
        self.wait(2)
        
        # Update with wheel odometry
        firstUpdateText = Text("First update")
        firstUpdateText.to_corner(UL)
        self.replace(firstMeasurementText, firstUpdateText)
        self.play(Transform(bel1, bel2_hat, stretch=True), runtime = 2)
        self.wait(2)
        
        