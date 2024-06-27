-- Supabase AI is experimental and may produce incorrect answers
-- Always verify the output before executing

create table
  people (
    person_id varchar(255) primary key,
    identification bigint not null,
    first_name varchar(255) not null,
    surname varchar(255) not null,
    address varchar(255) not null,
    phone bigint not null,
    created_at timestamp with time zone default current_timestamp,
    updated_at timestamp with time zone default current_timestamp
  );

create table
  roles (
    id_role varchar(255) primary key,
    name varchar(255) not null,
    role_description varchar(255) not null,
    created_at timestamp with time zone default current_timestamp,
    updated_at timestamp with time zone default current_timestamp
  );

create table
  user_photos (
    id_user_photo varchar(255) primary key,
    photo_url varchar(255) not null,
    created_at timestamp with time zone default current_timestamp,
    updated_at timestamp with time zone default current_timestamp
  );

create table
  users (
    user_id varchar(255) primary key,
    person_id varchar(255) not null,
    id_role varchar(255) not null,
    id_user_photo varchar(255) not null,
    email varchar(255) not null,
    password varchar(255) not null,
    status varchar(10) check (status in ('ACTIVE', 'INACTIVE')) not null,
    created_at timestamp with time zone default current_timestamp,
    updated_at timestamp with time zone default current_timestamp,
    foreign key (person_id) references people (person_id),
    foreign key (id_role) references roles (id_role),
    foreign key (id_user_photo) references user_photos (id_user_photo)
  );

create table
  pet_traits (
    traits_id varchar(255) primary key,
    name varchar(255),
    description varchar(255),
    color varchar(255),
    height float,
    weight float,
    age int,
    disabilities varchar(255),
    created_at timestamp with time zone default current_timestamp,
    updated_at timestamp with time zone default current_timestamp
  );

create table
  breeds (
    breed_id varchar(255) primary key,
    name varchar(255),
    breed_description varchar(255),
    created_at timestamp with time zone default current_timestamp,
    updated_at timestamp with time zone default current_timestamp
  );

create table
  species (
    specie_id varchar(255) primary key,
    breed_id varchar(255) not null,
    name varchar(255),
    specie_description varchar(255),
    created_at timestamp with time zone default current_timestamp,
    updated_at timestamp with time zone default current_timestamp,
    foreign key (breed_id) references breeds (breed_id)
  );

create table
  pets (
    pet_id varchar(255) primary key,
    specie_id varchar(255) not null,
    traits_id varchar(255) not null,
    status varchar(10) check (
      status in ('ACTIVE', 'INACTIVE', 'DELETED', 'ADOPTED')
    ) not null,
    created_at timestamp with time zone default current_timestamp,
    updated_at timestamp with time zone default current_timestamp,
    foreign key (specie_id) references species (specie_id),
    foreign key (traits_id) references pet_traits (traits_id)
  );

create table
  pet_photos (
    id_pet_photo varchar(255) primary key,
    pet_id varchar(255) not null,
    photo_url varchar(255) not null,
    created_at timestamp with time zone default current_timestamp,
    updated_at timestamp with time zone default current_timestamp,
    foreign key (pet_id) references pets (pet_id)
  );

create table
  posts (
    post_id varchar(255) primary key,
    user_id varchar(255) not null,
    pet_id varchar(255) not null,
    date DATE not null,
    created_at timestamp with time zone default current_timestamp,
    updated_at timestamp with time zone default current_timestamp,
    foreign key (user_id) references users (user_id),
    foreign key (pet_id) references pets (pet_id)
  );

create table
  interactions (
    id_interaction varchar(255) primary key,
    user_id varchar(255) not null,
    post_id varchar(255) not null,
    date DATE not null,
    created_at timestamp with time zone default current_timestamp,
    updated_at timestamp with time zone default current_timestamp,
    foreign key (user_id) references users (user_id),
    foreign key (post_id) references posts (post_id)
  );

create table
  adoptions (
    adoption_id varchar(255) primary key,
    temporary_owner_id varchar(255) not null,
    adopter_id varchar(255) not null,
    pet_id varchar(255) not null,
    date DATE not null,
    created_at timestamp with time zone default current_timestamp,
    updated_at timestamp with time zone default current_timestamp,
    foreign key (temporary_owner_id) references users (user_id),
    foreign key (adopter_id) references users (user_id),
    foreign key (pet_id) references pets (pet_id)
  );