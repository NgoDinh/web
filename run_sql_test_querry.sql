select * from emp_data;

insert into emp_data(name, age) values ('tien', 26);
insert into emp_data(name, age) values ('the', 18);

CREATE TABLE flights(origin text, destination text, duaration integer)

insert into flights(origin, destination, duaration) values ('HUE', 'SG', 90)

select * from flights

insert into flights(origin, destination, duaration) values ('HUE', 'HN', 60)
insert into flights(origin, destination, duaration) values ('HUE', 'DN', 20)
insert into flights(origin, destination, duaration) values ('DN', 'SG', 70)
insert into flights(origin, destination, duaration) values ('DN', 'HN', 70)
insert into flights(origin, destination, duaration) values ('SG', 'HN', 120)


ALTER TABLE flights ADD COLUMN id integer;

With cte As
(
SELECT origin,destination,
ROW_NUMBER() OVER (ORDER BY id DESC) AS RN
FROM flights
)
-- select * from cte
UPDATE flights
SET id = 6

where origin = 'SG' and destination = 'HN'

create table passengers (flight_id integer, name text)

select * from passengers
