from flask import Flask, render_template, request
from matplotlib import pyplot as plt


# creating the data list by reading data.csv file

f = open('data.csv', 'r')
data_row = f.readline()
cols = data_row.split(',')
n = len(cols)
for i in range(n):
    cols[i] = cols[i].strip()
data_row = f.readline()
data = []
students = []
courses = []
while(data_row):
    row = {}
    data_row_list = data_row.split(',')
    for i in range(n):
        row[cols[i]] = int(data_row_list[i].strip())
        if i == 0:
            if int(data_row_list[0]) not in students:
                students.append(int(data_row_list[0]))
        elif i == 1:
            if int(data_row_list[1]) not in courses:
                courses.append(int(data_row_list[1]))
    data.append(row)
    data_row = f.readline()
f.close()


# required functions

def total_marks(l):
    sum_marks = 0
    for ele in l:
        sum_marks += ele['Marks']
    return sum_marks


def avg_marks(l):
    sum_marks = total_marks(l)
    return (sum_marks/len(l))


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def get_details():
    if request.method == "GET":
        return render_template("get_details.html")
    elif request.method == "POST":
        data_id = request.form['ID']
        try:
            id_value = int(request.form['id_value'])
        except:
            return render_template("invalid_details.html")

        if data_id == "student_id":
            if id_value in students:
                student_data = []
                for dict in data:
                    if dict["Student id"] == id_value:
                        student_data.append(dict)
                sum_marks = total_marks(student_data)
                return render_template("student_details.html", student_data=student_data, total_marks=sum_marks)
            else:
                return render_template("invalid_details.html")

        elif data_id == "course_id":
            if id_value in courses:
                course_data = []
                marks = []
                for dict in data:
                    if dict["Course id"] == id_value:
                        course_data.append(dict)
                        marks.append(dict['Marks'])
                avg = avg_marks(course_data)
                maximum_marks = max(marks)
                plt.hist(marks)
                plt.savefig("static/histogram.png")
                return render_template("course_details.html", average_marks=avg, maximum_marks=maximum_marks)
            else:
                return render_template("invalid_details.html")
    else:
        return render_template("invalid_details.html")


if __name__ == '__main__':
    app.run()
