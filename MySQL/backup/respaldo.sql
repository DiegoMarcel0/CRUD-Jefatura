CREATE DATABASE IF NOT EXISTS comisaria_db;
USE comisaria_db;
-- MySQL dump 10.13  Distrib 9.1.0, for Linux (x86_64)
--
-- Host: localhost    Database: comisaria_db
-- ------------------------------------------------------
-- Server version	9.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Comisaria_empleado`
--

DROP TABLE IF EXISTS `Comisaria_empleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Comisaria_empleado` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `last_name2` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  `puesto` int NOT NULL,
  `register_date` datetime(6) DEFAULT NULL,
  `num_phone` varchar(14) NOT NULL,
  `salario` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Comisaria_empleado`
--

LOCK TABLES `Comisaria_empleado` WRITE;
/*!40000 ALTER TABLE `Comisaria_empleado` DISABLE KEYS */;
INSERT INTO `Comisaria_empleado` VALUES (1,'pbkdf2_sha256$870000$Molx782PahCDsjgJTGRdI9$ljhvvz7KIha5dyesrH1AnSXwkIpIyGdRSp45R60I84I=','2024-11-13 05:30:54.254801',1,'admin',1,1,'2024-11-13 05:18:24.941235','','','','diego.marceloslv@gmail.com',1,'2024-11-13 05:18:24.941247','',0.00),(2,'pbkdf2_sha256$870000$r0GAgQYFJd53Y4S6zg7dXY$OfCXlSyyJ1a1yGCc2OF2qLSTcgwbD4UFLCh++mkNOlM=',NULL,0,'DiegoGonzales0257',0,1,'2024-11-13 05:27:20.085548','Diego','Gonzales','De la mancha','diego@gmail.com',10,'2024-11-13 00:00:00.000000','18818181',2000.00),(3,'pbkdf2_sha256$870000$12VzSXEHr9i80WSQIa27zd$nyaCiE0dTUO1ndjDOgLVUQcXsHgPogWvCN3nzMchVdg=',NULL,0,'EmilianoZapata6309',0,1,'2024-11-13 05:28:35.836419','Emiliano','Zapata','De la mancha','emiliano@zapata.com',10,'2024-11-13 00:00:00.000000','18818181',1000.00);
/*!40000 ALTER TABLE `Comisaria_empleado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Comisaria_empleado_groups`
--

DROP TABLE IF EXISTS `Comisaria_empleado_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Comisaria_empleado_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `empleado_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Comisaria_empleado_groups_empleado_id_group_id_2831588f_uniq` (`empleado_id`,`group_id`),
  KEY `Comisaria_empleado_groups_group_id_f44af446_fk_auth_group_id` (`group_id`),
  CONSTRAINT `Comisaria_empleado_g_empleado_id_24f5bff0_fk_Comisaria` FOREIGN KEY (`empleado_id`) REFERENCES `Comisaria_empleado` (`id`),
  CONSTRAINT `Comisaria_empleado_groups_group_id_f44af446_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Comisaria_empleado_groups`
--

LOCK TABLES `Comisaria_empleado_groups` WRITE;
/*!40000 ALTER TABLE `Comisaria_empleado_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `Comisaria_empleado_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Comisaria_empleado_user_permissions`
--

DROP TABLE IF EXISTS `Comisaria_empleado_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Comisaria_empleado_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `empleado_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Comisaria_empleado_user__empleado_id_permission_i_fc9ac450_uniq` (`empleado_id`,`permission_id`),
  KEY `Comisaria_empleado_u_permission_id_ddcb2168_fk_auth_perm` (`permission_id`),
  CONSTRAINT `Comisaria_empleado_u_empleado_id_c8856487_fk_Comisaria` FOREIGN KEY (`empleado_id`) REFERENCES `Comisaria_empleado` (`id`),
  CONSTRAINT `Comisaria_empleado_u_permission_id_ddcb2168_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Comisaria_empleado_user_permissions`
--

LOCK TABLES `Comisaria_empleado_user_permissions` WRITE;
/*!40000 ALTER TABLE `Comisaria_empleado_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `Comisaria_empleado_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Comisaria_oficiales`
--

DROP TABLE IF EXISTS `Comisaria_oficiales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Comisaria_oficiales` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `num_placa` int unsigned NOT NULL,
  `rank` int NOT NULL,
  `id_emp_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_emp_id` (`id_emp_id`),
  CONSTRAINT `Comisaria_oficiales_id_emp_id_5a8f5dcc_fk_Comisaria_empleado_id` FOREIGN KEY (`id_emp_id`) REFERENCES `Comisaria_empleado` (`id`),
  CONSTRAINT `Comisaria_oficiales_chk_1` CHECK ((`num_placa` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Comisaria_oficiales`
--

LOCK TABLES `Comisaria_oficiales` WRITE;
/*!40000 ALTER TABLE `Comisaria_oficiales` DISABLE KEYS */;
INSERT INTO `Comisaria_oficiales` VALUES (2,39451,1,2),(3,36981,3,3);
/*!40000 ALTER TABLE `Comisaria_oficiales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Comisaria_registro_casos`
--

DROP TABLE IF EXISTS `Comisaria_registro_casos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Comisaria_registro_casos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `titulo` varchar(50) NOT NULL,
  `descripcion` longtext NOT NULL,
  `estatus` int NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_fin` date DEFAULT NULL,
  `num_placa_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Comisaria_registro_c_num_placa_id_1033ebf8_fk_Comisaria` (`num_placa_id`),
  CONSTRAINT `Comisaria_registro_c_num_placa_id_1033ebf8_fk_Comisaria` FOREIGN KEY (`num_placa_id`) REFERENCES `Comisaria_oficiales` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Comisaria_registro_casos`
--

LOCK TABLES `Comisaria_registro_casos` WRITE;
/*!40000 ALTER TABLE `Comisaria_registro_casos` DISABLE KEYS */;
/*!40000 ALTER TABLE `Comisaria_registro_casos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Comisaria_reportes_caso`
--

DROP TABLE IF EXISTS `Comisaria_reportes_caso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Comisaria_reportes_caso` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha_reporte` datetime(6) NOT NULL,
  `titulo` varchar(50) NOT NULL,
  `contenido` longtext NOT NULL,
  `tipo` int NOT NULL,
  `id_caso_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Comisaria_reportes_c_id_caso_id_b280b417_fk_Comisaria` (`id_caso_id`),
  CONSTRAINT `Comisaria_reportes_c_id_caso_id_b280b417_fk_Comisaria` FOREIGN KEY (`id_caso_id`) REFERENCES `Comisaria_registro_casos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Comisaria_reportes_caso`
--

LOCK TABLES `Comisaria_reportes_caso` WRITE;
/*!40000 ALTER TABLE `Comisaria_reportes_caso` DISABLE KEYS */;
/*!40000 ALTER TABLE `Comisaria_reportes_caso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Comisaria_reportes_de_servicio`
--

DROP TABLE IF EXISTS `Comisaria_reportes_de_servicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Comisaria_reportes_de_servicio` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `titulo` varchar(50) NOT NULL,
  `contenido` longtext NOT NULL,
  `tipo` int NOT NULL,
  `fecha` date NOT NULL,
  `num_placa_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Comisaria_reportes_d_num_placa_id_9607cc60_fk_Comisaria` (`num_placa_id`),
  CONSTRAINT `Comisaria_reportes_d_num_placa_id_9607cc60_fk_Comisaria` FOREIGN KEY (`num_placa_id`) REFERENCES `Comisaria_oficiales` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Comisaria_reportes_de_servicio`
--

LOCK TABLES `Comisaria_reportes_de_servicio` WRITE;
/*!40000 ALTER TABLE `Comisaria_reportes_de_servicio` DISABLE KEYS */;
/*!40000 ALTER TABLE `Comisaria_reportes_de_servicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add Oficial',6,'add_oficiales'),(22,'Can change Oficial',6,'change_oficiales'),(23,'Can delete Oficial',6,'delete_oficiales'),(24,'Can view Oficial',6,'view_oficiales'),(25,'Can add Registro de caso',7,'add_registro_casos'),(26,'Can change Registro de caso',7,'change_registro_casos'),(27,'Can delete Registro de caso',7,'delete_registro_casos'),(28,'Can view Registro de caso',7,'view_registro_casos'),(29,'Can add Reporte de caso',8,'add_reportes_caso'),(30,'Can change Reporte de caso',8,'change_reportes_caso'),(31,'Can delete Reporte de caso',8,'delete_reportes_caso'),(32,'Can view Reporte de caso',8,'view_reportes_caso'),(33,'Can add Reporte de servicio',9,'add_reportes_de_servicio'),(34,'Can change Reporte de servicio',9,'change_reportes_de_servicio'),(35,'Can delete Reporte de servicio',9,'delete_reportes_de_servicio'),(36,'Can view Reporte de servicio',9,'view_reportes_de_servicio'),(37,'Can add Empleado',10,'add_empleado'),(38,'Can change Empleado',10,'change_empleado'),(39,'Can delete Empleado',10,'delete_empleado'),(40,'Can view Empleado',10,'view_empleado');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_Comisaria_empleado_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_Comisaria_empleado_id` FOREIGN KEY (`user_id`) REFERENCES `Comisaria_empleado` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(10,'Comisaria','empleado'),(6,'Comisaria','oficiales'),(7,'Comisaria','registro_casos'),(8,'Comisaria','reportes_caso'),(9,'Comisaria','reportes_de_servicio'),(4,'contenttypes','contenttype'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-11-13 05:17:30.822226'),(2,'contenttypes','0002_remove_content_type_name','2024-11-13 05:17:30.849423'),(3,'auth','0001_initial','2024-11-13 05:17:30.963475'),(4,'auth','0002_alter_permission_name_max_length','2024-11-13 05:17:30.992899'),(5,'auth','0003_alter_user_email_max_length','2024-11-13 05:17:30.999775'),(6,'auth','0004_alter_user_username_opts','2024-11-13 05:17:31.019650'),(7,'auth','0005_alter_user_last_login_null','2024-11-13 05:17:31.026124'),(8,'auth','0006_require_contenttypes_0002','2024-11-13 05:17:31.028849'),(9,'auth','0007_alter_validators_add_error_messages','2024-11-13 05:17:31.035058'),(10,'auth','0008_alter_user_username_max_length','2024-11-13 05:17:31.041696'),(11,'auth','0009_alter_user_last_name_max_length','2024-11-13 05:17:31.048046'),(12,'auth','0010_alter_group_name_max_length','2024-11-13 05:17:31.060549'),(13,'auth','0011_update_proxy_permissions','2024-11-13 05:17:31.067716'),(14,'auth','0012_alter_user_first_name_max_length','2024-11-13 05:17:31.073830'),(15,'Comisaria','0001_initial','2024-11-13 05:17:31.363159'),(16,'admin','0001_initial','2024-11-13 05:17:31.432082'),(17,'admin','0002_logentry_remove_auto_add','2024-11-13 05:17:31.440634'),(18,'admin','0003_logentry_add_action_flag_choices','2024-11-13 05:17:31.448767'),(19,'sessions','0001_initial','2024-11-13 05:17:31.468840');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-13  5:34:47
