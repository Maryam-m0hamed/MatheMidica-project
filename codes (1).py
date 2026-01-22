import mathemedica as mm

# ============================== test 1==================================

weight = 70  # kg
height = 175  # cm
age = 25  # years
gender = "male"
activity_level = "moderate"

# Calculate BMR
bmr, bmr_rating = mm.check_BMR(weight, height, age, gender)

# Calculate carbohydrates
carbs = mm.calculate_carbohydrates(bmr, activity_level)

print("Test Case 1")
print(f"  Weight: {weight} kg, Height: {height} cm, Age: {age} years, Gender: {gender}")
print(f"  Activity Level: {activity_level}")
print(f"  BMR: {bmr:.2f}, Rating: {bmr_rating}")
print(f"  Daily Carbohydrates Needed: {carbs:.2f} grams \n")


# ============================== test 2==================================

matrix1 = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12]]
matrix2 = [[1, 2],
           [3, 4],
           [5, 6],
           [7, 8]]

result_matrix = mm.times_matrices(matrix1, matrix2)

print("Test Case 2")
for row in result_matrix:
  print(f"  {row}")