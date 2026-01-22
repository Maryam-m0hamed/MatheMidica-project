# MatheMedica Library

A Python library bridging **Mathematics** and **Medicine** through programming.  

MatheMedica consists of **40 custom-built functions** developed from scratch, without using any external libraries, divided into two main categories:

---

## 🔹 Mathematical Functions (20 functions)

Some examples include:  
- Printing Pascal’s Triangle (standard and inverted)  
- Generating the Fibonacci sequence  
- Computing statistical measures like Mean, Median, and Mode  

---

## 🔹 Medical Functions (20 functions)

Some examples include:  
- Calculating BMI (Body Mass Index)  
- Calculating BMR (Basal Metabolic Rate)  
- Tracking blood glucose levels  

---

## 🚀 Usage Example

```python
import mathemedica as mm

# ============================== Test 1 ==================================
weight = 70  # kg
height = 175  # cm
age = 25  # years
gender = "male"
activity_level = "moderate"

# Calculate BMR
bmr, bmr_rating = mm.check_BMR(weight, height, age, gender)

# Calculate daily carbohydrates
carbs = mm.calculate_carbohydrates(bmr, activity_level)

print("Test Case 1")
print(f"  Weight: {weight} kg, Height: {height} cm, Age: {age} years, Gender: {gender}")
print(f"  Activity Level: {activity_level}")
print(f"  BMR: {bmr:.2f}, Rating: {bmr_rating}")
print(f"  Daily Carbohydrates Needed: {carbs:.2f} grams \n")

# ============================== Test 2 ==================================
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
