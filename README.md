# **MODULE: Programming and Scripting**
## **WEEKLY TASKS**
## **AUTHOR: Ante Dujic**

This README file contains explanation of the code written to solve the problems assigned in weekly tasks for Programming and Scripting Module.

## **WEEK 2**
### **bmi.py**
Write a program that calculates somebody’s Body Mass Index (BMI)
-	The inputs are the person's height in centimetres and weight in kilograms
-	The output is their weight divided by their height in metres squared

*CODE:*

``` python
height = float (input ("Enter height (cm):"))
weight = float (input ("Enter weight (kg): "))

BMI = round((weight/((height/100)**2)),2)

print ("BMI is:",BMI)     
```
*EXPLANATION:*

_Program asks the user to input height (cm) and weight (kg) as a float number. It then calculates BMI using formula BMI = kg/m2 (converting cm to m), rounds it using round() function  and prints it out._

*REFERENCES:*
-	https://www.diabetes.ca/managing-my-diabetes/tools---resources/body-mass-index-(bmi)-calculator
-	https://www.w3schools.com/python/ref_func_round.asp
-	https://stackoverflow.com/questions/20405610/bmi-calculator-in-python/20405792

![alt text](https://github.com/AnteDujic/pands-problem-sheet/blob/main/functionsPlot.png)

- *shape()* returns the shape of an array (dataset) - *shape[0]* gives the number of rows, and *shape[1]* the number of columns

<details>
<summary>OUTPUT</summary>
<br>

```
This data set consists of 150 samples, grouped by 5 different variables.

Dataset variables are:
Sepal Length (cm)
Sepal Width (cm)
Petal Length (cm)
Petal Width (cm)
Iris SpeciesThis is how you dropdown.
```

</details>

<p float="left">
  <img src="https://github.com/AnteDujic/pands-project2021/blob/main/speciesBar.png" width="60%" />
  <img src="https://github.com/AnteDujic/pands-project2021/blob/main/speciesPie.png" width="60%" /> 
</p>



![](https://github.com/AnteDujic/pands-project2021/blob/main/speciesBar.png | width = 100) ![](https://github.com/AnteDujic/pands-project2021/blob/main/speciesPie.png | width = 100)
