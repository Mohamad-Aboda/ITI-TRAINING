-- 1
CREATE OR REPLACE FUNCTION mul(a INTEGER, b INTEGER) RETURNS INTEGER AS $$
    BEGIN
        RETURN a * b 
    END;
$$ LANGUAGE plpgsql;


-- 2
CREATE OR REPLACE FUNCTION check_even_odd(a integer) RETURNS INTEGER AS $$
    BEGIN
        IF MOD(a, 2) = 0 THEN RETURN 0;
        ELSE RETURN 1;
        END IF;
    END;
$$ LANGUAGE plpgsql



-- 3
// CREATE TABLE FIRST 

CREATE TABLE LAB4(first_name varchar(30), last_name varchar(30), birthdate date, track_name varchar(30));

CREATE OR REPLACE FUNCTION AddNewStudent(firstName varchar, lastName varchar, birthdate date, trackName varchar) RETURNS void AS 
$$

    BEGIN
        INSERT INTO LAB4 VALUES(firstName, lastName, birthdate, trackName);
    END;
$$ LANGUAGE plpgsql


SELECT AddNewStudent('Mohamed', 'ali', '2001-09-28', 'python');


-- 4



CREATE OR REPLACE FUNCTION student_score(student_id integer, subject_id integer) RETURNS INTEGER AS 
$$
declare res int;
    BEGIN
        select std_id, max_score into res from student inner join subject on subject.subject_id = student.std_id;
        return res;
    END;
$$ LANGUAGE plpgsql


select student_score(1, 1);


-- 5
CREATE OR REPLACE FUNCTION student_fail(subject_id integer) RETURNS integer AS 
$$
declare res int;
    BEGIN
        perform count(*) from subject where max_score < 50;
		return res;
    END;
$$ LANGUAGE plpgsql


select student_fail(1);

-- 6

CREATE OR REPLACE FUNCTION avg_grade(subject_name varchar) RETURNS integer AS 

$$
declare res int;
    BEGIN
        select sum(max_score) / count(*) into res from subject;
		return res;
    END;
$$ LANGUAGE plpgsql


select avg_grade('web');

-- 7
CREATE TABLE persons(id INT NOT NULL PRIMARY KEY, name VARCHAR(100), gender BOOLEAN);


-- 8

CREATE TABLE staff_members(dept_name VARCHAR(100), course_name VARCHAR(100)) INHERITS(persons);
















