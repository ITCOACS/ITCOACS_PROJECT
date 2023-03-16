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
-- Table structure for table `freighttype`
--

DROP TABLE IF EXISTS `freighttype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `freighttype` (
  `freighttypeid` int NOT NULL AUTO_INCREMENT,
  `freighttype_name` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `freightmodel_idd` int DEFAULT NULL,
  PRIMARY KEY (`freighttypeid`),
  KEY `yuk_turu_ıdd` (`freightmodel_idd`),
  CONSTRAINT `freighttype_ibfk_1` FOREIGN KEY (`freightmodel_idd`) REFERENCES `freightmodel` (`freightmodelid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `freighttype`
--

LOCK TABLES `freighttype` WRITE;
/*!40000 ALTER TABLE `freighttype` DISABLE KEYS */;
INSERT INTO `freighttype` VALUES (1,'Hayvansal kaynaklı diğer ham malzemeler',1),(2,'Balık ve diğer balık ürünleri',1),(3,'Tahıllar',1),(4,'Patates',1),(5,'Şeker pancarı',1),(6,'Diğer taze meyve ve sebzeler',1),(7,'Ormancılık ve tomrukçuluk ürünleri',1),(8,'Canlı bitkiler ve çiçekler',1),(9,' Bitkisel kaynaklı diğer maddeler',1),(10,'Canlı hayvanlar',1),(11,'Sığır, koyun ve keçi sütü (işlenmemiş)',1),(12,'Taş kömürü ve linyit',2),(13,'Ham petrol',2),(14,'Doğal gaz',2),(15,'Demir cevherleri',3),(16,'Demir dışı metal cevherleri (uranyum ve toryum cevherleri hariç)',3),(17,'Kimyasal ve (doğal) gübre mineralleri',3),(18,'Tuz',3),(19,'Başka yerle tanımlanamayan taş, kum, çakıl, kil, turba ve diğer madencilik ve taş ocakçılığı ürünleri',3),(20,'Uranyum ve toryum cevherleri',3),(21,'Et, et ürünleri, ham deri ve post',4),(22,'Balık ve balık ürünleri, işlenmiş ve korunmuş',4),(23,'Sebze ve meyveler, işlenmiş ve korunmuş',4),(24,'Hayvansal ve bitkisel sıvı ve katı yağlar',4),(25,'Süt ürünleri ve dondurma',4),(26,'Tahıl değirmen ürünleri, nişasta ve nişasta ürünleri, hazır hayvan yemleri',4),(27,'İçecekler',4),(28,'Başka yerde sınıflandırılmamış diğer gıda ürünleri ve tütün ürünleri ( kolilenmiş olanlar ve büyük hacimlerde gruplanmış olanlar hariç)',4),(29,'Çeşitli gıda ürünleri ve tütün ürünleri (paketlenmiş veya büyük hacimlerde gruplanmış olanlar)',4),(30,'Tekstil ürünleri',5),(31,'Giyim eşyası ve kürkten eşyalar',5),(32,'Deri ve deri ürünleri',5),(33,'Ağaç ve mantar ürünleri (mobilya hariç)',6),(34,'Kağıt hamuru, kağıt ve kağıt ürünleri',6),(35,'Basılı maddeler ve kayıtlı medya',6),(36,'Kok fırını ürünleri',7),(37,'Sıvı rafine petrol ürünleri',7),(38,'Gaz, sıvılaştırılmış veya sıkıştırılmış petrol ürünleri',7),(39,'katı veya mumsu rafine petrol ürünleri',7),(40,'Temel mineral kimyasal ürünler',8),(41,'Temel organik kimyasal ürünler',8),(42,'Azot bileşikleri ve gübreler (doğal gübreler hariç)',8),(43,'Temel plastikler ve sentetik kauçuklar, birincil formda',8),(44,'Eczacılık ürünleri ve parakimyasallar (haşarat öldürücüler ve tarımsal amaçlı kimyasal ürünler dahil)',8),(45,'Kauçuk ve plastik ürünler',8),(46,'Nükleer yakıt',8),(47,'Cam ve cam ürünleri, seramik ve porselen ürünleri',9),(48,'Çimento, kireç ve alçı',9),(49,'Diğer inşaat malzemeleri',9),(50,'Ana demir-çelik ile demir alaşımları, demir ve çeliğin ilk işlenmesinden elde edilmiş ürünler (borular hariç)',10),(51,'Demir dışı metaller ve ürünleri',10),(52,'Tüpler, borular, içi boş profiller ve ilgili bağlantı parçaları',10),(53,'Yapısal metal ürünler',10),(54,'Boylerler (kazanlar), hırdavat, silah ve diğer fabrikasyon metal ürünler',10),(55,'Tarım ve orman makineleri',11),(56,'Başka yerde sınıflandırılmamış ev aletleri (beyaz eşya)',11),(57,'Büro makineleri ve bilgisayarlar',11),(58,'Başka yerde sınıflandırılmamış elektrikli makine ve teçhizat',11),(59,'Elektronik parçalar, alıcı ve verici cihazları',11),(60,'Televizyon ve radyo alıcıları; ses ve görüntü kaydetme ve çoğaltma cihazları ile ilgili ürünler (kahverengi eşya)',11),(61,'Tıbbi, hassas ve optik aletler, saatler',11),(62,'Diğer makineler, takım tezgahları ve parçaları',11),(63,'Otomobil sanayi ürünleri',12),(64,'Diğer ulaştırma ekipmanları',12),(65,'Mobilya',13),(66,'Diğer imalat malları',13),(67,'Ev ve belediye atıkları',14),(68,'Diğer atık ve ikincil hammaddeler',14),(69,'Posta',15),(70,'Koliler ve küçük paketler',15),(71,'Konteynerler ve yük nakil kasaları (swap bodies), boş olanlar',16),(72,'Paletler ve diğer paketleme malzemeleri, boş olanlar',16),(73,'Hane halkı eşyalarının taşınması',17),(74,'Seyahat edenlerin bagajları ve el bagajları',17),(75,'Tamir için araçların taşınması',17),(76,'Fabrika ekipmanları ve yapı iskelesi malzemeleri',17),(77,'Başka yerde sınıflandırılmamış diğer piyasa dışı mallar',17),(78,'Gruplandırılmış mallar',18),(79,'Tanımlanamayan mallar, (konteynerlerde veya yük nakil kasalarında)',19),(80,'Diğer tanımlanamayan mallar',19),(81,'Başka yerde sınıflandırılmamış diğer mallar',20);
/*!40000 ALTER TABLE `freighttype` ENABLE KEYS */;
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
