CREATE DATABASE lecture_notes;

USE lecture_notes;

CREATE TABLE notes (

id INT PRIMARY KEY AUTO_INCREMENT,

lecture_title VARCHAR(255),

content TEXT,

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
