import manim as mn
from manim import *


config.media_width = "75%"
config.verbosity = "WARNING"

print(mn.__version__)

class CreateCircle(InteractiveScene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE_E, opacity=0.5)
        circle.move_to(ORIGIN)

        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": WHITE},
        )
        axes.add_coordinates()
        axes.set_color(WHITE)
        
 
        self.add(circle)  
        self.begin_ambient_camera_rotation(rate=0.5, about='phi')   
        self.wait(10)