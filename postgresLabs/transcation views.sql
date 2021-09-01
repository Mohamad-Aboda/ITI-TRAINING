BEGIN TRANSACTION;

INSERT INTO subject values
(6, 'web', 'learn web', 55, 6);

INSERT INTO student values
(6, 'Mohamed Aboda', 'Mit ghmar', 'Mohaed@gmail.com', '01221312699', 6);


COMMIT;

select * from student;




BEGIN TRANSACTION;

INSERT INTO subject values
(7, 'web', 'learn web', 55, 7);

INSERT INTO student values
(7, 'Mohamed Aboda', 'Mit ghmar', 'Mohaed@gmail.com', '01221312699', 7);



COMMIT;
ROLLBACK WORK;

select * from student;



CREATE VIEW student_studentName_trackName AS SELECT s.name, t.track_name from student s join track t on s.std_id = t.track_id;
select * from student_studentName_trackName;



CREATE VIEW track_trackName_subjectName AS SELECT t.track_name, s.name from track t join subject s on t.track_id = s.subject_id;
select * from track_trackName_subjectName;




CREATE VIEW student_studentName_subjectName AS SELECT std.name AS studentName , sub.name AS subjectName from student std join subject sub on std.std_id = sub.subject_id;
select * from student_studentName_subjectName;


CREATE VIEW student_studentFullName_subjectScore_exam_examDate AS SELECT std.name AS FULLNAME,
sub.max_score, e.exam_date 
from 
	student std
	join subject sub on std.std_id = sub.subject_id
	join exam e on std.std_id = e.exam_id;
select * from student_studentFullName_subjectScore_exam_examDate;




CREATE LOCAL TEMP VIEW subject_maxScore AS 
select * from subject;


