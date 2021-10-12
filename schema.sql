PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
DROP TABLE users;
Create Table users(
	id INTEGER PRIMARY KEY,
	username TEXT UNIQUE,
	pwhash TEXT
);

INSERT INTO users VALUES(
	1,
	'EternalAzure',
	'letmein'
);

COMMIT;