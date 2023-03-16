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
-- Table structure for table `truckmodel`
--

DROP TABLE IF EXISTS `truckmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `truckmodel` (
  `marka_id` int DEFAULT NULL,
  `modelid` int NOT NULL,
  `model` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  PRIMARY KEY (`modelid`),
  KEY `marka_id` (`marka_id`),
  CONSTRAINT `FK_tırmodel_markaid` FOREIGN KEY (`marka_id`) REFERENCES `truckbrands` (`markaid`),
  CONSTRAINT `truckmodel_ibfk_1` FOREIGN KEY (`marka_id`) REFERENCES `truckbrands` (`markaid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `truckmodel`
--

LOCK TABLES `truckmodel` WRITE;
/*!40000 ALTER TABLE `truckmodel` DISABLE KEYS */;
INSERT INTO `truckmodel` VALUES (1,1,'AS'),(1,2,'Fargo'),(2,3,'Pro'),(2,4,'Tuğra'),(3,5,'105'),(3,6,'ATI'),(3,7,'CF'),(4,8,'Fiat'),(5,9,'Cargo'),(5,10,'Diğerleri'),(5,11,'F-Max'),(6,12,'Euro Star'),(6,13,'Eurotech'),(6,14,'Stralis'),(6,15,'S-way'),(6,16,'Trakker'),(6,17,'Turbostar'),(7,18,'K-125 CR'),(8,19,'Diğerleri'),(9,20,'26 230'),(9,21,'26 270'),(9,22,'26 281'),(9,23,'26 321'),(9,24,'33 372'),(9,25,'33 423'),(9,26,'F2000'),(9,27,'TGA'),(9,28,'TGS'),(9,29,'TGX'),(9,30,'Others'),(10,31,'Actros'),(10,32,'Arocs'),(10,33,'Axor'),(11,34,'C 460'),(11,35,'D Wide'),(11,36,'Magnum'),(11,37,'Premium'),(11,38,'R'),(11,39,'T'),(12,40,'G'),(12,41,'H'),(12,42,'L'),(12,43,'M'),(12,44,'P'),(12,45,'R'),(12,46,'S'),(12,47,'Diğerleri'),(13,48,'F'),(13,49,'FH'),(13,50,'FM'),(13,51,'N');
/*!40000 ALTER TABLE `truckmodel` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-16 23:56:53
