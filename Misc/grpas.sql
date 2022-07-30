select name from teams 

select title from book_catalog, book_author
where book_catalog.ISBN_non = book_author.ISBN_non
and book_author.fname = 'Joh Paul' and 
book_author.lname = 'Mueller'


select titles from book_catalog
where publisher = 'McGraw Hill Education'

select student_fname, student_lname from students , members
where students.roll_no = members.roll_no and member_type = 'PG'

w3q1

select distinct student_fname, student_lname 
from faculty natural join members natural join book_issue
where faculty.department_code = 'ME'

select count(title) from book_catalog where isbn_no in 
(select isbn_no from book_issue a, book_copes b
where a.accession = b.accession and a.doi = '2021-08-11')

select faculty_fname, faculty_lname from faculty
where faculty.id not in 
(select members.id from members natural join book_issue 
where members.id is is not null)

select distinct(title) from book_catalog natural join book_copes
natural join book_issue natural join members 
where member_type = 'PG'
except
select distinct(title) from book_catalog natural join book_copes
natural join book_issue natural join members 
where member_type = 'UG'


select fourth_refree from matche_refrees
where match_num  ='M0001'

select match_num, fourth_refree from matche_refrees
where assistant_refree_1 = 'R0002'

select jersey_no from players p, teams t
where p.team_id = p.team_id and t.name = 'Thunder'

select student_fname, roll_no from students 
where department_code = 'CS' and dob > '2002-06-15'


select faculty_fname from faculty, departments
where departments.department_code = faculty.department_code and
department_name = 'Mechanical Engineering'

-- OR

select faculty_fname from faculty natural join departments
where department_name like 'Mechanical Engineering'

-- WEEK 3

select match_num, name from matche_refrees, matches 
where matche_refrees.refree = matches.refree_id AND
match_num = (select match_num
from matches where match_date = '2020-05-15')


select p.name from players p, teams t
where p.team_id = t.team_id and t.name = 'Aravali'and dob < = all
(select p.dob from players p, teams t, where t.name = 'Aravali' and t.team_id = p.team_id)

select t.name from players p, teams t
where p.team_id = t.team_id  jersey_no not like 74

select department_code , member_type from
students natural join members natural join book_issue
where dob = '2021-08-02'

select title, count(title)
from book_catalog, book_copies
where book_catalog.acession_no = book_copies.acession_no
and title like '%Programming%'
group by title