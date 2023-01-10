-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: test1
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts`
--

DROP TABLE IF EXISTS `accounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts` (
  `accID` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `passWords` varchar(45) NOT NULL,
  `phoneNumber` varchar(15) NOT NULL,
  PRIMARY KEY (`accID`),
  UNIQUE KEY `phoneNumber_UNIQUE` (`phoneNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts`
--

LOCK TABLES `accounts` WRITE;
/*!40000 ALTER TABLE `accounts` DISABLE KEYS */;
INSERT INTO `accounts` VALUES ('Anthony\'s','Anthony.10@gmail.com','A179tony','09638938'),('Anthony99','toxorn999@gmail.com','123','816464'),('Anthony999','anthony.tannous999@gmail.com','123','81646453'),('Burger King','burgerking@gmail.com','WhoTFisMacDonalds','1525'),('Hawa Chicken','hawachicken@gmail.com','WeMadeMalakElTawouk','1520'),('KaremK','Karemkhadd@hotmail.com','Therage3','71795975'),('KFC','KFC.@gmail.com','KFC123','1277'),('Malak el Tawouk','malakeltawouk@gmail.com','TheOnlyMalak','1592'),('McDonald\'s','Mcdo.1@gmail.com','Mcdo3217','1297'),('MohamadF','Mohamadfares@gmail.com','theWhite4','03021133'),('NaderCh','naderchanaa@hotmail.com','naderChanaa3','76678899'),('Pizza Hut','pizzahut@gmail.com','WeMissedLebanonSoMuch','01514008'),('RolaK','rolakaouk@gmail.com','rol2rolR','71177117'),('Tonino','tonino@gmail.com','tonino4life','01845502');
/*!40000 ALTER TABLE `accounts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-19  6:12:27
