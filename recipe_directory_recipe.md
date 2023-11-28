1. User Story

As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep a list of all my recipes with their names.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep the average cooking time (in minutes) for each recipe.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to give a rating to each of the recipes (from 1 to 5).

2. Table Design

Table Name: Recipes
Columns:
name (text)
avg_time (int)
rating (int)

3. SQL

CREATE TABLE recipes (
    name text,
    avg_time int,
    rating int
);