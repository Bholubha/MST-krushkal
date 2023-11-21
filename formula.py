from pickle import TRUE
from re import S
from turtle import fillcolor
from manim import *
import numpy as np
import random
from manim_slides import Slide
import networkx as nx
# import matplotlib.pyplot as plt


class formula(Slide):
    def construct(self):
        text1 = Text("TIME ",color=BLUE,font_size=30).move_to([-5,2.5,0])
        self.play(Write(text1))
        formula1 = MathTex(
            "= O(m.log n) + \sum_{i=1}^{m}",
            color = WHITE,
            font_size = 25
        ).move_to([-3.2,2.5,0])
        t_1 = Text("Time taken to change Label in Iteration i",font_size=25,color=YELLOW).move_to([1.4,2.5,0])
     
        formula2 = MathTex(
            "= O(m.logn) + \sum_{i=1}^{m}",
            color = WHITE,
            font_size = 25
        ).move_to([-3.2,1.5,0])
        t_2 = Text("#vertices that have changed Lables at Iteration i",font_size=25,color=YELLOW).move_to([1.8,1.5,0])

        formula3 = MathTex(
            "= O(m.logn) + \sum_{v\epsilon x}",
            color = WHITE,
            font_size = 25
        ).move_to([-3.2,0.5,0])
        t_3 = Text("#v Changes its Label",font_size=25,color=YELLOW).move_to([-0.2,0.5,0])

        self.play(Write(formula1))
        self.play(FadeIn(t_1))
        self.play(Write(formula2))
        self.play(FadeIn(t_2))
        self.play(Write(formula3))
        self.play(FadeIn(t_3))

        question_text = Text("Q: How Many times v changes its Label ?",font_size=30,color=RED).move_to([-1.8,-0.2,0])
        self.play(FadeIn(question_text))

        c1 = Circle(radius=0.5,color=WHITE).move_to([-4.5,-1.6,0])
        lbl1 = MathTex(
            "1",
            color = WHITE,
            font_size=25
        ).move_to([-4.5,-2.3,0])
        dot1 = Dot(point=np.array([-4.6, -1.6, 0]))
        txt1 = Text("v",font_size=25).next_to(dot1,DOWN * 0.4)
        self.play(FadeIn(c1),FadeIn(lbl1),FadeIn(dot1),FadeIn(txt1))
        arrow_1 = Arrow(start=LEFT,end=RIGHT)
        arrow_1.scale(0.4)
        arrow_1.shift(LEFT * 3.7, DOWN * 1.6)
        self.play(FadeIn(arrow_1))

        c2 = Circle(radius=0.6,color=WHITE).move_to([-2.7,-1.6,0])
        lbl2 = MathTex(
            " \geq 2",
            color = WHITE,
            font_size=25
        ).move_to([-2.7,-2.5,0])
        dot2 = Dot(point=np.array([-2.9, -1.6, 0]))
        dot3 = Dot(point=np.array([-2.5, -1.6, 0]))
        txt2 = Text("v",font_size=25).next_to(dot2,DOWN * 0.4)
        self.play(FadeIn(c2),FadeIn(lbl2),FadeIn(dot2),FadeIn(dot3),FadeIn(txt2))
        arrow_2 = Arrow(start=LEFT,end=RIGHT)
        arrow_2.scale(0.4)
        arrow_2.shift(LEFT * 1.7, DOWN * 1.6)
        self.play(FadeIn(arrow_2))

        c3 = Circle(radius=0.7,color=WHITE).move_to([-0.7,-1.6,0])
        lbl3 = MathTex(
            " \geq 4",
            color = WHITE,
            font_size=25
        ).move_to([-0.7,-2.6,0])
        dot4 = Dot(point=np.array([-1.0, -1.6, 0]))
        dot5 = Dot(point=np.array([-0.7, -1.3, 0]))
        dot6 = Dot(point=np.array([-0.4, -1.6, 0]))
        dot7 = Dot(point=np.array([-0.7, -1.9, 0]))
        txt3 = Text("v",font_size=25).next_to(dot4,DOWN * 0.4)
        self.play(FadeIn(c3),FadeIn(lbl3),FadeIn(dot4),FadeIn(dot5),FadeIn(dot6),FadeIn(dot7),FadeIn(txt3))

        dot_text = Text(". . . . . . .",font_size=30,color=WHITE).shift(DOWN * 1.6 + RIGHT * 1)
        self.play(FadeIn(dot_text))

        arrow_3 = Arrow(start=LEFT,end=RIGHT)
        arrow_3.scale(0.4)
        arrow_3.shift(RIGHT * 2.5, DOWN * 1.6)
        self.play(FadeIn(arrow_3))

        c4 = Circle(radius=0.9,color=WHITE).move_to([3.7,-1.6,0])
        lbl4 = MathTex(
            " 2^{logn}",
            color = WHITE,
            font_size=25
        ).move_to([3.7,-2.8,0])
        dot8 = Dot(point=np.array([3.1, -1.6, 0]))
        dot9 = Dot(point=np.array([3.7, -1.7, 0]))
        dot10 = Dot(point=np.array([3.7, -1.2, 0]))
        dot11 = Dot(point=np.array([3.8, -1.4, 0]))
        dot12 = Dot(point=np.array([4, -2.1, 0]))
        dot13 = Dot(point=np.array([3.7, -2, 0]))
        dot14 = Dot(point=np.array([4, -1.6, 0]))
        dot15 = Dot(point=np.array([4, -1.2, 0]))
        txt4 = Text("v",font_size=25).next_to(dot8,DOWN * 0.4)
        self.play(FadeIn(c4),FadeIn(lbl4),FadeIn(dot8),FadeIn(dot9),FadeIn(dot10),FadeIn(dot11),FadeIn(dot12),FadeIn(dot13),FadeIn(dot14),FadeIn(dot15),FadeIn(txt4))
        
        last_text = Text("# Times v changed its Label = logn",font_size=30,color=BLUE).move_to([-2,-3.1,0])
        self.play(FadeIn(last_text))

        self.wait()

        self.play(FadeOut(dot1,dot2,dot3,dot4,dot5,dot6,dot7,dot8,dot9,dot10,dot11,dot12,dot13,dot14,dot15,txt1,txt2,txt3,txt4),FadeOut(c1,c2,c3,c4),FadeOut(arrow_1,arrow_2,arrow_3),FadeOut(question_text,last_text,dot_text),FadeOut(lbl1,lbl2,lbl3,lbl4))

        formula4 = MathTex(
            "= O(m.logn) + n.logn",
            color = WHITE,
            font_size = 25
        ).move_to([-3,-0.5,0])
        self.play(FadeIn(formula4))

        formula5 = MathTex(
            "= O((m+n).logn)",
            color = WHITE,
            font_size = 25
        ).move_to([-3.2,-1.5,0])
        self.play(FadeIn(formula5))
