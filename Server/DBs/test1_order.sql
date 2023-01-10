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
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order` (
  `orderID` int NOT NULL,
  `userName` varchar(45) NOT NULL,
  `orderTime` time DEFAULT NULL,
  `arrivalTime` time DEFAULT NULL,
  `delivFee` decimal(6,0) NOT NULL,
  `driverID` int DEFAULT NULL,
  `orderDate` date DEFAULT NULL,
  PRIMARY KEY (`orderID`),
  KEY `driverID_idx` (`driverID`),
  KEY `userNAME1_idx` (`userName`),
  CONSTRAINT `driverID` FOREIGN KEY (`driverID`) REFERENCES `driver` (`driverID`),
  CONSTRAINT `userNAME1` FOREIGN KEY (`userName`) REFERENCES `customer` (`userName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
INSERT INTO `order` VALUES (1,'Anthony999',NULL,NULL,30000,NULL,NULL),(2,'KaremK','04:22:13','05:01:05',30000,3,'2022-12-14'),(3,'MohamadF','02:45:57','03:17:35',30000,1,'2022-12-14'),(4,'KaremK','05:10:10','05:50:55',30000,1,'2022-12-14'),(5,'RolaK','01:20:30','11:55:12',30000,1,'2022-12-14'),(6,'KaremK','02:25:20','02:57:42',30000,3,'2022-12-14'),(7,'Anthony999','02:20:21','02:55:12',30000,2,'2022-12-14'),(8,'NaderCh','06:01:03','06:38:15',30000,2,'2022-12-14'),(9,'KaremK','06:20:04','06:59:27',30000,3,'2022-12-14');
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-19  6:12:28
