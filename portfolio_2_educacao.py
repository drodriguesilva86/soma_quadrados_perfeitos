from manim import *

class portfolio2(Scene):
    def construct(self):
        #circ = Circle(fill_color=RED, fill_opacity=0.7)                   # create a circle
        #circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        #self.play(DrawBorderThenFill(circ))
        #self.wait(1)
        #texto

        tnome_1 = Text("Douglas Rodrigues Silva")
        
        tnome_2 = Text("RA: 8149734")

        t = VGroup(tnome_1, tnome_2).arrange(DOWN)

        t2 = Text(
            "Qual é o maior número de quadrados, presentes na figura ?",
            t2c = {'[19:29]': ORANGE}
        ).scale(0.6).shift(3*UP)
        
        quadrado = Square(side_length=2.0)

        grupo_4_por_4 = VGroup(*[quadrado.copy() for i in range(4)]).arrange(RIGHT).next_to(t2, DOWN).scale(0.5)
        grupo_2_4_por_4 = VGroup(*[grupo_4_por_4.copy() for i in range(4)]).arrange(DOWN)
        
        t3 = Text(
            "Quantos quadrados podemos formar com quadrados ?",
            t2c = {'[7:16]': YELLOW, '[32:41]': YELLOW}
        ).scale(0.6).shift(3*UP)
        #t.set_stroke(color=GREEN, width=20)
        #t.shift(3*UP)
        quadrado_1 = quadrado.set_fill(YELLOW, opacity=1.0)

        t4 = Text("1", color=YELLOW).next_to(quadrado_1, DOWN)
        
        quadrado_1_2 = VGroup(*[quadrado.copy() for i in range(2)]).arrange(RIGHT).set_fill(RED, opacity=1.0)
        quadrado_2_2 = VGroup(*[quadrado_1_2.copy() for i in range(2)]).arrange(DOWN).set_fill(GREEN, opacity=1.0)
        #t.align_to(circ.get_edge_center(UP), DOWN).shift(0.1*UP)
        t5 = MathTex(r"4 = 2 \cdot 2 = 2^{2}", color=GREEN).next_to(quadrado_2_2, DOWN)

        quadrado_1_3 = VGroup(*[quadrado.copy() for i in range(3)]).arrange(RIGHT)
        quadrado_3_3 = VGroup(*[quadrado_1_3.copy() for i in range(3)]).arrange(DOWN).set_fill(BLUE, opacity=1.0).scale(0.8)

        t6 = MathTex(r"9 = 3 \cdot 3 = 3^{2}", color=BLUE).next_to(quadrado_3_3, DOWN)

        #quadrado_1_4 = VGroup(*[quadrado.copy() for i in range(4)]).arrange(RIGHT).next_to(t2, DOWN).scale(0.5)
        #quadrado_4_4 = VGroup(*[quadrado_1_4.copy() for i in range(4)]).arrange(DOWN).set_fill(ORANGE, opacity=1.0)

        t7 = MathTex(r"16 = 4 \cdot 4 = 4^{2}", color=ORANGE).next_to(grupo_2_4_por_4, DOWN)
        
        t8 = Text(
            "Quadrados perfeitos", 
            t2c = {'[0:9]': PINK}
            ).scale(0.7).shift(3*UP)

        t9 = Text(
            "Um número a é quadrado perfeito, se:",
            t2c = {'[10:18]': PINK}
            ).scale(0.6).next_to(t8, DOWN).shift(2.3*LEFT)

        t10 = MathTex(r"n \in \mathbb{N}^{*} | n \cdot n = n^{2} = a").next_to(t9, RIGHT)

        # numeros = TexMobject(
        #     r"1 \cdot 1 = 1^{2} = 1",
        #     r"2 \cdot 2 = 2^{2} = 4",
        #     r"3 \cdot 3 = 3^{2} = 9",
        #     r"4 \cdot 4 = 4^{2} = 16",
        #     r"5 \cdot 5 = 5^{2} = 25",
        #     r"6 \cdot 6 = 6^{2} = 36",
        #     r"7 \cdot 7 = 7^{2} = 49")

        # numeros[0].shift(UP)
        # numeros[1].next_to(numeros[0], DOWN)
        # numeros[2].next_to(numeros[1], DOWN)
        # numeros[3].next_to(numeros[2], DOWN)
        # numeros[4].next_to(numeros[3], DOWN)
        # numeros[5].next_to(numeros[4], DOWN)
        # numeros[6].next_to(numeros[5], DOWN)
        
        n_1 = MathTex(r"1 \cdot 1 = 1^{2} = 1").shift(UP)
        n_2 = MathTex(r"2 \cdot 2 = 2^{2} = 4").next_to(n_1, DOWN)
        n_3 = MathTex(r"3 \cdot 3 = 3^{2} = 9").next_to(n_2, DOWN)
        n_4 = MathTex(r"4 \cdot 4 = 4^{2} = 16").next_to(n_3, DOWN)
        n_5 = MathTex(r"5 \cdot 5 = 5^{2} = 25").next_to(n_4, DOWN)
        n_6 = MathTex(r"6 \cdot 6 = 6^{2} = 36").next_to(n_5, DOWN)
        n_7 = MathTex(r"7 \cdot 7 = 7^{2} = 49").next_to(n_6, DOWN)

        numeros = VGroup(n_1, n_2, n_3, n_4)

        box_1 = SurroundingRectangle(numeros, color=YELLOW)

        self.play(GrowFromCenter(t))
        #self.play(Write(t))
       # self.wait(2)
        #self.play(FadeOut(t))
        #form = MathTex(r"F(x) = \int f(x) dx")
        #form.align_to(circ.get_edge_center(DOWN), UP).shift(0.2*DOWN)
        #self.play(Write(form))
        self.wait(2)
        #self.remove(t)
        
        self.play(Transform(t, t2))

        #self.play(FadeIn(t2))
        #self.play(Write(t2))
        
        self.wait(1)
        
        self.play(Write(grupo_2_4_por_4))

        self.wait(2)

        self.play(FadeOut(t), FadeOut(t2), FadeOut(grupo_2_4_por_4))

        self.wait(1)

        self.play(Write(t3))

        self.wait(1)

        self.play(Write(quadrado_1))

        self.wait(1)

        self.play(Write(t4))

        self.wait(1)

        self.play(FadeOut(t4))

        self.play(ReplacementTransform(quadrado_1, quadrado_1_2))
        
        self.wait(2)

        self.play(ReplacementTransform(quadrado_1_2, quadrado_2_2))

        self.wait(1)

        self.play(Write(t5), run_time=5)

        self.wait(1)

        self.play(FadeOut(t5))

        self.wait(1)

        self.play(ReplacementTransform(quadrado_2_2, quadrado_3_3))
        
        self.wait(1)

        self.play(Write(t6), run_time=5)

        self.wait(1)

        self.play(FadeOut(t6))

        self.wait(1)

        self.play(ReplacementTransform(quadrado_3_3, grupo_2_4_por_4.set_fill(ORANGE, opacity=1.0)))

        self.wait(1)

        self.play(Write(t7), run_time=5)

        self.wait(1)

        self.play(FadeOut(t7), FadeOut(t3), FadeOut(grupo_2_4_por_4.set_fill(ORANGE, opacity=1.0)))

        self.wait(1)

        self.play(Write(t8))

        self.wait(1)

        self.play(Write(t9))

        self.wait(1)

        self.play(Write(t10))

        self.wait(1)

        self.play(Write(n_1))

        self.wait(1)

        self.play(Write(n_2))

        self.wait(1)

        self.play(Write(n_3))

        self.wait(1)

        self.play(Write(n_4))

        self.wait(1)

        self.play(Write(n_5))

        self.wait(1)

        self.play(Write(n_6))

        self.wait(1)

        self.play(Write(n_7))

        self.wait(1)

        self.play(Create(box_1))
        #basel = MathTex(r"ZZ, R^{3}")
        #VGroup(title, basel).arrange(DOWN).scale(1.5)
        #self.remove(t)
        self.wait(1)

        self.play(FadeOut(t8), FadeOut(t9), FadeOut(t10), FadeOut(n_1), FadeOut(n_2), FadeOut(n_3), FadeOut(n_4), FadeOut(n_5), FadeOut(n_6), FadeOut(n_7), FadeOut(box_1))

        self.wait()

class Soma_portfolio_2(Scene):
    def construct(self):
        t2 = Text(
            "Qual é o maior número de quadrados, presentes na figura ?",
            t2c = {'[19:29]': ORANGE}
        ).scale(0.6).shift(3*UP)

        quadrado = Square(side_length=2.0)

        quadrado_1_3 = VGroup(*[quadrado.copy() for i in range(3)]).arrange(RIGHT)
        quadrado_3_3 = VGroup(*[quadrado_1_3.copy() for i in range(3)]).arrange(DOWN)

        quadrado_1_2 = VGroup(*[quadrado.copy() for i in range(2)]).arrange(RIGHT)
        quadrado_2_2 = VGroup(*[quadrado_1_2.copy() for i in range(2)]).arrange(DOWN)
        
        quadrado_1_4 = VGroup(*[quadrado.copy() for i in range(4)]).arrange(RIGHT)
        quadrado_4_4 = VGroup(*[quadrado_1_4.copy() for i in range(4)]).arrange(DOWN)
        #texto referente ao tabuleiro 2x2

        t = MathTex(r"1", r"+", r"4", r" = 5")
        t[0].set_color(GREEN)
        t[2].set_color(YELLOW)

        #texto referente ao tabuleiro 3x3

        ta = MathTex(r"1", r"+", r"4", r"+", r"9", r" = 14")
        ta[0].set_color(BLUE)
        ta[2].set_color(GREEN)
        ta[4].set_color(YELLOW)

        #texto referente ao tabuleiro 4x4

        tb = MathTex(r"1", r"+", r"4", r"+", r"9", r"+", r"16", r" = 30")
        tb[0].set_color(ORANGE)
        tb[2].set_color(BLUE)
        tb[4].set_color(GREEN)
        tb[6].set_color(YELLOW)

        #texto da soma dos quadrados perfeitos

        t_1_1 = MathTex(r"1 = 1^{2}", color=YELLOW)
        t_2_2 = MathTex(r"5 = 1 + 4 = 1^{2} + 2^{2}", color=GREEN)
        t_3_3 = MathTex(r"14 = 1 + 4 + 9 = 1^{2} + 2^{2} + 3^{2}", color=BLUE)
        t_4_4 = MathTex(r"30 = 1 + 4 + 9 + 16 = 1^{2} + 2^{2} + 3^{2} + 4^{2}", color=ORANGE)

        #Animacao
        self.play(Write(t2))
        self.wait(1)

        self.play(FadeOut(t2))
        self.wait()

        self.play(Create(quadrado_2_2.scale(0.8)))

        self.wait(1)

        self.play(quadrado_2_2.animate.set_fill(GREEN, opacity=1.0))
        self.play(Write(t[0].scale(2).shift(3*UP + LEFT)), run_time=1)

        self.wait(1)

        self.play(quadrado_2_2.animate.set_fill(GREEN, opacity=0.0))

        self.wait(1)

        self.play(Create(quadrado.set_fill(YELLOW, opacity=1.0).scale(0.8).shift(0.9*LEFT+0.9*UP)))
        self.wait(1)

        self.play(quadrado.animate.shift(1.8*RIGHT))
        self.play(quadrado.animate.shift(1.8*DOWN))
        self.play(quadrado.animate.shift(1.8*LEFT))

        self.play(Write(t[1:].scale(2).next_to(t[0], RIGHT)), run_time=2)
        
        self.wait(1)

        self.play(FadeOut(t), FadeOut(quadrado), FadeOut(quadrado_2_2))
        
        self.wait(1)

        #Quadrado 3x3

        self.play(Create(quadrado_3_3.scale(0.8).shift(0.5*DOWN)))

        self.wait(1)

        self.play(quadrado_3_3.animate.set_fill(BLUE, opacity=1.0))
        self.play(Write(ta[0].scale(2).shift(3*UP + 1.5*LEFT)), run_time=1)

        self.wait(1)

        self.play(quadrado_3_3.animate.set_fill(BLUE, opacity=0.0))

        self.wait(1)

        self.play(Create(quadrado_2_2.set_fill(GREEN, opacity=1.0).shift(0.9*LEFT + 0.4*UP)))
        self.wait(1)

        self.play(quadrado_2_2.animate.shift(1.8*RIGHT))
        self.play(quadrado_2_2.animate.shift(1.8*DOWN))
        self.play(quadrado_2_2.animate.shift(1.8*LEFT))

        self.play(Write(ta[1:3].scale(2).next_to(ta[0], RIGHT)), run_time=2)

        self.wait(1)

        self.play(FadeOut(quadrado_2_2))
        self.play(Create(quadrado.set_fill(YELLOW, opacity=1.0).shift(0.9*LEFT+2.2*UP)))

        self.wait(1)
        self.play(quadrado.animate.shift(1.8*RIGHT))
        self.play(quadrado.animate.shift(1.8*RIGHT))
        self.play(quadrado.animate.shift(1.8*DOWN))
        self.play(quadrado.animate.shift(1.8*LEFT))
        self.play(quadrado.animate.shift(1.8*LEFT))
        self.play(quadrado.animate.shift(1.8*DOWN))
        self.play(quadrado.animate.shift(1.8*RIGHT))
        self.play(quadrado.animate.shift(1.8*RIGHT))

        self.play(Write(ta[3:].scale(2).next_to(ta[1:3], RIGHT)), run_time=2)

        self.wait(1)
        self.play(FadeOut(quadrado), FadeOut(quadrado_3_3), FadeOut(ta))
        self.wait(1)

        #Quadrado 4x4

        self.play(Create(quadrado_4_4.scale(0.6).shift(0.5*DOWN)))

        self.wait(1)

        self.play(quadrado_4_4.animate.set_fill(ORANGE, opacity=1.0))
        self.play(Write(tb[0].scale(2).shift(3*UP + 1.5*LEFT)), run_time=1)

        self.wait(1)

        self.play(quadrado_4_4.animate.set_fill(ORANGE, opacity=0.0))

        self.wait(1)

        self.play(Create(quadrado_3_3.scale(0.75).set_fill(BLUE, opacity=1.0).shift(0.67*LEFT + 0.67*UP)))
        self.wait(1)

        self.play(quadrado_3_3.animate.shift(1.34*RIGHT))
        self.play(quadrado_3_3.animate.shift(1.34*DOWN))
        self.play(quadrado_3_3.animate.shift(1.34*LEFT))

        self.play(Write(tb[1:3].scale(2).next_to(tb[0], RIGHT)), run_time=2)

        self.wait(1)

        self.play(FadeOut(quadrado_3_3))
        self.play(Create(quadrado_2_2.scale(0.75).set_fill(GREEN, opacity=1.0).shift(0.43*LEFT + 2.26*UP)))

        self.wait(1)
        self.play(quadrado_2_2.animate.shift(1.34*RIGHT))
        self.play(quadrado_2_2.animate.shift(1.34*RIGHT))
        self.play(quadrado_2_2.animate.shift(1.34*DOWN))
        self.play(quadrado_2_2.animate.shift(1.34*LEFT))
        self.play(quadrado_2_2.animate.shift(1.34*LEFT))
        self.play(quadrado_2_2.animate.shift(1.34*DOWN))
        self.play(quadrado_2_2.animate.shift(1.34*RIGHT))
        self.play(quadrado_2_2.animate.shift(1.34*RIGHT))

        self.play(Write(tb[3:5].scale(2).next_to(tb[1:3], RIGHT)), run_time=2)

        self.wait(1)
        
        self.play(FadeOut(quadrado_2_2))
        self.play(Create(quadrado.scale(0.75).set_fill(YELLOW, opacity=1.0).shift(3.805*LEFT + 3.825*UP)))
        
        self.wait(1)
        self.play(quadrado.animate.shift(1.34*RIGHT))
        self.play(quadrado.animate.shift(1.34*RIGHT))
        self.play(quadrado.animate.shift(1.34*RIGHT))
        self.play(quadrado.animate.shift(1.34*DOWN))
        self.play(quadrado.animate.shift(1.34*LEFT))
        self.play(quadrado.animate.shift(1.34*LEFT))
        self.play(quadrado.animate.shift(1.34*LEFT))
        self.play(quadrado.animate.shift(1.34*DOWN))
        self.play(quadrado.animate.shift(1.34*RIGHT))
        self.play(quadrado.animate.shift(1.34*RIGHT))
        self.play(quadrado.animate.shift(1.34*RIGHT))
        self.play(quadrado.animate.shift(1.34*DOWN))
        self.play(quadrado.animate.shift(1.34*LEFT))
        self.play(quadrado.animate.shift(1.34*LEFT))
        self.play(quadrado.animate.shift(1.34*LEFT))

        self.play(Write(tb[5:].scale(2).next_to(tb[3:5], RIGHT)), run_time=2)
        
        self.wait(1)

        self.play(FadeOut(quadrado), FadeOut(tb), FadeOut(quadrado_4_4))

        self.wait(1)

        self.play(Create(quadrado.set_fill(YELLOW, opacity=0.0).shift(3*LEFT + 5.5*UP)))
        self.play(Create(quadrado_2_2.set_fill(YELLOW, opacity=0.0).scale(0.5).next_to(quadrado, DOWN, buff=0.5)))
        self.play(Create(quadrado_3_3.set_fill(YELLOW, opacity=0.0).scale(0.4).next_to(quadrado_2_2, DOWN, buff=0.5)))
        self.play(Create(quadrado_4_4.set_fill(YELLOW, opacity=0.0).scale(0.3).next_to(quadrado_3_3, DOWN, buff=0.5)))

        self.wait(1)
        self.play(Write(t_1_1.scale(1.2).next_to(quadrado, RIGHT)), run_time = 1)
        self.wait(1)
        self.play(Write(t_2_2.scale(1.2).next_to(quadrado_2_2, RIGHT)), run_time = 2)
        self.wait(1)
        self.play(Write(t_3_3.scale(1.2).next_to(quadrado_3_3, RIGHT)), run_time = 3)
        self.wait(1)
        self.play(Write(t_4_4.scale(1.2).next_to(quadrado_4_4, RIGHT)), run_time = 4)

        self.wait(2)

        self.play(FadeOut(t_1_1), FadeOut(t_2_2), FadeOut(t_3_3), FadeOut(t_4_4), FadeOut(quadrado), FadeOut(quadrado_2_2), FadeOut(quadrado_3_3), FadeOut(quadrado_4_4))
        self.wait(2)

class Claretiano(Scene):
    def construct(self):
        t = Text("Educação Matemática")
        t2 = Text("Prática Pedagógica - Portfólio 2")
        t3 = Text("Aplicação")

        self.play(Write(t.shift(2*UP)), run_time=2.0)
        self.play(Write(t2.next_to(t, DOWN, buff=1)), run_time=2.0)
        self.play(Write(t3.next_to(t2, DOWN, buff=1)), run_time=2.0)

        self.wait(1)

        self.play(FadeOut(t), FadeOut(t2), FadeOut(t3))
        self.wait(3)
