-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: instagramstory.mysql.pythonanywhere-services.com    Database: instagramstory$instagram_storys
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `User_storymodel`
--

DROP TABLE IF EXISTS `User_storymodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User_storymodel` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` longtext NOT NULL,
  `story_time` longtext NOT NULL,
  `story_id` bigint NOT NULL,
  `story_link` longtext,
  `tag_list` longtext,
  `testing_time` date DEFAULT NULL,
  `media_path` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `story_id` (`story_id`)
) ENGINE=InnoDB AUTO_INCREMENT=160 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User_storymodel`
--

LOCK TABLES `User_storymodel` WRITE;
/*!40000 ALTER TABLE `User_storymodel` DISABLE KEYS */;
INSERT INTO `User_storymodel` VALUES (1,'krishh.naaaa_20','10 September 2023 12:17 AM Sunday',3188218265432528894,'uploads/krishh.naaaa_20/3188218265432528894.mp4','','2023-09-10','uploads/story_img/krishna.png'),(2,'_iamdev.__','10 September 2023 09:25 AM Sunday',3188494068723128249,'uploads/_iamdev.__/3188494068723128249.mp4','karandabhi_0210','2023-09-10','uploads/story_img/dev.png'),(3,'_iamdev.__','10 September 2023 09:28 AM Sunday',3188495902682400447,'uploads/_iamdev.__/3188495902682400447.mp4','sharvan_.zzy_','2023-09-10','uploads/story_img/dev.png'),(4,'_iamdev.__','10 September 2023 11:18 AM Sunday',3188551369685248709,'uploads/_iamdev.__/3188551369685248709.mp4','','2023-09-10','uploads/story_img/dev.png'),(5,'dhairyame','10 September 2023 01:10 AM Sunday',3188244916118975541,'uploads/dhairyame/3188244916118975541.mp4','','2023-09-10','uploads/story_img/dhairya.png'),(6,'dhairyame','10 September 2023 01:12 AM Sunday',3188246143053341600,'uploads/dhairyame/3188246143053341600.png','','2023-09-10','uploads/story_img/dhairya.png'),(7,'dhairyame','10 September 2023 01:24 AM Sunday',3188251959476180448,'uploads/dhairyame/3188251959476180448.mp4','nityaa._06','2023-09-10','uploads/story_img/dhairya.png'),(23,'d3v_chill.out','10 September 2023 06:06 PM Sunday',3188756167826367980,'uploads/d3v_chill.out/3188756167826367980.mp4','','2023-09-10','uploads/story_img/soni_dev.png'),(32,'dhairyame','11 September 2023 01:10 AM Monday',3188969593523991254,'uploads/dhairyame/3188969593523991254.png','','2023-09-11','uploads/story_img/dhairya.png'),(50,'paramm_w','11 September 2023 08:22 PM Monday',3189549669116480429,'uploads/paramm_w/3189549669116480429.png','','2023-09-11','uploads/story_img/param.png'),(52,'krishh.naaaa_20','12 September 2023 12:18 AM Tuesday',3189668521051478303,'uploads/krishh.naaaa_20/3189668521051478303.mp4','','2023-09-12','uploads/story_img/krishna.png'),(53,'dhairyame','12 September 2023 12:04 AM Tuesday',3189661923713242915,'uploads/dhairyame/3189661923713242915.mp4','','2023-09-12','uploads/story_img/dhairya.png'),(59,'krishh.naaaa_20','12 September 2023 07:49 AM Tuesday',3189895335659268818,'uploads/krishh.naaaa_20/3189895335659268818.png','','2023-09-12','uploads/story_img/krishna.png'),(75,'d3v_chill.out','13 September 2023 02:02 PM Wednesday',3190807591345078761,'uploads/d3v_chill.out/3190807591345078761.mp4','','2023-09-13','uploads/story_img/soni_dev.png'),(76,'krishh.naaaa_20','13 September 2023 08:33 PM Wednesday',3191004532404720908,'uploads/krishh.naaaa_20/3191004532404720908.mp4','','2023-09-13','uploads/story_img/krishna.png'),(79,'krishh.naaaa_20','14 September 2023 12:13 AM Thursday',3191115188074324289,'uploads/krishh.naaaa_20/3191115188074324289.mp4','kahanishah_02, rangrasiyagarbaclasses, vipul_p0206, spamziiii_4001','2023-09-14','uploads/story_img/krishna.png'),(88,'dhairyame','15 September 2023 12:58 AM Friday',3191862534356732842,'uploads/dhairyame/3191862534356732842.png','','2023-09-15','uploads/story_img/dhairya.png'),(109,'krishh.naaaa_20','15 September 2023 11:59 PM Friday',3192558069318390394,'uploads/krishh.naaaa_20/3192558069318390394.mp4','preksha_94','2023-09-15','uploads/story_img/krishna.png'),(110,'dhairyame','16 September 2023 12:42 AM Saturday',3192579732118319989,'uploads/dhairyame/3192579732118319989.mp4','','2023-09-16','uploads/story_img/dhairya.png'),(135,'dhairyame','16 September 2023 10:55 AM Saturday',3192888299458289718,'uploads/dhairyame/3192888299458289718.mp4','royal_shivaholic5057','2023-09-16','uploads/story_img/dhairya.png'),(145,'vishwas_soni_24','16 September 2023 08:26 PM Saturday',3193175404456587620,'uploads/vishwas_soni_24/3193175404456587620.png','_rosshh.nii','2023-09-16','uploads/27971610797/vishwas_soni_24.png');
/*!40000 ALTER TABLE `User_storymodel` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
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
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
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
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add story model',1,'add_storymodel'),(2,'Can change story model',1,'change_storymodel'),(3,'Can delete story model',1,'delete_storymodel'),(4,'Can view story model',1,'view_storymodel'),(5,'Can add log entry',2,'add_logentry'),(6,'Can change log entry',2,'change_logentry'),(7,'Can delete log entry',2,'delete_logentry'),(8,'Can view log entry',2,'view_logentry'),(9,'Can add permission',3,'add_permission'),(10,'Can change permission',3,'change_permission'),(11,'Can delete permission',3,'delete_permission'),(12,'Can view permission',3,'view_permission'),(13,'Can add group',4,'add_group'),(14,'Can change group',4,'change_group'),(15,'Can delete group',4,'delete_group'),(16,'Can view group',4,'view_group'),(17,'Can add user',5,'add_user'),(18,'Can change user',5,'change_user'),(19,'Can delete user',5,'delete_user'),(20,'Can view user',5,'view_user'),(21,'Can add content type',6,'add_contenttype'),(22,'Can change content type',6,'change_contenttype'),(23,'Can delete content type',6,'delete_contenttype'),(24,'Can view content type',6,'view_contenttype'),(25,'Can add session',7,'add_session'),(26,'Can change session',7,'change_session'),(27,'Can delete session',7,'delete_session'),(28,'Can view session',7,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
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
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (2,'admin','logentry'),(4,'auth','group'),(3,'auth','permission'),(5,'auth','user'),(6,'contenttypes','contenttype'),(7,'sessions','session'),(1,'User','storymodel');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'User','0001_initial','2023-09-07 17:38:46.081679'),(2,'contenttypes','0001_initial','2023-09-07 17:38:46.162486'),(3,'auth','0001_initial','2023-09-07 17:38:46.510702'),(4,'admin','0001_initial','2023-09-07 17:38:47.043255'),(5,'admin','0002_logentry_remove_auto_add','2023-09-07 17:38:47.170785'),(6,'admin','0003_logentry_add_action_flag_choices','2023-09-07 17:38:47.187583'),(7,'contenttypes','0002_remove_content_type_name','2023-09-07 17:38:47.291296'),(8,'auth','0002_alter_permission_name_max_length','2023-09-07 17:38:47.354015'),(9,'auth','0003_alter_user_email_max_length','2023-09-07 17:38:47.423109'),(10,'auth','0004_alter_user_username_opts','2023-09-07 17:38:47.433992'),(11,'auth','0005_alter_user_last_login_null','2023-09-07 17:38:47.485866'),(12,'auth','0006_require_contenttypes_0002','2023-09-07 17:38:47.493429'),(13,'auth','0007_alter_validators_add_error_messages','2023-09-07 17:38:47.504554'),(14,'auth','0008_alter_user_username_max_length','2023-09-07 17:38:47.578026'),(15,'auth','0009_alter_user_last_name_max_length','2023-09-07 17:38:47.658248'),(16,'auth','0010_alter_group_name_max_length','2023-09-07 17:38:47.741121'),(17,'auth','0011_update_proxy_permissions','2023-09-07 17:38:47.756516'),(18,'auth','0012_alter_user_first_name_max_length','2023-09-07 17:38:47.831142'),(19,'sessions','0001_initial','2023-09-07 17:38:47.889902'),(20,'User','0002_storymodel_testing_time','2023-09-08 09:11:39.268748'),(21,'User','0003_storymodel_media_path','2023-09-16 12:20:21.043848');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
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

-- Dump completed on 2023-09-16 18:23:37
