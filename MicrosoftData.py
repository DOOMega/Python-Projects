import numpy as np
import pandas as pd

#df_students = pd.read_csv('grades.csv', delimiter=",", header="infer")

#df_students = df_students.dropna(axis=0, how='any')

#print(df_students)

#mean_study = df_students["StudyHours"].mean()
#mean_grade = df_students.Grade.mean()

#print(df_students[df_students["StudyHours"] > mean_study].Grade.mean())
data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]
grades = np.array(data)
study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]
student_data = np.array([study_hours, grades])

avg_studyhours = student_data[0].mean()
avg_grades = student_data[1].mean()
print("avg_studyhours: {:.2f} \navg_grades: {:.2f}".format(avg_studyhours, avg_grades))