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
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item` (
  `itemID` int NOT NULL,
  `restName` varchar(45) NOT NULL,
  `itemName` varchar(45) NOT NULL,
  `itemDesc` varchar(255) NOT NULL,
  `subCategory` varchar(45) NOT NULL,
  `price` varchar(45) NOT NULL,
  PRIMARY KEY (`itemID`),
  KEY `restName123_idx` (`restName`),
  CONSTRAINT `restName123` FOREIGN KEY (`restName`) REFERENCES `restaurant` (`restName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item`
--

LOCK TABLES `item` WRITE;
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` VALUES (1,'Malak el Tawouk','Tawouk Sandwich','Tawouk sandwich, medium, with pickles','Sandwich','110000'),(2,'Hawa Chicken','Chicken Sandwich','Chicken sandwich, with pickles','Sandwich','105000'),(3,'Burger King','Chicken Burger','Burger with onions and pickles','Burger','150000'),(4,'Burger King','Double CheeseBurger','Cheese Burger with onions and pickles','Burger','180000'),(5,'Pizza Hut','Vegeterian Pizza','Pizza with vegetables','Pizza','200000'),(6,'Tonino','Nutella Kinder crepe','Crepe with nutella, kinder and brown chocolate','Dessert','900000'),(7,'Anthony\'s','Chicken Mozzarella Affair','A choice of grilled or fried chicken, breaded mozzarella, garlic mayo,pickles,lettuce and tomato','Burger','195000'),(8,'Anthony\'s','Chicky Swiss','Grilled chicken breast dipped in melted swiss cheese, sriracha mayo sauce,lollo verde, and pickles','Burger','172000'),(9,'Anthony\'s','Anthony\'s Burger','Beef patty, Smoked turkey, Pepperoni, Swiss Cheese,Lettuce and Tomato','Burger','176000'),(10,'Anthony\'s','BBQ Burger','Beef patty, BBQ mayo sauce, Cheddar cheese, Bacon, and Grilled onions','Burger','178000'),(11,'Anthony\'s','Dilly Chick','Grilled chicken breast, cheddar, BBQ mayo sauce, pickles, lettuce and onions','Sandwich','240000'),(12,'Anthony\'s','Chicken Avocado','Grilled chicken breast, Rocket leaves, and Brown baguette','Sandwich','194000'),(13,'Anthony\'s','Chicken Fajita','Marinated chicken breast, Mexican sauce, Onions, Lettuce, and Sub bread','Sandwich','210000'),(17,'Burger King','Whopper Jr. Meal','Flame Grilled 100% Beef Patty, Crispy Lettuce, Fresh Onions, Fresh Tomatoes.','Burger','175000'),(18,'Burger King','King Chicken Fillet Steakhouse','Chicken Breast Fillet, Crispy Lettuce, Mayo, Cheese, Beef Bacon and BBQ','Burger','235000'),(19,'Burger King','Lite Chicken Whopper','Grilled Chicken Breast, Lettuce, Lite Mayonnaise, and Tomatoes','Burger','195000'),(20,'Burger King','Lite Whopper','Flame Grilled Beed, Crispy Lettuce, Fresh Onions, Fresh Tomatoes and pickles','Burger','195000'),(21,'Burger King','Chicken Royale Steakhouse','Breaded Chicken Breast,2 Cheese Slices, 4 Beef Bacon, and Tomata','Sandwich','225000'),(25,'Hawa Chicken','Taouk Sandwich','Fresh Chicken Taouk, Pickles, Garlic, and Coleslow','Sandwich','140000'),(29,'Hawa Chicken','Chicken Sandwich','Original taste of chicken with tomato, and lettuce','Sandwich','160000'),(30,'KFC','Spicy Twister Sandwich','Spicy Crispy Strips (2 Pcs) , Lettuce and Toamato','Sandwich','130000'),(31,'KFC','Spicy Zinger Fillet Sandwich','Spicy Chicken Fillet, Mayo and Lettuce','Sandwich','150000'),(32,'KFC','Chicken Fillet Sandwich','Original Chicken Fillet, Mayo, Lettuce and Tomato','Sandwich','150000'),(35,'Malak el Tawouk','Escalop Sandwich','Crispy chicken, garlic mayo, iceberg, and pickles','Sandwich','125000'),(36,'Malak el Tawouk','Special Tawouk Sandwich','Marinated chicken breast,cheese,turkey,garlic,coleslaw and pickles','Sandwich','180000'),(37,'Malak el Tawouk','Soujouk Sandwich','soujouk, tomatoes, pickles and fries /23 CM','Sandwich','90000'),(38,'Malak el Tawouk','Chicken Burger Extra Kbir','Two grilled chicken breasts, cheese, turkey, garlic mayo, fries, and pickles','Burger','260000'),(39,'Malak el Tawouk','Burger Extra Kbir','Two grilled beef burger patties, cheese, turkey, garlic mayo, fries, and pickles','Burger','260000'),(41,'McDonald\'s','Chicken Mushroom Burger','grand chicken patty, mayo pepper and emmental cheese','Burger','250000'),(42,'McDonald\'s','Beef Mushroom Burger','two beef patty, mayo pepperand emmental cheese','Burger','250000'),(43,'McDonald\'s','Big Mac Burger','two hamburger patties, lettuce, pickles with big mac sauce','Burger','180000'),(44,'McDonald\'s','Big Tasty Burger','big tasty patty, lettuce, fresh onion, and two emmental cheese','Burger','230000'),(47,'Pizza hut','Small Plain Pizza','With two layers of Cheese','Pizza','210000'),(48,'Pizza hut','Small Vegetarian Pizza','green pepper, onions, sweet corn and tomatoes','Pizza','210000'),(51,'Tonino','Nutella Hersheys','Nutella with black chocolate and hercheys','Dessert','110000'),(52,'Tonino','Nutella Strawberry','Nutella with black chocolate and hercheys + strawberry','Dessert','125000');
/*!40000 ALTER TABLE `item` ENABLE KEYS */;
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
