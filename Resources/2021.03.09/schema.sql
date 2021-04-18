PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS genres (
	id INTEGER PRIMARY KEY,
	name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS countries (
	id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	isocode TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS books (
	id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	genre_id INTEGER REFERENCES genres(id)
);

CREATE TABLE IF NOT EXISTS authors (
	id INTEGER PRIMARY KEY,
	first_name TEXT,
	last_name TEXT,
	nationality_id INTEGER,
	FOREIGN KEY (nationality_id) REFERENCES countries(id)
);

CREATE TABLE IF NOT EXISTS book_authors (
	id INTEGER PRIMARY KEY,
	book_id INTEGER REFERENCES books(id),
	author_id INTEGER REFERENCES authors(id)
);