import pandas as pd

data = {
    'Student_ID': ['S001','S002','S003','S004','S005','S006','S007','S008','S009','S010','S011','S012','S013','S014','S015','S016','S017','S018','S019','S020','S021','S022','S023','S024','S025','S026','S027','S028','S029','S030'],
    
    'Name': ['Student_1','Student_2','Student_3','Student_4','Student_5','Student_6','Student_7','Student_8','Student_9','Student_10','Student_11','Student_12','Student_13','Student_14','Student_15','Student_16','Student_17','Student_18','Student_19','Student_20','Student_21','Student_22','Student_23','Student_24','Student_25','Student_26','Student_27','Student_28','Student_29','Student_30'],
    
    'Age': [21,22,20,22,22,19,20,20,20,22,21,20,None,22,19,21,None,None,19,21,22,18,21,19,None,22,21,18,18,20],
    
    'Gender': ['Male','Male','Female','Female','Female','Female','Female','Male','Female','Female','Male','Female','Male','Female','Male','Female','Female','Male','Male','Male','Male','Male','Male','Male','Male','Female','Female','Male','Female','Female'],
    
    'Marks_Math': [99,58,75,51,69,77,96,56,93,57,96,84,63,66,85,99,89,53,51,55,91,53,78,67,75,93,83,59,85,63],
    
    'Marks_Science': [80,97,64,57,63,72,89,70,65,94,67,96,73,75,74,94,90,78,64,94,50,74,56,58,73,50,93,57,73,60],
    
    'Marks_English': [None,66,57,84,84,82,54,91,88,90,77,56,58,57,61,83,82,97,72,73,86,84,93,89,71,76,84,50,84,86],
    
    'Attendance_Percentage': [73,62,60,64,85,73,98,86,68,74,74,85,72,91,98,91,63,89,96,82,98,74,88,95,72,91,66,81,87,61],
    
    'City': ['Noida',None,'Delhi',None,'Ghaziabad','Ghaziabad','Ghaziabad','Ghaziabad','Ghaziabad','Gurgaon','Noida','Ghaziabad','Delhi','Delhi','Delhi','Delhi','Gurgaon','Delhi','Ghaziabad',None,'Delhi','Gurgaon','Gurgaon','Delhi',None,'Delhi','Gurgaon','Noida','Ghaziabad','Gurgaon'],
    
    'Placement_Status': ['Not Placed','Not Placed','Not Placed','Not Placed','Placed','Not Placed','Placed','Not Placed','Placed','Not Placed','Not Placed','Not Placed','Not Placed','Placed','Not Placed','Placed','Placed','Placed','Placed','Not Placed','Placed','Placed','Placed','Not Placed','Not Placed','Not Placed','Not Placed','Placed','Placed','Not Placed']
}




df = pd.DataFrame(data)
print(df.head())

# print(df.isnull().sum())

# df['Age'].fillna(df['Age'].mean(), inplace=True)
# df['Marks_English'].fillna(df['Marks_English'].mean(), inplace=True)

#for catogerial data 
df['City'].fillna(df['City'].mode()[0], inplace=True)
print(df.isnull().sum())

df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

df['Placement_Status'] = df['Placement_Status'].map({'Not Placed': 0, 'Placed': 1})

print(df.isnull().sum())