-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE languages (
    name varchar(50)   NOT NULL,
    first_appeared integer   NOT NULL,
    CONSTRAINT pk_languages PRIMARY KEY (
        name
     )
);

CREATE TABLE populatiry (
    name varchar(50)   NOT NULL,
    date varchar(20)   NOT NULL,
    rating float   NOT NULL,
    CONSTRAINT pk_populatiry PRIMARY KEY (
        name,date
     )
);

ALTER TABLE populatiry ADD CONSTRAINT fk_populatiry_name FOREIGN KEY(name)
REFERENCES languages (name);

