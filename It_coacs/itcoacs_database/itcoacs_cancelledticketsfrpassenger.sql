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
-- Table structure for table `cancelledticketsfrpassenger`
--

DROP TABLE IF EXISTS `cancelledticketsfrpassenger`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cancelledticketsfrpassenger` (
  `drivername` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `passengername` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `ticket_id` int DEFAULT NULL,
  `cancelledticketsfrpassid` int NOT NULL AUTO_INCREMENT,
  `canceleddate` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`cancelledticketsfrpassid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cancelledticketsfrpassenger`
--

LOCK TABLES `cancelledticketsfrpassenger` WRITE;
/*!40000 ALTER TABLE `cancelledticketsfrpassenger` DISABLE KEYS */;
INSERT INTO `cancelledticketsfrpassenger` VALUES ('ahm123','jale123',1,1,NULL),('ahm123','jale123',2,2,NULL),('ahm123','jale123',1,3,NULL),('ahm123','jale123',6,4,'2023-01-19 11:08:13'),('ahm123','jale123',6,5,'2023-01-20 09:41:08'),('ahm123','jale123',10,6,'2023-01-26 19:58:31'),('ahm123','g1234',10,7,'2023-02-21 11:58:57');
/*!40000 ALTER TABLE `cancelledticketsfrpassenger` ENABLE KEYS */;
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
