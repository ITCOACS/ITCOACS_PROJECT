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
-- Table structure for table `canc_shippingjobfr_consignor`
--

DROP TABLE IF EXISTS `canc_shippingjobfr_consignor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `canc_shippingjobfr_consignor` (
  `canc_shippingjobfr_consignorid` int NOT NULL AUTO_INCREMENT,
  `job_id` int DEFAULT NULL,
  `drivername` varchar(100) DEFAULT NULL,
  `consignorname` varchar(100) DEFAULT NULL,
  `cancelleddate` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`canc_shippingjobfr_consignorid`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `canc_shippingjobfr_consignor`
--

LOCK TABLES `canc_shippingjobfr_consignor` WRITE;
/*!40000 ALTER TABLE `canc_shippingjobfr_consignor` DISABLE KEYS */;
INSERT INTO `canc_shippingjobfr_consignor` VALUES (1,12,'ahm123','Ali123','2023-02-20 12:29:04'),(2,13,'ahm123','Ali123','2023-02-20 12:33:05'),(3,12,'Ali123','Ali123','2023-02-20 13:26:58'),(4,12,'Ali123','Ali123','2023-02-20 13:27:25'),(5,12,'Ali123','Ali123','2023-02-20 13:27:31'),(6,12,'Ali123','Ali123','2023-02-20 13:28:14'),(7,12,'Ali123','Ali123','2023-02-20 13:28:21'),(8,13,'Ali123','Ali123','2023-02-20 13:28:27'),(9,13,'Ali123','Ali123','2023-02-20 13:28:32'),(10,12,'Ali123','Ali123','2023-02-20 13:35:20'),(11,12,'Ali123','Ali123','2023-02-20 13:37:43'),(12,12,'Ali123','Ali123','2023-02-20 13:41:11'),(13,12,'Ali123','Ali123','2023-02-20 13:44:24'),(14,13,'Ali123','Ali123','2023-02-20 19:27:01'),(15,14,'ahm123','Ali123','2023-02-20 19:39:19'),(16,14,'-','Ali123','2023-02-20 19:41:26'),(17,15,'ahm123','Ali123','2023-02-20 19:42:24'),(18,15,'-','Ali123','2023-02-20 19:42:29');
/*!40000 ALTER TABLE `canc_shippingjobfr_consignor` ENABLE KEYS */;
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
