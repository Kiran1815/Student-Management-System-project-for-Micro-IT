import streamlit as st
import student_operations as ops
import pandas as pd

st.set_page_config(page_title="Student Management System", layout="centered")
st.title("🎓 Student Management System")

menu = ["Add Student", "View Students", "Update Student", "Delete Student"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Student":
    st.subheader("➕ Add New Student")
    id = st.number_input("ID", min_value=1)
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1)
    course = st.text_input("Course")
    grade = st.selectbox("Grade", ["A+", "A", "B+", "B", "C", "D", "E", "F"])
    attendance = st.number_input("Attendance (%)", min_value=0.0, max_value=100.0, format="%.2f")

    if st.button("Add"):
        student = {
            "ID": id,
            "Name": name,
            "Age": age,
            "Course": course,
            "Grade": grade,
            "Attendance": round(attendance, 2)
        }
        ops.add_student(student)
        st.success("Student added successfully!")

elif choice == "View Students":
    st.subheader("📋 All Students")
    df = ops.get_all_students()

    def highlight_failing(row):
        return ['background-color: #ffcccc' if str(row['Grade']).strip().upper() == 'F' else '' for _ in row]

    if not df.empty:
        df['Attendance'] = df['Attendance'].apply(lambda x: f"{float(str(x).replace('%', '').strip()):.2f}%")
        styled_df = df.style.apply(highlight_failing, axis=1)
        st.dataframe(styled_df, use_container_width=True)
    else:
        st.info("No student records found.")

elif choice == "Update Student":
    st.subheader("✏ Update Student")
    df = ops.get_all_students()
    if not df.empty:
        st.dataframe(df)
        index = st.number_input("Enter the index to update", min_value=0, max_value=len(df)-1)
        id = st.number_input("ID", min_value=1, value=int(df.loc[index, "ID"]))
        name = st.text_input("Name", value=df.loc[index, "Name"])
        age = st.number_input("Age", min_value=1, value=int(df.loc[index, "Age"]))
        course = st.text_input("Course", value=df.loc[index, "Course"])
        grades = ["A+", "A", "B+", "B", "C", "D", "E", "F"]
        grade = st.selectbox("Grade", grades, index=grades.index(str(df.loc[index, "Grade"]).strip().upper()))
        attendance = st.number_input("Attendance (%)", min_value=0.0, max_value=100.0, value=float(df.loc[index, "Attendance"]), format="%.2f")

        if st.button("Update"):
            updated_student = {
                "ID": id,
                "Name": name,
                "Age": age,
                "Course": course,
                "Grade": grade,
                "Attendance": round(attendance, 2)
            }
            ops.update_student(index, updated_student)
            st.success("Student updated successfully!")
    else:
        st.warning("No data to update.")

elif choice == "Delete Student":
    st.subheader("🗑 Delete Student")
    df = ops.get_all_students()
    if not df.empty:
        st.dataframe(df)
        index = st.number_input("Enter the index to delete", min_value=0, max_value=len(df)-1)
        if st.button("Delete"):
            ops.delete_student(index)
            st.success("Student deleted successfully!")
    else:
        st.warning("No data to delete.")