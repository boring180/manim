from manim import *

def gaussian(x, mu, sigma):
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

def uniform(x, a, b):
    return 1 / (b - a) if a <= x <= b else 0 

class EKF(MovingCameraScene):
    def construct(self):
        
        # Number line and axis
        ax = Axes(x_range=[0, 12], y_range=[0, 1], 
        y_axis_config={"include_numbers": False, "tip_width": 0.1, "tip_height": 0.1}, 
        x_axis_config=({"length": 10, "tip_width": 0.1, "tip_height": 0.1})
        )
        l = NumberLine(x_range=[0, 12], include_numbers=False, include_tip=False, length=10)
        
        # uniform distribution
        a = 0
        b = 10
        uniformDistribution = ax.plot(lambda x: uniform(x, a, b), color=BLUE, x_range=[0, 10])
        
        # Gaussian distribution
        mu = 5
        sigma = 1
        gaussianDistributionTag1 = ax.plot(lambda x: gaussian(x, mu, sigma), color=RED, x_range=[0, 10])
        
        # Robot image
        robot= ImageMobject("robot.png")
        robot.height = 2
        robot.width = 2
        
        
        # We imagine the world coordinate as a 1D number line, we are placing our robot on the line
        self.play(Create(l), runtime = 2)
        self.wait()
        
        # With no prior informtion, we have no idea about the robot's pose
        # self.add(robot)
        # In probability theory, this is called a uniform distribution
        self.play(Transform(l, ax), runtime = 2)
        self.play(Create(uniformDistribution), runtime = 2)
        self.wait(1)