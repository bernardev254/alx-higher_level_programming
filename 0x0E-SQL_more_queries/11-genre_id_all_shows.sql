-- lists all shows contained in the database hbtn_0d_tvshows
-- lists all shows contained in the database hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id ORDER BY tv_shows.title ASC, tv_shows_genres.genre_id ASC;

