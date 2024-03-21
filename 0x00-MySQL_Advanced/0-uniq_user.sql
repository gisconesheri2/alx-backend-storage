-- create a table user on any database
CREATE TABLE `users` IF NOT EXISTS (
    `id` INT NOT NULL AUTO_INCREMENT,
    `email` VARCHAR(255) NOT NULL,
    `name` VARCHAR(255),
    PRIMARY KEY (`id`),
    UNIQUE (`email`)
);
