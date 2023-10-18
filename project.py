from curses.textpad import Textbox
from pickle import TRUE
from re import S
from turtle import fillcolor
from manim import *
import numpy as np
import random
from manim_slides import Slide
import networkx as nx
import matplotlib.pyplot as plt


class intro(Slide):
    def construct(self):
        
        header = MarkupText(
            f'Greedy Algorithm',font="Britannic Bold",font_size=80
        )

      
        header2 = MarkupText(f'MST Krushkal\'s Algorithm',font="Britannic Bold",font_size=80 )

        self.play(Write(header))
        self.play(RemoveTextLetterByLetter(header))
        self.play(Write(header2))
        self.clear()
        self.next_slide()
        
        #What is MST 
        mst_text1 = ["What","Is","MST ?"]
      
        # Create dot groups
        
        groups = VGroup(*[MarkupText(text) for text  in mst_text1]).arrange_submobjects(buff=0.3)
        self.play(Write(groups))
  
        self.play(groups.animate(run_time=1, lag_ratio=0.1).shift(UP*3.2,LEFT*3.9))
        START = (-6.3,2.7,0)
        END = (4,2.7,0)
        line = Line(START,END,color=YELLOW)
        self.play(Create(line))

        definition = MarkupText(f'A minimum spanning tree (MST) is defined as a spanning tree that has the minimum weight among all the possible spanning trees.',font_size=60,width=12).to_edge(UP,buff=1.6)
        definition.to_edge(LEFT,buff=0.95)
    
        self.play(Write(definition))

        #CReating Graph

        vertices = [1, 2, 3]
        edges = [(1, 2), (2, 3), (1, 3)]
        lt = {1: [0.3, 0, 0], 2: [-2, 1.5, 0], 3: [-2, -1.5, 0]}
        labels = "ABC"
        label_dict = {i: label for i, label in zip(vertices, labels)}
        g = Graph(vertices,edges,labels=label_dict,layout= lt)
        g.shift((-3,-0.8,0))
        self.play(Create(g))
        
        self.wait()
        