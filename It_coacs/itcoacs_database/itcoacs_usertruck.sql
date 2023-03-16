CREATE DATABASE  IF NOT EXISTS `itcoacs` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `itcoacs`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: itcoacs
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `usertruck`
--

DROP TABLE IF EXISTS `usertruck`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usertruck` (
  `usertruck_id` int NOT NULL AUTO_INCREMENT,
  `user_idd` int DEFAULT NULL,
  `user_name` varchar(50) DEFAULT NULL,
  `truckbrands` int DEFAULT NULL,
  `truckmodel` int DEFAULT NULL,
  `truckmodeltype` int DEFAULT NULL,
  `truckyear` int DEFAULT NULL,
  `wheeldrive` int DEFAULT NULL,
  `km` int DEFAULT NULL,
  `transportcapasity` char(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `passengercapasity` int DEFAULT NULL,
  `wheelpercent` int DEFAULT NULL,
  `fueltype` varchar(55) DEFAULT NULL,
  `licence_plate` varchar(55) DEFAULT NULL,
  PRIMARY KEY (`usertruck_id`),
  KEY `user_idd` (`user_idd`),
  CONSTRAINT `usertruck_ibfk_1` FOREIGN KEY (`user_idd`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usertruck`
--

LOCK TABLES `usertruck` WRITE;
/*!40000 ALTER TABLE `usertruck` DISABLE KEYS */;
INSERT INTO `usertruck` VALUES (3,3,'ahm123',2,4,6,2,2,200,'100000',2,80,'Benzin+LPG','26BBBB26'),(4,3,'ahm123',3,6,9,3,3,1,'1',1,80,'Benzin','26BBBB26');
/*!40000 ALTER TABLE `usertruck` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-16 23:56:52
