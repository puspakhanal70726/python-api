
-- Table structure for table `books`
--
CREATE DATABASE apidb;
USE apidb;
DROP TABLE IF EXISTS `books`;
CREATE TABLE `books` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `year` int(11) NOT NULL,
  `author` varchar(45) NOT NUll,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (1,'hello','1997', 'Ranu'),(2,'Mr.X',2001,'Krishna'),
(3,'Hey brohter',2007,'Ram Goupal'),(4,'Heropanthi', 2017,'Govinda');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;
