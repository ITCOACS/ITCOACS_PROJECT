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
-- Table structure for table `freightmodel`
--

DROP TABLE IF EXISTS `freightmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `freightmodel` (
  `freightmodelid` int NOT NULL AUTO_INCREMENT,
  `freightmodel_name` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`freightmodelid`),
  KEY `Yük_türü_yük_tür_id_IDX` (`freightmodelid`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `freightmodel`
--

LOCK TABLES `freightmodel` WRITE;
/*!40000 ALTER TABLE `freightmodel` DISABLE KEYS */;
INSERT INTO `freightmodel` VALUES (1,'Tarım, avcılık ve ormancılık ürünleri; balık ve diğer balıkçılık ürünleri'),(2,'Taş kömürü ve linyit; ham petrol ve doğalgaz'),(3,'Metal cevherleri ve diğer maden ve madencilik ürünleri; turba; uranyum ve toryum'),(4,'Gıda ürünleri, içecekler ve tütün'),(5,'Tekstil ve tekstil ürünleri; deri ve deri ürünleri'),(6,'Kereste, ağaç ürünleri ve mantar ürünleri (mobilya hariç); saz, saman ve benzeri malzemelerden yapılmış ürünler; kağıt hamuru, kağıt ve kağıt ürünleri; basılı malzemeler, kayıtlı medya'),(7,'Kok kömürü ve rafine edilmiş petrol ürünleri'),(8,'Kimyasallar, kimyasal ürünler, insan yapımı elyaflar; kauçuk ve plastik ürünler; nükleer yakıt'),(9,'Diğer metalik olmayan mineral ürünler'),(10,'Ana metaller; fabrikasyon metal ürünleri (makine ve ekipman hariç)'),(11,'Başka yerde sınıflandırılmamış makine ve ekipmanlar; büro makineleri ve bilgisayarlar; başka yerle sınıflandırılmamış elektrikli makineler ve cihazlar; radyo, televizyon ve iletişim ekipmanları ve cihazları; tıbbi, hassas ve optik aletler; saatler'),(12,'Taşımacılık ekipmanları'),(13,'Mobilya; başka yerde sınıflandırılmamış diğer imalat malları'),(14,'İkincil hammaddeler; belediye atıkları ve diğer atıklar'),(15,'Mektup, koli'),(16,'Malların taşınmasında kullanılan ekipman ve malzemeler'),(17,'Hanehalkı ve büro eşyalarının taşınması; yolcuların yanlarındaki bagajları ve eşyaları; tamir için taşınan motorlu araçlar; başka yerde sınıflandırılmamış diğer piyasa dışı mallar'),(18,'Gruplandırılmış mallar: bir arada taşınan karışık kategorilerdeki mallar'),(19,'Tanımlanamayan mallar: herhangi bir nedenle tanımlanamayan ve bundan dolayı 01-16 gruplarına tahsis edilemeyen mallar.'),(20,'Başka yerde sınıflandırılmamış diğer mallar');
/*!40000 ALTER TABLE `freightmodel` ENABLE KEYS */;
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
