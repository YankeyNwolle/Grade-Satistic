
# un programme permettant d'imprimer des statistiques de notes pour un cours universitaire

#   demande à l'utilisateur points examen et nombre d'exercices effectués
def users():
    new_list = []
    while True:
        user_input = input("Exam points and exercises completed: ")
        if not user_input:
            break
        try:
            points, nb_exercise = map(int, user_input.split())
            #si l'utilisateur n'entre pas deux (2) valeurs
        except ValueError:
            print("Merci d'entrer deux valeurs séparées par un espace!")
            continue
        if (points>=0 and points <=20) and (nb_exercise>=0 and nb_exercise<=100):
            new_list.append((points, nb_exercise))
        else:
            print("Please enter a valid integers!")
    return new_list

def exercise_point(nb_exercise, total_exercise=100):
    pourcentage = (nb_exercise / total_exercise) * 10
    exercices_point = int(pourcentage)
    return exercices_point

def grade(points, nb_exercise):
    mark = exercise_point(nb_exercise) + points
    if mark>= 0 and mark <=14:
        return 0
    elif mark>= 15 and mark <=17:
        return 1
    elif mark>= 18 and mark <=20:
        return 2
    elif mark>= 21 and mark <=23:
        return 3
    elif mark>= 24 and mark <=27:
        return 4
    elif mark>= 28 and mark <=30:
        return 5

def calculate_statistics(results):
    # Calcule de la somme des points
    total_points = sum(points for points, _ in results)
    
    # Calcule de la moyenne des points
    average_points = total_points / len(results)

    # Calcule des notes
    grades = [grade(points, nb_exercise) for points, nb_exercise in results]

    # Calcule du pourcentage de réussite
    pass_percentage = sum(1 for grade in grades if grade >= 1) / len(grades) * 100
    grade_distribution = {i: grades.count(i) for i in set(grades)}
    return average_points, pass_percentage, grade_distribution

# Appel de la fonction
results = users()

average_points, pass_percentage, grade_distribution = calculate_statistics(results)
print("Statistic")
print(f"Points average: {average_points:.1f}")
print(f"Pass percentage: {pass_percentage:.1f}")
print("Grade distribution:")
for grade in range(min(grade_distribution.keys()), max(grade_distribution.keys()) + 1):
    count = grade_distribution.get(grade, 0)
    if count > 0:
        print(f"{grade}: {'*' * count}")
    else:
        print(f"{grade}:")


