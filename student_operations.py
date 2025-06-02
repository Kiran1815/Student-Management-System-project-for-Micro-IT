import pandas as pd
import os

FILENAME = "students.csv"

def load_data():
    if os.path.exists(FILENAME):
        df = pd.read_csv(FILENAME)
        return df
    else:
        return pd.DataFrame(columns=["ID", "Name", "Age", "Course", "Grade", "Attendance"])

def save_data(df):
    df.to_csv(FILENAME, index=False)

def add_student(student):
    df = load_data()
    df = pd.concat([df, pd.DataFrame([student])], ignore_index=True)
    save_data(df)

def get_all_students():
    df = load_data()
    return df

def update_student(index, updated_student):
    df = load_data()
    df.loc[index] = updated_student
    save_data(df)

def delete_student(index):
    df = load_data()
    df = df.drop(index).reset_index(drop=True)
    save_data(df)