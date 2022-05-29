from matplotlib import pyplot as plt
from jinja2 import Template
import csv
import sys
stud = []
l = []
c = []
# command line arguments
sy1 = sys.argv[1]
sy2 = sys.argv[2]
# function for average


def average(c):
    sum = 0
    for i in c:
        sum = sum + int(i)
    return (sum/len(c))


# read data from csv file
m = []
with open('data.csv') as f:
    heading = next(f)
    read = csv.reader(f)
    for row in read:
        stud.append((row[0], row[1].lstrip(), row[2]))
        l.append(row[0])
        c.append(row[1].lstrip())
        m.append(int(row[2]))
# checking 3 conditions given in problem statement

ETEMPLATE = """ 
    <!DOCTYPE html>
    <html>
    <title> Something Went Wrong</title>
    <Body> <h1> Wrong Inputs</h1>
    <p> Something went wrong</p></body>
    </html>"""
z = []
if sy1 == "-s":
    if sy2 in l:
        sum = 0
        for i in stud:
            if i[0] == sy2:
                z.append((sy2, i[1], i[2]))
                sum = sum + int(i[2])
        TEMPLATE = """ 
                    <!DOCTYPE html>
                    <html>
                    <thead>
                    <title>
                    Student data
                    </title>
                    </thead>
                    <tbody>
                    <h1> Student Details </h1>
                    <table>
                    <tr> 
                         <th> Student id</th>
                         <th> Course id</th>
                         <th> Marks</th>
                    </tr>
                    {% for stu in z %}
                    <tr>
                      <td> {{ stu[0] }} </td>
                      <td> {{ stu[1] }} </td>
                      <td> {{ stu[2] }} </td>
                    </tr>
                    {% endfor %}
                <tr>
                <td colspan = "2"> Total Marks  </td>
                <td> {{ sum }} </td>
                </tr>
                </table>
                </tbody>
                </html>"""

        template = Template(TEMPLATE)
        con = template.render(z=z, sum=sum)
        output = open("output.html", 'w')
        output.write(con)
        output.close()
    else:
        template = Template(ETEMPLATE)
        con = template.render()
        output = open("output.html", 'w')
        output.write(con)
        output.close()

elif sy1 == "-c":
    if sy2 in c:
        m = []
        for i in stud:
            if i[1] == sy2:
                m.append(int(i[2]))
        ma = max(m)
        av = average(m)
        TEMPLATE = """<!DOCTYPE html>
    <html>
    <thead>
    <title>
    Course  data
    </title>
    </thead>
    <tbody>
    <h1>  Course Details </h1>
    <table border = "1">
    <tr> <th> Average Marks</th>
        <th> Maximum Marks</th>
    </tr>
     <tr>
       <td>{{ av }}</td>
       <td>{{ ma }}</td>
    </tr>
    </table>
    <img src = "hist.png">
    </tbody>
    </html>
    """
        template = Template(TEMPLATE)
        con = template.render(av=av, ma=ma)
        output = open("output.html", 'w')
        output.write(con)
        output.close()
        d = {}
        for i in m:
            d[i] = m.count(i)
        val = []
        for i in d.keys():
            val.append(d[i])
        plt.xlabel("Marks")
        plt.ylabel("Frequency")
        plt.hist(d.keys())
        plt.savefig('hist.png')
    else:
        template = Template(ETEMPLATE)
        con = template.render()
        output = open("output.html", 'w')
        output.write(con)
        output.close()
else:
    template = Template(ETEMPLATE)
    con = template.render()
    output = open("output.html", 'w')
    output.write(con)
    output.close()
