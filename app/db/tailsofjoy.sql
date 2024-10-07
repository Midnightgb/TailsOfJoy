CREATE DATABASE tailsofjoy;

USE tailsofjoy;

CREATE TABLE `users` (
	`user_id` INT NOT NULL AUTO_INCREMENT,
	`name` varchar(20) NOT NULL,
	`last_name` varchar(40) NOT NULL,
	`birth_day` DATETIME NOT NULL,
	`phone_number` varchar(30) NOT NULL,
	`address` varchar(100) NOT NULL,
	`country` varchar(60) NOT NULL,
	`email` varchar(100) NOT NULL,
	`password` varchar(255) NOT NULL,
	`role` enum('basic','admin') NOT NULL DEFAULT 'basic',
	`status` enum('active','inactive','deleted') NOT NULL DEFAULT 'active',
	`created_at` TIMESTAMP NOT NULL DEFAULT current_timestamp(),
	`updated_at` TIMESTAMP NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
	PRIMARY KEY (`user_id`)
);

CREATE TABLE `pets` (
	`pet_id` INT NOT NULL AUTO_INCREMENT,
	`registered_by` INT NOT NULL,
	`status` enum('active','adopted','inactive','deleted') NOT NULL DEFAULT 'active',
	`species_id` INT,
	`breed_id` INT,
	`name` varchar(20) NOT NULL,
	`size_id` INT,
	`weight` INT NOT NULL,
	`age` INT NOT NULL,
	`color` varchar(30) NOT NULL,
	`description` varchar(160),
	`photo_url` varchar(200) NOT NULL,
	`created_at` TIMESTAMP NOT NULL,
	`updated_at` TIMESTAMP NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
	PRIMARY KEY (`pet_id`)
);

CREATE TABLE `adoptions` (
	`adoption_id` INT NOT NULL AUTO_INCREMENT,
	`pet_id` INT NOT NULL,
	`adopter_id` INT NOT NULL,
	`adoption_date` DATETIME NOT NULL,
	`created_at` TIMESTAMP NOT NULL DEFAULT current_timestamp(),
	`updated_at` TIMESTAMP NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
	PRIMARY KEY (`adoption_id`)
);

CREATE TABLE `breeds` (
	`breed_id` INT NOT NULL AUTO_INCREMENT,
	`breed_name` varchar(50) NOT NULL,
	`breed_description` varchar(60) NOT NULL,
	`created_at` TIMESTAMP NOT NULL DEFAULT current_timestamp(),
	`updated_at` TIMESTAMP NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
	PRIMARY KEY (`breed_id`)
);

CREATE TABLE `species` (
	`species_id` INT NOT NULL AUTO_INCREMENT,
	`species_name` varchar(20) NOT NULL,
	`species_description` varchar(60) NOT NULL,
	`created_at` TIMESTAMP NOT NULL DEFAULT current_timestamp(),
	`updated_at` TIMESTAMP NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
	PRIMARY KEY (`species_id`)
);

CREATE TABLE `sizes` (
	`size_id` INT NOT NULL AUTO_INCREMENT,
	`size_name` varchar(20) NOT NULL,
	`created_at` TIMESTAMP NOT NULL DEFAULT current_timestamp(),
	`updated_at` TIMESTAMP NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
	PRIMARY KEY (`size_id`)
);

ALTER TABLE `pets` ADD CONSTRAINT `pets_fk0` FOREIGN KEY (`registered_by`) REFERENCES `users`(`user_id`);

ALTER TABLE `pets` ADD CONSTRAINT `pets_fk1` FOREIGN KEY (`species_id`) REFERENCES `species`(`species_id`);

ALTER TABLE `pets` ADD CONSTRAINT `pets_fk2` FOREIGN KEY (`breed_id`) REFERENCES `breeds`(`breed_id`);

ALTER TABLE `pets` ADD CONSTRAINT `pets_fk3` FOREIGN KEY (`size_id`) REFERENCES `sizes`(`size_id`);

ALTER TABLE `adoptions` ADD CONSTRAINT `adoptions_fk0` FOREIGN KEY (`pet_id`) REFERENCES `pets`(`pet_id`);

ALTER TABLE `adoptions` ADD CONSTRAINT `adoptions_fk1` FOREIGN KEY (`adopter_id`) REFERENCES `users`(`user_id`);







