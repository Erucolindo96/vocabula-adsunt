
CREATE TABLE IF NOT EXISTS age(
   id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   name TEXT NOT NULL UNIQUE,
   slug TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS book(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   title TEXT NOT NULL,
   content TEXT,
   uri TEXT,
   age_id INTEGER,
   author TEXT,
   author_slug TEXT,
   FOREIGN KEY(age_id) REFERENCES age(id)
);








