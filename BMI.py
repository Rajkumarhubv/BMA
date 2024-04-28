
import streamlit as st

st.title('Body Mass Index(BMI)')
if(st.checkbox("Click me to know more..")):
	st.markdown("Body Mass Index (BMI) is a simple yet commonly used measure to assess an individual's body weight relative to their height. It is calculated by dividing a person's weight in kilograms by the square of their height in meters. BMI provides a quick and easy way to categorize individuals into different weight status categories, such as underweight, normal weight, overweight, and obese. While BMI is a useful tool for population-level assessments of weight status, it does not directly measure body fat and may not accurately reflect body composition for certain individuals, such as athletes or those with a high muscle mass. Despite its limitations, BMI remains a widely used screening tool in healthcare settings for assessing weight-related health risks.")

weight = st.number_input("Enter your weight (in kgs)")

status = st.radio('Select your height format: ',
				('cms', 'meters', 'feet'))

if(status == 'cms'):
	height = st.number_input('Centimeters')

	try:
		bmi = weight / ((height/100)**2)
	except:
		st.text("Enter some value of height")

elif(status == 'meters'):
	height = st.number_input('Meters')

	try:
		bmi = weight / (height ** 2)
	except:
		st.text("Enter some value of height")

else:
	height = st.number_input('Feet')

	try:
		bmi = weight / (((height/3.28))**2)
	except:
		st.text("Enter some value of height")

if(st.button('Calculate BMI')):

	st.text("Your BMI Index is {}.".format(bmi))

	if(bmi < 16):
		st.error("You are Extremely Underweight")
	elif(bmi >= 16 and bmi < 18.5):
		st.warning("You are Underweight")
	elif(bmi >= 18.5 and bmi < 25):
		st.success("Healthy")
	elif(bmi >= 25 and bmi < 30):
		st.warning("Overweight")
	elif(bmi >= 30):
		st.error("Extremely Overweight")
