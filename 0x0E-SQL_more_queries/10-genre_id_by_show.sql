-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_shows.title, tv_shows.genres.genre_id FROM tv_shows INNER JOIN tv_shows.genres ON tv_shows_genres.show_id ORDER BY tv_shows.title ASC, tv_shows_genres.genre_id ASC;

