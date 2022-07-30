SELECT student_fname, rol_no from student
where department_cdoe ='CS' and dob > '2022-060-15'

select facult_fname from facult_fname f , departmets d
where department_name = 'Mechanical Engineering'


select name from  teams t . matches ma
where 

select name from teams where team_id in
(select team_id
from ((select host_team_id as team_id, count(*) as c
from matches
group by host_team_id)
union all
(select guest_team_id as team_id, count(*) as c
from matches
group by guest_team_id)) as t1
group by team_id having sum(c) > 3
)


select match_num, name from
matches m, referees r
where m.referee = r.referee_id
and match_num = (select match_num from matches
 where match_data = '2020-05-15')


-- Week 3 graded 2
select p.name from players p, teams t
where p.team_id = t.team_id
and t.name = t.name  = 'Aravali' 
and p.dob <= all(select p.dob from players p, teams t
where p.team_id = t.team_id and t.name = 'Aravali')


-- Week 3 graded 3
select distinct t.name from players p, teams t WHERE
p.team_id = t.team_id and 
jersey_no != 74 

-- or

select distinct t.name from players p, teams t WHERE
team_id.team_id not in (select team_id from players where jersey_no in (74)) 

-- Week 3 graded 4

select s.department_code, m.member_type from students s, members m, book_issue bi
where s.roll_no = m.roll_no and m.member_no = bi.member_no
and (doi = '2021-08-02')


-- Week 3 graded 5

select bc.title, count(bc.title) from book_catalog bc, 
where title = '%Programming%'

-- or 

select bc.title, count(bc.title) from book_catalog bca, book_copies bc
where bca.ISBN_no = bc.ISBN_no and bca.title like '%Programming%'


