-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 30, 2024 at 11:25 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tailsofjoy`
--

--
-- Dumping data for table `breeds`
--

INSERT INTO `breeds` (`breed_id`, `species_id`, `breed_name`, `breed_description`, `created_at`, `updated_at`) VALUES
(1, 1, 'Labrador Retriever', 'Medium to large-sized breed', '2024-01-30 22:22:14', '2024-01-30 22:22:14'),
(2, 2, 'Siamese', 'Domestic cat breed', '2024-01-30 22:22:14', '2024-01-30 22:22:14'),
(3, 3, 'Budgerigar', 'Small parrot breed', '2024-01-30 22:22:14', '2024-01-30 22:22:14'),
(4, 4, 'Mixed Breed', 'Mixed breed', '2024-01-30 22:22:14', '2024-01-30 22:22:14');

--
-- Dumping data for table `pets`
--

INSERT INTO `pets` (`pet_id`, `registered_by`, `status`, `species_id`, `breed_id`, `name`, `size_id`, `weight`, `age`, `color`, `description`, `photo_url`, `created_at`, `updated_at`) VALUES
(1, 1, 'active', 1, 1, 'Buddy', 1, 15, 2, 'Golden', 'Friendly and playful', 'buddy.jpg', '2024-01-30 22:22:14', '2024-01-30 22:22:14'),
(2, 1, 'active', 2, 2, 'Whiskers', 2, 8, 1, 'Siamese mix', 'Loves to nap', 'whiskers.jpg', '2024-01-30 22:22:14', '2024-01-30 22:22:14'),
(3, 1, 'active', 3, 3, 'Polly', 3, 1, 1, 'Green and yellow', 'Chirpy bird', 'polly.jpg', '2024-01-30 22:22:14', '2024-01-30 22:22:14');

--
-- Dumping data for table `sizes`
--

INSERT INTO `sizes` (`size_id`, `size_name`, `created_at`, `updated_at`) VALUES
(1, 'Small', '2024-01-30 22:22:14', '2024-01-30 22:22:14'),
(2, 'Medium', '2024-01-30 22:22:14', '2024-01-30 22:22:14'),
(3, 'Large', '2024-01-30 22:22:14', '2024-01-30 22:22:14');

--
-- Dumping data for table `species`
--

INSERT INTO `species` (`specie_id`, `specie_name`, `specie_description`, `created_at`, `updated_at`) VALUES
(1, 'Dog', 'Domestic dog', '2024-01-30 22:22:14', '2024-01-30 22:22:14'),
(2, 'Cat', 'Domestic cat', '2024-01-30 22:22:14', '2024-01-30 22:22:14'),
(3, 'Bird', 'Various bird species', '2024-01-30 22:22:14', '2024-01-30 22:22:14'),
(4, 'Other', 'Other species', '2024-01-30 22:22:14', '2024-01-30 22:22:14');

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `name`, `last_name`, `birth_day`, `phone_number`, `address`, `country`, `email`, `password`, `status`, `created_at`, `updated_at`, `role`) VALUES
(1, 'julian', 'vasquez', '2001-06-23', '304645665', 'km 9 via armenia pereira', 'colombia', 'midnight3424@gmail.com', 'holasoyunacontra', 'active', '2024-01-30 22:13:11', '2024-01-30 22:24:11', 'admin');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
