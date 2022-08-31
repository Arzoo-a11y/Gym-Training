def fat_loss():
    print("stPlate thrusters (15 reps x 3 sets)")
    print("Mountain climbers (20 reps x 3 sets)")
    print("Box jumps (10 reps x 3 sets)")
    print("Lunges (10 reps x 3 sets)")
    print("Renegade rows (10 reps x 3 sets)")
    print("Press ups (15 reps x 3 sets)")
    print("Treadmill (10 mins x 3 sets)")
    print("Supermans (10 reps x 3 sets)")
    print("Crunches (10 reps x 3 sets)")
def stretch_and_relax():
    print("Quad stretchs (2 mins x 3 sets)")
    print("Hamstring stretchs (2 mins x 3 sets)")
    print("Chest and shoulder stretchs (2 mins x 2 sets)")
    print("Upper back stretchs (3 mins x 2 sets)")
    print("Biceps stretchs (2 mins x 2 sets)")
    print("Triceps stretchs (2 mins x 3 sets)")
    print("Hip flexors (2 mins x 3 sets)")
    print("Calf stretchs (2 mins x 3 sets)")
    print("Lower back stretchs (2 mins x 3 sets)")
def high_intensity_exercises():
    print("Jumping jacks (20 reps x 4 sets)")
    print("Sprints (20 reps x 3 sets)")
    print("Mountain climbers (20 reps x 4 sets)")
    print("Squat jumps (20 reps x 4 sets)")
    print("Lunges (20 reps x 3 sets)")
    print("Crunches (20 reps x 3 sets)")
    print("Treadmill (15 mins x 2 sets)")
    print("Side planks (15 reps x 3 sets)")
    print("Burpees (15 reps x 3 sets)")
def strong_legs():
    print("Back squats (10 reps x 5 sets)")
    print("Hip thrusts (12 reps x 3 sets)")
    print("Overhead presses (10 reps x 5 sets)")
    print("Rack pulls (10 reps x 5 sets)")
    print("Squats (10 reps x 4 sets)")
    print("Dumbbell lunges (10 reps x 3 sets)")
    print("Leg curls (15 reps x 3 sets)")
    print("Standing calf raises (20 reps x 2 sets)")
def strong_abs():
    print("Cross crunchs (12 reps x 3 sets)")
    print("Knee ups (15 reps x 5 sets)")
    print("Hip thrusts (15 reps x 3 sets)")
    print("Mountain climbers (15 reps x 3 sets)")
    print("Vertical hip thrusts (12 reps x 3 sets)")
    print("Bicycles (15 mins x 2 sets)")
    print("Front planks (15 mins x 3 sets)")
    print("Dragon flags (12 reps x 4 sets)")
    print("Reverse crunches (10 reps x 3 sets)")
def strong_shoulder_arms():
    print("Bench presses (10 reps x 5 sets)")
    print("Triceps dips (10 reps x 5 sets)")
    print("Incline dumbbell presses (12 reps x 3 sets)")
    print("dumbbell flyes (15 reps x 3 sets)")
    print("Triceps extensions (15 reps x 3 sets)")
    print("Pull ups (10 reps x 5 sets)")
    print("Treadmill (15 mins x 2 sets)")
    print("Bent over rows (10 reps x 5 sets)")
    print("Chin ups (10 reps x 3 sets)")
def male_less_18():
    print("High knees (20 reps x 3 sets)")
    print("Squats (10 reps x 3 sets)")
    print("Calf raises (10 reps x 3 sets)")
    print("Scissor jumps (12 reps x 3 sets)")
    print("Burpees (10 reps x 3 sets)")
    print("Treadmill (10 mins x 2 sets)")
def female_less_18():
    print("Squats (10 reps x 3 sets)")
    print("Crunches (10 reps x 2 sets)")
    print("Jumping jacks (10 reps x 3 sets)")
    print("Push ups (10 reps x 2 sets)")
    print("Burpees (10 reps x 3 sets)")
    print("Treadmill (10 mins x 2 sets)")
def male_above_18():
    print("Standing biceps curls (20 reps x 3 sets)")
    print("Seated incline curls (18 reps x 3 sets)")
    print("Seated dumbbell presses (12 reps x 3 sets)")
    print("Leg presses (15 reps x 3 sets)")
    print("Bench presses (10 reps x 4 sets)")
    print("Tricep kickbacks (15 reps x 3 sets)")
    print("Hip thrusts (12 reps x 3 sets)")
    print("Seated rows (10 reps x 4 sets)")
def female_above_18():
    print("Lateral raises (15 reps x 3 sets)")
    print("Reverse flyes (12 reps x 3 sets)")
    print("Hip thrusts (12 reps x 3 sets)")
    print("Incline dumbbell presses (15 reps x 3 sets)")
    print("Squats (10 reps x 4 sets)")
    print("Dumbbell lunges (10 reps x 3 sets)")
    print("Leg presses (12 reps x 3 sets)")
    print("Dumbbell presses (10 reps x 4 sets)")
name = input("please enter your name\n")
age=int(input("please enter your age\n"))
sex=input("please enter your biological sex (male/female)\n");
print("what do you get out of your training?\n")
print("1. Your goal is loosing fat\n")
print("2. Your goal is staying calm and relax\n")
print("3. Your goal is increasing your heart rate\n")
print("4. Your goal is having stronger legs\n")
print("5. Your goal is having stronger ABS\n")
print("6. Your goal is having strtonger shoulders and arms\n")
print("Choose a number between 1 to 6:\n")
choice= int(input())
print("How many days per week you can train:\n")
day=int(input())


print("Hello",name,"! Here is your training:")
print("-------------------------------------")
if(choice == 1):
    for i in range(day):
        print("Day ", i + 1)
        if (i % 2 == 0):
            print("Gym workout for fat loss")
            fat_loss()
        else:
            if(sex == "male"):
                if(age>=18):
                    print("Gym workout for a male at least 18 years old")
                    male_above_18()
                else:
                    print("Gym workout for a male younger than 18 years old")
                    male_less_18()
            else:
                if(sex == "female"):
                    if (age >= 18):
                        print("Gym workout for a female at least 18 years old")
                        female_above_18()
                    else:
                        print("Gym workout for a female younger than 18 years old")
                        female_less_18()





else:
    if(choice == 2):
        for i in range(day):
            print("Day ", i + 1)
            if (i % 2 == 0):
                print("Gym workout for stretch and relax")
                stretch_and_relax()
            else:
                if(sex == "male"):
                    if(age>=18):
                        print("Gym workout for a male at least 18 years old")
                        male_above_18()
                    else:
                        print("Gym workout for a male younger than 18 years old")
                        male_less_18()
                else:
                    if(sex == "female"):
                        if (age >= 18):
                            print("Gym workout for a female at least 18 years old")
                            female_above_18()
                        else:
                            print("Gym workout for a female younger than 18 years old")
                            female_less_18()

    if(choice == 3):
        for i in range(day):
            print("Day ", i + 1)
            if (i % 2 == 0):
                print("Gym workout for high-intensity exercises")
                high_intensity_exercises()
            else:
                if(sex == "male"):
                    if(age>=18):
                        print("Gym workout for a male at least 18 years old")
                        male_above_18()
                    else:
                        print("Gym workout for a male younger than 18 years old")
                        male_less_18()
                else:
                    if(sex == "female"):
                        if (age >= 18):
                            print("Gym workout for a female at least 18 years old")
                            female_above_18()
                        else:
                            print("Gym workout for a female younger than 18 years old")
                            female_less_18()

    if(choice == 4):
        for i in range(day):
            print("Day ", i + 1)
            if (i % 2 == 0):
                print("Gym workout for strong legs")
                strong_legs()
            else:
                if(sex == "male"):
                    if(age>=18):
                        print("Gym workout for a male at least 18 years old")
                        male_above_18()
                    else:
                        print("Gym workout for a male younger than 18 years old")
                        male_less_18()
                else:
                    if(sex == "female"):
                        if (age >= 18):
                            print("Gym workout for a female at least 18 years old")
                            female_above_18()
                        else:
                            print("Gym workout for a female younger than 18 years old")
                            female_less_18()

    if(choice == 5):
        for i in range(day):
            print("Day ", i + 1)
            if (i % 2 == 0):
                print("Gym workout for strong ABS")
                strong_abs()
            else:
                if(sex == "male"):
                    if(age>=18):
                        print("Gym workout for a male at least 18 years old")
                        male_above_18()
                    else:
                        print("Gym workout for a male younger than 18 years old")
                        male_less_18()
                else:
                    if(sex == "female"):
                        if (age >= 18):
                            print("Gym workout for a female at least 18 years old")
                            female_above_18()
                        else:
                            print("Gym workout for a female younger than 18 years old")
                            female_less_18()

    if(choice == 6):
        for i in range(day):
            print("Day ", i + 1)
            if (i % 2 == 0):
                print("Gym workout for strong shoulder and arms")
                strong_shoulder_arms()
            else:
                if(sex == "male"):
                    if(age>=18):
                        print("Gym workout for a male at least 18 years old")
                        male_above_18()
                    else:
                        print("Gym workout for a male younger than 18 years old")
                        male_less_18()
                else:
                    if(sex == "female"):
                        if (age >= 18):
                            print("Gym workout for a female at least 18 years old")
                            female_above_18()
                        else:
                            print("Gym workout for a female younger than 18 years old")
                            female_less_18()


