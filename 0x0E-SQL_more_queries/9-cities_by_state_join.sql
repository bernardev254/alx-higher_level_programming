 -- lists all cities contained in the database hbtn_0d_usa.
-- lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, cities.name, state.name FROM cities LEFT JOIN ststes ON states.id = cities.state.id ORDER BY cities.id;

