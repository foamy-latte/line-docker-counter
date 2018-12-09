CREATE TABLE `counters` (
	`uuid`	TEXT NOT NULL UNIQUE,
	`expires`	INTEGER NOT NULL,
	PRIMARY KEY(`uuid`)
);