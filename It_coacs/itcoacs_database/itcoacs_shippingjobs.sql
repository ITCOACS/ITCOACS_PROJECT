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
-- Table structure for table `shippingjobs`
--

DROP TABLE IF EXISTS `shippingjobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shippingjobs` (
  `jobid` int NOT NULL AUTO_INCREMENT,
  `consignor_username` varchar(100) DEFAULT NULL,
  `freightmodelid` int DEFAULT NULL,
  `freighttypeid` int DEFAULT NULL,
  `shippingstartdate` date DEFAULT NULL,
  `shippingenddate` date DEFAULT NULL,
  `shippingstartplace` varchar(100) DEFAULT NULL,
  `shippingstartplacedetailed` varchar(100) DEFAULT NULL,
  `shippingendplace` varchar(100) DEFAULT NULL,
  `shippingendplacedetailed` varchar(100) DEFAULT NULL,
  `shippingendlocationperson` varchar(100) DEFAULT NULL,
  `shippingendlocationpersonphone` varchar(100) DEFAULT NULL,
  `shippingendlocationpersonemail` varchar(100) DEFAULT NULL,
  `shippingcargo` varchar(100) DEFAULT NULL,
  `shippingcargoquantity` int DEFAULT NULL,
  `shippingcargoweight` int DEFAULT NULL,
  `shippingcargovolume` int DEFAULT NULL,
  `shippingcargounitvalue` bigint DEFAULT NULL,
  `shippingcargounitvaluecurrency` varchar(100) DEFAULT NULL,
  `shippingcargowidth` int DEFAULT NULL,
  `shippingcargolength` int DEFAULT NULL,
  `shippingcargoheight` int DEFAULT NULL,
  `shippingcargopackage` varchar(100) DEFAULT NULL,
  `shippingcargopackagequantity` int DEFAULT NULL,
  `shippingcargopackageweight` int DEFAULT NULL,
  `shippingcargopackagewidth` int DEFAULT NULL,
  `shippingcargopackagelength` int DEFAULT NULL,
  `shippingcargopackageheight` int DEFAULT NULL,
  `shippingcargopackagevolume` int DEFAULT NULL,
  `shippingcargopackagetotalweight` int DEFAULT NULL,
  `shippingcargopackagetotalvolume` int DEFAULT NULL,
  `shippingcargopackagetotalquantity` int DEFAULT NULL,
  `shippingcargototalvaluecurrency` varchar(100) DEFAULT NULL,
  `shippingcargoinsurance` varchar(100) DEFAULT NULL,
  `shippingcargoinsurancevalue` int DEFAULT NULL,
  `shippingcargoinsurancecurrency` varchar(100) DEFAULT NULL,
  `shippingcargodangerousname` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `shippingcargodangerousnumber` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `shippingcargodangerousclass` varchar(100) DEFAULT NULL,
  `shippingcargototalvalue` int DEFAULT NULL,
  `unitdriverfee` int DEFAULT NULL,
  `shippingcreateddate` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `unitdriverfeecurrency` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`jobid`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shippingjobs`
--

LOCK TABLES `shippingjobs` WRITE;
/*!40000 ALTER TABLE `shippingjobs` DISABLE KEYS */;
INSERT INTO `shippingjobs` VALUES (16,'Ali123',3,16,'2023-03-22','2023-02-03','Afyonkarahisar','aaaaaaaaaaaaa','Burdur','aaaaaaaaaaaaaa','Halil',NULL,NULL,'AAAAAA',11111,11111,11111,11111,'GBP',11111,11111,11111,'11111',11111,11111,11111,11111,11111,11111,11111,11111,11111,'USD','11111',11111,'USD','11111','11111','SINIF 1 Patlayıcılar',11111,11111,'2023-02-20 11:46:59','USD'),(17,'Ali123',3,16,'2023-03-22','2023-02-03','Afyonkarahisar','aaaaaaaaaaaaa','Burdur','aaaaaaaaaaaaaa','Halil',NULL,NULL,'AAAAAA',11111,11111,11111,11111,'GBP',11111,11111,11111,'11111',11111,11111,11111,11111,11111,11111,11111,11111,11111,'USD','11111',11111,'USD','11111','11111','SINIF 1 Patlayıcılar',11111,11111,'2023-02-20 11:47:04','USD'),(18,'Ali123',3,16,'2023-03-22','2023-02-03','Afyonkarahisar','aaaaaaaaaaaaa','Burdur','aaaaaaaaaaaaaa','Halil',NULL,NULL,'AAAAAA',11111,11111,11111,11111,'GBP',11111,11111,11111,'11111',11111,11111,11111,11111,11111,11111,11111,11111,11111,'USD','11111',11111,'USD','11111','11111','SINIF 1 Patlayıcılar',11111,11111,'2023-02-20 11:47:09','USD'),(19,'Ali123',3,16,'2023-03-22','2023-02-03','Afyonkarahisar','aaaaaaaaaaaaa','Burdur','aaaaaaaaaaaaaa','Halil',NULL,NULL,'AAAAAA',11111,11111,11111,11111,'GBP',11111,11111,11111,'11111',11111,11111,11111,11111,11111,11111,11111,11111,11111,'USD','11111',11111,'USD','11111','11111','SINIF 1 Patlayıcılar',11111,11111,'2023-02-20 11:47:12','USD'),(20,'Ali123',3,16,'2023-03-22','2023-02-03','Afyonkarahisar','aaaaaaaaaaaaa','Burdur','aaaaaaaaaaaaaa','Halil',NULL,NULL,'AAAAAA',11111,11111,11111,11111,'GBP',11111,11111,11111,'11111',11111,11111,11111,11111,11111,11111,11111,11111,11111,'USD','11111',11111,'USD','11111','11111','SINIF 1 Patlayıcılar',11111,11111,'2023-02-20 11:47:17','USD');
/*!40000 ALTER TABLE `shippingjobs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-16 23:56:51
