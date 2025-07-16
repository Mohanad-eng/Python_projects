cgpa = []
hours = []
while True :
 try :
  grade = input("enter your grade (to stop press x) :")
  if grade == 'x' :
     break
  h = int(input("no of hours :"))
  if grade == "A+" :
      cgpa.append(4.00*h)
      hours.append(h)
  
  elif grade == "A":
     cgpa.append(4.00*h)
     hours.append(h)
  
  elif grade == "A-":
     cgpa.append(3.70*h)
     hours.append(h)
   
  elif grade == "B+":
     cgpa.append(3.30*h)
     hours.append(h)
   
  elif grade == "B":
     cgpa.append(3.00*h)
     hours.append(h)

  elif  grade == "B-":
     cgpa.append(2.70*h)
     hours.append(h)

  elif grade == "C+":
     cgpa.append(2.30*h)
     hours.append(h)

  elif grade == "C":
     cgpa.append(2.00*h)
     hours.append(h)
  elif grade == "C-":
     cgpa.append(1.70*h)
     hours.append(h)
  elif  grade == "D+":
     cgpa.append(1.30*h)
     hours.append(h)
  elif grade == "D":
     cgpa.append(1.00*h)
     hours.append(h)
  elif grade == "F":
     cgpa.append(0.00*h)
     hours.append(h)
 except Exception as e :
    print(f"error is {e}")


x = sum(cgpa)/sum(hours)
print(f"cgpa :{x}")
if x >= 3.00:
   state = "overload"
elif x >= 2.50 and x <= 3.00 :
   state = "fullload"
else : 
   state = "haifload"
print(f"{state}")
