from manim import * 
from math import *

class Miniature(Scene):
    def construct(self):
        psi = Text("Ψ", color=BLUE)
        codeMath = Text("CodeMath").next_to(psi, DOWN)

        self.play(Write(psi), run_time = 2)
        self.play(Write(codeMath), run_time = 2)
        self.wait(2)
        self.play(FadeOut(psi, codeMath))
        self.wait(2)

        ordre = Text("Take a number between 1 and 10", font_size=20).shift(2*UP)
        x = MathTex(r"x", color=BLUE)
        double = MathTex(r"2x", color=BLUE)
        add_4 = MathTex(r"2x + 4", color=BLUE)
        divide_by_2 = MathTex(r"\frac{2x + 4}{2} - x", color=BLUE)
        
        result = VGroup(
        MarkupText(f'I can say that your <span fgcolor="{BLUE}">result</span> is', font_size=20).shift(2*UP),
        MathTex(r"2")
        ).arrange(RIGHT)


        self.play(Write(ordre), run_time = 2)
        self.wait(3)
        self.play(Write(x), run_time = 2)
        self.wait(2)
        self.play(FadeOut(ordre))
        self.play(ReplacementTransform(x, double), run_time = 2)
        self.wait(2)
        self.play(ReplacementTransform(double, add_4), run_time = 2)
        self.wait(2)
        self.play(ReplacementTransform(add_4, divide_by_2), run_time = 2)
        self.wait(2)
        self.play(FadeOut(divide_by_2))
        self.wait(2)
        self.play(Write(result))
        self.wait(3)
        self.play(FadeOut(result))

        #Sigma Character Intervention

        sigma = MathTex("\\Sigma", color=BLUE).scale(5)

        # Créer les yeux
        left_eye = Circle(radius=0.2, color=WHITE, fill_opacity=1).shift(UP * 1.2 + LEFT * 0.5)
        right_eye = Circle(radius=0.2, color=WHITE, fill_opacity=1).shift(UP * 1.2 + RIGHT * 0.5)

        # Créer les pupilles
        left_pupil = Circle(radius=0.1, color=BLACK, fill_opacity=1).move_to(left_eye.get_right())
        right_pupil = Circle(radius=0.1, color=BLACK, fill_opacity=1).move_to(right_eye.get_right())

        # Grouper les yeux et les pupilles
        eyes = VGroup(left_eye, right_eye, left_pupil, right_pupil)

        # Grouper le Sigma et les yeux
        sigma_character = VGroup(sigma, eyes).to_edge(LEFT)

        self.play(Write(sigma_character))        
        
        question = Text("But how did you do that ?", font_size=20).next_to(sigma_character, UP+RIGHT)

        self.play(Write(question))
        self.wait(2)

        pi = MathTex("\\Pi", color=MAROON).scale(5)

        # Créer les yeux
        pi_left_eye = Circle(radius=0.2, color=WHITE, fill_opacity=1).shift(UP * 1.2 + LEFT * 0.5)
        pi_right_eye = Circle(radius=0.2, color=WHITE, fill_opacity=1).shift(UP * 1.2 + RIGHT * 0.5)

        # Créer les pupilles
        pi_left_pupil = Circle(radius=0.1, color=BLACK, fill_opacity=1).move_to(pi_left_eye.get_right())
        pi_right_pupil = Circle(radius=0.1, color=BLACK, fill_opacity=1).move_to(pi_right_eye.get_right())

        # Grouper les yeux et les pupilles
        eyes = VGroup(pi_left_eye, pi_right_eye, pi_left_pupil, pi_right_pupil)

        # Grouper le Sigma et les yeux
        pi_character = VGroup(pi, eyes).move_to(ORIGIN)

        mirror_pi = pi_character.copy().scale([-1,1,1]).to_edge(RIGHT)

        self.play(Write(mirror_pi))

        answer = Text("That's what we are going to see right now !", font_size=20).next_to(mirror_pi, UP+LEFT)

        self.play(Write(answer))
        self.wait(2)
        self.play(FadeOut(sigma_character, question, answer, mirror_pi))

        
        functions = Text("Functions", font_size=20, color=BLUE)

        self.play(FadeIn(functions))
        self.wait(2)
        self.play(functions.animate.scale(2))
        self.play(FadeOut(functions))

        #Functions 

        functions_title = Title("Functions")

        self.play(Write(functions_title))
        self.wait(2)

        #Function Explanation

        coffee_machine = Text("Coffee Machine", font_size=20).shift(2*UP)
        
        beans = Text("Beans", font_size=20, color=DARK_BROWN).shift(2*LEFT)
        coffee = Text("Coffee", font_size=20, color=DARK_BROWN).shift(4*RIGHT)
        
        surround_rect = SurroundingRectangle(beans, color=YELLOW)

        
        square = Square(side_length=2, color=BLUE)

        self.play(Create(square))
        self.play(Write(coffee_machine))
        self.wait(2)
        self.play(Write(beans))
        self.wait(2)
        self.play(Create(surround_rect))
        self.wait(3)
        self.play(FadeOut(surround_rect))
        self.wait(2)
        self.play(beans.animate.move_to(square.get_center()))
        self.wait(2)
        self.play(beans.animate.shift(4*RIGHT))
        self.play(ReplacementTransform(beans, coffee))
        self.wait(2)
        self.play(FadeOut(coffee_machine, square, coffee))

        input = Text("Input :", font_size=20, color=BLUE)
        output = Text("Output :", font_size=20, color=GREEN).next_to(input, DOWN)

        beans_input = Text("Beans", font_size=20, color=DARK_BROWN).next_to(input, RIGHT)
        coffee_output = Text("Coffee", font_size=20, color=DARK_BROWN).next_to(output, RIGHT)
        
        self.play(Write(input))
        self.wait(2)
        self.play(Write(output))
        self.wait(2)
        self.play(Write(beans_input))
        self.wait(2)
        self.play(Write(coffee_output))
        self.wait(2)
        self.play(FadeOut(input, output, beans_input, coffee_output))


        # Function Definition 

        
        function_def = Text("A function is a process that takes an input (number) and produces an output (result)", font_size=20).shift(2*UP)

        self.play(Write(function_def))
        self.wait(3)

        # Mathematical notation
        math_notation = MathTex(r"Function", ":", "X" r"\rightarrow Y", color=BLUE)
        coffee_example = MathTex(r"Coffee = Beans \rightarrow Espresso", color=GREEN).next_to(math_notation, DOWN)

        self.play(Write(math_notation))
        self.wait(2)
        self.play(Write(coffee_example))
        self.wait(2)
        self.play(FadeOut(math_notation, coffee_example, function_def))
        
        # Function Notation
        
        notation_example = MathTex(r"f(x)", "=", "2x", "+", "1").shift(UP)
        
        notation_example[0].set_color(BLUE)
        notation_example[2].set_color(GREEN)
        notation_example[4].set_color(RED)

        
        function_brace = Brace(notation_example[0], direction=DOWN, color=WHITE)
        rule_brace = Brace(notation_example[2:4], direction=DOWN, color=WHITE)

        name = Text("Name", font_size=20, color=BLUE).next_to(function_brace, DOWN)
        rule = Text("Rule", font_size=20, color=GREEN).next_to(rule_brace, DOWN)

        f_of_x = Text("f of x is equal to...", font_size=20).shift(DOWN)

        self.play(Write(notation_example))
        self.wait(2)
        self.play(Create(function_brace))
        self.play(Write(name))
        self.wait(2)
        self.play(Create(rule_brace))
        self.wait(2)
        self.play(Write(rule))
        self.wait(2)
        self.play(Write(f_of_x))
        self.play(FadeOut(notation_example, function_brace, rule_brace, name, rule, f_of_x))



        # Function Notation
        
        notation_example = MathTex(r"g(x)", "=", "2", "+", "x").shift(UP)
        
        notation_example[0].set_color(BLUE)
        notation_example[2].set_color(GREEN)
        notation_example[4].set_color(RED)

        
        function_brace = Brace(notation_example[0], direction=DOWN, color=WHITE)
        rule_brace = Brace(notation_example[2:4], direction=DOWN, color=WHITE)

        name = Text("Name", font_size=20, color=BLUE).next_to(function_brace, DOWN)
        rule = Text("Rule", font_size=20, color=GREEN).next_to(rule_brace, DOWN)

        self.play(Write(notation_example))
        self.wait(2)
        self.play(Create(function_brace))
        self.play(Write(name))
        self.wait(2)
        self.play(Create(rule_brace))
        self.wait(2)
        self.play(Write(rule))
        self.wait(2)
        self.play(FadeOut(notation_example, function_brace, rule_brace, name, rule))


        function_name = MathTex(r"f", r"(x)")
        function_name[0].set_color(BLUE)
        function_name[1].set_color(GREEN)

        reason = Text("You must always put the parenthesis with the used variable after the letter.", font_size=20).shift(2*DOWN)

        self.play(Write(function_name))
        self.wait(2)
        self.play(function_name[0].animate.set_color(BLUE))
        self.wait(2)
        self.play(function_name[1].animate.set_color(GREEN))
        self.wait(2)
        self.play(Write(reason))
        self.play(FadeOut(function_name, reason))
    
        
        question = Text("How do functions work ?", font_size=20).next_to(sigma_character, UP+RIGHT)
        
        self.play(Create(sigma_character))
        self.wait(2)
        self.play(Write(question))
        self.wait(2)
        self.play(FadeOut(question, sigma_character))



        #How Functions Work

        # Create input-output visualization
        input_box = Square(side_length=1, color=BLUE).shift(LEFT*3)
        output_box = Square(side_length=1, color=GREEN).shift(RIGHT*3)
        arrow = Arrow(input_box.get_right(), output_box.get_left(), color=YELLOW)

        # Function machine
        machine = Rectangle(height=2, width=3, color=WHITE).shift(UP)
        function_text = MathTex("f(x) = 2x + 1").scale(0.7).move_to(machine)

        self.play(Create(machine))
        self.wait(2)
        self.play(Write(function_text))
        self.wait(2)
        self.play(Create(arrow))
        self.wait(2)
        self.play(Create(input_box))
        self.play(Create(output_box))
        self.play(FadeOut(input_box, output_box, arrow, machine))

        suppose = VGroup(Text("Suppose", font_size=20), MathTex("x = 2", color=BLUE)).arrange(RIGHT, buff=0.5).shift(UP)
        function_text1 = MathTex("f(x) = 2(3) + 1").scale(0.7)
        function_text2 = MathTex(r"f(x) = 2 \times 3 + 1").scale(0.7)
        function_text_text3 = MathTex("f(x) = 6 + 1").scale(0.7)
        function_text4 = MathTex("f(x) = 7").scale(0.7)

        self.play(function_text.animate.move_to(ORIGIN))
        self.play(Write(suppose))
        self.wait(2)
        self.play(function_text.animate.scale(1.5))
        self.wait(2)
        self.play(ReplacementTransform(function_text, function_text1))
        self.wait(2)
        self.play(ReplacementTransform(function_text1, function_text2))
        self.wait(2)
        self.play(ReplacementTransform(function_text2, function_text))
        self.wait(2)
        self.play(ReplacementTransform(function_text, function_text2))
        self.wait(2)
        self.play(ReplacementTransform(function_text2, function_text_text3))
        self.wait(2)
        self.play(ReplacementTransform(function_text_text3, function_text4))
        self.wait(2)
        self.play(FadeOut(suppose, function_text4))

        result_text = VGroup(Text("We often call the result/output of the function", font_size=20), MathTex("y", color=GREEN)).arrange(RIGHT, buff=0.5).shift(UP)   
        result = MathTex("y", "=", "7")
        f_equal_y = MathTex(r"f(x)", "=", "y").next_to(result, DOWN)

        result[0].set_color(GREEN)
        f_equal_y[0].set_color(BLUE)
        f_equal_y[2].set_color(GREEN)

        self.play(Write(result_text))
        self.wait(2)
        self.play(Write(result))
        self.wait(2)
        self.play(Write(f_equal_y))
        self.wait(2)
        self.play(FadeOut(result_text, result, f_equal_y))
    
        #Image and Antecedent


        image_definition = MarkupText(f'An <span fgcolor="{BLUE}">image</span> is the output of a function.', font_size=20).shift(2*UP)
        antecedent = MarkupText(f'The <span fgcolor="{GREEN}">antecedent</span> is the input of a function.', font_size=20).next_to(image_definition, DOWN)
        
        x = MathTex("x = 2", color=BLUE).shift(2*UP)

        function_text1 = MathTex("f(x) = 2(2) + 1")
        function_text2 = MathTex(r"f(x) = 2 \times 2 + 1")
        function_text_text3 = MathTex("f(x) = 4 + 1")
        function_text4 = MathTex("f(x)", "=", "5")

        antecedent_to_image = MathTex("2", r"\rightarrow", "5").shift(2*UP)
        antecedent_to_image1 = VGroup(MathTex("2"), Text("is the antecedent of", font_size=20),  MathTex("5", color=GREEN)).arrange(RIGHT, buff=0.5).shift(UP)
        image = VGroup(MathTex("5"), Text("is the image of", font_size=20), MathTex("2", color=GREEN)).arrange(RIGHT, buff=0.5).next_to(antecedent_to_image1, DOWN)

        self.play(Write(image_definition))
        self.wait(2)
        self.play(Write(antecedent))
        self.wait(2)
        self.play(FadeOut(image_definition, antecedent))


        self.play(FadeIn(function_text))
        self.play(Write(x))
        self.wait(2)
        self.play(ReplacementTransform(function_text, function_text1))
        self.wait(2)
        self.play(ReplacementTransform(function_text1, function_text2))
        self.wait(2)
        self.play(ReplacementTransform(function_text2, function_text1))
        self.wait(2)
        self.play(ReplacementTransform(function_text1, function_text_text3))
        self.wait(2)
        self.play(ReplacementTransform(function_text_text3, function_text4))
        self.wait(2)

        self.play(function_text4[2].animate.set_color(GREEN))
        self.wait(2)

        self.play(FadeOut(function_text4, x))
        self.play(Write(antecedent_to_image))
        self.play(Write(antecedent_to_image1))
        self.wait(2)
        self.play(Write(image))
        self.wait(2)

        self.play(FadeOut(antecedent_to_image, antecedent_to_image1, image, functions_title))
        
        

        #Domain and Range

        domain_title = Title("Domain and Range")
        self.play(Write(domain_title))
        self.wait(2)

        # Function example
        function = MathTex("f(x) = 2x + 1", color=BLUE).shift(UP)
        self.play(Write(function))
        self.wait(2)

        # Domain explanation
        domain_text = Text("Domain: All possible input values (x)", font_size=20, color=GREEN).shift(UP * 0.5)
        domain_math = MathTex(r"\mathbb{R}", color=GREEN).next_to(domain_text, RIGHT)
        
        self.play(Write(domain_text))
        self.play(Write(domain_math))
        self.wait(2)

        # Range explanation
        range_text = Text("Range: All possible output values (y)", font_size=20, color=RED).next_to(domain_text, DOWN)
        range_math = MathTex(r"\mathbb{R}", color=RED).next_to(range_text, RIGHT)
        
        self.play(Write(range_text))
        self.wait(2)
        self.play(Write(range_math))
        self.wait(2)

        domain_ellipse = Ellipse(width=2, height=4, color=GREEN).to_edge(LEFT)
        range_ellipse = Ellipse(width=2, height=4, color=RED).to_edge(RIGHT)
        domain = Text("Domain", font_size=20, color=GREEN).next_to(domain_ellipse, DOWN)
        range = Text("Range", font_size=20, color=GREEN).next_to(range_ellipse, DOWN)

        arrow_domain = Arrow(domain_ellipse.get_center(), range_ellipse.get_center(), color=YELLOW)

        zero = MathTex(r"0").next_to(domain_ellipse.get_center(), DOWN)
        five = MathTex(r"5").next_to(domain_ellipse.get_center(), UP)
        minus_six = MathTex(r"-6").next_to(domain_ellipse.get_center(), LEFT)

        zero1 = MathTex(r"0").next_to(range_ellipse.get_center(), DOWN)
        ten = MathTex(r"10").next_to(range_ellipse.get_center(), UP)
        minus_twelve = MathTex(r"-12").next_to(range_ellipse.get_center(), LEFT)

        
        self.play(FadeOut(domain_text, domain_math, range_text, range_math, function))
        self.play(Create(domain_ellipse))
        self.wait(2)
        self.play(Create(arrow_domain))
        self.wait(2)
        self.play(Write(domain_ellipse))
        self.wait(2)
        self.play(Write(domain))
        self.wait(2)
        self.play(Write(range_ellipse))
        self.wait(2)
        self.play(Write(range))
        self.wait(2)
        self.play(Write(zero))
        self.wait(2)
        self.play(Write(five))
        self.wait(2)
        self.play(Write(minus_six))
        self.wait(2)
        self.play(Write(zero1))
        self.wait(2)
        self.play(Write(ten))
        self.wait(2)
        self.play(Write(minus_twelve))
        self.wait(2)
        self.play(FadeOut(domain_ellipse, arrow_domain, domain, range_ellipse, range, zero, five, minus_six, zero1, ten, minus_twelve))

        reciprocal = MathTex(r"f(x) = \frac{1}{x}")
        div0 = MathTex(r"f(x) = \frac{1}{0}")
        restriction = Text("x cannot be 0", font_size=20, color=RED).next_to(reciprocal, DOWN)
        restriction1 = Text("The output cannot also be 0", font_size=20, color=RED).next_to(restriction, DOWN)
        

        square_root = MathTex(r"f(x) = \sqrt{x}")
        square_root_neg = MathTex(r"\sqrt{-x}")
        restriction2 = Text("x cannot be negative", font_size=20, color=RED).next_to(square_root, DOWN)
        restriction3 = Text("The output cannot be negative", font_size=20, color=RED).next_to(restriction2, DOWN)

        four = MathTex(r"4").next_to(domain_ellipse.get_center(), DOWN)
        sixteen = MathTex(r"16").next_to(range_ellipse.get_center(), UP)

        five = MathTex(r"5").next_to(domain_ellipse.get_center(), LEFT)
        twenty_five = MathTex(r"25").next_to(range_ellipse.get_center(), RIGHT)
        
        self.play(Write(reciprocal))
        self.wait(2)
        self.play(Write(restriction))
        self.wait(2)
        self.play(ReplacementTransform(reciprocal, div0))
        self.wait(2)
        self.play(Write(restriction))
        self.wait(2)
        self.play(ReplacementTransform(reciprocal, div0))
        self.wait(2)
        self.play(Write(restriction1))
        self.wait(2)
        self.play(ReplacementTransform(div0, reciprocal))
        self.wait(2)
        self.play(FadeOut(restriction, restriction1, reciprocal))
        self.play(div0.animate.shift(UP))


        self.play(Create(domain_ellipse))
        self.wait(2)
        self.play(Create(arrow_domain))
        self.wait(2)
        self.play(Create(range_ellipse))
        self.wait(2)
        self.play(Create(domain))
        self.wait(2)
        self.play(Create(range))
        self.wait(2)
        self.play(Write(five))
        self.wait(2)
        self.play(Write(minus_six))
        self.wait(2)
        self.play(Write(ten))
        self.play(Write(minus_twelve))
        self.wait(2)
        self.play(FadeOut(domain_ellipse, arrow_domain, range_ellipse, domain, range, five, minus_six, ten, minus_twelve, div0))
        
        self.play(Write(square_root))
        self.wait(2)
        self.play(Write(restriction2))
        self.wait(2)
        self.play(Write(restriction3))
        self.wait(2)
        self.play(ReplacementTransform(square_root, square_root_neg))

        self.play(FadeOut(restriction2, restriction3))
        self.play(square_root_neg.animate.shift(UP))

        self.play(Create(domain_ellipse))
        self.wait(2)
        self.play(Create(arrow_domain))
        self.wait(2)
        self.play(Create(range_ellipse))
        self.wait(2)
        self.play(Create(domain))
        self.wait(2)
        self.play(Create(range))
        self.wait(2)
        self.play(Write(four))
        self.wait(2)
        self.play(Write(sixteen))
        self.wait(2)
        self.play(Write(five))
        self.wait(2)
        self.play(Write(twenty_five))
        self.wait(2)
        self.play(FadeOut(domain_ellipse, arrow_domain, range_ellipse, domain, range, four, five, sixteen, twenty_five, square_root_neg))
        self.wait(4)
        

        #Exercice

        question = Text("What is the domain and range of the function below?", font_size=20, color=BLUE).shift(2*UP)
        function = MathTex(r"\frac{1}{5 - x}")
        domain =  MathTex(r"\text{Domain : }x \in \mathbb{R} \backslash \{5\}").shift(DOWN)
        range = MathTex(r"\text{Range : }y \in \mathbb{R} \backslash \{0\}").next_to(domain, DOWN)

        self.play(Write(question))
        self.wait(2)
        self.play(Write(function))
        self.wait(5)
        self.play(Write(domain))
        self.wait(3)
        self.play(Write(range))
        self.wait(5)
        self.play(FadeOut(question, function, domain, range))

  
        #Tables of Values
        
        function = MathTex("f(x) = x^2", color=BLUE)
        input0 = MathTex(r"f(x) = 0^2 = 0")
        input1 = MathTex(r"f(x) = 1^2 = 1")
        input2 = MathTex(r"f(x) = 2^2 = 4")
        input3 = MathTex(r"f(x) = 3^2 = 9")
        input4 = MathTex(r"f(x) = 4^2 = 16")
        input5 = MathTex(r"f(x) = 5^2 = 25")


        table = Table(
            [["0", "0"],
            ["1", "1"],
            ["2", "4"],
            ["3", "9"],
            ["4", "16"],
            ["5", "25"]],

            col_labels=[Text("Input", font_size=20), Text("Output", font_size=20)],
            include_outer_lines=True,        
        ).scale(0.5).to_edge(RIGHT)

        self.play(Write(function))
        self.wait(2)
        self.play(function.animate.to_edge(LEFT))
        self.play(Write(table))
        self.wait(2)
        self.play(ReplacementTransform(function, input0))
        self.wait(2)
        self.play(table.get_entries((2, 2)).animate.set_color(BLUE))
        self.wait(2)
        self.play(ReplacementTransform(input0, input1))
        self.wait(2)
        self.play(table.get_entries((3, 2)).animate.set_color(BLUE))
        self.wait(2)
        self.play(ReplacementTransform(input1, input2))
        self.wait(2)
        self.play(table.get_entries((4, 2)).animate.set_color(BLUE))
        self.wait(2)
        self.play(ReplacementTransform(input2, input3))
        self.wait(2)
        self.play(table.get_entries((5, 2)).animate.set_color(BLUE))
        self.wait(2)
        self.play(ReplacementTransform(input3, input4))
        self.wait(2)
        self.play(table.get_entries((6, 2)).animate.set_color(BLUE))
        self.wait(2)
        self.play(ReplacementTransform(input4, input5))
        self.wait(2)
        self.play(table.get_entries((7, 2)).animate.set_color(BLUE))
        self.wait(2)
        self.play(FadeOut(input5, table, domain_title))


        #Graphs


        graphs_title = Title("Function Graphs")
        self.play(Write(graphs_title))
        self.wait(2)
        self.play(FadeOut(graphs_title))

        frame_width = config.frame_width
        frame_height = config.frame_height

        # Calculer le ratio d'aspect
        aspect_ratio = frame_width / frame_height

        # Définir les plages x et y en fonction du ratio d'aspect
        y_range = [-5, 10, 1]
        x_range = [y_range[0] * aspect_ratio, y_range[1] * aspect_ratio, 1]

        # Créer le plan cartésien avec des axes bleus
        plane = NumberPlane(
            x_range=x_range,
            y_range=y_range,
            x_length=frame_width,
            y_length=frame_height,
            background_line_style={
                "stroke_color": LIGHT_GREY,
                "stroke_width": 2,
                "stroke_opacity": 0.5
            },
            axis_config={
                "color": BLUE,  # Couleur des axes
                "include_numbers": True,
                "include_tip": True
            }
        )

        # Ajouter des étiquettes pour les axes
        x_label = plane.get_x_axis_label("x")
        y_label = plane.get_y_axis_label("f(x)")

        # Créer un groupe avec le plan et les étiquettes
        plane_group = VGroup(plane, x_label, y_label)

        function = MathTex(r"f(x) = 2x + 1", color=BLUE)
        input0 = MathTex(r"f(x) = 2(0) + 1 = 1").to_edge(UP+LEFT)
        input1 = MathTex(r"f(x) = 2(1) + 1 = 3").to_edge(UP+LEFT)
        input2 = MathTex(r"f(x) = 2(2) + 1 = 5").to_edge(UP+LEFT)
        input3 = MathTex(r"f(x) = 2(3) + 1 = 7").to_edge(UP+LEFT)
        input4 = MathTex(r"f(x) = 2(4) + 1 = 9").to_edge(UP+LEFT)
        input5 = MathTex(r"f(x) = 2(5) + 1 = 11").to_edge(UP+LEFT)

        table = Table(
            [["0", "1"],
            ["1", "3"],
            ["2", "5"],
            ["3", "7"],
            ["4", "9"],
            ["5", "11"]],

            col_labels=[Text("Input", font_size=20), Text("Output", font_size=20)],
            include_outer_lines=True,        
        ).scale(0.5).to_edge(RIGHT)

        graph = plane.plot(lambda x: 2*x + 1, color=BLUE)

        x_axis = plane.get_x_axis()
        y_axis = plane.get_y_axis()
        

        self.play(Write(function))
        self.wait(2)
        self.play(function.animate.to_edge(LEFT + UP))
        self.play(Write(table))
        
        self.wait(2)
        self.play(ReplacementTransform(function, input0))
        self.wait(2)
        self.play(table.get_entries((2, 2)).animate.set_color(BLUE))
        self.wait(2)
        self.play(ReplacementTransform(input0, input1))
        self.wait(2)
        self.play(table.get_entries((3, 2)).animate.set_color(BLUE))
        self.wait(2)
        self.play(ReplacementTransform(input1, input2))
        self.wait(2)
        self.play(table.get_entries((4, 2)).animate.set_color(BLUE))
        self.wait(2)
        self.play(ReplacementTransform(input2, input3))
        self.wait(2)
        self.play(table.get_entries((5, 2)).animate.set_color(BLUE))
        self.wait(2)
        self.play(ReplacementTransform(input3, input4))
        self.wait(2)
        self.play(table.get_entries((6, 2)).animate.set_color(BLUE))
        self.wait(2)
        self.play(ReplacementTransform(input4, input5))

        point1 = Dot(plane.c2p(1, 3), color=RED)
        point2 = Dot(plane.c2p(2, 5), color=RED)
        point3 = Dot(plane.c2p(3, 7), color=RED)
        point4 = Dot(plane.c2p(4, 9), color=RED)
        point5 = Dot(plane.c2p(5, 11), color=RED)


        
        plane_group.shift(UP)
    
        self.play(Create(plane_group), run_time=5)
        self.play(FadeOut(input5))
        self.wait(2)
        self.play(x_axis.animate.set_color(GREEN))
        self.wait(2)
        self.play(y_axis.animate.set_color(RED))
        self.wait(2)
        self.play(Create(point1))
        self.wait(2)
        self.play(Create(point2))
        self.wait(2)
        self.play(Create(point3))
        self.wait(2)
        self.play(Create(point4))
        self.wait(2)
        self.play(Create(point5))
        self.wait(3)
        self.play(Create(graph))
        self.wait(3)
        self.play(FadeOut(plane_group, graph, table, point1, point2, point3, point4, point5))

        x_representation = Text("x represents all possible inputs.", font_size=20) 
        
        self.play(Write(x_representation))
        self.wait(3)
        self.play(FadeOut(x_representation))

        

        #Polynomials 

        

        #Types of Functions 

                        # Different Types of Functions
        types_title = Title("Types of Functions")
        self.play(Write(types_title))
        self.wait(2)
        
        # Create axes
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-5, 5],
            axis_config={"color": BLUE},
            tips=True
        )
        
        # Linear Function
        linear = axes.plot(lambda x: 2*x - 1, color=YELLOW)
        linear_label = MathTex("f(x) = 2x - 1", "\\text{ (Linear)}", color=YELLOW).to_corner(UL)
        
        self.play(Create(axes))
        self.play(Create(linear), Write(linear_label))
        self.wait(2)
        
        # Quadratic Function
        quadratic = axes.plot(lambda x: x**2, color=GREEN)
        quad_label = MathTex("f(x) = x^2", "\\text{ (Quadratic)}", color=GREEN).to_corner(UL)
        
        self.play(ReplacementTransform(linear, quadratic))
        self.play(ReplacementTransform(linear_label, quad_label))
        self.wait(2)
        
        # Exponential Function
        exponential = axes.plot(lambda x: np.exp(x), color=RED)
        exp_label = MathTex("f(x) = e^x", "\\text{ (Exponential)}", color=RED).to_corner(UL)
        
        self.play(ReplacementTransform(quadratic, exponential))
        self.play(ReplacementTransform(quad_label, exp_label))
        self.wait(2)
        
        # Logarithmic Function
        logarithmic = axes.plot(lambda x: np.log(x+6)-1, x_range=[-5,5], color=PURPLE)
        log_label = MathTex("f(x) = \\ln(x+6)-1", "\\text{ (Logarithmic)}", color=PURPLE).to_corner(UL)
        
        self.play(ReplacementTransform(exponential, logarithmic))
        self.play(ReplacementTransform(exp_label, log_label))
        self.wait(2)
        
        # Trigonometric Functions
        sine = axes.plot(lambda x: 2*np.sin(x), color=BLUE)
        sine_label = MathTex("f(x) = 2\\sin(x)", "\\text{ (Trigonometric)}", color=BLUE).to_corner(UL)
        
        self.play(ReplacementTransform(logarithmic, sine))
        self.play(ReplacementTransform(log_label, sine_label))
        self.wait(2)
        
        # Summary of Function Types
        function_types = VGroup(
            Text("• Linear: f(x) = mx + b", font_size=20, color=YELLOW),
            Text("• Quadratic: f(x) = ax² + bx + c", font_size=20, color=GREEN),
            Text("• Exponential: f(x) = a^(bx)", font_size=20, color=RED),
            Text("• Logarithmic: f(x) = log_a(x)", font_size=20, color=PURPLE),
            Text("• Trigonometric: sin(x), cos(x), tan(x)", font_size=20, color=BLUE)
        ).arrange(DOWN, buff=0.5).to_edge(RIGHT)
        
        self.play(Write(function_types))
        self.wait(3)
        
        # Clear scene
        self.play(FadeOut(
            axes, sine, sine_label,
            function_types, types_title
        ))


        #Polynomials
        types_title = Title("Types of Functions")
        self.play(Write(types_title))
        self.wait(2)
        
        # Create numberplane

        frame_width = config.frame_width
        frame_height = config.frame_height

        # Calculer le ratio d'aspect
        aspect_ratio = frame_width / frame_height

        # Définir les plages x et y en fonction du ratio d'aspect
        y_range = [-5, 5, 1]
        x_range = [y_range[0] * aspect_ratio, y_range[1] * aspect_ratio, 1]

        numberplane = NumberPlane(
            x_range=x_range,
            y_range=y_range,
            x_length=frame_width,
            y_length=frame_height,
            background_line_style={
                "stroke_color": LIGHT_GREY,
                "stroke_width": 2,
                "stroke_opacity": 0.5
            },
            axis_config={
                "color": BLUE,  # Couleur des axes
                "include_numbers": True,
                "include_tip": True
            }
        )

        
        # Linear Function
        linear = numberplane.plot(lambda x: 2*x - 1, color=YELLOW)
        linear_label = MathTex("f(x) = 2x - 1", "\\text{ (Linear)}", color=YELLOW).to_corner(UL)
        
        self.play(FadeOut(types_title))
        self.play(Create(numberplane))
        self.play(Create(linear), Write(linear_label))
        self.wait(2)
        
        # Quadratic Function
        quadratic = numberplane.plot(lambda x: x**2, color=GREEN)
        quad_label = MathTex("f(x) = x^2", "\\text{ (Quadratic)}", color=GREEN).to_corner(UL)
        
        self.play(ReplacementTransform(linear, quadratic))
        self.play(ReplacementTransform(linear_label, quad_label))
        self.wait(2)
        
        # Exponential Function
        exponential = numberplane.plot(lambda x: np.exp(x), color=RED)
        exp_label = MathTex("f(x) = e^x", "\\text{ (Exponential)}", color=RED).to_corner(UL)
        
        self.play(ReplacementTransform(quadratic, exponential))
        self.play(ReplacementTransform(quad_label, exp_label))
        self.wait(2)
        
        # Logarithmic Function
        logarithmic = numberplane.plot(lambda x: np.log(x+6)-1, x_range=[-5,5], color=PURPLE)
        log_label = MathTex("f(x) = \\ln(x+6)-1", "\\text{ (Logarithmic)}", color=PURPLE).to_corner(UL)
        
        self.play(ReplacementTransform(exponential, logarithmic))
        self.wait(1)
        self.play(ReplacementTransform(exp_label, log_label))
        self.wait(2)
        
        # Trigonometric Functions
        sine = numberplane.plot(lambda x: 2*np.sin(x), color=BLUE)
        sine_label = MathTex("f(x) = 2\\sin(x)", "\\text{ (Trigonometric)}", color=BLUE).to_corner(UL)
        
        self.play(ReplacementTransform(logarithmic, sine))
        self.play(ReplacementTransform(log_label, sine_label))
        self.wait(2)
        
        # Summary of Function Types
        function_types = VGroup(
            Text("• Linear: f(x) = mx + b", font_size=20, color=YELLOW),
            Text("• Quadratic: f(x) = ax² + bx + c", font_size=20, color=GREEN),
            Text("• Exponential: f(x) = a^(bx)", font_size=20, color=RED),
            Text("• Logarithmic: f(x) = log_a(x)", font_size=20, color=PURPLE),
            Text("• Trigonometric: sin(x), cos(x), tan(x)", font_size=20, color=BLUE)
        ).arrange(DOWN, buff=0.5).to_edge(RIGHT)
        
        self.play(FadeOut(sine, sine_label))
        self.play(Write(function_types))
        self.wait(3)
        
        # Clear scene
        self.play(FadeOut(
            numberplane,
            function_types, types_title
        ))


        #Polynomials
        polynomials_title = Title("Polynomials")
        self.play(Write(polynomials_title))
        self.wait(2)


        general_formula = MathTex(
            "P(x) = a_nx^n + a_{n-1}x^{n-1} + ... + a_1x + a_0",
            color=BLUE
        ).shift(UP)

        formula_explanation = VGroup(
            Text("where:", font_size=20),
            MathTex("n", "\\text{ is the degree of polynomial}"),
            MathTex("a_n, a_{n-1}, ..., a_1, a_0", "\\text{ are coefficients}"),
            MathTex("a_n \\neq 0")
        ).arrange(DOWN, buff=0.3).shift(DOWN)

        self.play(Write(general_formula))
        self.wait(2)
        self.play(Write(formula_explanation))
        self.wait(3)
        self.play(FadeOut(general_formula, formula_explanation))

        # Definition
        poly_def = Text("A polynomial is a function made up of variables and coefficients", font_size=20).shift(2*UP)
        self.play(Write(poly_def))
        self.wait(2)

        # Examples of polynomials
        poly_examples = VGroup(
            MathTex("f(x) = x^2 + 2x + 1", color=BLUE),
            MathTex("g(x) = 3x^3 - 4x + 2", color=GREEN),
            MathTex("h(x) = x^4 - 2x^2 + 4", color=RED)
        ).arrange(DOWN, buff=0.5)

        self.play(Write(poly_examples))
        self.wait(2)

        # Degree explanation
        degree_text = Text("The degree is the highest power of x", font_size=20).shift(2*DOWN)
        self.play(Write(degree_text))
        self.wait(2)

        # Highlight degrees
        for i, poly in enumerate(poly_examples):
            self.play(poly.animate.scale(1.2), run_time=0.5)
            self.play(poly.animate.scale(1/1.2), run_time=0.5)

        self.play(FadeOut(poly_examples, degree_text, poly_def, polynomials_title))    

        #Analysis
        analysis_title = Title("Function Analysis")
        self.play(Write(analysis_title))
        self.wait(2)

        # Create axes for demonstrations
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-5, 5],
            axis_config={"color": BLUE},
            tips=True
        )

        derivation = MathTex("\\frac{d}{dx}", color=YELLOW).to_corner(DL).shift(UP)
        integration = MathTex("\\int", color=YELLOW).to_corner(DR).shift(UP)
        
        self.play(FadeOut(analysis_title))
        self.play(Create(axes))

        # Example function
        function = axes.plot(lambda x: 0.5*x**3 - 2*x, color=YELLOW)
        function_label = MathTex("f(x) = 0.5x^3 - 2x", color=YELLOW).to_corner(UL)
        
        self.play(Create(function), Write(function_label))
        self.wait(2)

        # Show key points of analysis
        analysis_points = VGroup(
            Text("• Finding maximum/minimum points", font_size=20),
            Text("• Rate of change", font_size=20),
            Text("• Area under curves", font_size=20),
            Text("• Intersection points", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT)

        self.play(Write(analysis_points))
        self.wait(2)

        # Highlight maximum/minimum points
        

        # Show tangent line for rate of change
        tangent = axes.plot(lambda x: -2*x, x_range=[-1, 1], color=GREEN)
        tangent_label = Text("Slope = Rate of Change", font_size=20, color=GREEN).next_to(tangent, UP)
        
        self.play(Create(tangent), Write(tangent_label))
        self.wait(2)

        # Area visualization
        area = axes.get_area(function, x_range=[-1, 1], color=BLUE, opacity=0.3)
        area_label = Text("Area", font_size=20, color=BLUE).next_to(area, DOWN)
        
        self.play(Write(derivation), Write(integration))
        self.wait(2)
        
        self.play(Create(area), Write(area_label))
        self.wait(2)
        

        self.play(FadeOut(
            axes, function, function_label,
            tangent, tangent_label, area, area_label,
            analysis_points, derivation, integration
        ))


        #Thanks

        thanks = Text("Thank you for watching!", font_size=30, color=BLUE).shift(2*UP)

        self.play(Write(thanks))
        self.wait(3)
##########################