-- Author Prajwal Kedari


-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
--
-- Database: `mytestdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `keylink`
--

CREATE TABLE `keylink` (
  `link` varchar(5) NOT NULL,
  `msg` text NOT NULL,
  `counter` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Author : Prajwal';
COMMIT;
