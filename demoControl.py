from manim import *


def getGraphs(function1, function2, y_label, shift):
        axis = Axes(x_range=[0, 12], 
        y_range=[0, function2(10) + 0.1], 
        y_axis_config={"tip_width": 0.1, "tip_height": 0.1, "include_ticks": False, "include_numbers": True, "numbers_to_include": [0, function1(10)]} ,
        y_length=2,
        x_axis_config={"tip_width": 0.1, "tip_height": 0.1},
        x_length=10
        )
        axis_label = axis.get_axis_labels(
            Tex("x").scale(0.7), Tex(y_label).scale(0.45)
        )
        axis_group = VGroup(axis, axis_label)
        graph1 = axis.plot(lambda x: function1(x), color=BLUE, x_range=[0, 10])
        graph2 = axis.plot(lambda x: function2(x), color=RED, x_range=[0, 10])
        axis_group.shift(shift)
        graph1.shift(shift)
        graph2.shift(shift)
        # graph1_tip_text = Text('(10, 1)', font_size=25).next_to(graph1.get_end(), DOWN)
        # graph1 = VGroup(graph1, graph1_tip_text)
        # graph2_tip_text = Text('(10, 1.1)', font_size=25).next_to(graph2.get_end(), UP)
        # graph2 = VGroup(graph2, graph2_tip_text)
        return axis_group, graph1, graph2

class demoControl(Scene):
    def construct(self):
        accelerationAxisGroup, acceleration, control = getGraphs(lambda x: 1, lambda x: 1.1, "a(x)", UP * 2.5)
        
        velocityAxisGroup, velocity, velocityEstimation = getGraphs(lambda x: x, lambda x: 1.1 * x, "v(x)", 0)
        
        displacementAxisGroup, displacement, displacementEstimation = getGraphs(lambda x: x * x / 2, lambda x: 1.1 * x * x / 2, "d(x)", DOWN * 2.5)
        
        self.play(Create(accelerationAxisGroup))
        self.play(Create(acceleration))
        self.play(Create(velocityAxisGroup))
        self.play(Create(velocity))
        self.play(Create(displacementAxisGroup))
        self.play(Create(displacement))
        self.play(AnimationGroup(TransformFromCopy(acceleration, control), TransformFromCopy(velocity, velocityEstimation), TransformFromCopy(displacement, displacementEstimation)))
        self.wait(1)