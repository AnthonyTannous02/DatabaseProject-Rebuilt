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
-- Table structure for table `hasoption`
--

DROP TABLE IF EXISTS `hasoption`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hasoption` (
  `optionID` int NOT NULL,
  `itemID` int NOT NULL,
  PRIMARY KEY (`optionID`,`itemID`),
  KEY `IETMID_idx` (`itemID`),
  CONSTRAINT `IETMID` FOREIGN KEY (`itemID`) REFERENCES `item` (`itemID`),
  CONSTRAINT `optionID11` FOREIGN KEY (`optionID`) REFERENCES `option` (`optionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hasoption`
--

LOCK TABLES `hasoption` WRITE;
/*!40000 ALTER TABLE `hasoption` DISABLE KEYS */;
INSERT INTO `hasoption` VALUES (1,1),(1,2),(1,3),(3,4),(4,6),(1,7),(2,7),(1,8),(4,8),(2,9),(7,10),(1,11),(2,11),(3,11),(2,13),(3,13),(2,17),(3,17),(4,17),(2,18),(7,18),(2,19),(4,19),(5,19),(2,20),(3,20),(4,20),(4,21),(7,21),(6,25),(2,29),(4,29),(2,30),(4,30),(2,31),(2,32),(4,32),(1,35),(6,35),(1,36),(1,38),(6,38),(7,38),(1,39),(6,39),(7,41),(7,42),(2,43),(2,44),(3,44),(7,44),(3,48),(4,48),(8,48);
/*!40000 ALTER TABLE `hasoption` ENABLE KEYS */;
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
