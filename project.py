from pickle import TRUE
from re import S
from turtle import fillcolor
from manim import *
import numpy as np
import random
from manim_slides import Slide
import networkx as nx
# import matplotlib.pyplot as plt


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

        self.wait(1)
        self.makeGraph()

        #CReating Graph and MST
    def makeGraph(self):
        self.node_A = Dot(point=np.array([-5, -0.5, 0]))
        self.node_B = Dot(point=np.array([-2, 0.5, 0]))
        self.node_C = Dot(point=np.array([-2, -2.5, 0]))

        self.node_grp = Group(self.node_A,self.node_B,self.node_C)

        self.edge_1 = Line(self.node_grp[0],self.node_grp[1])
        self.edge_2 = Line(self.node_grp[1],self.node_grp[2])   
        self.edge_3 = Line(self.node_grp[0],self.node_grp[2])

        self.w_label1 = Tex("5", color=WHITE, font_size=30).shift(UP * 0.25 + 3.5 * LEFT)
        self.w_label2 = Tex("7", color=WHITE, font_size=30).shift(DOWN * 1.8 + 3.5 * LEFT)
        self.w_label3 = Tex("11", color=WHITE, font_size=30).shift(LEFT * 1.8 + DOWN * 1)

        self.Tnode1 = Tex("A", color=WHITE, font_size=30).next_to(self.node_A, LEFT)
        self.Tnode2 = Tex("B", color=WHITE, font_size=30).next_to(self.node_B, RIGHT)
        self.Tnode3 = Tex("C", color=WHITE, font_size=30).next_to(self.node_C, LEFT)

        self.nodeGrp = Group(self.node_A,self.node_B,self.node_C)
        self.play(FadeIn(self.nodeGrp))

        self.wait(1)
        self.play(Create(self.Tnode1), Create(self.Tnode2), Create(self.Tnode3))

        self.edgeGrp = Group(self.edge_1,self.edge_2,self.edge_3)
        self.play(FadeIn(self.edgeGrp))
        
        self.play(Write(self.w_label1), Write(self.w_label2), Write(self.w_label3))

        self.wait()

        #Making Middle Arrow
        arrow_3 = Arrow(start=LEFT, end=RIGHT)
        g2 = Group(arrow_3)
        g2.shift((0,-0.8,0))
        self.add(g2)
        self.wait()

        #Making MSt layout from Graph Above
        self.node_MA = Dot(point=np.array([-5, -0.5, 0]))
        self.node_MB = Dot(point=np.array([-2, 0.5, 0]))
        self.node_MC = Dot(point=np.array([-2, -2.5, 0]))
        
        self.node_MA.shift(RIGHT*7)
        self.node_MB.shift(RIGHT*7)
        self.node_MC.shift(RIGHT*7)

        self.Mnode1 = Tex("A", color=WHITE, font_size=30).next_to(self.node_MA, LEFT)
        self.Mnode2 = Tex("B", color=WHITE, font_size=30).next_to(self.node_MB, RIGHT)
        self.Mnode3 = Tex("C", color=WHITE, font_size=30).next_to(self.node_MC, LEFT)

        self.nodeGrp1 = Group(self.node_MA,self.node_MB,self.node_MC)
        self.play(FadeIn(self.nodeGrp1))

        self.wait(1)
        self.play(Create(self.Mnode1), Create(self.Mnode2), Create(self.Mnode3))

        #highliting the MST edges
        edge_M1 = Line(self.node_grp[0],self.node_grp[1])
        M_label1 = Tex("5", color=WHITE, font_size=30).shift(UP * 0.25 + 3.5 * LEFT)
        self.play(Create(edge_M1))
        edge_M1.set_color(color=RED)
        self.wait(1)
        self.play(edge_M1.animate.shift(RIGHT*7),M_label1.animate.shift(RIGHT*7))

        self.wait(1)

        edge_M2 = Line(self.node_grp[0],self.node_grp[2])
        M_label2 = Tex("7", color=WHITE, font_size=30).shift(DOWN * 1.8 + 3.5 * LEFT)
        self.play(Create(edge_M2))
        edge_M2.set_color(color=RED)
        self.wait(1)
        self.play(edge_M2.animate.shift(RIGHT*7),M_label2.animate.shift(RIGHT*7))
            
            