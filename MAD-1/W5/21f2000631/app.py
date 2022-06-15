from crypt import methods
from flask import Flask, request
from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.sqlite3"


db = SQLAlchemy()
db.init_app(app)
app.app_context().push()


class Student(db.Model):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    roll_number = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)
    courses = db.relationship('Course', secondary="enrollments")


class Course(db.Model):
    __tablename__ = 'course'
    course_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    course_code = db.Column(db.String, unique=True, nullable=False)
    course_name = db.Column(db.String, nullable=False)
    course_description = db.Column(db.String)


class Enrollments(db.Model):
    __tablename__ = 'enrollments'
    enrollment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    estudent_id = db.Column(db.Integer, db.ForeignKey(
        "student.student_id"), nullable=False)
    ecourse_id = db.Column(db.Integer, db.ForeignKey(
        "course.course_id"), nullable=False)


@app.route('/', methods=['GET'])
def home():

    students = Student.query.all()
    return render_template('index.html', students=students)


@app.route('/student/create', methods=['GET', 'POST'])
def addStudent():

    if request.method == 'GET':
        return render_template('create_form.html')

    elif request.method == 'POST':
        # return "<h1>Pehli fursat me nikal lejiye</h1>"

        student_check = Student.query.filter_by(
            roll_number=request.form['roll']).first()
        if student_check is None:

            rn = request.form['roll']
            fn = request.form['f_name']
            ln = request.form['l_name']
            try:
                new_student = Student(
                    roll_number=rn, first_name=fn, last_name=ln)
                courses_selected = request.form.getlist('courses')
                for course in courses_selected:
                    if course == 'course_1':
                        new_student.courses.append(
                            Course.query.filter_by(course_id=1).one())
                    elif course == 'course_2':
                        new_student.courses.append(
                            Course.query.filter_by(course_id=2).one())
                    elif course == 'course_3':
                        new_student.courses.append(
                            Course.query.filter_by(course_id=3).one())
                    elif course == 'course_4':
                        new_student.courses.append(
                            Course.query.filter_by(course_id=4).one())

                    db.session.add(new_student)
                    db.session.commit()

                    return redirect('/')
            except:
                db.session.rollback()
        else:
            return render_template('already_exists.html')


@app.route('/student/<int:student_id>/update', methods=['GET', 'POST'])
def update(student_id):

    if request.method == 'GET':
        st_details = Student.query.filter_by(student_id=student_id).one()
        return render_template('update_record.html', student_details=st_details)

    if request.method == 'POST':

        try:
            temp = Enrollments.query.filter_by(estudent_id=student_id).all()
            for enrollment_record in temp:
                db.session.delete(enrollment_record)

            student = Student.query.filter_by(student_id=student_id).one()
            student.first_name = request.form['f_name']
            student.last_name = request.form['l_name']
            updated_courses = request.form.getlist('courses')

            for course in updated_courses:
                student.courses.append(
                    Course.query.filter_by(course_id=course[-1]).one())

            db.session.commit()
            return redirect('/')

        except:
            db.session.rollback()
            return "Kuch Masla Hain"


@app.route('/student/<int:student_id>/delete', methods=['GET', 'POST'])
def delete_record(student_id):

    try:
        # note i am manually using delete rather than through relationship.
        Student.query.filter(Student.student_id == student_id).delete()
        Enrollments.query.filter(
            Enrollments.estudent_id == student_id).delete()

        ''' 2nd method)
        temp = Enrollments.query.filter_by(estudent_id = studentid).all()
        for enrollment in temp:
            db.session.delete(enrollment)
        studa = Student.query.filter_by(student_id = studentid).one()
        db.session.delete(studa)
        '''
        db.session.commit()
        return redirect('/')
    except:
        db.session.rollback()
        return "Kuch Masla Hain"


@app.route('/student/<int:student_id>', methods=['GET'])
def display_student_data(student_id):
    try:
        student = Student.query.filter_by(student_id=student_id).one()
        return render_template('display_st_details.html', student_details=student)

    except:
        db.session.rollback()
        return "Kuch Masla Hain"


if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', debug=True, port=8080)


# Gaali Gaurav Krishna 21f2000631
