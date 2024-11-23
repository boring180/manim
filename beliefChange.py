from manim import *

# Global constants

# Functions
def gaussian(x, mu, sigma):
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

def uniform(x, a, b):
    return 1 / (b - a) if a <= x <= b else 0 

class beliefChange(Scene):
    def measurementUpdate(self, bel, bel_axis_group, mu, sigma, text):
        new_text = Text("Measurement Update")
        new_text.to_corner(UL)
        self.play(AnimationGroup(bel.animate.shift(DOWN * 1.5), bel_axis_group.animate.shift(DOWN * 1.5), Transform(text, new_text)), runtime = 2)
        
        z_axis = Axes(x_range=[0, 12], 
        y_range=[0, 1], 
        y_axis_config={"tip_width": 0.1, "tip_height": 0.1}, 
        y_length=2,
        x_axis_config={"tip_width": 0.1, "tip_height": 0.1},
        x_length=10
        )
        z_axis_label = z_axis.get_axis_labels(
            Tex("x").scale(0.7), Text("p(z | x)").scale(0.45)
        )
        
        z_axis_group = VGroup(z_axis, z_axis_label)
        z = z_axis.plot(lambda x: gaussian(x, mu, sigma), color=RED, x_range=[0, 10])
        z.shift(UP * 1.5)
        z_axis_group.shift(UP * 1.5)
        
        self.play(Create(z_axis_group), runtime = 2)
        self.play(Create(z), runtime = 2)
        
        return z, bel, z_axis_group
    
    def fusion(self, bel, bel_axis_group, z, z_axis_group, mu, sigma):
        new_bel = self.bel_axis.plot(lambda x: gaussian(x, mu, sigma), color=RED, x_range=[0, 10])
        
        new_bel.shift(UP * 1.5)
        self.play(AnimationGroup(Transform(bel, new_bel), Transform(z, new_bel), FadeOut(z_axis_group), bel_axis_group.animate.shift(UP * 1.5)), runtime = 2)
        self.remove(z)

        return bel
    
    def update(self, bel, mu, sigma, text):
        new_text = Text("State Update")
        new_text.to_corner(UL)
        new_bel = self.bel_axis.plot(lambda x: gaussian(x, mu, sigma), color=RED, x_range=[0, 10])
        
        self.play(AnimationGroup(Transform(bel, new_bel), Transform(text, new_text)), runtime = 2)
        
        return bel
    
    def construct(self):
        
        # Number line and axis
        self.bel_axis = Axes(x_range=[0, 12], 
        y_range=[0, 1], 
        y_axis_config={"tip_width": 0.1, "tip_height": 0.1}, 
        y_length=1.5,
        x_axis_config={"tip_width": 0.1, "tip_height": 0.1},
        x_length=10
        )
        bel_axis_label = self.bel_axis.get_axis_labels(
            Tex("x").scale(0.7), Text("bel(x)").scale(0.45)
        )
        
        
        l = NumberLine(x_range=[0, 12], include_numbers=False, include_tip=False, length=10)
        
        
        bel_axis_group = VGroup(self.bel_axis, bel_axis_label)
        
        # init belief
        a = 0
        b = 10
        bel = self.bel_axis.plot(lambda x: uniform(x, a, b), color=BLUE, x_range=[0, 10])
        
        # # The first measurement
        # meaAxis = VGroup(measureAxis, measureAxisLabel)
        # mu = 1
        # sigma = 1
        # gaussianDistributionTag1 = measureAxis.plot(lambda x: gaussian(x, mu, sigma), color=RED, x_range=[0, 10])
        
        # # After the first measurement
        # mu = 1
        # sigma = 0.75
        # bel1 = measureAxis.plot(lambda x: gaussian(x, mu, sigma), color=RED, x_range=[0, 10])
        
        # # The first update
        # mu = 4
        # sigma = 1.25
        # bel2_hat = measureAxis.plot(lambda x: gaussian(x, mu, sigma), color=RED, x_range=[0, 10])
        
        # # The second measurement
        # mu = 4
        # sigma = 1
        # gaussianDistributionTag2 = measureAxis.plot(lambda x: gaussian(x, mu, sigma), color=RED, x_range=[0, 10])
        
        # # After the second measurement
        # mu = 4
        # sigma = 0.25
        # bel2 = measureAxis.plot(lambda x: gaussian(x, mu, sigma), color=RED, x_range=[0, 10])
        
        # # The second update
        # mu = 6
        # sigma = 0.5
        # bel3_hat = measureAxis.plot(lambda x: gaussian(x, mu, sigma), color=RED, x_range=[0, 10])
        
        # We imagine the world coordinate as a 1D number line, we are placing our robot on the line
        self.play(Create(l), runtime = 2)
        self.wait(2)
        
        # With no prior informtion, we have no idea about the robot's pose
        # self.add(robot)
        # In probability theory, this is called a uniform distribution
        text = Text("Initial State")
        text.to_corner(UL)
        self.add(text)
        self.play(ReplacementTransform(l, bel_axis_group), runtime = 2)
        self.wait(2)
        
        self.play(Create(bel), runtime = 2)
        self.wait(2)
        
        z, bel, z_axis_group = self.measurementUpdate(bel, bel_axis_group, 1, 1, text)
        bel = self.fusion(bel, bel_axis_group, z, z_axis_group, 1, 0.75)
        bel = self.update(bel, 4, 1.25, text)