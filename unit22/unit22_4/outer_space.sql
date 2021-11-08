-- from the terminal run:
-- psql < outer_space.sql

DROP DATABASE IF EXISTS outer_space;

CREATE DATABASE outer_space;

\c outer_space

CREATE TABLE planets
(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  orbital_period_in_years FLOAT NOT NULL,
  orbits_around INTEGER NOT NULL
);

INSERT INTO planets (name, orbital_period_in_years,orbits_around)
VALUES
('Earth', 1, 1),
('Mars', 1.88, 1),
('Venus', 0.62, 1),
('Neptune', 164.8, 1),
('Proxima Centauri b', 0.03, 2),
('Gliese 876 b', 0.23,3);

CREATE TABLE orbitsaround
(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    galaxy INTEGER NOT NULL
);

INSERT INTO orbitsaround (name, galaxy)
VALUES
('The Sun' , 1),
('Proxima Centauri', 1),
('Gliese 876', 1);

CREATE TABLE galaxy
(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL
);

INSERT INTO galaxy (name)
VALUES
('Milky Way');

CREATE TABLE moons
(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  planets_id INTEGER NOT NULL
);

INSERT INTO moons (name, planets_id)
VALUES
('The Moon', 1),
('Phobos', 2),
('Deimos', 2),
('Naiad', 3),
('Thalassa', 3),
('Despina', 3),
('Galatea', 3),
('Larissa', 3),
('S/2004 N 1', 3),
('Proteus', 3),
('Triton', 3),
('Nereid', 3),
('Halimede', 3),
('Sao', 3),
('Laomedeia', 3),
('Psamathe', 3),
('Neso', 3);