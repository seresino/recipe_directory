-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    avg_time INTEGER,
    rating INTEGER
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (title, avg_time, rating) VALUES ('Shepherds Pie', 60, 4);
INSERT INTO recipes (title, avg_time, rating) VALUES ('Mushroom Noodle Soup', 30, 5);
INSERT INTO recipes (title, avg_time, rating) VALUES ('Polenta Cake', 45, 2);
INSERT INTO recipes (title, avg_time, rating) VALUES ('Salmon Stir Fry', 35, 4);
INSERT INTO recipes (title, avg_time, rating) VALUES ('Pesto Pasta', 15, 3);