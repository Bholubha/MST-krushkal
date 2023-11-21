from pickle import TRUE
from re import S
from turtle import fillcolor
from manim import *
import numpy as np
import random
from manim_slides import Slide
import networkx as nx

class mst(Slide):
    def construct(self):
        self.writeTxt()
        self.wait()
        self.MSTGraph()

    def writeTxt(self):
        mst_text1 = ["Finding "," MST "," using ", " Kruskal's ", " Algorithm"]
      
        # Create dot groups
        
        groups = VGroup(*[MarkupText(text) for text  in mst_text1]).arrange_submobjects(buff=0.3)
        self.play(Write(groups))
  
        self.play(groups.animate(run_time=1, lag_ratio=0.1).shift(UP*3.2))
        START = (-6.3,2.7,0)
        END = (7,2.7,0)
        line = Line(START,END,color=YELLOW)
        self.play(Create(line))
        
    def MSTGraph(self):
        node_S = LabeledDot(Text("S",color=RED,font_size=40),point=np.array([-3, 1, 0]))
        node_A = LabeledDot(Text("A",color=RED,font_size=40),point=np.array([0, 2, 0]))
        node_C = LabeledDot(Text("C",color=RED,font_size=40),point=np.array([3, 3, 0]))
        node_D = LabeledDot(Text("D",color=RED,font_size=40),point=np.array([2, 1, 0]))
        node_B = LabeledDot(Text("B",color=RED,font_size=40),point=np.array([0, -1, 0]))
        node_E = LabeledDot(Text("E",color=RED,font_size=40),point=np.array([3, -1, 0]))
        node_T = LabeledDot(Text("T",color=RED,font_size=40),point=np.array([4, 1, 0]))

        node_S.shift(DOWN * 1.5)
        node_A.shift(DOWN * 1.5)
        node_B.shift(DOWN * 1.5)
        node_C.shift(DOWN * 1.5)
        node_D.shift(DOWN * 1.5)
        node_E.shift(DOWN * 1.5)
        node_T.shift(DOWN * 1.5)

        self.node_grp = Group(node_S,node_A,node_B,node_C,node_D,node_E,node_T)

        edge1 =  Line(self.node_grp[0],self.node_grp[1])
        edge2 =  Line(self.node_grp[0],self.node_grp[2])
        edge3 =  Line(self.node_grp[1],self.node_grp[3])
        edge4 =  Line(self.node_grp[1],self.node_grp[4])
        edge5 =  Line(self.node_grp[2],self.node_grp[4])
        edge6 =  Line(self.node_grp[2],self.node_grp[5])
        edge7 =  Line(self.node_grp[3],self.node_grp[6])
        edge8 =  Line(self.node_grp[4],self.node_grp[5])
        edge9 =  Line(self.node_grp[4],self.node_grp[6])
        edge10 = Line(self.node_grp[5],self.node_grp[6])

        self.edge_grp = Group(edge1,edge2,edge3,edge4,edge5,edge6,edge7,edge8,edge9,edge10)

        weight_label1 = Tex("10", color=WHITE, font_size=30).shift(1.65 * UP + 2 * LEFT + DOWN * 1.5)
        weight_label2 = Tex("20", color=WHITE, font_size=30).shift(2 * LEFT + DOWN * 1.5)
        weight_label3 = Tex("20", color=WHITE, font_size=30).shift(2.65 * UP + 1 * RIGHT + DOWN * 1.5)
        weight_label4 = Tex("10", color=WHITE, font_size=30).shift(1.2 * UP, 0.8 * RIGHT + DOWN * 1.5)
        weight_label5 = Tex("10", color=WHITE, font_size=30).shift(0.6 * RIGHT + DOWN * 1.5)
        weight_label6 = Tex("40", color=WHITE, font_size=30).shift(1.3 * UP + 2.7 * RIGHT + DOWN * 1.5)
        weight_label7 = Tex("10", color=WHITE, font_size=30).shift(2.9 * RIGHT + DOWN * 1.5)
        weight_label8 = Tex("10", color=WHITE, font_size=30).shift(3.9 * RIGHT + DOWN * 1.5)
        weight_label9 = Tex("10", color=WHITE, font_size=30).shift(0.8 * DOWN + 1.5 * RIGHT + DOWN * 1.5)
        weight_label10 = Tex("30", color=WHITE, font_size=30).shift(2.5 * UP + 3.7 * RIGHT + DOWN * 1.5)
        
        self.weight_grp = Group(weight_label1, weight_label2, weight_label3, weight_label4, weight_label5,weight_label6, weight_label7, weight_label8, weight_label9, weight_label10)

        self.play(FadeIn(self.node_grp))
        self.wait()

        self.play(FadeIn(self.edge_grp))
        self.wait()

        self.play(Write(weight_label1),Write(weight_label2),Write(weight_label3),Write(weight_label4),Write(weight_label5),Write(weight_label6),Write(weight_label7),Write(weight_label8),Write(weight_label9),Write(weight_label10))

        mainGrp = VGroup(node_S,node_A,node_B,node_C,node_D,node_E,node_T,edge1,edge2,edge3,edge4,edge5,edge6,edge7,edge8,edge9,edge10,weight_label1, weight_label2, weight_label3, weight_label4, weight_label5,weight_label6, weight_label7, weight_label8, weight_label9, weight_label10)

        mainGrp.scale(0.8)
        self.play(mainGrp.animate.shift(LEFT * 4))
    
        text1 = Text("Step 1 :",stroke_width = 2,color=RED,font_size=30).move_to([1,2,0])
        self.play(Write(text1))
        text2 = Text("Sort all the edges in non-decreasing order \nof their weight",font_size = 25,color=WHITE).move_to([3.5,1.4,0])
        self.play(Write(text2))

        self.play(FadeOut(self.edge_grp),FadeOut(self.weight_grp))

        #making the side edges 
        node_1 = LabeledDot(Text("S",color=BLACK,font_size=20),point=np.array([1.5, 0.5, 0]))
        node_2 = LabeledDot(Text("A",color=BLACK,font_size=20),point=np.array([3.5, 0.5, 0]))

        node_3 = LabeledDot(Text("B",color=BLACK,font_size=20),point=np.array([1.5, -0.3, 0]))
        node_4 = LabeledDot(Text("D",color=BLACK,font_size=20),point=np.array([3.5, -0.3, 0]))

        node_5 = LabeledDot(Text("A",color=BLACK,font_size=20),point=np.array([1.5, -1.1, 0]))
        node_6 = LabeledDot(Text("D",color=BLACK,font_size=20),point=np.array([3.5, -1.1, 0]))

        node_7 = LabeledDot(Text("B",color=BLACK,font_size=20),point=np.array([1.5, -1.9, 0]))
        node_8 = LabeledDot(Text("E",color=BLACK,font_size=20),point=np.array([3.5, -1.9, 0]))

        node_9 = LabeledDot(Text("D",color=BLACK,font_size=20),point=np.array([1.5, -2.7, 0]))
        node_10 = LabeledDot(Text("E",color=BLACK,font_size=20),point=np.array([3.5, -2.7, 0]))

        node_11 = LabeledDot(Text("E",color=BLACK,font_size=20),point=np.array([4.5, 0.5, 0]))
        node_12 = LabeledDot(Text("T",color=BLACK,font_size=20),point=np.array([6.5, 0.5, 0]))

        node_13 = LabeledDot(Text("S",color=BLACK,font_size=20),point=np.array([4.5, -0.3, 0]))
        node_14 = LabeledDot(Text("B",color=BLACK,font_size=20),point=np.array([6.5, -0.3, 0]))

        node_15 = LabeledDot(Text("A",color=BLACK,font_size=20),point=np.array([4.5, -1.1, 0]))
        node_16 = LabeledDot(Text("C",color=BLACK,font_size=20),point=np.array([6.5, -1.1, 0]))

        node_17 = LabeledDot(Text("C",color=BLACK,font_size=20),point=np.array([4.5, -1.9, 0]))
        node_18 = LabeledDot(Text("T",color=BLACK,font_size=20),point=np.array([6.5, -1.9, 0]))

        node_19 = LabeledDot(Text("D",color=BLACK,font_size=20),point=np.array([4.5, -2.7, 0]))
        node_20 = LabeledDot(Text("T",color=BLACK,font_size=20),point=np.array([6.5, -2.7, 0]))

        self.MST_grp = Group(node_1,node_2,node_3,node_4,node_5,node_6,node_7,node_8,node_9,node_10,node_11,node_12,node_13,node_14,node_15,node_16,node_17,node_18,node_19,node_20)

        self.play(FadeIn(self.MST_grp))

        medge1 =  Line(self.MST_grp[0],self.MST_grp[1])
        medge2 =  Line(self.MST_grp[2],self.MST_grp[3])
        medge3 =  Line(self.MST_grp[4],self.MST_grp[5])
        medge4 =  Line(self.MST_grp[6],self.MST_grp[7])
        medge5 =  Line(self.MST_grp[8],self.MST_grp[9])
        medge6 =  Line(self.MST_grp[10],self.MST_grp[11])
        medge7 =  Line(self.MST_grp[12],self.MST_grp[13])
        medge8 =  Line(self.MST_grp[14],self.MST_grp[15])
        medge9 =  Line(self.MST_grp[16],self.MST_grp[17])
        medge10 = Line(self.MST_grp[18],self.MST_grp[19])

        self.edge_grp = Group(medge1,medge2,medge3,medge4,medge5,medge6,medge7,medge8,medge9,medge10)
        self.play(FadeIn(self.edge_grp))

        w_label1 = Tex("10", color=WHITE, font_size=30).next_to(medge1,UP)
        w_label2 = Tex("10", color=WHITE, font_size=30).next_to(medge2,UP)
        w_label3 = Tex("10", color=WHITE, font_size=30).next_to(medge3,UP)
        w_label4 = Tex("10", color=WHITE, font_size=30).next_to(medge4,UP)
        w_label5 = Tex("10", color=WHITE, font_size=30).next_to(medge5,UP)
        w_label6 = Tex("10", color=WHITE, font_size=30).next_to(medge6,UP)
        w_label7 = Tex("20", color=WHITE, font_size=30).next_to(medge7,UP)
        w_label8 = Tex("20", color=WHITE, font_size=30).next_to(medge8,UP)
        w_label9 = Tex("30", color=WHITE, font_size=30).next_to(medge9,UP)
        w_label10 = Tex("40", color=WHITE, font_size=30).next_to(medge10,UP)
        

        self.play(Write(w_label1),Write(w_label2),Write(w_label3),Write(w_label4),Write(w_label5),Write(w_label6),Write(w_label7),Write(w_label8),Write(w_label9),Write(w_label10))

        self.wait()

        self.play(FadeOut(text1,text2))
        text1 = Text("Step 2 :",stroke_width = 2,color=RED,font_size=30).move_to([1,2,0])
        self.play(Write(text1))
        text2 = Text("Pick the smallest edge and check for a cycle \nin graph.",font_size = 25,color=WHITE).move_to([3.5,1.4,0])
        self.play(Write(text2))

        medge1.set_color(color=RED)
        self.play(FadeIn(medge1))
        self.wait()
        edge1.set_color(color=RED)
        self.play(FadeIn(edge1),Write(weight_label1))
        self.play(FadeToColor(edge1,color=GREEN),FadeOut(node_1,node_2,w_label1,medge1))
        self.wait()
        self.play(FadeToColor(edge1,color=WHITE))

        medge2.set_color(color=RED)
        self.play(FadeIn(medge2))
        self.wait()
        edge5.set_color(color=RED)
        self.play(FadeIn(edge5),Write(weight_label5))
        self.play(FadeToColor(edge5,color=GREEN),FadeOut(node_3,node_4,w_label2,medge2))
        self.wait()
        self.play(FadeToColor(edge5,color=WHITE))

        medge3.set_color(color=RED)
        self.play(FadeIn(medge3))
        self.wait()
        edge4.set_color(color=RED)
        self.play(FadeIn(edge4),Write(weight_label4))
        self.play(FadeToColor(edge4,color=GREEN),FadeOut(node_5,node_6,w_label3,medge3))
        self.wait()
        self.play(FadeToColor(edge4,color=WHITE))
        
        medge4.set_color(color=RED)
        self.play(FadeIn(medge4))
        self.wait()
        edge6.set_color(color=RED)
        self.play(FadeIn(edge6),Write(weight_label9))
        self.play(FadeToColor(edge6,color=GREEN),FadeOut(node_7,node_8,w_label4,medge4))
        self.wait()
        self.play(FadeToColor(edge6,color=WHITE))

        medge5.set_color(color=RED)
        self.play(FadeIn(medge5))
        self.wait()
        edge8.set_color(color=RED)
        self.play(FadeIn(edge8),Write(weight_label7))
        for i in range(1,3):
            if(i%2==0):
                self.play(FadeOut(edge8))
            else:
                self.play(FadeIn(edge8))

        self.play(FadeOut(node_9,node_10,w_label5,medge5,edge8,weight_label7))
        self.wait()

        medge6.set_color(color=RED)
        self.play(FadeIn(medge6))
        self.wait()
        edge10.set_color(color=RED)
        self.play(FadeIn(edge10),Write(weight_label8))
        self.play(FadeToColor(edge10,color=GREEN),FadeOut(node_11,node_12,w_label6,medge6))
        self.wait()
        self.play(FadeToColor(edge10,color=WHITE))

        medge7.set_color(color=RED)
        self.play(FadeIn(medge7))
        self.wait()
        edge2.set_color(color=RED)
        self.play(FadeIn(edge2),Write(weight_label2))
        for i in range(1,3):
            if(i%2==0):
                self.play(FadeOut(edge2))
            else:
                self.play(FadeIn(edge2))

        self.play(FadeOut(node_13,node_14,w_label7,medge7,edge2,weight_label2))
        self.wait()

        medge8.set_color(color=RED)
        self.play(FadeIn(medge8))
        self.wait()
        edge3.set_color(color=RED)
        self.play(FadeIn(edge3),Write(weight_label3))
        self.play(FadeToColor(edge3,color=GREEN),FadeOut(node_15,node_16,w_label8,medge8))
        self.wait()
        self.play(FadeToColor(edge3,color=WHITE))

        self.play(FadeOut(text1,text2))
        text1 = Text("MST Formed:",stroke_width = 2,color=RED,font_size=30).move_to([1.6,2,0])
        self.play(Write(text1))
        text2 = Text("Discard all the remaining edges",font_size = 25,color=WHITE).move_to([3,1.4,0])
        self.play(Write(text2))

        self.play(FadeOut(node_17,node_18,node_19,node_20,w_label10,w_label9,medge10,medge9))