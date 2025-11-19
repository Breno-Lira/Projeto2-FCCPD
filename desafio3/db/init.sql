CREATE TABLE IF NOT EXISTS survivors (
    id SERIAL PRIMARY KEY,
    name TEXT
);

INSERT INTO survivors (name) VALUES ('Loader');
INSERT INTO survivors (name) VALUES ('Operator');
INSERT INTO survivors (name) VALUES ('Drifter');
INSERT INTO survivors (name) VALUES ('Captain');
