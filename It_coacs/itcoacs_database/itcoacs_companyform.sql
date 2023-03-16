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
-- Table structure for table `companyform`
--

DROP TABLE IF EXISTS `companyform`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `companyform` (
  `companyid` int NOT NULL AUTO_INCREMENT,
  `companyname` varchar(100) DEFAULT NULL,
  `companydescription` varchar(100) DEFAULT NULL,
  `companytypelegally` varchar(100) DEFAULT NULL,
  `companytypefunctionally` varchar(100) DEFAULT NULL,
  `companyaddress` varchar(100) DEFAULT NULL,
  `companyphone` bigint DEFAULT NULL,
  `companyemail` varchar(100) DEFAULT NULL,
  `companywebsite` varchar(100) DEFAULT NULL,
  `companylinkedin` varchar(100) DEFAULT NULL,
  `companyfacebook` varchar(100) DEFAULT NULL,
  `companytwitter` varchar(100) DEFAULT NULL,
  `companyinstagram` varchar(100) DEFAULT NULL,
  `companyyoutube` varchar(100) DEFAULT NULL,
  `companygoogleplus` varchar(100) DEFAULT NULL,
  `companytaxnumber` bigint DEFAULT NULL,
  `companytaxoffice` varchar(100) DEFAULT NULL,
  `companytaxadmin` varchar(100) DEFAULT NULL,
  `companytaxadminphone` bigint DEFAULT NULL,
  `companytaxadmineposta` varchar(100) DEFAULT NULL,
  `companytaxadminaddress` varchar(100) DEFAULT NULL,
  `companytaxadminidentitynumber` bigint DEFAULT NULL,
  `companytaxadminidentitydate` date DEFAULT NULL,
  `companytaxadminidentityplace` varchar(100) DEFAULT NULL,
  `companycurrency` varchar(100) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`companyid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `companyform`
--

LOCK TABLES `companyform` WRITE;
/*!40000 ALTER TABLE `companyform` DISABLE KEYS */;
INSERT INTO `companyform` VALUES (1,'Eskişehir Un','Eskişehir un fabrikası','komanditsirket','tarımisletmeleri','Eskişehir Türkiye',2221,'esesun@gmail.com','esesun.com','esesun','esesun','esesun','esesun','esesun','esesun',4445,'esesuneses','esesuneses',2222222,'esesun@gmail.com','esesuneseses',222222,'2023-02-24','esesuneses','euro','Ali123');
/*!40000 ALTER TABLE `companyform` ENABLE KEYS */;
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
