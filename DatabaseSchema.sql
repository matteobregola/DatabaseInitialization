CREATE TYPE AwardResult AS ENUM
    ('won', 'nominated');	
CREATE TABLE Directors
(
    director varchar(50) NOT NULL,
    yearOfBirth integer NOT NULL,
    CONSTRAINT "Directors_pkey" PRIMARY KEY (director)
);
CREATE TABLE Movies
(
    title varchar(100) NOT NULL,
    year integer NOT NULL,
    director varchar(50) NOT NULL,
    budget integer NOT NULL,
    gross integer NOT NULL,
    CONSTRAINT "Movies_pkey" PRIMARY KEY (title, year),
	CONSTRAINT "DirectorAwards_director_fkey" FOREIGN KEY (director)
        REFERENCES Directors(director) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);
CREATE TABLE DirectorAwards
(
    director varchar(50) NOT NULL,
    year integer NOT NULL,
    award varchar(100) NOT NULL,
    result AwardResult NOT NULL,
	CONSTRAINT "DirectorAwards_pkey" PRIMARY KEY (director, year, award),
    CONSTRAINT "DirectorAwards_director_fkey" FOREIGN KEY (director)
        REFERENCES Directors(director) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);
CREATE TABLE MovieAwards
(
    title varchar(100) NOT NULL,
    year integer NOT NULL,
    award varchar(100) NOT NULL,
    result AwardResult NOT NULL,
	CONSTRAINT "MovieAwards_pkey" PRIMARY KEY (title, year, award),
    CONSTRAINT "MovieAwards_year_title_fkey" FOREIGN KEY (title, year)
        REFERENCES Movies(title, year) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);
