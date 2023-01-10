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
-- Table structure for table `hascombo`
--

DROP TABLE IF EXISTS `hascombo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hascombo` (
  `itemID` int NOT NULL,
  `comboID` int NOT NULL,
  PRIMARY KEY (`itemID`,`comboID`),
  KEY `comboID1_idx` (`comboID`),
  CONSTRAINT `comboID1` FOREIGN KEY (`comboID`) REFERENCES `combo` (`comboID`),
  CONSTRAINT `ITEMID76` FOREIGN KEY (`itemID`) REFERENCES `item` (`itemID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hascombo`
--

LOCK TABLES `hascombo` WRITE;
/*!40000 ALTER TABLE `hascombo` DISABLE KEYS */;
INSERT INTO `hascombo` VALUES (1,1),(2,1),(3,1),(4,1),(5,1),(7,1),(8,1),(9,1),(10,1),(11,1),(12,1),(13,1),(17,1),(18,1),(19,1),(20,1),(21,1),(25,1),(30,1),(31,1),(32,1),(35,1),(36,1),(37,1),(38,1),(39,1),(41,1),(42,1),(43,1),(44,1),(47,1),(48,1),(1,2),(2,2),(3,2),(4,2),(5,2),(7,2),(8,2),(9,2),(10,2),(11,2),(12,2),(13,2),(17,2),(18,2),(19,2),(20,2),(21,2),(25,2),(30,2),(31,2),(32,2),(35,2),(36,2),(37,2),(38,2),(39,2),(41,2),(42,2),(43,2),(44,2),(47,2),(48,2),(51,2),(52,2),(1,3),(2,3),(3,3),(4,3),(5,3),(7,3),(8,3),(9,3),(10,3),(11,3),(12,3),(13,3),(17,3),(18,3),(19,3),(20,3),(21,3),(25,3),(30,3),(31,3),(32,3),(35,3),(36,3),(37,3),(38,3),(39,3),(41,3),(42,3),(43,3),(44,3),(47,3),(48,3);
/*!40000 ALTER TABLE `hascombo` ENABLE KEYS */;
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
