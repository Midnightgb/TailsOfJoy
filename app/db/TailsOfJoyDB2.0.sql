CREATE DATABASE tails_of_joy;

USE tails_of_joy;

CREATE TABLE people(
    person_id VACRHAR(255) PRIMARY KEY,
    identification BIGINT NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    phone BIGINT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE roles(
    id_role VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    role_description VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE user_photos(
    id_user_photo VARCHAR(255) PRIMARY KEY,
    photo_url VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE users(
    user_id VARCHAR(255) PRIMARY KEY,
    person_id VARCHAR(255) NOT NULL,
    id_role VARCHAR(255) NOT NULL,
    id_user_photo VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    status ENUM('ACTIVE', 'INACTIVE') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (person_id) REFERENCES people(person_id),
    FOREIGN KEY (id_role) REFERENCES roles(id_role),
    FOREIGN KEY (id_user_photo) REFERENCES user_photos(id_user_photo)
);

CREATE TABLE pet_traits(
    traits_id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    color VARCHAR(255),
    height FLOAT,
    weight FLOAT,
    age INT,
    disabilities VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE breeds(
    breed_id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    breed_description VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE species(
    specie_id VARCHAR(255) PRIMARY KEY,
    breed_id VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    specie_description VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (breed_id) REFERENCES breeds(breed_id)
);

CREATE TABLE pets(
    pet_id VARCHAR(255) PRIMARY KEY,
    specie_id VARCHAR(255) NOT NULL,
    traits_id VARCHAR(255) NOT NULL,
    status ENUM('ACTIVE', 'INACTIVE', 'DELETED', 'ADOPTED') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (specie_id) REFERENCES species(specie_id),
    FOREIGN KEY (traits_id) REFERENCES pet_traits(traits_id)
);

CREATE TABLE pet_photos(
    id_pet_photo VARCHAR(255) PRIMARY KEY,
    pet_id VARCHAR(255) NOT NULL,
    photo_url VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (pet_id) REFERENCES pets(pet_id)
);

CREATE TABLE posts(
    post_id VARCHAR(255) PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    pet_id VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (pet_id) REFERENCES pets(pet_id)
);

CREATE TABLE interactions(
    id_interaction VARCHAR(255) PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    post_id VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (post_id) REFERENCES posts(post_id)
);

CREATE TABLE adoptions(
    adoption_id VARCHAR(255) PRIMARY KEY,
    temporary_owner_id VARCHAR(255) NOT NULL,
    adopter_id VARCHAR(255) NOT NULL,
    pet_id VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (temporary_owner_id) REFERENCES users(user_id),
    FOREIGN KEY (adopter_id) REFERENCES users(user_id),
    FOREIGN KEY (pet_id) REFERENCES pets(pet_id)
);