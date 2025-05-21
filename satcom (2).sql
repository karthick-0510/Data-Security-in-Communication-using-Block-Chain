-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 02, 2024 at 05:58 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `satcom`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `uname` varchar(10) NOT NULL,
  `password` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--


-- --------------------------------------------------------

--
-- Table structure for table `datablock`
--

CREATE TABLE `datablock` (
  `id` int(10) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `maddress` varchar(100) NOT NULL,
  `fname` varchar(100) NOT NULL,
  `b1` varchar(1000) NOT NULL,
  `b2` varchar(1000) NOT NULL,
  `status` varchar(50) NOT NULL,
  `date` varchar(10) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=21 ;

--
-- Dumping data for table `datablock`
--

INSERT INTO `datablock` (`id`, `name`, `maddress`, `fname`, `b1`, `b2`, `status`, `date`) VALUES
(1, 'sundar', 'A0-36-BC-26-CD-ED', 'Placement_Data_Full_Class.csv', '0', 'b59774f08375c35879286e833a5be36dc45724c8', '', ''),
(2, 'sundar', 'A0-36-BC-26-CD-ED', 'Placement_Data_Full_Class.csv', '0', 'b59774f08375c35879286e833a5be36dc45724c8', 'Attack Found', ''),
(3, 'sundar', 'A0-36-BC-26-CD-ED', 'Placement_Data_Full_Class.csv', 'b59774f08375c35879286e833a5be36dc45724c8', 'b59774f08375c35879286e833a5be36dc45724c8', 'Attack Found', ''),
(4, 'sundar', 'A0-36-BC-26-CD-ED', 'Placement_Data_Full_Class.csv', 'b59774f08375c35879286e833a5be36dc45724c8', 'b59774f08375c35879286e833a5be36dc45724c8', '', ''),
(5, 'sundar', 'A0-36-BC-26-CD-ED', 'Placement_Data_Full_Class.csv', 'b59774f08375c35879286e833a5be36dc45724c8', 'b59774f08375c35879286e833a5be36dc45724c8', '', ''),
(6, 'sundar', 'A0-36-BC-26-CD-ED', 'Placement_Data_Full_Class.csv', 'b59774f08375c35879286e833a5be36dc45724c8', 'b59774f08375c35879286e833a5be36dc45724c8', '', ''),
(7, 'sundar', 'A0-36-BC-26-CD-ED', 'Placement_Data_Full_Class.csv', 'b59774f08375c35879286e833a5be36dc45724c8', 'b59774f08375c35879286e833a5be36dc45724c8', '', ''),
(8, 'sundar', 'A0-36-BC-26-CD-ED', 'Placement_Data_Full_Class.csv', 'b59774f08375c35879286e833a5be36dc45724c8', 'b59774f08375c35879286e833a5be36dc45724c8', '', ''),
(9, 'sundar', 'A0-36-BC-26-CD-ED', 'Placement_Data_Full_Class.csv', 'b59774f08375c35879286e833a5be36dc45724c8', 'b59774f08375c35879286e833a5be36dc45724c8', '', ''),
(10, 'sundar', 'A0-36-BC-26-CD-ED', 'Placement_Data_Full_Class.csv', 'b59774f08375c35879286e833a5be36dc45724c8', 'b59774f08375c35879286e833a5be36dc45724c8', '', ''),
(11, 'sundar', 'A0-36-BC-26-CD-ED', '1facedb.sql', 'b59774f08375c35879286e833a5be36dc45724c8', 'c374d64ba6aa487428ee79c54d68f43231fbf772', '', ''),
(12, 'sundar', 'A0-36-BC-26-CD-ED', '1facedb.sql', 'c374d64ba6aa487428ee79c54d68f43231fbf772', 'c374d64ba6aa487428ee79c54d68f43231fbf772', '', ''),
(13, 'sundar', 'A0-36-BC-26-CD-ED', '1facedb.sql', 'c374d64ba6aa487428ee79c54d68f43231fbf772', 'c374d64ba6aa487428ee79c54d68f43231fbf772', 'Attack Found', ''),
(14, 'sundar', 'A0-36-BC-26-CD-ED', '1facedb.sql', 'c374d64ba6aa487428ee79c54d68f43231fbf772', 'c374d64ba6aa487428ee79c54d68f43231fbf772', 'Attack Found', ''),
(15, 'sundar', 'A0-36-BC-26-CD-ED', '1facedb.sql', 'c374d64ba6aa487428ee79c54d68f43231fbf772', 'c374d64ba6aa487428ee79c54d68f43231fbf772', 'Attack Found', ''),
(16, 'sundar', 'A0-36-BC-26-CD-ED', 'Placement_Data_Full_Class.csv', 'c374d64ba6aa487428ee79c54d68f43231fbf772', 'b59774f08375c35879286e833a5be36dc45724c8', 'Attack Found', '2024-03-13'),
(17, 'sundar', 'A0-36-BC-26-CD-ED', 'Placement_Data_Full_Class.csv', 'b59774f08375c35879286e833a5be36dc45724c8', 'b59774f08375c35879286e833a5be36dc45724c8', '', '2024-03-13'),
(18, 'sundar', 'A0-36-BC-26-CD-ED', '1facedb.sql', 'b59774f08375c35879286e833a5be36dc45724c8', 'c374d64ba6aa487428ee79c54d68f43231fbf772', '', '2024-03-13'),
(19, 'sundar', 'A0-36-BC-26-CD-ED', 'Placement_Data_Full_Class.csv', 'c374d64ba6aa487428ee79c54d68f43231fbf772', 'b59774f08375c35879286e833a5be36dc45724c8', 'Attack Found', '2024-03-13'),
(20, 'sundar', 'A0-36-BC-26-CD-ED', 'main_animal_detection.py', 'b59774f08375c35879286e833a5be36dc45724c8', 'ea426fd9a52a6b0f44c4352e3bee190faf5f07aa', '', '2024-04-11');

-- --------------------------------------------------------

--
-- Table structure for table `newdata`
--

CREATE TABLE `newdata` (
  `id` int(50) NOT NULL auto_increment,
  `sno` varchar(50) NOT NULL,
  `file` varchar(50) NOT NULL,
  `details` varchar(100) NOT NULL,
  `b0` varchar(1000) NOT NULL,
  `b1` varchar(1000) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `newdata`
--

INSERT INTO `newdata` (`id`, `sno`, `file`, `details`, `b0`, `b1`) VALUES
(1, 's1', 'Placement_Data_Full_Class.csv', 'sample', '0', '9733ddfdc3815933670750285ada870f9693e4fa'),
(2, 's1', '1facedb.sql', 'test', '0', 'be8c8433157794cf09f6a948cf185b7ca525526a'),
(3, '1', 'main_animal_detection.py', 'sample', '0', 'eb64408d164d67b9ffa6eefda9528258c0550548');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `id` int(50) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `maddress` varchar(100) NOT NULL,
  `uname` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `sno` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`id`, `name`, `phone`, `email`, `maddress`, `uname`, `password`, `sno`) VALUES
(1, 'sundar', '7904461600', 'sundarv06@gmail.com', 'A0-36-BC-26-CD-ED', 'sundar', '1234', 's1'),
(2, 'sundar', '9840234119', 'sundarv06@gmail.com', 'A0-36-BC-26-CD-ED', 's123', 's123', '1');

-- --------------------------------------------------------

--
-- Table structure for table `satelliteinfo`
--

CREATE TABLE `satelliteinfo` (
  `id` int(10) NOT NULL auto_increment,
  `sno` varchar(10) NOT NULL,
  `sname` varchar(50) NOT NULL,
  `saddress` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `satelliteinfo`
--

INSERT INTO `satelliteinfo` (`id`, `sno`, `sname`, `saddress`) VALUES
(1, 's1', 'sample', 'A0-36-BC-26-CD-EJ'),
(2, '3', 'sundar', 'A0-36-BC-26-CD-EJ'),
(3, '1', 'sample', 'A0-36-BC-26-CD-ED');
