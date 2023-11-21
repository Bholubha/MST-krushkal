from pickle import TRUE
from re import S
from turtle import fillcolor
from manim import *
import numpy as np
import random
from manim_slides import Slide
import networkx as nx

class findUnion(Slide):
    def construct(self):
        text1 = ["What "," Is "," The ", " Problem ", " ?"]
      
        # Create dot groups
        groups = VGroup(*[MarkupText(text) for text  in text1]).arrange_submobjects(buff=0.3)
        self.play(Write(groups))

        self.play(groups.animate(run_time=1, lag_ratio=0.1).shift(UP*3.2 + LEFT * 2.5))
        START = (-6.3,2.7,0)
        END = (4,2.7,0)
        line = Line(START,END,color=YELLOW)
        self.play(Create(line))

        # Problem text
        text1 = Text("The Problem :",stroke_width = 1,color=BLUE,font_size=25).move_to([-5,2.2,0])
        self.play(Write(text1))
        text2 = Text("For an edge (u,v), how do we find that u and v are in the same \nconnected component ?",font_size = 25,color=WHITE).move_to([1.2,2,0])
        self.play(Write(text2))

        # Solution text
        text3 = Text("The Solution :",stroke_width = 1,color=BLUE,font_size=25).move_to([-5,1.2,0])
        self.play(Write(text3))
        text4 = Text("All vertices in the same connected component have the same label.",font_size = 25,color=WHITE).move_to([1.3,1.2,0])
        self.play(Write(text4))

        self.play(FadeOut(text1,text2))

        text3.shift(UP * 1)
        text4.shift(UP * 1)
        self.play(FadeIn(text3),FadeIn(text4))

        #The vertices graph 
        node_1 = LabeledDot(Text("1",color=RED,font_size=20),point=np.array([-2 , 1, 0]))
        node_2 = LabeledDot(Text("2",color=RED,font_size=20),point=np.array([0, 2, 0]))
        node_3 = LabeledDot(Text("3",color=RED,font_size=20),point=np.array([0, -1, 0]))
        node_4 = LabeledDot(Text("4",color=RED,font_size=20),point=np.array([2, 1, 0]))
        node_5 = LabeledDot(Text("5",color=RED,font_size=20),point=np.array([3, -1, 0]))
        node_6 = LabeledDot(Text("6",color=RED,font_size=20),point=np.array([4, 0.6, 0]))
        node_7 = LabeledDot(Text("7",color=RED,font_size=20),point=np.array([3, 3, 0]))
        node_8 = LabeledDot(Text("8",color=RED,font_size=20),point=np.array([5, -1, 0]))
        node_9 = LabeledDot(Text("9",color=RED,font_size=20),point=np.array([6, 0.6, 0]))

        self.node_grp = Group(node_1,node_2,node_3,node_4,node_5,node_6,node_7,node_8,node_9)
        self.node_grp.scale(0.7)
        self.node_grp.shift(DOWN * 1 + LEFT * 2)
        self.play(FadeIn(self.node_grp))

        #The array code

        findArr = Rectangle(height=0.6, width=9, grid_xstep=1)
        findArr.shift(DOWN*2.5)
        mobj = VGroup()

        t1 = Text("1",font_size=20).move_to(findArr).shift(LEFT * 4)
        t2 = Text("2",font_size=20).move_to(findArr).shift(LEFT * 3)
        t3 = Text("3",font_size=20).move_to(findArr).shift(LEFT * 2)
        t4 = Text("4",font_size=20).move_to(findArr).shift(LEFT * 1)
        t5 = Text("5",font_size=20).move_to(findArr)
        t6 = Text("6",font_size=20).move_to(findArr).shift(RIGHT * 1)
        t7 = Text("7",font_size=20).move_to(findArr).shift(RIGHT * 2)
        t8 = Text("8",font_size=20).move_to(findArr).shift(RIGHT * 3)
        t9 = Text("9",font_size=20).move_to(findArr).shift(RIGHT * 4)
        
        
        l1 = Text("1",font_size=20,color=BLUE).shift(LEFT * 4 + DOWN * 3)
        l2 = Text("2",font_size=20,color=BLUE).shift(LEFT * 3 + DOWN * 3)
        l3 = Text("3",font_size=20,color=BLUE).shift(LEFT * 2 + DOWN * 3)
        l4 = Text("4",font_size=20,color=BLUE).shift(LEFT * 1 + DOWN * 3)
        l5 = Text("5",font_size=20,color=BLUE).shift(DOWN * 3)
        l6 = Text("6",font_size=20,color=BLUE).shift(RIGHT * 1 + DOWN * 3)
        l7 = Text("7",font_size=20,color=BLUE).shift(RIGHT * 2 + DOWN * 3)
        l8 = Text("8",font_size=20,color=BLUE).shift(RIGHT * 3 + DOWN * 3)
        l9 = Text("9",font_size=20,color=BLUE).shift(RIGHT * 4 + DOWN * 3)
                
        mobj.add(findArr,t1,t2,t3,t4,t5,t6,t7,t8,t9,l1,l2,l3,l4,l5,l6,l7,l8,l9)
        self.play(FadeIn(mobj))


        e1 = Line(self.node_grp[3],self.node_grp[4])
        self.play(FadeIn(e1))
        self.play(FadeOut(node_5),FadeOut(t5))
        node_5 = LabeledDot(Text("4",color=RED,font_size=20),point=np.array([3, -1, 0]))
        node_5.scale(0.7)
        node_5.shift(DOWN * 0.45 + LEFT * 2.3)
        t5 = Text("4",font_size=20).move_to(findArr)
        self.play(FadeIn(node_5),FadeIn(t5))

        e2 = Line(self.node_grp[5], self.node_grp[7])
        self.play(FadeIn(e2))
        self.play(FadeOut(node_8),FadeOut(t8))
        node_8 = LabeledDot(Text("6",color=RED,font_size=20),point=np.array([5, -1, 0]))
        node_8.scale(0.7)
        node_8.shift(DOWN * 0.45 + LEFT * 2.9)
        t8 = Text("6",font_size=20).move_to(findArr).shift(RIGHT * 3)
        self.play(FadeIn(node_8),FadeIn(t8))

        e3 = Line(self.node_grp[5], self.node_grp[8])
        self.play(FadeIn(e3))
        self.play(FadeOut(node_9),FadeOut(t9))
        node_9 = LabeledDot(Text("6",color=RED,font_size=20),point=np.array([6, 0.6, 0]))
        node_9.scale(0.7)
        node_9.shift(DOWN * 0.9 + LEFT * 3.2)
        t9 = Text("6",font_size=20).move_to(findArr).shift(RIGHT * 4)
        self.play(FadeIn(node_9),FadeIn(t9))

        e4 = Line(self.node_grp[3], self.node_grp[5])
        self.play(FadeIn(e4))
        self.play(FadeOut(text3),FadeOut(text4))
        text3 = Text("Main Idea :",stroke_width = 1,color=BLUE,font_size=25).move_to([-5,1.2,0]).shift(UP * 1)
        text4 = Text("Change the Label of the Smaller tree",font_size = 25,color=WHITE).move_to([-1.3,1.15,0]).shift(UP * 1)
        self.play(Write(text3),Write(text4))

        ellipse1 = Ellipse(
            width=2, height=2.6 ,stroke_width=5
        ).move_to(UP * -0.6 + RIGHT * 0.2)
        self.play(FadeIn(ellipse1))
        self.wait()

        self.play(FadeOut(node_4),FadeOut(node_5),FadeOut(t4),FadeOut(t5))
        node_4 = LabeledDot(Text("6",color=RED,font_size=20),point=np.array([2, 1, 0]))
        node_4.scale(0.7)
        node_4.shift(DOWN * 1 + LEFT * 2)
        node_5 = LabeledDot(Text("6",color=RED,font_size=20),point=np.array([3, -1, 0]))
        node_5.scale(0.7)
        node_5.shift(DOWN * 0.45 + LEFT * 2.3)
        t5 = Text("6",font_size=20).move_to(findArr)
        t4 = Text("6",font_size=20).move_to(findArr).shift(LEFT * 1)
        self.play(FadeIn(node_4),FadeIn(node_5),FadeIn(t5),FadeIn(t4))




