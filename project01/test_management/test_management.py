import math

def enter_user_name() -> None:
    user_name = input("Enter your name :")
    print(f"Hello, {user_name}.")

def calculate_cubic_meters_of_concrete_should_max_order() -> float:
    radius_hole = 0.175
    area_of_hole = math.pi * radius_hole ** 2
    volume_of_hole = area_of_hole * 0.8
    shoud_order_volume_concrete = 4 * volume_of_hole
    return shoud_order_volume_concrete
    


def questions() -> None:
    questions_options = {
        "PhysicsQ1"   : "Which is a physical quantity that has a magnitude but not direction?",
        "PhysicsQ2"   : "What results from multiplying or dividing vectors by scalars?",
        "PhysicsQ3"   : "Which is an example of a vector quantity?",
        "MathQ4"      : "What is area of the ellipse? Use 22/7 for pi. Where a = 4 and b = 14. Use formula pi * a * b ",
        "MathQ5"      :  """ Max is building a house. The first step is to drill holes and fill them with concrete. 
                             The holes are 35 cm wide and 80 cm deep, and Max drills four holes. 
                             How many cubic meters of concrete schould Max order? """,
        "PhysicsQ6"   : """ Newton's Second Law of Motion states that the force, F Newtwon's, acting on an object of mass m kg, moving 
                            with an acceleration of a m/s2 is geven by the formula: F = m * a  
                            What is the value of F when m = 50 and a = 9.8 ?    """,
        "GeographyQ7" : " Which is the tallest mountain in on Earth ?"
    }
    your_answer = input(f"Physics : {questions_options['PhysicsQ1']} : ")
    if your_answer == "Scalar" or "scalar":
        print("Awesome. Keep going!")
    your_answer = input(f"Physics : {questions_options['PhysicsQ2']} : ")
    if your_answer == "Vectors" or "vectors":
        print("Good. Keep going!")
    your_answer = input(f"Physics : {questions_options['PhysicsQ3']} : ")
    if your_answer == "Velocity" or "velocity":
        print("Very good. Keep going!")  
    your_answer = float(input(f"Math : {questions_options['MathQ4']} : ")) 
    if  your_answer == math.ceil(math.pi * 4 * 14):
        print("Awesome. Keep going!")
    your_answer = float(input(f"Math : {questions_options['MathQ5']} : "))
    cubic_meters_of_concrete_should_max_order = calculate_cubic_meters_of_concrete_should_max_order()
    if your_answer == round(cubic_meters_of_concrete_should_max_order, 3):
        print("Awesome. Keep going!")
    your_answer = float(input(f"Physics : {questions_options['PhysicsQ6']} : "))
    if your_answer == round(50 * 9.8):
        print("Awesome. Keep going!")
    your_answer = input(f"Geography : {questions_options['GeographyQ7']} : ")
    if your_answer == "Mount Everest":
        print("Good! Keep going!")


def keep_going() -> None:
    go = input("Type here: ")
    if go == "Go" :
        print("Right. Keep going!")
        questions()
   

    
