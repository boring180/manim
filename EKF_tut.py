from manimlib import *

def Gaussian(x, miu, sigma):
    return 1 / (math.sqrt(2 * math.pi) * sigma) * math.exp(-1/2 * ((x - miu) / sigma) ** 2)

class N(Scene):
    def construct(self):
        axes = Axes((-5, 5), (-0.5, 1))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        miu = 2
        sigma = 0.5
        # Axes.get_graph will return the graph of a function
        Gaussian1 = axes.get_graph(
            lambda x: Gaussian(x, miu, sigma),
            color=BLUE,
        )
        
        # sin_label = axes.get_graph_label(sin_graph, Text("X~N(2, 0.5)"))
        
        miu = 0
        sigma = 0.75
        # Axes.get_graph will return the graph of a function
        Gaussian2 = axes.get_graph(
            lambda x: Gaussian(x, miu, sigma),
            color=BLUE,
        )
        
        # sin_label = axes.get_graph_label(sin_graph, Text("X~N(2, 0.5)"))

        self.play(
            ShowCreation(Gaussian1),
            # FadeIn(sin_label, RIGHT),
        )
        
        self.wait(2)
        
        self.play(
            ReplacementTransform(Gaussian1, Gaussian2),
            # FadeTransform(sin_label, relu_label),
        )
        
        self.wait(2)

        self.wait()