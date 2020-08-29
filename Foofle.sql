-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 19, 2020 at 10:30 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Foofle`
--

-- --------------------------------------------------------

--
-- Table structure for table `BlockedUsers`
--

CREATE TABLE `BlockedUsers` (
  `username` varchar(15) NOT NULL,
  `blocked` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `BlockedUsers`
--

INSERT INTO `BlockedUsers` (`username`, `blocked`) VALUES
('ghazal77', 'sadaf22');

-- --------------------------------------------------------

--
-- Table structure for table `Email`
--

CREATE TABLE `Email` (
  `Sender` varchar(30) NOT NULL,
  `Subject` varchar(100) NOT NULL,
  `SentTime` datetime NOT NULL,
  `Content` varchar(512) NOT NULL,
  `ID` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Email`
--

INSERT INTO `Email` (`Sender`, `Subject`, `SentTime`, `Content`, `ID`) VALUES
('ghazal77', 'welcome', '2020-05-28 16:55:50', 'welcome to my Foofle project :D', 21),
('vahid44', 'new email', '2020-06-17 17:09:56', 'hello guys:D ))))))))))))))))))))))', 25);

--
-- Triggers `Email`
--
DELIMITER $$
CREATE TRIGGER `afterSendEmail` AFTER INSERT ON `Email` FOR EACH ROW BEGIN
INSERT INTO EmailForUser
	VALUES (new.ID,new.Sender,'1');

END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `EmailForUser`
--

CREATE TABLE `EmailForUser` (
  `ID` int(5) NOT NULL,
  `User` varchar(30) NOT NULL,
  `SenderOrReceiver` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `EmailForUser`
--

INSERT INTO `EmailForUser` (`ID`, `User`, `SenderOrReceiver`) VALUES
(21, 'ghazal77', '1'),
(21, 'sadaf22', '0'),
(21, 'soheila47', '0'),
(21, 'vahid44', '0'),
(25, 'ghazal77', '0'),
(25, 'vahid44', '1');

--
-- Triggers `EmailForUser`
--
DELIMITER $$
CREATE TRIGGER `afterDeleteAnEmail` AFTER DELETE ON `EmailForUser` FOR EACH ROW BEGIN
INSERT INTO Notification
	VALUES (NOW(),"Deletion of selected Email was Successful",old.User);
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `Login`
--

CREATE TABLE `Login` (
  `Time` datetime NOT NULL,
  `User` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Login`
--

INSERT INTO `Login` (`Time`, `User`) VALUES
('2020-06-10 18:39:25', 'vahid44');

--
-- Triggers `Login`
--
DELIMITER $$
CREATE TRIGGER `AddToLoginTable` AFTER INSERT ON `Login` FOR EACH ROW BEGIN
   INSERT INTO Notification
	VALUES (now(),"Successful \tLogin!",new.User);
    END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `Notification`
--

CREATE TABLE `Notification` (
  `Time` datetime NOT NULL,
  `Content` varchar(512) NOT NULL,
  `Owner` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Notification`
--

INSERT INTO `Notification` (`Time`, `Content`, `Owner`) VALUES
('2020-05-28 16:50:54', 'Successful Signup!', 'ghazal77'),
('2020-05-28 16:51:59', 'Successful Signup!', 'sadaf22'),
('2020-05-28 16:53:06', 'Successful Signup!', 'soheila47'),
('2020-05-28 16:54:31', 'Successful Signup!', 'vahid44'),
('2020-05-28 16:54:44', 'Successful 	Login!', 'ghazal77'),
('2020-05-28 16:55:50', 'new Email!', 'sadaf22'),
('2020-05-28 16:55:50', 'new Email!', 'soheila47'),
('2020-05-28 16:55:50', 'new Email!', 'vahid44'),
('2020-05-28 16:57:07', 'ghazal77 who has access to your profile,requested for getting your personal information', 'soheila47'),
('2020-05-28 16:57:17', 'ghazal77 who doesn\'t have access to your profile,requested for getting your personal information', 'sadaf22'),
('2020-05-28 16:58:03', 'Successful 	Login!', 'sadaf22'),
('2020-05-28 17:00:21', 'sadaf22 who doesn\'t have access to your profile,requested for getting your personal information', 'ghazal77'),
('2020-05-28 17:02:27', 'profile editted', 'sadaf22'),
('2020-06-10 18:04:29', 'new Email!', 'ghazal77'),
('2020-06-10 18:04:29', 'new Email!', 'vahid44'),
('2020-06-10 18:38:45', 'ghazal77 who doesn\'t have access to your profile,requested for getting your personal information', 'sadaf22'),
('2020-06-10 18:38:54', 'Successful 	Login!', 'sadaf22'),
('2020-06-10 18:39:12', 'ghazal77 who has access to your profile,requested for getting your personal information', 'sadaf22'),
('2020-06-10 18:39:25', 'Successful 	Login!', 'vahid44'),
('2020-06-10 18:39:31', 'vahid44 who doesn\'t have access to your profile,requested for getting your personal information', 'sadaf22'),
('2020-06-10 18:39:39', 'vahid44 who has access to your profile,requested for getting your personal information', 'ghazal77'),
('2020-06-12 13:57:17', 'Successful Signup!', 'usertest22'),
('2020-06-12 14:38:46', 'Successful Signup!', 'arshida11'),
('2020-06-17 13:57:23', 'Successful 	Login!', 'ghazal77'),
('2020-06-17 15:08:15', 'ghazal77 who doesn\'t have access to your profile,requested for getting your personal information', 'usertest22'),
('2020-06-17 15:12:34', 'profile editted', 'ghazal77'),
('2020-06-17 16:23:31', 'ghazal77 who has access to your profile,requested for getting your personal information', 'sadaf22'),
('2020-06-17 16:34:32', 'vahid44 who has access to your profile,requested for getting your personal information', 'ghazal77'),
('2020-06-17 17:09:56', 'new Email!', 'ghazal77'),
('2020-06-17 17:13:58', 'vahid44 who has access to your profile,requested for getting your personal information', 'ghazal77'),
('2020-06-17 17:19:27', 'profile editted', 'vahid44');

-- --------------------------------------------------------

--
-- Table structure for table `PermittedUsers`
--

CREATE TABLE `PermittedUsers` (
  `username` varchar(15) NOT NULL,
  `permitted` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `PermittedUsers`
--

INSERT INTO `PermittedUsers` (`username`, `permitted`) VALUES
('sadaf22', 'ghazal77');

-- --------------------------------------------------------

--
-- Table structure for table `PersonalInfo`
--

CREATE TABLE `PersonalInfo` (
  `Address` varchar(512) DEFAULT NULL,
  `FirstName` varchar(15) DEFAULT NULL,
  `Surname` varchar(15) DEFAULT NULL,
  `Mobile` varchar(15) DEFAULT NULL,
  `BirthDate` date DEFAULT NULL,
  `Alias` varchar(15) DEFAULT NULL,
  `Username` varchar(15) NOT NULL,
  `AccessPermission` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `PersonalInfo`
--

INSERT INTO `PersonalInfo` (`Address`, `FirstName`, `Surname`, `Mobile`, `BirthDate`, `Alias`, `Username`, `AccessPermission`) VALUES
('vanak', 'arshida', 'sadeghi', '02178351', '1387-03-02', 'arshid', 'arshida11', 1),
('saadatabad-arista', 'ghazal', 'sad', '0278915238', '1377-04-01', 'gg', 'ghazal77', 1),
('shahrak egharb-zarafshan', 'sadaf', 'sdn', '0925914', '1377-04-01', 'sadaf--', 'sadaf22', 0),
('saadatabad, 24 metri', 'soheila', 'key', '02514893', '1347-03-01', 's.key', 'soheila47', 1),
('vanak', 'user', 'test', '0012477', '1374-09-06', 'user', 'usertest22', 0),
('saadat abad- sarv e sharghi', 'vahid', 'sadeghi', '027915e', '1344-09-28', 'vahid...sdn', 'vahid44', 1);

--
-- Triggers `PersonalInfo`
--
DELIMITER $$
CREATE TRIGGER `editPersonalInfo` AFTER UPDATE ON `PersonalInfo` FOR EACH ROW BEGIN
INSERT INTO Notification
	VALUES (NOW(),"profile editted",new.Username);
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `Reciever`
--

CREATE TABLE `Reciever` (
  `UserR` varchar(15) NOT NULL,
  `ID` int(4) NOT NULL,
  `State` varchar(1) NOT NULL DEFAULT '0',
  `receiverID` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Reciever`
--

INSERT INTO `Reciever` (`UserR`, `ID`, `State`, `receiverID`) VALUES
('vahid44', 21, '1', 34),
('sadaf22', 21, '1', 35),
('soheila47', 21, '0', 36),
('ghazal77', 25, '0', 39);

--
-- Triggers `Reciever`
--
DELIMITER $$
CREATE TRIGGER `AfterReceivingEmail` AFTER INSERT ON `Reciever` FOR EACH ROW BEGIN
INSERT INTO Notification
	VALUES (NOW(),"new Email!",new.UserR);
INSERT INTO EmailForUser
	VALUES (new.ID,new.UserR,'0');
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `StateCheckForReceiverInsert` BEFORE INSERT ON `Reciever` FOR EACH ROW BEGIN
    IF  new.State NOT IN ('0','1') then
        SIGNAL SQLSTATE '45000'   
        SET MESSAGE_TEXT = 'unknown state';
   
		END IF;
    
 END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `StateCheckForReceiverUpdate` BEFORE UPDATE ON `Reciever` FOR EACH ROW BEGIN
    IF  new.State NOT IN ('0','1') then
        SIGNAL SQLSTATE '45000'   
        SET MESSAGE_TEXT = 'unknown state';
   
		END IF;
    
 END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `SysInfo`
--

CREATE TABLE `SysInfo` (
  `Username` varchar(15) NOT NULL,
  `Password` varchar(42) NOT NULL,
  `DateCreated` date NOT NULL,
  `Tele` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `SysInfo`
--

INSERT INTO `SysInfo` (`Username`, `Password`, `DateCreated`, `Tele`) VALUES
('arshida11', '*CE954B05993645D4FE227A89AA14DBA30B3283CA', '2020-06-12', '718251'),
('ghazal77', '*B2F715F71755273BCAF6AAF7AC10E189CC0B98D5', '2020-05-28', '883588252'),
('sadaf22', '*FF8D82208B4B09631DA5E95E9A728E180BA85174', '2020-05-28', '177251853'),
('soheila47', '*BEEB702885A891D8241AED19DC097725606138D1', '2020-05-28', '883695138'),
('usertest22', '*1F1B2C2AC1F4153DA5B126F59D6FFBCA4F92EE2A', '2020-06-12', '77128351'),
('vahid44', '*2CA6AE2BF4D117F8B24E422F5AF91F2DA3433E53', '2020-05-28', '8828741');

--
-- Triggers `SysInfo`
--
DELIMITER $$
CREATE TRIGGER `AfterSignup` AFTER INSERT ON `SysInfo` FOR EACH ROW BEGIN
INSERT INTO Notification
	VALUES (NOW(),"Successful Signup!",new.Username);
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `BeforeSignUp` BEFORE INSERT ON `SysInfo` FOR EACH ROW BEGIN
    IF  new.Username NOT REGEXP "^[a-zA-Z0-9]{6,}$" then
        SIGNAL SQLSTATE '45000'   
        SET MESSAGE_TEXT = 'username must contain at least 6 alphanumeric characters';
   
		END IF;
    
 END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `editSysInfo` AFTER UPDATE ON `SysInfo` FOR EACH ROW BEGIN
INSERT INTO Notification
	VALUES (NOW(),"Profile editted",new.Username);
END
$$
DELIMITER ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `BlockedUsers`
--
ALTER TABLE `BlockedUsers`
  ADD PRIMARY KEY (`username`,`blocked`),
  ADD KEY `blocked` (`blocked`);

--
-- Indexes for table `Email`
--
ALTER TABLE `Email`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Sender` (`Sender`);

--
-- Indexes for table `EmailForUser`
--
ALTER TABLE `EmailForUser`
  ADD PRIMARY KEY (`ID`,`User`),
  ADD KEY `User` (`User`);

--
-- Indexes for table `Login`
--
ALTER TABLE `Login`
  ADD PRIMARY KEY (`User`);

--
-- Indexes for table `Notification`
--
ALTER TABLE `Notification`
  ADD PRIMARY KEY (`Time`,`Content`,`Owner`),
  ADD KEY `Owner` (`Owner`);

--
-- Indexes for table `PermittedUsers`
--
ALTER TABLE `PermittedUsers`
  ADD PRIMARY KEY (`username`,`permitted`),
  ADD KEY `permitted` (`permitted`);

--
-- Indexes for table `PersonalInfo`
--
ALTER TABLE `PersonalInfo`
  ADD PRIMARY KEY (`Username`),
  ADD UNIQUE KEY `Username` (`Username`);

--
-- Indexes for table `Reciever`
--
ALTER TABLE `Reciever`
  ADD PRIMARY KEY (`receiverID`),
  ADD KEY `User` (`UserR`,`ID`),
  ADD KEY `ID` (`ID`);

--
-- Indexes for table `SysInfo`
--
ALTER TABLE `SysInfo`
  ADD PRIMARY KEY (`Username`),
  ADD UNIQUE KEY `username` (`Username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Email`
--
ALTER TABLE `Email`
  MODIFY `ID` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `Reciever`
--
ALTER TABLE `Reciever`
  MODIFY `receiverID` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `BlockedUsers`
--
ALTER TABLE `BlockedUsers`
  ADD CONSTRAINT `blockedusers_ibfk_1` FOREIGN KEY (`blocked`) REFERENCES `SysInfo` (`Username`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `blockedusers_ibfk_2` FOREIGN KEY (`username`) REFERENCES `SysInfo` (`Username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Email`
--
ALTER TABLE `Email`
  ADD CONSTRAINT `email_ibfk_1` FOREIGN KEY (`Sender`) REFERENCES `SysInfo` (`Username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `EmailForUser`
--
ALTER TABLE `EmailForUser`
  ADD CONSTRAINT `EmailForUser_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `Email` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `EmailForUser_ibfk_2` FOREIGN KEY (`User`) REFERENCES `SysInfo` (`Username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Login`
--
ALTER TABLE `Login`
  ADD CONSTRAINT `Login_ibfk_1` FOREIGN KEY (`User`) REFERENCES `SysInfo` (`Username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Notification`
--
ALTER TABLE `Notification`
  ADD CONSTRAINT `Notification_ibfk_1` FOREIGN KEY (`Owner`) REFERENCES `SysInfo` (`Username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `PermittedUsers`
--
ALTER TABLE `PermittedUsers`
  ADD CONSTRAINT `permittedusers_ibfk_1` FOREIGN KEY (`permitted`) REFERENCES `SysInfo` (`Username`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `permittedusers_ibfk_2` FOREIGN KEY (`username`) REFERENCES `SysInfo` (`Username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `PersonalInfo`
--
ALTER TABLE `PersonalInfo`
  ADD CONSTRAINT `PersonalInfo_ibfk_1` FOREIGN KEY (`Username`) REFERENCES `SysInfo` (`Username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Reciever`
--
ALTER TABLE `Reciever`
  ADD CONSTRAINT `Reciever_ibfk_2` FOREIGN KEY (`UserR`) REFERENCES `SysInfo` (`Username`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Reciever_ibfk_3` FOREIGN KEY (`ID`) REFERENCES `Email` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
