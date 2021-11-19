-- from the terminal run:
-- psql < air_traffic.sql

DROP DATABASE IF EXISTS air_traffic;

CREATE DATABASE air_traffic;

\c air_traffic

CREATE TABLE tickets
(
  id SERIAL PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  seat TEXT NOT NULL,
  flight_id  INTEGER NOT NULL
);

INSERT INTO tickets
(first_name, last_name, seat, flight_id)
VALUES
('Jennifer', 'Finch', '33B', 1),
('Thadeus', 'Gathercoal','8A', 2),
('Sonja', 'Pauley', '12F', 3),
('Jennifer', 'Finch', '20A', 4),
('Waneta', 'Skeleton', '23D',5),
('Thadeus', 'Gathercoal', '18C', 6),
('Berkie', 'Wycliff', '9E', 7),
('Alvin', 'Leathes', '1A', 8),
('Berkie', 'Wycliff', '32B', 9),
('Cory', 'Squibbes', '10D', 10);


CREATE TABLE countries
(
 id SERIAL PRIMARY KEY,
 country TEXT NOT NULL
);

INSERT INTO countries (country)
VALUES
('United States'),
('Japan'),
('France'),
('UAE'),
('Brazil'),
('United Kingdom'),
('Mexico'),
('Morocco'),
('China'),
('Chile');

CREATE TABLE cities
(
 id SERIAL PRIMARY KEY,
 city TEXT NOT NULL,
 country_id INTEGER NOT NULL
);

INSERT INTO cities (city, country_id)
VALUES
('Washington DC', 1),
('Tokyo', 2),
('Los Angeles', 1),
('Seattle', 1),
('Paris', 3), 
('Dubai', 4), 
('New York', 1),
('Cedar Rapids', 1), 
('Charlotte', 1),
('Sao Paolo', 5), 
('London', 6),
('Las Vegas', 1),
('Mexico City', 7),
('Casablanca', 8),
('Beijing', 9),
('Chicago', 1),
('New Orleans', 1),
('Santiago', 10);

CREATE TABLE airlines
(
 id SERIAL PRIMARY KEY,
 name TEXT NOT NULL
);

INSERT INTO airlines (name)
VALUES
('United'),
('British Airways'),
('Delta'),
('TUI Fly Belgium'),
('Air China'),
('American Airlines'),
('Avianca Brasil');

CREATE TABLE flights
(
 flights_id SERIAL PRIMARY KEY,
 departure TIMESTAMP NOT NULL,
 arrival TIMESTAMP NOT NULL,
 airline_id INTEGER NOT NULL,
 from_city_id  INTEGER NOT NULL,
 from_country_id  INTEGER NOT NULL,
 to_city_id  INTEGER NOT NULL,
 to_country_id  INTEGER NOT NULL
);

INSERT INTO flights (departure, arrival, airline_id, from_city_id, from_country_id, to_city_id, to_country_id)
VALUES
('2018-04-08 09:00:00', '2018-04-08 12:00:00', 1, 1, 1, 4, 1),
('2018-12-19 12:45:00', '2018-12-19 16:15:00', 2, 2, 2, 11, 6),
('2018-01-02 07:00:00', '2018-01-02 08:03:00', 3, 3, 1, 12, 1),
('2018-04-15 16:50:00', '2018-04-15 21:00:00', 3, 4, 1, 13, 7),
('2018-08-01 18:30:00', '2018-08-01 21:50:00', 4, 5, 3, 14, 8),
('2018-10-31 01:15:00', '2018-10-31 12:55:00', 5, 6, 4, 15, 9),
('2019-02-06 06:00:00', '2019-02-06 07:47:00', 1, 7, 1, 9, 1),
('2018-12-22 14:42:00', '2018-12-22 15:56:00', 6, 8, 1, 16, 1),
('2019-02-06 16:28:00', '2019-02-06 19:18:00', 6, 9, 1, 17, 1),
('2019-01-20 19:30:00', '2019-01-20 22:45:00', 7, 10, 5, 18, 10);