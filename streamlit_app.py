# -*- coding: utf-8 -*-
"""streamlit_app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RUE_6zK3njERKPe5XeVNo4WuEZzGDPqF
"""

import streamlit as st

st.title("Find the largest among the 3 numbers")
num1 = st.number_input("Enter the first number: ")
num2 = st.number_input("Enter the second number: ")
num3 = st.number_input("Enter the third number: ")

calculate = st.button("Find the largest number")

def largest_number(a,b,c):
  if a>b and a>c:
    return a
  elif b>a and b>c:
    return b
  else:
    return c

if calculate:
  largest_num = largest_number(num1,num2,num3)
  st.write("The largest number is: ",largest_num)