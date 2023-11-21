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
from manim_pptx import *


        

class intro(Slide):
    def construct(self):
        
        header = MarkupText(
            f'Greedy Algorithm',font="Britannic Bold",font_size=80
        )

      
        header2 = MarkupText(f'MST Kruskal\'s Algorithm',font="Britannic Bold",font_size=80 )

        self.play(Write(header),run_time=1)
        self.play(RemoveTextLetterByLetter(header),run_time=2)
        self.play(Write(header2),run_time=2)
        self.wait(2)
        self.clear()
        self.next_slide()
        
        #What is MST 
        mst_text1 = ["What","Is","MST ?"]
       
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
       

        # MST example

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
        self.play(FadeIn(self.nodeGrp),run_time=0.7)

        self.wait(1)
        self.play(Create(self.Tnode1), Create(self.Tnode2), Create(self.Tnode3),run_time=1.3)

        self.edgeGrp = Group(self.edge_1,self.edge_2,self.edge_3)
        self.play(FadeIn(self.edgeGrp),run_time=0.6)
        
        self.play(Write(self.w_label1), Write(self.w_label2), Write(self.w_label3),run_time=0.6)

        

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
        self.play(FadeIn(self.nodeGrp1),run_time=0.7)

        
        self.play(Create(self.Mnode1), Create(self.Mnode2), Create(self.Mnode3),run_time=0.7)

        #highliting the MST edges
        edge_M1 = Line(self.node_grp[0],self.node_grp[1])
        M_label1 = Tex("5", color=WHITE, font_size=30).shift(UP * 0.25 + 3.5 * LEFT)
        self.play(Create(edge_M1),run_time=0.6)
        edge_M1.set_color(color=RED)
       
        self.play(edge_M1.animate.shift(RIGHT*7),M_label1.animate.shift(RIGHT*7),run_time=0.6)

        

        edge_M2 = Line(self.node_grp[0],self.node_grp[2])
        M_label2 = Tex("7", color=WHITE, font_size=30).shift(DOWN * 1.8 + 3.5 * LEFT)
        self.play(Create(edge_M2),run_time=0.6)
        edge_M2.set_color(color=RED)
        self.wait(1)
        self.play(edge_M2.animate.shift(RIGHT*7),M_label2.animate.shift(RIGHT*7),run_time=0.6)
        
        self.wait(2)
        self.clear()

        # Approaches 

        START = (-6.3,2.7,0)
        END = (4,2.7,0)
        question = MarkupText(f'Any Greedy Solution?',font="Britannic Bold",font_size=50 )
        self.play(Write(question),run_time=0.7)
        self.play(question.animate.shift(3.3*UP + 2.7*LEFT),run_time=0.6)
        line = Line(START,END,color=YELLOW)
        self.play(Create(line),run_time=0.6)

        
        a1 = Tex("$\\rightarrow$ Sort All the Edges of the Graph in Ascending Order of Their Weight.", font_size=40,stroke_width=2,tex_template=TexFontTemplates.droid_sans)
        a1.shift(UP*2.2+LEFT*0.1)
        self.play(Write(a1),run_time=1.7)
    
        a2 = Tex("$\\rightarrow$ Initialize a Set S to be Empty.", font_size=40, stroke_width=2,tex_template=TexFontTemplates.droid_sans)
        a2.align_to(a1,LEFT)
        a2.shift(UP*1.5)
        self.play(Write(a2),run_time=1.7)

        a3 = Tex("$\\rightarrow$ Add Edges to S in Increasing order If The Edge Does Not Create Cycle.", font_size=40, stroke_width=2,tex_template=TexFontTemplates.droid_sans)
        a3.align_to(a2,LEFT)
        a3.shift(UP*0.8)
        self.play(Write(a3),run_time=1.7)
        self.wait(1.5)
        
        self.clear()
        self.next_slide()

        #CReating Graph
        
        mst_text1 = ["Finding "," MST "," using ", " Kruskal's ", " Algorithm"]
      
        # Create dot groups
        
        groups = VGroup(*[MarkupText(text) for text  in mst_text1]).arrange_submobjects(buff=0.3)
        self.play(Write(groups),run_time=1)
  
        self.play(groups.animate(run_time=1, lag_ratio=0.1).shift(UP*3.2),run_time=1)
        START = (-6.3,2.7,0)
        END = (7,2.7,0)
        line = Line(START,END,color=YELLOW)
        self.play(Create(line),run_time=1)
        self.next_slide()

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

        self.play(FadeIn(self.node_grp),run_time=1)
        

        self.play(FadeIn(self.edge_grp),run_time=1)
        

        self.play(Write(weight_label1),Write(weight_label2),Write(weight_label3),Write(weight_label4),Write(weight_label5),Write(weight_label6),Write(weight_label7),Write(weight_label8),Write(weight_label9),Write(weight_label10),run_time=1)
        self.next_slide()
        
        mainGrp = VGroup(node_S,node_A,node_B,node_C,node_D,node_E,node_T,edge1,edge2,edge3,edge4,edge5,edge6,edge7,edge8,edge9,edge10,weight_label1, weight_label2, weight_label3, weight_label4, weight_label5,weight_label6, weight_label7, weight_label8, weight_label9, weight_label10)

        mainGrp.scale(0.8)
        self.play(mainGrp.animate.shift(LEFT * 4),run_time=1)
        self.next_slide()

        text1 = Text("Step 1 :",stroke_width = 2,color=RED,font_size=30).move_to([1,2,0])
        self.play(Write(text1),run_time=1)
        text2 = Text("Sort all the edges in non-decreasing order \nof their weight",font_size = 25,color=WHITE).move_to([3.5,1.4,0])
        self.play(Write(text2),run_time=1)
        self.next_slide()

        self.play(FadeOut(self.edge_grp),FadeOut(self.weight_grp),run_time=1)
        self.next_slide()



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

        self.play(FadeIn(self.MST_grp),run_time=1)
        self.next_slide()

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
        self.play(FadeIn(self.edge_grp),run_time=1)
        self.next_slide()

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
        

        self.play(Write(w_label1),Write(w_label2),Write(w_label3),Write(w_label4),Write(w_label5),Write(w_label6),Write(w_label7),Write(w_label8),Write(w_label9),Write(w_label10),run_time=1)
        self.next_slide()
        

        self.play(FadeOut(text1,text2),run_time=1)
        text1 = Text("Step 2 :",stroke_width = 2,color=RED,font_size=30).move_to([1,2,0])
        self.play(Write(text1),run_time=1)
        text2 = Text("Pick the smallest edge and check for a cycle \nin graph.",font_size = 25,color=WHITE).move_to([3.5,1.4,0])
        self.play(Write(text2),run_time=1)
        self.next_slide()

        medge1.set_color(color=RED)
        self.play(FadeIn(medge1),run_time=0.5)
        self.next_slide()

        edge1.set_color(color=RED)
        self.play(FadeIn(edge1),Write(weight_label1),run_time=0.5)
        self.play(FadeToColor(edge1,color=GREEN),FadeOut(node_1,node_2,w_label1,medge1),run_time=0.5)
        self.next_slide()

        self.play(FadeToColor(edge1,color=WHITE),run_time=0.5)
        self.next_slide()

        medge2.set_color(color=RED)
        self.play(FadeIn(medge2),run_time=0.5)
        
        edge5.set_color(color=RED)
        self.play(FadeIn(edge5),Write(weight_label5),run_time=0.5)
        self.play(FadeToColor(edge5,color=GREEN),FadeOut(node_3,node_4,w_label2,medge2),run_time=0.5)
    
        self.play(FadeToColor(edge5,color=WHITE),run_time=0.5)
        self.next_slide()

        medge3.set_color(color=RED)
        self.play(FadeIn(medge3),run_time=0.5)
        
        edge4.set_color(color=RED)
        self.play(FadeIn(edge4),Write(weight_label4),run_time=0.5)
        self.play(FadeToColor(edge4,color=GREEN),FadeOut(node_5,node_6,w_label3,medge3),run_time=0.5)
        
        self.play(FadeToColor(edge4,color=WHITE),run_time=0.5)
        self.next_slide()

        medge4.set_color(color=RED)
        self.play(FadeIn(medge4),run_time=0.5)
        
        edge6.set_color(color=RED)
        self.play(FadeIn(edge6),Write(weight_label9),run_time=0.5)
        self.play(FadeToColor(edge6,color=GREEN),FadeOut(node_7,node_8,w_label4,medge4),run_time=0.5)
        
        self.play(FadeToColor(edge6,color=WHITE),run_time=0.5)
        self.next_slide()

        medge5.set_color(color=RED)
        self.play(FadeIn(medge5),run_time=0.5)
        self.next_slide()

        edge8.set_color(color=RED)
        self.play(FadeIn(edge8),Write(weight_label7),run_time=0.5)
        for i in range(1,3):
            if(i%2==0):
                self.play(FadeOut(edge8),run_time=0.5)
            else:
                self.play(FadeIn(edge8),run_time=0.5)

        self.play(FadeOut(node_9,node_10,w_label5,medge5,edge8,weight_label7))
        self.next_slide()

        medge6.set_color(color=RED)
        self.play(FadeIn(medge6),run_time=0.5)
        
        edge10.set_color(color=RED)
        self.play(FadeIn(edge10),Write(weight_label8),run_time=0.5)
        self.play(FadeToColor(edge10,color=GREEN),FadeOut(node_11,node_12,w_label6,medge6))
        
        self.play(FadeToColor(edge10,color=WHITE),run_time=0.5)
        self.next_slide()

        medge7.set_color(color=RED)
        self.play(FadeIn(medge7),run_time=1)
        
        edge2.set_color(color=RED)
        self.play(FadeIn(edge2),Write(weight_label2),run_time=0.5)
        for i in range(1,3):
            if(i%2==0):
                self.play(FadeOut(edge2),run_time=1)
            else:
                self.play(FadeIn(edge2),run_time=1)

        self.play(FadeOut(node_13,node_14,w_label7,medge7,edge2,weight_label2),run_time=0.5)
        self.next_slide()

        medge8.set_color(color=RED)
        self.play(FadeIn(medge8),run_time=0.5)
        
        edge3.set_color(color=RED)
        self.play(FadeIn(edge3),Write(weight_label3),run_time=0.5)
        self.play(FadeToColor(edge3,color=GREEN),FadeOut(node_15,node_16,w_label8,medge8),run_time=0.5)
        
        self.play(FadeToColor(edge3,color=WHITE),run_time=0.5)
        self.next_slide()

        self.play(FadeOut(text1,text2),run_time=0.5)
        text1 = Text("MST Formed:",stroke_width = 2,color=RED,font_size=30).move_to([1.6,2,0])
        self.play(Write(text1),run_time=0.5)
        text2 = Text("Discard all the remaining edges",font_size = 25,color=WHITE).move_to([3,1.4,0])
        self.play(Write(text2),run_time=1)

        self.play(FadeOut(node_17,node_18,node_19,node_20,w_label10,w_label9,medge10,medge9),run_time=0.5)
        self.next_slide()
        self.wait(2)
        self.clear()


        

        #ALGORITHM

        START = (-6.3,2.7,0)
        END = (4,2.7,0)
        question = MarkupText(f'ALGORITHM',font="Britannic Bold",font_size=50 )
        question.shift(3.3*UP + 4*LEFT)
        self.play(Write(question),run_time=0.5)
        line = Line(START,END,color=YELLOW)
        self.play(Create(line),run_time=0.2)
        self.next_slide()

        a1 = Tex("1. \;\; T \; $\\leftarrow$ \; $\\emptyset$", font_size=40,stroke_width=2)
        a1.shift(UP*2+LEFT*4.7)
        self.play(Write(a1),run_time=1)
        self.next_slide()

        a2 = Tex("2. \;\; S \; $\\leftarrow$ \; Sort Edges According To their Weight", font_size=40, stroke_width=2)
        a2.align_to(a1,LEFT)
        a2.shift(UP*1.3)
        self.play(Write(a2),run_time=1)
        self.next_slide()

        FE = Tex("3.\;\; FOREACH ",stroke_width = 2,color=RED_D)
        T = Tex("( e in E ) :", font_size=40, stroke_width=2)
        FE.align_to(a2,LEFT)
        T.next_to(FE)
        a3 = VGroup(FE,T)
        a3.align_to(a2,LEFT)
        a3.shift(UP*0.7)
        self.play(Write(a3),run_time=1)
        

        a4 = Tex("${\{}$", font_size=40, stroke_width=2,color=RED_A)
        a4.align_to(a3)
        a4.shift(5*LEFT)
        a4.shift(UP*(-0))
        self.play(Write(a4),run_time=1)
        self.next_slide()

        IF = Tex("IF ", font_size=40, stroke_width=2,color=RED_D)
        T = Tex("T + e Does not Contains a Cycle :",stroke_width=2)
        IF.align_to(a4,LEFT)
        

        T.next_to(IF, RIGHT)
        a5 = VGroup(IF,T)
        a5.align_to(a4)
        a5.shift(LEFT*(-0.3))
        a5.shift(UP*(-0.6))
        self.play(Write(a5),run_time=1)
        self.next_slide()

        a6 = Tex("${\{}$", font_size=40, stroke_width=2,color=RED_A)
        a6.align_to(a5,LEFT)
        a6.shift(UP*(-1.2))
        self.play(Write(a6),run_time=0.5)
       

        a7 = Tex("T \; $\\leftarrow$ \; T + e", font_size=40, stroke_width=2)
        a7.align_to(a6,LEFT)
        a7.shift(LEFT*(-0.1))
        a7.shift(UP*(-1.8))
        self.play(Write(a7),run_time=1)
     

        a8 = Tex("${\}}$", font_size=40, stroke_width=2,color=RED_A)
        a8.align_to(a6,LEFT)
        a8.shift(UP*(-2.3))
        self.play(Write(a8),run_time=0.5)
        self.next_slide()

        a9 = Tex("${\}}$", font_size=40, stroke_width=2,color=RED_A)
        a9.align_to(a4,LEFT)
        a9.shift(UP*(-3.1))
        self.play(Write(a9),run_time=0.5)
        self.next_slide()

        a10 = Tex("4. \;\; END", font_size=40, stroke_width=2)
        a10.align_to(a1,LEFT)
        a10.shift(UP*(-3.8))
        self.play(Write(a10),run_time=0.5)
        self.next_slide()

        self.wait(2)
        self.clear()
        self.next_slide()



        #Lemma and proof
   
        
        
        START = (-6.3,3.2,0)
        END = (4,3.2,0)
        question = MarkupText(f"Is This Algorithm Correct?",font_size=40,stroke_width=2)
        self.play(Write(question),run_time=1.3)
        self.play(question.animate.shift(3.6*UP + 3*LEFT),run_time=1)
        line = Line(START,END,color=YELLOW)
        self.play(Create(line),run_time=1)

        Le=Tex( "$\\bullet$ Lemma : ",font_size=34,stroke_width=2)
        Le.set_color_by_tex_to_color_map({"$\\bullet$ Lemma : ":BLUE})
        Le.align_to(np.array([-6.2,3,0]),LEFT+UP)
        self.play(Write(Le),run_time = 1)

        lemma=MarkupText(f' Assume That at K<sup>th</sup>  Iteration, Edge (u,v) Is Added By Our Algorithm Then ',font_size=24,stroke_width=1.3)
        lemma.next_to(Le,RIGHT)
        self.play(Write(lemma),run_time = 2)

        lemma2 = Text( "(u,v) Lies In Minimum Spanning Tree.",font_size=24,stroke_width=1.3)
        lemma2.align_to(np.array([-4.45,2.6,0]),LEFT+UP)
        self.play(Write(lemma2),run_time = 2)

        proof=Tex( "$\\bullet$ Proof : ",font_size=30,stroke_width=2)
        proof.set_color_by_tex_to_color_map({"$\\bullet$ Proof : ":BLUE})
        proof.align_to(np.array([-6.2,2.2,0]),LEFT+UP)
        self.play(Write(proof),run_time = 1)

        a1 = Tex("$\\rightarrow$ For Arbitrary Graph Consider $K^{th}$ Iteration Of Kruskal's Algorithm.", font_size=30,stroke_width=1.3)
        a1.align_to(np.array([-6,1.65,0]),LEFT+UP)
        self.play(Write(a1),run_time=2)

        
        self.node_S = Dot(point=np.array([-5.7,-2, 0]))
        self.node_A = Dot(point=np.array([-4.7, -1, 0]))
        self.node_B = Dot(point=np.array([-4.7, -3, 0]))
        self.node_C = Dot(point=np.array([-3.6, -2, 0]))
        self.node_D = Dot(point=np.array([-2.7, -2, 0]))   
        self.node_E = Dot(point=np.array([-1.6, -2, 0]))
        self.node_T = Dot(point=np.array([0, -2, 0]))
        self.node_F = Dot(point=np.array([1.1, -1 ,0]))
        self.node_G = Dot(point=np.array([1.1, -3, 0]))


        self.wnode1 = Tex("S", color=WHITE, font_size=30).next_to(self.node_S, LEFT)
        self.wnode2 = Tex("A", color=WHITE, font_size=30).next_to(self.node_A, UP)
        self.wnode3 = Tex("B", color=WHITE, font_size=30).next_to(self.node_B, DOWN)
        self.wnode4 = Tex("U'", color=WHITE, font_size=30).next_to(self.node_C, UP)
        self.wnode5 = Tex("D", color=WHITE, font_size=30).next_to(self.node_D, UP)
        self.wnode6 = Tex("U", color=WHITE, font_size=30).next_to(self.node_E, UP)
        self.wnode7 = Tex("V", color=WHITE, font_size=30).next_to(self.node_T, RIGHT)
        self.wnode8 = Tex("F", color=WHITE, font_size=30).next_to(self.node_F, UP)
        self.wnode9 = Tex("V'", color=WHITE, font_size=30).next_to(self.node_G, DOWN)
        
        

        self.edge1 = Line(self.node_S, self.node_A, buff=0.05)
        self.edge2 = Line(self.node_S, self.node_B, buff=0.06)
        self.edge3 = Line(self.node_C, self.node_D, buff=0.06)
        self.edge4 = Line(self.node_D, self.node_E, buff=0.06)
        self.edge5 = DashedLine(self.node_E, self.node_T, buff=0.06,color=RED_D)
        self.edge6 = Line(self.node_T, self.node_F, buff=0.06)
        self.edge7 = Line(self.node_T, self.node_G, buff=0.06)

        node_group=Group(self.node_S,self.node_B,self.node_C,self.node_A,self.node_D,self.node_E,self.node_T,self.node_G,self.node_F,self.wnode1,self.wnode2,self.wnode3,self.wnode4,self.wnode5,self.wnode6,self.wnode7,self.wnode8,self.wnode9,self.edge1,self.edge2,self.edge3,self.edge4,self.edge5,self.edge6,self.edge7)
        node_group.shift(LEFT*1.6+UP*1)
        node_group.scale(0.7)
        self.play(FadeIn(node_group),run_time=1.3)

        arrow = Arrow(np.array([-2.8,-0.9,0]), np.array([-3.2,-2.8,0]),color=BLUE_D)
        text = Tex("Edge to be Add", color=WHITE, font_size=30,stroke_width=1.8).next_to(arrow, DOWN)
        edgetobe = Group(arrow,text)
        self.play(FadeIn(edgetobe),run_time=1)



        ellipse1 = Ellipse(
            width=3.5, height=6.2 ,stroke_width=5
        ).move_to(UP*(-1.2)+3*LEFT)
        ellipse1.set_color(color=WHITE)
        ellipse2 = ellipse1.copy().set_color(color=WHITE).move_to(3.2*RIGHT+(-1.2)*UP)
        ellipse_group = Group( ellipse1, ellipse2)
        ellipse_group.scale(0.7)
        ellipse_group.shift(3*RIGHT+UP*0.1)
        self.play(FadeIn(ellipse_group),run_time=1)

        

        self.Node_S = Dot(point=np.array([4.6,0, 0]))
        self.Node_A = Dot(point=np.array([5.5, 0.7, 0]))
        self.Node_B = Dot(point=np.array([5.5, -0.8, 0]))
        self.Node_C = Dot(point=np.array([0, -1, 0]))
        self.Node_D = Dot(point=np.array([0.9, -1, 0]))   
        self.Node_E = Dot(point=np.array([1.8, -1, 0]))
        self.Node_T = Dot(point=np.array([4.8, -2.0, 0]))
        self.Node_F = Dot(point=np.array([5.5, -1.2 ,0]))
        self.Node_G = Dot(point=np.array([5.5, -2.8, 0]))

        self.Wnode1 = Tex("S", color=WHITE, font_size=20).next_to(self.Node_S, UP)
        self.Wnode2 = Tex("A", color=WHITE, font_size=20).next_to(self.Node_A, RIGHT)
        self.Wnode3 = Tex("B", color=WHITE, font_size=20).next_to(self.Node_B, RIGHT)
        self.Wnode4 = Tex("U'",  font_size=20,color=RED_B).next_to(self.Node_C, UP)
        self.Wnode5 = Tex("D", color=WHITE, font_size=20).next_to(self.Node_D, UP)
        self.Wnode6 = Tex("U",  font_size=20,color=GREEN_B).next_to(self.Node_E, UP)
        self.Wnode7 = Tex("V",  font_size=20,color=GREEN_B).next_to(self.Node_T, LEFT)
        self.Wnode8 = Tex("F", color=WHITE, font_size=20).next_to(self.Node_F, RIGHT)
        self.Wnode9 = Tex("V'",  font_size=20,color=RED_B).next_to(self.Node_G, RIGHT)
        self.Wnode9.shift(RIGHT*(-0.2))
        self.Wnode2.shift(RIGHT*(-0.2))

        self.Edge1 = Line(self.Node_S, self.Node_A, buff=0.05,color=BLUE_D)
        self.Edge2 = Line(self.Node_S, self.Node_B, buff=0.06,color=BLUE_D)
        self.Edge3 = Line(self.Node_C, self.Node_D, buff=0.06,color=BLUE_D)
        self.Edge4 = Line(self.Node_D, self.Node_E, buff=0.06,color=BLUE_D)
        self.Edge5 = DashedLine(self.Node_E, self.Node_T, buff=0.06,color=GREEN_D)
        self.Edge6 = Line(self.Node_T, self.Node_F, buff=0.06,color=BLUE_D)
        self.Edge7 = Line(self.Node_T, self.Node_G, buff=0.06,color=BLUE_D)

        ShiftEdge1 = Group(self.node_C,self.node_D,self.edge3,self.wnode4,self.wnode5)
        ShiftEdge1 = ShiftEdge1.copy()
        self.play(self.edge3.animate.set_color(RED),run_time=0.5)
        ShiftedEdge1 = Group(self.Node_C,self.Node_D,self.Edge3,self.Wnode4,self.Wnode5)
        self.play(Transform(ShiftEdge1,ShiftedEdge1),run_time=0.5)
        # self.play(ShiftEdge1.animate.move_to(UP*(-1)+LEFT*(2)))

        ShiftEdge2 = Group(self.node_D,self.node_E,self.edge4,self.wnode5,self.wnode6)
        ShiftEdge2 = ShiftEdge2.copy()
        self.play(self.edge4.animate.set_color(RED),run_time=0.5)
        ShiftedEdge2 = Group(self.Node_D,self.Node_E,self.Edge4,self.Wnode5,self.Wnode6)
        self.play(Transform(ShiftEdge2,ShiftedEdge2),run_time=0.5)

        ShiftEdge3 = Group(self.node_S,self.node_A,self.edge1,self.wnode1,self.wnode2)
        ShiftEdge3 = ShiftEdge3.copy()
        self.play(self.edge1.animate.set_color(RED),run_time=0.5)
        ShiftedEdge3 = Group(self.Node_S,self.Node_A,self.Edge1,self.Wnode1,self.Wnode2)
        self.play(Transform(ShiftEdge3,ShiftedEdge3),run_time=0.5)

        ShiftEdge4 = Group(self.node_S,self.node_B,self.edge2,self.wnode1,self.wnode3)
        ShiftEdge4 = ShiftEdge4.copy()
        self.play(self.edge2.animate.set_color(RED),run_time=0.5)
        ShiftedEdge4 = Group(self.Node_S,self.Node_B,self.Edge2,self.Wnode1,self.Wnode3)
        self.play(Transform(ShiftEdge4,ShiftedEdge4),run_time=0.5)

        ShiftEdge5 = Group(self.node_T,self.node_F,self.edge6,self.wnode7,self.wnode8)
        ShiftEdge5 = ShiftEdge5.copy()
        self.play(self.edge6.animate.set_color(RED),run_time=0.5)
        ShiftedEdge5 = Group(self.Node_T,self.Node_F,self.Edge6,self.Wnode7,self.Wnode8)
        self.play(Transform(ShiftEdge5,ShiftedEdge5),run_time=0.5)

        ShiftEdge6 = Group(self.node_T,self.node_G,self.edge7,self.wnode7,self.wnode9)
        ShiftEdge6 = ShiftEdge6.copy()
        self.play(self.edge7.animate.set_color(RED),run_time=0.5)
        ShiftedEdge6 = Group(self.Node_T,self.Node_G,self.Edge7,self.Wnode7,self.Wnode9)
        self.play(Transform(ShiftEdge6,ShiftedEdge6),run_time=0.5)

        self.ContraEdge = DashedLine(self.Node_C, self.Node_G, buff=0.06,color=RED_D)
        self.play(FadeIn(self.Edge5),run_time=1.5)
        self.play(FadeOut(self.Edge5),run_time=1.5)
        self.play(FadeIn(self.ContraEdge))

        Graph_Group = Group(self.node_S,self.node_B,self.node_C,self.node_A,self.node_D,self.node_E,self.node_T,self.node_G,self.node_F,self.wnode1,self.wnode2,self.wnode3,self.wnode4,self.wnode5,self.wnode6,self.wnode7,self.wnode8,self.wnode9,self.edge1,self.edge2,self.edge3,self.edge4,self.edge5,self.edge6,self.edge7,self.Node_S,self.Node_B,self.Node_C,self.Node_A,self.Node_D,self.Node_E,self.Node_T,self.Node_G,self.Node_F,self.Wnode1,self.Wnode2,self.Wnode3,self.Wnode4,self.Wnode5,self.Wnode6,self.Wnode7,self.Wnode8,self.Wnode9,self.Edge1,self.Edge2,self.Edge3,self.Edge4,self.Edge6,self.Edge7,ellipse1, ellipse2,self.ContraEdge,ShiftedEdge1,ShiftedEdge2,ShiftedEdge3,ShiftedEdge4,ShiftedEdge5,ShiftedEdge6,edgetobe,ShiftEdge1,ShiftEdge2,ShiftEdge3,ShiftEdge4,ShiftEdge5,ShiftEdge6)


        self.play(FadeIn(Graph_Group))

        self.play(Graph_Group.animate.shift(LEFT*2.4).scale(0.55),run_time=1)
        

        # About proof

        pr1 = Tex("$\\rightarrow$","\; Concetrate On Edge ","U'V'.", font_size=30,stroke_width=1.3)
        pr1.align_to(np.array([1.8,0.9,0]),LEFT+UP)
        pr1.set_color_by_tex("$\\rightarrow$",RED_D)
        pr1.set_color_by_tex("U'V'.",RED_D)
        self.play(Write(pr1),run_time = 1)

        pr2 = Tex("$\\rightarrow$","\; Wt(","U'V'","$) > Wt($","UV",")",font_size=30,stroke_width=1.3)
        pr2.align_to(pr1,LEFT)
        pr2.shift(UP*(0.25))
        pr2.set_color_by_tex("U'V'",RED_D)
        pr2.set_color_by_tex("$\\rightarrow$",RED_D)
        pr2.set_color_by_tex("UV",GREEN_C)
        self.play(Write(pr2),run_time=1)
        
        pr3 = Tex("$\\rightarrow$","\; Consider the Tree T - U'V' + UV ",font_size=30,stroke_width=1.3)
        pr3.align_to(pr2,LEFT)
        pr3.shift(UP*(-0.15))
        pr3.set_color_by_tex("$\\rightarrow$",RED_D)
        self.play(Write(pr3),run_time=0.9)

        pr4 = Tex("Where T is the minimum spanning",font_size=30,stroke_width=1.3)
        pr4.align_to(pr3,LEFT)
        pr4.shift(UP*(-0.55))
        pr4.shift(RIGHT*(0.4))
        self.play(Write(pr4),run_time=0.9)

        pr5 = Tex("Tree",font_size=30,stroke_width=1.3)
        pr5.align_to(pr4,LEFT)
        pr5.shift(UP*(-0.95))
        pr5.shift(RIGHT*(0.1))
        self.play(Write(pr5),run_time=1)

        pr6 = Tex("$\\rightarrow$","\; Wt(","T - U'V'+ UV","$) < Wt($","T",")",font_size=30,stroke_width=1.3)
        pr6.align_to(pr1,LEFT)
        pr6.shift(UP*(-1.35))
        pr6.set_color_by_tex("T",RED_D)
        pr6.set_color_by_tex("$\\rightarrow$",RED_D)
        pr6.set_color_by_tex("T - U'V'+ UV",GREEN_C)
        self.play(Write(pr6),run_time=2)

        pr7 = Tex("$\\rightarrow$","\; A CONTRADICTION !!",font_size=30,stroke_width=1.3)
        pr7.align_to(pr1,LEFT)
        pr7.shift(UP*(-1.75))
        pr7.set_color_by_tex("\; A CONTRADICTION !!",RED_D)
        pr7.set_color_by_tex("$\\rightarrow$",RED_D)
        self.play(Write(pr7),run_time=1)
        self.wait(2)
        self.next_slide()
        self.clear()

        # Time Complexity Without Find Union

        START = (-6.3,2.7,0)
        END = (4,2.7,0)
        question = MarkupText(f'ALGORITHM',font="Britannic Bold",font_size=50 )
        question.shift(3.3*UP + 4*LEFT)
        # self.play(Write(question),run_time=0.2)
        line = Line(START,END,color=YELLOW)
        # self.play(Create(line),run_time=0.2)
        

        a1 = Tex("1. \;\; T \; $\\leftarrow$ \; $\\emptyset$", font_size=40,stroke_width=2)
        a1.shift(UP*2+LEFT*4.7)
        # self.play(Write(a1),run_time=0.5)
        

        a2 = Tex("2. \;\; S \; $\\leftarrow$ \; Sort Edges According To their Weight", font_size=40, stroke_width=2)
        a2.align_to(a1,LEFT)
        a2.shift(UP*1.3)
        # self.play(Write(a2),run_time=0.5)
        

        FE = Tex("3.\;\; FOREACH ",stroke_width = 2,color=RED_D)
        T = Tex("( e in E ) :", font_size=40, stroke_width=2)
        FE.align_to(a2,LEFT)
        T.next_to(FE)
        a3 = VGroup(FE,T)
        a3.align_to(a2,LEFT)
        a3.shift(UP*0.7)
        # self.play(Write(a3),run_time=0.5)
        

        a4 = Tex("${\{}$", font_size=40, stroke_width=2,color=RED_A)
        a4.align_to(a3)
        a4.shift(5*LEFT)
        a4.shift(UP*(-0))
        # self.play(Write(a4),run_time=0.5)
    

        IF = Tex("IF ", font_size=40, stroke_width=2,color=RED_D)
        T = Tex("T + e Does not Contains a Cycle :",stroke_width=2)
        IF.align_to(a4,LEFT)
        

        T.next_to(IF, RIGHT)
        a5 = VGroup(IF,T)
        a5.align_to(a4)
        a5.shift(LEFT*(-0.3))
        a5.shift(UP*(-0.6))
        # self.play(Write(a5),run_time=0.5)
        

        a6 = Tex("${\{}$", font_size=40, stroke_width=2,color=RED_A)
        a6.align_to(a5,LEFT)
        a6.shift(UP*(-1.2))
        # self.play(Write(a6),run_time=0.5)
       

        a7 = Tex("T \; $\\leftarrow$ \; T + e", font_size=40, stroke_width=2)
        a7.align_to(a6,LEFT)
        a7.shift(LEFT*(-0.1))
        a7.shift(UP*(-1.8))
        # self.play(Write(a7),run_time=0.5)
     

        a8 = Tex("${\}}$", font_size=40, stroke_width=2,color=RED_A)
        a8.align_to(a6,LEFT)
        a8.shift(UP*(-2.3))
        # self.play(Write(a8),run_time=0.5)
       

        a9 = Tex("${\}}$", font_size=40, stroke_width=2,color=RED_A)
        a9.align_to(a4,LEFT)
        a9.shift(UP*(-3.1))
        # self.play(Write(a9),run_time=0.5)
        

        a10 = Tex("4. \;\; END", font_size=40, stroke_width=2)
        a10.align_to(a1,LEFT)
        a10.shift(UP*(-3.8))
        # self.play(Write(a10),run_time=0.5)
        
        algo_group = Group(question,line,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10)
        self.play(algo_group.animate.shift(UP*1.6+LEFT*2.4).scale(0.55),run_time=1)
        self.next_slide()

        START = (-2,2.8,0)
        END = (9,2.8,0)
        question = MarkupText(f'Running Time',font="Britannic Bold",font_size=50 )
        question.shift(3.3*UP )
        question.shift((-0.5)*LEFT)
        line = Line(START,END,color=YELLOW)
        run_time_group = Group(question,line)
        self.play(run_time_group.animate.scale(0.55),run_time=1)

        t1 = Tex("$\\rightarrow$", "\; Kruskal's Algorithm : ","O(mn)" ,font_size=32, stroke_width=2)
        t1.shift(RIGHT*(3)+UP*(2.2))
        t1[0].set_color(RED_C)
        t1[2].set_color(YELLOW_C)
        self.play(Write(t1),run_time=1)

        t2 = Tex("$\\rightarrow$", "\; Prim's Algorithm : ","O((m+n)logn)" ,font_size=32, stroke_width=2)
        t2.align_to(t1,LEFT)
        t2.shift(UP*(1.6))
        t2[0].set_color(RED_C)
        t2[2].set_color(YELLOW_C)
        self.play(Write(t2),run_time = 1)
        self.next_slide()
        self.wait(2.2)
        self.clear()

        # Find and Union

        text1 = ["What "," Is "," The ", " Problem ", " ?"]
      
        # Create dot groups
        groups = VGroup(*[MarkupText(text) for text  in text1]).arrange_submobjects(buff=0.3)
        self.play(Write(groups),run_time=1)

        self.play(groups.animate(run_time=1, lag_ratio=0.1).shift(UP*3.2 + LEFT * 2.5),run_time=1)
        START = (-6.3,2.7,0)
        END = (4,2.7,0)
        line = Line(START,END,color=YELLOW)
        self.play(Create(line),run_time=0.6)

        # Problem text
        text1 = Text("The Problem :",stroke_width = 1,color=BLUE,font_size=25).move_to([-5,2.2,0])
        self.play(Write(text1),run_time=1)
        text2 = Text("For an edge (u,v), how do we find that u and v are in the same \nconnected component ?",font_size = 25,color=WHITE).move_to([1.2,2,0])
        self.play(Write(text2),run_time=1.2)

        # Solution text
        text3 = Text("The Solution :",stroke_width = 1,color=BLUE,font_size=25).move_to([-5,1.2,0])
        self.play(Write(text3),run_time=1.2)
        text4 = Text("All vertices in the same connected component have the same label.",font_size = 25,color=WHITE).move_to([1.3,1.2,0])
        self.play(Write(text4),run_time=1.2)

        self.play(FadeOut(text1,text2),run_time=1)

        text3.shift(UP * 1)
        text4.shift(UP * 1)
        self.play(FadeIn(text3),FadeIn(text4),run_time=1)

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
        self.play(FadeIn(self.node_grp),run_time=1)

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
        self.play(FadeIn(mobj),run_time=1)


        e1 = Line(self.node_grp[3],self.node_grp[4])
        self.play(FadeIn(e1),run_time=1)
        self.play(FadeOut(node_5),FadeOut(t5),run_time=1)
        node_5 = LabeledDot(Text("4",color=RED,font_size=20),point=np.array([3, -1, 0]))
        node_5.scale(0.7)
        node_5.shift(DOWN * 0.45 + LEFT * 2.3)
        t5 = Text("4",font_size=20).move_to(findArr)
        self.play(FadeIn(node_5),FadeIn(t5),run_time=1)

        e2 = Line(self.node_grp[5], self.node_grp[7])
        self.play(FadeIn(e2),run_time=1)
        self.play(FadeOut(node_8),FadeOut(t8),run_time=1)
        node_8 = LabeledDot(Text("6",color=RED,font_size=20),point=np.array([5, -1, 0]))
        node_8.scale(0.7)
        node_8.shift(DOWN * 0.45 + LEFT * 2.9)
        t8 = Text("6",font_size=20).move_to(findArr).shift(RIGHT * 3)
        self.play(FadeIn(node_8),FadeIn(t8),run_time=1)

        e3 = Line(self.node_grp[5], self.node_grp[8])
        self.play(FadeIn(e3),run_time=1)
        self.play(FadeOut(node_9),FadeOut(t9),run_time=1)
        node_9 = LabeledDot(Text("6",color=RED,font_size=20),point=np.array([6, 0.6, 0]))
        node_9.scale(0.7)
        node_9.shift(DOWN * 0.9 + LEFT * 3.2)
        t9 = Text("6",font_size=20).move_to(findArr).shift(RIGHT * 4)
        self.play(FadeIn(node_9),FadeIn(t9),run_time=1)

        e4 = Line(self.node_grp[3], self.node_grp[5])
        self.play(FadeIn(e4),run_time=1)
        self.play(FadeOut(text3),FadeOut(text4),run_time=1)
        text3 = Text("Main Idea :",stroke_width = 1,color=BLUE,font_size=25).move_to([-5,1.2,0]).shift(UP * 1)
        text4 = Text("Change the Label of the Smaller tree",font_size = 25,color=WHITE).move_to([-1.3,1.15,0]).shift(UP * 1)
        self.play(Write(text3),Write(text4),run_time=1)

        ellipse1 = Ellipse(
            width=2, height=2.6 ,stroke_width=5
        ).move_to(UP * -0.6 + RIGHT * 0.2)
        self.play(FadeIn(ellipse1),run_time=1.5)
        self.wait()

        self.play(FadeOut(node_4),FadeOut(node_5),FadeOut(t4),FadeOut(t5),run_time=1)
        node_4 = LabeledDot(Text("6",color=RED,font_size=20),point=np.array([2, 1, 0]))
        node_4.scale(0.7)
        node_4.shift(DOWN * 1 + LEFT * 2)
        node_5 = LabeledDot(Text("6",color=RED,font_size=20),point=np.array([3, -1, 0]))
        node_5.scale(0.7)
        node_5.shift(DOWN * 0.45 + LEFT * 2.3)
        t5 = Text("6",font_size=20).move_to(findArr)
        t4 = Text("6",font_size=20).move_to(findArr).shift(LEFT * 1)
        self.play(FadeIn(node_4),FadeIn(node_5),FadeIn(t5),FadeIn(t4),run_time=1)
        self.wait(2.2)
        self.clear()
        # Algorithm with Find and Union


        START = (-6.3,2.7,0)
        END = (4,2.7,0)
        question = MarkupText(f'ALGORITHM',font="Britannic Bold",font_size=50 )
        question.shift(3.3*UP + 4*LEFT)
        # self.play(Write(question),run_time=0.2)
        line = Line(START,END,color=YELLOW)
        # self.play(Create(line),run_time=0.2)
        

        a1 = Tex("1. \;\; T \; $\\leftarrow$ \; $\\emptyset$", font_size=40,stroke_width=2)
        a1.shift(UP*2+LEFT*4.7)
        # self.play(Write(a1),run_time=0.5)
        

        a2 = Tex("2. \;\; S \; $\\leftarrow$ \; Sort Edges According To their Weight", font_size=40, stroke_width=2)
        a2.align_to(a1,LEFT)
        a2.shift(UP*1.3)
        # self.play(Write(a2),run_time=0.5)
        

        FE = Tex("3.\;\; FOREACH ",stroke_width = 2,color=RED_D)
        ite = Tex("( e in E ) :", font_size=40, stroke_width=2)
        FE.align_to(a2,LEFT)
        ite.next_to(FE)
        a3 = VGroup(FE,ite)
        a3.align_to(a2,LEFT)
        a3.shift(UP*0.7)
        # self.play(Write(a3),run_time=0.5)
        

        a4 = Tex("${\{}$", font_size=40, stroke_width=2,color=RED_A)
        a4.align_to(a3)
        a4.shift(5*LEFT)
        a4.shift(UP*(-0))
        # self.play(Write(a4),run_time=0.5)
    

        IF = Tex("IF ", font_size=40, stroke_width=2,color=RED_D)
        T = Tex("T + e Does not Contains a Cycle :",stroke_width=2)
        IF.align_to(a4,LEFT)
        

        T.next_to(IF, RIGHT)
        a5 = VGroup(IF,T)
        a5.align_to(a4)
        a5.shift(LEFT*(-0.3))
        a5.shift(UP*(-0.6))
        # self.play(Write(a5),run_time=0.5)
        

        a6 = Tex("${\{}$", font_size=40, stroke_width=2,color=RED_A)
        a6.align_to(a5,LEFT)
        a6.shift(UP*(-1.2))
        # self.play(Write(a6),run_time=0.5)
       

        a7 = Tex("T \; $\\leftarrow$ \; T + e", font_size=40, stroke_width=2)
        a7.align_to(a6,LEFT)
        a7.shift(LEFT*(-0.1))
        a7.shift(UP*(-1.8))
        # self.play(Write(a7),run_time=0.5)
     

        a8 = Tex("${\}}$", font_size=40, stroke_width=2,color=RED_A)
        a8.align_to(a6,LEFT)
        a8.shift(UP*(-2.3))
        # self.play(Write(a8),run_time=0.5)
       

        a9 = Tex("${\}}$", font_size=40, stroke_width=2,color=RED_A)
        a9.align_to(a4,LEFT)
        a9.shift(UP*(-3.1))
        # self.play(Write(a9),run_time=0.5)
        

        a10 = Tex("4. \;\; END", font_size=40, stroke_width=2)
        a10.align_to(a1,LEFT)
        a10.shift(UP*(-3.8))
        # self.play(Write(a10),run_time=0.5)
        
        algo_group = Group(question,line,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10)
        self.play(algo_group.animate.shift(UP*1.8+LEFT*2.4).scale(0.55),run_time=1)
        self.next_slide()

        down_group=Group(a3,a4,a5,a6,a7,a8,a9,a10)
        self.play(down_group.animate.shift(DOWN*(1)),run_time=1)
        self.next_slide()

        n1 = Tex("3.\;\;FOREACH "," v "," $\\in$ "," $\\mathbb{V}$ ", font_size=26, stroke_width=2,color=YELLOW_C)
        n1.align_to(a1,LEFT)
        n1.shift(UP*(2))
        n1[1].set_color(BLUE_B)
        n1[3].set_color(RED_C)
        self.play(Write(n1),run_time=1)

        n2 = Tex("LABEL[","v","] $\\leftarrow$ ", " v; ", font_size=26, stroke_width=2,color=YELLOW_C)
        n2.align_to(a1,LEFT)
        n2.shift(UP*(1.6)+LEFT*(-1))
        n2[3].set_color(BLUE_B)
        n2[1].set_color(BLUE_B)
        self.play(Write(n2),run_time=1)
        self.next_slide()

        new_T = Tex("(" ," e = (u,v) "," In Increasing Order ) :",font_size=26, stroke_width=2)
        new_T[1].set_color(YELLOW_C)
        new_T.next_to(a3,RIGHT)
        new_T.shift(LEFT*1.15)
        new_FE = Tex("4.\;\; FOREACH ",font_size=26,stroke_width = 2,color=RED_D)
        new_FE.next_to(ite,LEFT)
        new_FE.align_to(a1,LEFT)
        self.play(Transform(FE,new_FE),Transform(ite, new_T),run_time=1)       
        self.play(FadeOut(Group(a8,a7,a6,a5)),Group(a9,a10).animate.shift(DOWN*1.3),run_time=1)
        self.next_slide()
        # inner part of for loop

        n3 = Tex("Do BFS from u ${\&}$ v In Parallel", font_size=26, stroke_width=2)
        n3.shift([-4,0.3,0])
        n4 = Tex("Assume WLOG that BFS(u) Finishes First", font_size=26, stroke_width=2)
        n4.shift([-3.4,-0.2,0])
        inner_group = Group(n3,n4)
        inner_group.shift(LEFT*(-0.5))
        self.play(FadeIn(n3),FadeIn(n4),run_time=1)
        self.next_slide()

        n5 = Tex("FOREACH ","w $\\in$ BFS-Tree(u) :",font_size=26, stroke_width=2,color=YELLOW_E)
        n5.align_to(inner_group,LEFT)
        n5.shift(DOWN*0.8)
        n6 = Tex("LABEL[w] $\\leftarrow$ LABEL[v] ;",font_size=26, stroke_width=2)
        n6.align_to(n5,LEFT)
        n6.shift(DOWN*1.2+RIGHT*(1))
        self.play(FadeIn(n5),FadeIn(n6),run_time=1)
        self.next_slide()

        n7 = Tex("T \; $\\leftarrow$ \; T + e", font_size=26, stroke_width=2,color = BLUE_C)
        n7.align_to(n5,LEFT)
        n7.shift(DOWN*1.9)
        self.play(FadeIn(n7),run_time=1)
        

        new_a10 = Tex("5. \;\; END", font_size=26, stroke_width=2)
        new_a10.align_to(a1,LEFT)
        new_a10.next_to(a9,DOWN)
        new_a10.shift(RIGHT*(0.1))
        self.play(Transform(a10,new_a10),run_time=1)
        self.next_slide()

        brace1 = Brace(a2,direction=RIGHT,color=RED_E)
        self.play(Create(brace1),run_time=1)

        text_group = Group(n1,n2)
        brace2 = Brace(text_group, direction=RIGHT,color=RED_E)
        self.play(Create(brace2),run_time=1)
        

        brace3 = Brace(Group(n3,n4,n5,n6),direction=RIGHT,color=RED_E)
        self.play(Create(brace3),run_time=1)

        t1 = Tex("O(mlogn)", font_size=26, stroke_width=2,color=BLUE_E)
        t1.next_to(brace1,RIGHT)

        t2= Tex("O(n)", font_size=26, stroke_width=2,color=BLUE_E)
        t2.next_to(brace2,RIGHT)

        t3 = Tex("O(${\#}$ Vertices In Connected Component of u)", font_size=26, stroke_width=2,color=BLUE_E)
        t3.next_to(brace3,RIGHT)

        self.play(FadeIn(t1,t2,t3),run_time=1)
        self.next_slide()
        self.wait(3)
        self.clear()

        # Time Complexity of Find and Union

        text1 = Text("TIME ",color=BLUE,font_size=30).move_to([-5,2.5,0])
        self.play(Write(text1),run_time=1)
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

        self.play(Write(formula1),run_time=1)
        self.play(FadeIn(t_1),run_time=1)
        self.play(Write(formula2),run_time=1)
        self.play(FadeIn(t_2),run_time=1)
        self.play(Write(formula3),run_time=1)
        self.play(FadeIn(t_3),run_time=1)

        question_text = Text("Q: How Many times v changes its Label ?",font_size=30,color=RED).move_to([-1.8,-0.2,0])
        self.play(FadeIn(question_text),run_time=1)

        c1 = Circle(radius=0.5,color=WHITE).move_to([-4.5,-1.6,0])
        lbl1 = MathTex(
            "1",
            color = WHITE,
            font_size=25
        ).move_to([-4.5,-2.3,0])
        dot1 = Dot(point=np.array([-4.6, -1.6, 0]))
        txt1 = Text("v",font_size=25).next_to(dot1,DOWN * 0.4)
        self.play(FadeIn(c1),FadeIn(lbl1),FadeIn(dot1),FadeIn(txt1),run_time=1)
        arrow_1 = Arrow(start=LEFT,end=RIGHT)
        arrow_1.scale(0.4)
        arrow_1.shift(LEFT * 3.7, DOWN * 1.6)
        self.play(FadeIn(arrow_1),run_time=1)

        c2 = Circle(radius=0.6,color=WHITE).move_to([-2.7,-1.6,0])
        lbl2 = MathTex(
            " \geq 2",
            color = WHITE,
            font_size=25
        ).move_to([-2.7,-2.5,0])
        dot2 = Dot(point=np.array([-2.9, -1.6, 0]))
        dot3 = Dot(point=np.array([-2.5, -1.6, 0]))
        txt2 = Text("v",font_size=25).next_to(dot2,DOWN * 0.4)
        self.play(FadeIn(c2),FadeIn(lbl2),FadeIn(dot2),FadeIn(dot3),FadeIn(txt2),run_time=1)
        arrow_2 = Arrow(start=LEFT,end=RIGHT)
        arrow_2.scale(0.4)
        arrow_2.shift(LEFT * 1.7, DOWN * 1.6)
        self.play(FadeIn(arrow_2),run_time=1)

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
        self.play(FadeIn(c3),FadeIn(lbl3),FadeIn(dot4),FadeIn(dot5),FadeIn(dot6),FadeIn(dot7),FadeIn(txt3),run_time=1)

        dot_text = Text(". . . . . . .",font_size=30,color=WHITE).shift(DOWN * 1.6 + RIGHT * 1)
        self.play(FadeIn(dot_text),run_time=1)

        arrow_3 = Arrow(start=LEFT,end=RIGHT)
        arrow_3.scale(0.4)
        arrow_3.shift(RIGHT * 2.5, DOWN * 1.6)
        self.play(FadeIn(arrow_3),run_time=1)

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
        self.play(FadeIn(c4),FadeIn(lbl4),FadeIn(dot8),FadeIn(dot9),FadeIn(dot10),FadeIn(dot11),FadeIn(dot12),FadeIn(dot13),FadeIn(dot14),FadeIn(dot15),FadeIn(txt4),run_time=1)
        
        last_text = Text("# Times v changed its Label = logn",font_size=30,color=BLUE).move_to([-2,-3.1,0])
        self.play(FadeIn(last_text),run_time=1)

        self.wait()

        self.play(FadeOut(dot1,dot2,dot3,dot4,dot5,dot6,dot7,dot8,dot9,dot10,dot11,dot12,dot13,dot14,dot15,txt1,txt2,txt3,txt4),FadeOut(c1,c2,c3,c4),FadeOut(arrow_1,arrow_2,arrow_3),FadeOut(question_text,last_text,dot_text),FadeOut(lbl1,lbl2,lbl3,lbl4),run_time=1)

        formula4 = MathTex(
            "= O(m.logn) + n.logn",
            color = WHITE,
            font_size = 25
        ).move_to([-3,-0.5,0])
        self.play(FadeIn(formula4),run_time=1)

        formula5 = MathTex(
            "= O((m+n).logn)",
            color = WHITE,
            font_size = 25
        ).move_to([-3.2,-1.5,0])
        self.play(FadeIn(formula5),run_time=1)
        self.wait(3)
