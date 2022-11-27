-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 22, 2022 at 09:54 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `DBMS Proj`
--

-- --------------------------------------------------------

--
-- Table structure for table `Bill`
--

CREATE TABLE `Bill` (
  `order_id` bigint(20) NOT NULL,
  `Customer_Aadhaar` bigint(20) NOT NULL,
  `total_amount` bigint(20) NOT NULL,
  `customer_payment` bigint(20) NOT NULL,
  `insurance_payment` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Bill`
--

INSERT INTO `Bill` (`order_id`, `Customer_Aadhaar`, `total_amount`, `customer_payment`, `insurance_payment`) VALUES
(984324, 784526471835, 51, 40, 11);

-- --------------------------------------------------------

--
-- Table structure for table `Customer`
--

CREATE TABLE `Customer` (
  `Aadhaar` bigint(20) NOT NULL,
  `first_name` char(255) NOT NULL,
  `last_name` char(255) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `gender` char(1) NOT NULL,
  `address` char(255) NOT NULL,
  `date_of_birth` date NOT NULL,
  `insurance_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Customer`
--

INSERT INTO `Customer` (`Aadhaar`, `first_name`, `last_name`, `phone`, `gender`, `address`, `date_of_birth`, `insurance_id`) VALUES
(6489075453, 'Ravi', 'Singh', 8976785649, 'M', 'Nice Road,Electronic City', '2002-02-13', 66554433),
(546790987890, 'Reha', 'Lal', 9966442211, 'F', 'Sarjapur Road,Whitefield', '2002-10-17', 99006655),
(784526471835, 'Shyam', 'Bhat', 7648964389, 'M', 'Hosa Road,Electronic City', '2002-09-03', 55446677);

-- --------------------------------------------------------

--
-- Table structure for table `Employee`
--

CREATE TABLE `Employee` (
  `ID` bigint(20) NOT NULL,
  `Aadhaar` bigint(20) NOT NULL,
  `License` bigint(20) DEFAULT NULL,
  `first_name` char(255) NOT NULL,
  `last_name` char(255) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT NULL,
  `role` char(255) NOT NULL,
  `salary` bigint(20) NOT NULL,
  `phone_number` bigint(20) NOT NULL,
  `date_of_birth` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Employee`
--

INSERT INTO `Employee` (`ID`, `Aadhaar`, `License`, `first_name`, `last_name`, `start_date`, `end_date`, `role`, `salary`, `phone_number`, `date_of_birth`) VALUES
(732, 658361987523, 9875, 'Rahul', 'Gupta', '2021-09-24', NULL, 'intern', 60000, 8899786432, '1992-06-19'),
(758, 658361985378, 8295, 'Veer', 'Das', '2015-09-24', NULL, 'pharmacist', 70000, 9112786432, '1987-06-19');

-- --------------------------------------------------------

--
-- Table structure for table `Insurance`
--

CREATE TABLE `Insurance` (
  `insurance_id` bigint(20) NOT NULL,
  `company_name` char(255) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `co_insurance` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Insurance`
--

INSERT INTO `Insurance` (`insurance_id`, `company_name`, `start_date`, `end_date`, `co_insurance`) VALUES
(55446677, 'Adani Insurance', '2002-09-03', '2102-09-03', 20),
(66554433, 'Reliance Insurance', '2002-02-13', '2102-02-13', 17),
(99006655, 'Big Insurance', '2002-10-17', '2102-10-17', 18);

-- --------------------------------------------------------

--
-- Table structure for table `Medicine`
--

CREATE TABLE `Medicine` (
  `drug_name` char(255) NOT NULL,
  `batch_number` bigint(20) NOT NULL,
  `MedicineType` char(255) NOT NULL,
  `Manufacturer` char(255) NOT NULL,
  `stock_quantity` bigint(20) NOT NULL,
  `expiry_date` date NOT NULL,
  `Price` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Medicine`
--

INSERT INTO `Medicine` (`drug_name`, `batch_number`, `MedicineType`, `Manufacturer`, `stock_quantity`, `expiry_date`, `Price`) VALUES
('Crocin', 893145, 'Targetted Pain', 'GSK', 800, '2022-01-02', 20),
('Dolo-650', 788907, 'Paracetamol', 'Micro Labs', 800, '2023-02-12', 31);

-- --------------------------------------------------------

--
-- Table structure for table `ORDERED_DRUGS`
--

CREATE TABLE `ORDERED_DRUGS` (
  `order_id` bigint(20) NOT NULL,
  `drug_name` char(255) NOT NULL,
  `batch_number` bigint(20) NOT NULL,
  `ordered_quantity` bigint(20) NOT NULL,
  `Price` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ORDERED_DRUGS`
--

INSERT INTO `ORDERED_DRUGS` (`order_id`, `drug_name`, `batch_number`, `ordered_quantity`, `Price`) VALUES
(984324, 'Crocin', 893145, 20, 20),
(984324, 'Dolo-650', 788907, 10, 31);

-- --------------------------------------------------------

--
-- Table structure for table `Orders`
--

CREATE TABLE `Orders` (
  `order_id` bigint(20) NOT NULL,
  `prescription_id` bigint(20) NOT NULL,
  `EmployeeID` bigint(20) NOT NULL,
  `order_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Orders`
--

INSERT INTO `Orders` (`order_id`, `prescription_id`, `EmployeeID`, `order_date`) VALUES
(984324, 112233, 732, '2022-09-11');

-- --------------------------------------------------------

--
-- Table structure for table `PRESCRIBED_DRUGS`
--

CREATE TABLE `PRESCRIBED_DRUGS` (
  `prescription_id` bigint(20) NOT NULL,
  `drug_name` char(255) NOT NULL,
  `prescribed_quantity` bigint(20) NOT NULL,
  `refill_limit` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `PRESCRIBED_DRUGS`
--

INSERT INTO `PRESCRIBED_DRUGS` (`prescription_id`, `drug_name`, `prescribed_quantity`, `refill_limit`) VALUES
(112233, 'Dolo-650', 3, 5);

-- --------------------------------------------------------

--
-- Table structure for table `Prescription`
--

CREATE TABLE `Prescription` (
  `prescription_id` bigint(20) NOT NULL,
  `Aadhaar` bigint(20) NOT NULL,
  `doctor_id` bigint(20) NOT NULL,
  `prescribed_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Prescription`
--

INSERT INTO `Prescription` (`prescription_id`, `Aadhaar`, `doctor_id`, `prescribed_date`) VALUES
(112233, 784526471835, 444, '2022-08-14'),
(223344, 546790987890, 666, '2022-05-24');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Bill`
--
ALTER TABLE `Bill`
  ADD PRIMARY KEY (`order_id`,`Customer_Aadhaar`),
  ADD KEY `pays` (`Customer_Aadhaar`);

--
-- Indexes for table `Customer`
--
ALTER TABLE `Customer`
  ADD PRIMARY KEY (`Aadhaar`),
  ADD UNIQUE KEY `phone` (`phone`),
  ADD KEY `insures` (`insurance_id`);

--
-- Indexes for table `Employee`
--
ALTER TABLE `Employee`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `License` (`License`);

--
-- Indexes for table `Insurance`
--
ALTER TABLE `Insurance`
  ADD PRIMARY KEY (`insurance_id`),
  ADD KEY `Insurance_Company_Name` (`company_name`);

--
-- Indexes for table `Medicine`
--
ALTER TABLE `Medicine`
  ADD PRIMARY KEY (`drug_name`,`batch_number`);

--
-- Indexes for table `ORDERED_DRUGS`
--
ALTER TABLE `ORDERED_DRUGS`
  ADD PRIMARY KEY (`order_id`,`drug_name`,`batch_number`),
  ADD KEY `Fulfilled_From` (`drug_name`,`batch_number`);

--
-- Indexes for table `Orders`
--
ALTER TABLE `Orders`
  ADD PRIMARY KEY (`order_id`),
  ADD KEY `prepares` (`EmployeeID`),
  ADD KEY `uses` (`prescription_id`);

--
-- Indexes for table `PRESCRIBED_DRUGS`
--
ALTER TABLE `PRESCRIBED_DRUGS`
  ADD PRIMARY KEY (`prescription_id`,`drug_name`);

--
-- Indexes for table `Prescription`
--
ALTER TABLE `Prescription`
  ADD PRIMARY KEY (`prescription_id`),
  ADD KEY `holds` (`Aadhaar`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Bill`
--
ALTER TABLE `Bill`
  ADD CONSTRAINT `makes` FOREIGN KEY (`order_id`) REFERENCES `Orders` (`order_id`),
  ADD CONSTRAINT `pays` FOREIGN KEY (`Customer_Aadhaar`) REFERENCES `Customer` (`Aadhaar`);

--
-- Constraints for table `Customer`
--
ALTER TABLE `Customer`
  ADD CONSTRAINT `insures` FOREIGN KEY (`insurance_id`) REFERENCES `Insurance` (`insurance_id`) ON DELETE CASCADE;

--
-- Constraints for table `ORDERED_DRUGS`
--
ALTER TABLE `ORDERED_DRUGS`
  ADD CONSTRAINT `Fulfilled_From` FOREIGN KEY (`drug_name`,`batch_number`) REFERENCES `Medicine` (`drug_name`, `batch_number`),
  ADD CONSTRAINT `containss` FOREIGN KEY (`order_id`) REFERENCES `Orders` (`order_id`) ON DELETE CASCADE;

--
-- Constraints for table `Orders`
--
ALTER TABLE `Orders`
  ADD CONSTRAINT `prepares` FOREIGN KEY (`EmployeeID`) REFERENCES `Employee` (`ID`),
  ADD CONSTRAINT `uses` FOREIGN KEY (`prescription_id`) REFERENCES `Prescription` (`prescription_id`);

--
-- Constraints for table `PRESCRIBED_DRUGS`
--
ALTER TABLE `PRESCRIBED_DRUGS`
  ADD CONSTRAINT `consists_of` FOREIGN KEY (`prescription_id`) REFERENCES `Prescription` (`prescription_id`) ON DELETE CASCADE;

--
-- Constraints for table `Prescription`
--
ALTER TABLE `Prescription`
  ADD CONSTRAINT `holds` FOREIGN KEY (`Aadhaar`) REFERENCES `Customer` (`Aadhaar`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
