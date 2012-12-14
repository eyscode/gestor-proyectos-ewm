-- --------------------------------------------------------
-- Host:                         localhost
-- Server version:               5.5.24 - MySQL Community Server (GPL)
-- Server OS:                    Win32
-- HeidiSQL version:             7.0.0.4053
-- Date/time:                    2012-12-12 23:31:14
-- --------------------------------------------------------

use ofisis;

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;

-- Dumping structure for table ofisis.appcuentas_check
CREATE TABLE IF NOT EXISTS `appcuentas_check` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `description` longtext NOT NULL,
  `condition` int(11) NOT NULL,
  `task_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `appcuentas_check_3ff01bab` (`task_id`),
  CONSTRAINT `task_id_refs_id_66cc5bd1` FOREIGN KEY (`task_id`) REFERENCES `appcuentas_task` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.appcuentas_check: ~0 rows (approximately)
/*!40000 ALTER TABLE `appcuentas_check` DISABLE KEYS */;
/*!40000 ALTER TABLE `appcuentas_check` ENABLE KEYS */;


-- Dumping structure for table ofisis.appcuentas_client
CREATE TABLE IF NOT EXISTS `appcuentas_client` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `profile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `appcuentas_client_141c6eec` (`profile_id`),
  CONSTRAINT `profile_id_refs_id_2b2eb7c8` FOREIGN KEY (`profile_id`) REFERENCES `appcuentas_profile` (`id`),
  CONSTRAINT `user_id_refs_id_632a857` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.appcuentas_client: ~16 rows (approximately)
/*!40000 ALTER TABLE `appcuentas_client` DISABLE KEYS */;
INSERT INTO `appcuentas_client` (`id`, `user_id`, `profile_id`) VALUES
	(1, 1, 1),
	(2, 2, 1),
	(3, 3, 1),
	(4, 4, 1),
	(5, 5, 1),
	(6, 6, 1),
	(7, 7, 1),
	(8, 8, 1),
	(9, 9, 1),
	(10, 10, 1),
	(11, 12, 1),
	(12, 13, 1),
	(13, 14, 1),
	(14, 15, 1),
	(15, 16, 1),
	(16, 17, 1);
/*!40000 ALTER TABLE `appcuentas_client` ENABLE KEYS */;


-- Dumping structure for table ofisis.appcuentas_client_has_project
CREATE TABLE IF NOT EXISTS `appcuentas_client_has_project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `client_id` int(11) NOT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `appcuentas_client_has_project_4a4e8ffb` (`client_id`),
  KEY `appcuentas_client_has_project_499df97c` (`project_id`),
  CONSTRAINT `client_id_refs_id_b9a5516` FOREIGN KEY (`client_id`) REFERENCES `appcuentas_client` (`id`),
  CONSTRAINT `project_id_refs_id_30453fbf` FOREIGN KEY (`project_id`) REFERENCES `appcuentas_project` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.appcuentas_client_has_project: ~15 rows (approximately)
/*!40000 ALTER TABLE `appcuentas_client_has_project` DISABLE KEYS */;
INSERT INTO `appcuentas_client_has_project` (`id`, `client_id`, `project_id`) VALUES
	(1, 1, 9),
	(2, 3, 9),
	(3, 3, 8),
	(4, 1, 7),
	(5, 3, 3),
	(6, 3, 1),
	(7, 2, 11),
	(8, 2, 12),
	(9, 7, 14),
	(11, 2, 17),
	(12, 1, 21),
	(13, 2, 21),
	(14, 3, 21),
	(15, 4, 23),
	(16, 2, 23);
/*!40000 ALTER TABLE `appcuentas_client_has_project` ENABLE KEYS */;


-- Dumping structure for table ofisis.appcuentas_column
CREATE TABLE IF NOT EXISTS `appcuentas_column` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `position` int(11) NOT NULL,
  `table_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `appcuentas_column_3f3c6161` (`table_id`),
  CONSTRAINT `table_id_refs_id_2164e8c0` FOREIGN KEY (`table_id`) REFERENCES `appcuentas_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.appcuentas_column: ~38 rows (approximately)
/*!40000 ALTER TABLE `appcuentas_column` DISABLE KEYS */;
INSERT INTO `appcuentas_column` (`id`, `name`, `position`, `table_id`) VALUES
	(1, 'Por hacer', 1, 1),
	(2, 'Haciendo', 2, 1),
	(3, 'terminadas', 3, 1),
	(4, 'columna 1', 1, 2),
	(5, 'nueva columna aaa', 4, 1),
	(6, 'por hacer', 1, 3),
	(7, 'columna 1', 1, 18),
	(8, 'yyy', 0, 19),
	(9, 'por hacer', 0, 20),
	(10, 'haciendo', 0, 20),
	(11, 'terminadas', 0, 20),
	(12, 'por hacer', 1, 21),
	(13, 'hecho', 2, 21),
	(14, 'por Hacer', 0, 22),
	(15, 'Haciendo', 0, 22),
	(16, 'Hecho', 0, 22),
	(17, 'por hacer', 0, 25),
	(18, 'haciendo', 0, 25),
	(19, 'hecho', 0, 25),
	(20, 'hecho', 0, 26),
	(21, 'haciendo', 0, 26),
	(22, 'por hacer', 0, 26),
	(23, 'por hacer', 0, 27),
	(24, 'haciendo', 0, 27),
	(25, 'hecho', 0, 27),
	(26, 'por hacer', 0, 28),
	(27, 'haciendo', 0, 28),
	(28, 'hecho', 0, 28),
	(29, 'hecho', 0, 29),
	(30, 'por hacer', 0, 29),
	(31, 'por aprobar', 0, 29),
	(32, 'por hacer', 0, 31),
	(33, 'haciendo ', 0, 31),
	(34, 'hecho', 0, 31),
	(35, 'nueva columna', 0, 31),
	(36, 'por hacer', 0, 33),
	(37, 'haciendo', 0, 33),
	(38, 'hecho', 0, 33);
/*!40000 ALTER TABLE `appcuentas_column` ENABLE KEYS */;


-- Dumping structure for table ofisis.appcuentas_comment
CREATE TABLE IF NOT EXISTS `appcuentas_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `like` int(11) NOT NULL,
  `task_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `appcuentas_comment_3ff01bab` (`task_id`),
  CONSTRAINT `task_id_refs_id_1e9d16a6` FOREIGN KEY (`task_id`) REFERENCES `appcuentas_task` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.appcuentas_comment: ~6 rows (approximately)
/*!40000 ALTER TABLE `appcuentas_comment` DISABLE KEYS */;
INSERT INTO `appcuentas_comment` (`id`, `content`, `like`, `task_id`) VALUES
	(1, 'manu', 0, 2),
	(2, 'jojojo', 0, 2),
	(3, 'manu', 0, 3),
	(4, 'manuss', 0, 3),
	(5, 'jojo', 0, 3),
	(6, 'manu', 0, 9);
/*!40000 ALTER TABLE `appcuentas_comment` ENABLE KEYS */;


-- Dumping structure for table ofisis.appcuentas_data
CREATE TABLE IF NOT EXISTS `appcuentas_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `max_members` int(11) NOT NULL,
  `section` varchar(100) NOT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `appcuentas_data_499df97c` (`project_id`),
  CONSTRAINT `project_id_refs_id_19759bc3` FOREIGN KEY (`project_id`) REFERENCES `appcuentas_project` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.appcuentas_data: ~0 rows (approximately)
/*!40000 ALTER TABLE `appcuentas_data` DISABLE KEYS */;
/*!40000 ALTER TABLE `appcuentas_data` ENABLE KEYS */;


-- Dumping structure for table ofisis.appcuentas_document
CREATE TABLE IF NOT EXISTS `appcuentas_document` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `path` varchar(100) NOT NULL,
  `date_creation` datetime NOT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `appcuentas_document_499df97c` (`project_id`),
  CONSTRAINT `project_id_refs_id_371738dc` FOREIGN KEY (`project_id`) REFERENCES `appcuentas_project` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.appcuentas_document: ~0 rows (approximately)
/*!40000 ALTER TABLE `appcuentas_document` DISABLE KEYS */;
/*!40000 ALTER TABLE `appcuentas_document` ENABLE KEYS */;


-- Dumping structure for table ofisis.appcuentas_group
CREATE TABLE IF NOT EXISTS `appcuentas_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `information` varchar(250) NOT NULL,
  `date_creation` datetime NOT NULL,
  `creador_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `appcuentas_group_71903877` (`creador_id`),
  CONSTRAINT `creador_id_refs_id_70d9685e` FOREIGN KEY (`creador_id`) REFERENCES `appcuentas_client` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.appcuentas_group: ~16 rows (approximately)
/*!40000 ALTER TABLE `appcuentas_group` DISABLE KEYS */;
INSERT INTO `appcuentas_group` (`id`, `name`, `information`, `date_creation`, `creador_id`) VALUES
	(1, 'nuevo grupo', 'nueva descripcion ', '2012-07-30 21:19:40', 2),
	(2, 'nuevo', 'nuevo', '2012-07-30 21:22:21', 2),
	(3, 'nuevo 2', 'nuevo 2', '2012-07-30 21:22:38', 2),
	(4, 'manu', 'manu', '2012-07-30 21:36:34', 1),
	(5, 'dfdff', 'fff', '2012-07-31 14:22:40', 5),
	(6, 'amigos de la universidad', 'aqui se encuentran mis amigos de la u', '2012-07-31 15:58:15', 5),
	(7, 'Universidad de San Marcos', 'Grupo integrado por alumnos de la Facultad de Ingeniería de Software', '2012-08-20 04:07:08', 8),
	(8, 'nuevo Grupo', 'Descripcion', '2012-08-22 20:55:06', 8),
	(9, 'nuevo grupo 2', '12', '2012-08-22 23:01:49', 8),
	(10, 'pucp', 'lkajsdlka', '2012-08-22 23:10:18', 8),
	(11, 'hhh', 'sdfsdf', '2012-08-22 23:41:14', 8),
	(12, 'infosoft', 'esta e suna descripcion', '2012-08-24 00:28:19', 8),
	(13, 'quipu', 'el quipucamayoc', '2012-11-09 01:06:17', 11),
	(14, 'trreee', 'desceieioer', '2012-11-26 23:52:19', 1),
	(15, '/manu', 'ddddd', '2012-11-26 23:53:07', 1),
	(16, 'SAN MARCOS', 'GRUPO DE SAN MARCOS', '2012-11-30 01:08:27', 16);
/*!40000 ALTER TABLE `appcuentas_group` ENABLE KEYS */;


-- Dumping structure for table ofisis.appcuentas_group_has_client
CREATE TABLE IF NOT EXISTS `appcuentas_group_has_client` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `client_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `appcuentas_group_has_client_425ae3c4` (`group_id`),
  KEY `appcuentas_group_has_client_4a4e8ffb` (`client_id`),
  CONSTRAINT `client_id_refs_id_1ec35ab0` FOREIGN KEY (`client_id`) REFERENCES `appcuentas_client` (`id`),
  CONSTRAINT `group_id_refs_id_6cd0fddf` FOREIGN KEY (`group_id`) REFERENCES `appcuentas_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.appcuentas_group_has_client: ~25 rows (approximately)
/*!40000 ALTER TABLE `appcuentas_group_has_client` DISABLE KEYS */;
INSERT INTO `appcuentas_group_has_client` (`id`, `group_id`, `client_id`) VALUES
	(1, 3, 1),
	(2, 1, 3),
	(3, 5, 2),
	(4, 5, 4),
	(5, 5, 3),
	(6, 6, 4),
	(7, 6, 2),
	(12, 7, 3),
	(13, 7, 6),
	(14, 7, 7),
	(15, 8, 1),
	(16, 8, 2),
	(17, 9, 6),
	(18, 9, 7),
	(19, 10, 3),
	(20, 10, 6),
	(21, 11, 2),
	(22, 11, 5),
	(23, 11, 6),
	(24, 12, 2),
	(25, 13, 3),
	(26, 13, 5),
	(27, 4, 2),
	(28, 4, 3),
	(29, 16, 4);
/*!40000 ALTER TABLE `appcuentas_group_has_client` ENABLE KEYS */;


-- Dumping structure for table ofisis.appcuentas_image
CREATE TABLE IF NOT EXISTS `appcuentas_image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `path` varchar(100) NOT NULL,
  `task_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `appcuentas_image_3ff01bab` (`task_id`),
  CONSTRAINT `task_id_refs_id_79c9da78` FOREIGN KEY (`task_id`) REFERENCES `appcuentas_task` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.appcuentas_image: ~0 rows (approximately)
/*!40000 ALTER TABLE `appcuentas_image` DISABLE KEYS */;
/*!40000 ALTER TABLE `appcuentas_image` ENABLE KEYS */;


-- Dumping structure for table ofisis.appcuentas_meeting
CREATE TABLE IF NOT EXISTS `appcuentas_meeting` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `summary` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `date_creation` datetime NOT NULL,
  `initial` datetime NOT NULL,
  `end` datetime NOT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `appcuentas_meeting_499df97c` (`project_id`),
  CONSTRAINT `project_id_refs_id_26a4b8c7` FOREIGN KEY (`project_id`) REFERENCES `appcuentas_project` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.appcuentas_meeting: ~6 rows (approximately)
/*!40000 ALTER TABLE `appcuentas_meeting` DISABLE KEYS */;
INSERT INTO `appcuentas_meeting` (`id`, `summary`, `description`, `date_creation`, `initial`, `end`, `project_id`) VALUES
	(1, 'nueva reunioj', 'esta es una nueva reu', '2012-07-31 00:41:52', '2012-08-01 00:42:01', '2012-07-31 11:00:00', 1),
	(2, '', '', '2012-07-31 11:33:51', '2012-07-31 11:33:51', '2012-07-31 11:33:51', 11),
	(3, 'nueva reu', 'nueva re', '2012-07-31 11:34:42', '2012-07-31 11:34:42', '2012-07-31 11:34:42', 11),
	(4, 'Reunion de Presentacion', 'Esta es la reu para presentar el proyecto', '2012-07-31 16:01:07', '2012-07-31 16:01:07', '2012-07-31 16:01:07', 12),
	(5, 'Inaguracion', 'Reunión antes de la inaguración del evento Infosoft 3 pm', '2012-08-20 04:10:04', '2012-08-20 04:10:04', '2012-08-20 04:10:04', 14),
	(6, 'planning meeting', 'reunion d ecoordinacion', '2012-11-30 01:21:50', '2012-11-30 01:21:50', '2012-11-30 01:21:50', 23);
/*!40000 ALTER TABLE `appcuentas_meeting` ENABLE KEYS */;


-- Dumping structure for table ofisis.appcuentas_profile
CREATE TABLE IF NOT EXISTS `appcuentas_profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.appcuentas_profile: ~1 rows (approximately)
/*!40000 ALTER TABLE `appcuentas_profile` DISABLE KEYS */;
INSERT INTO `appcuentas_profile` (`id`, `name`, `description`) VALUES
	(1, 'normal', 'ad');
/*!40000 ALTER TABLE `appcuentas_profile` ENABLE KEYS */;


-- Dumping structure for table ofisis.appcuentas_project
CREATE TABLE IF NOT EXISTS `appcuentas_project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) NOT NULL,
  `date_creation` datetime NOT NULL,
  `company` varchar(250) NOT NULL,
  `base` tinyint(1) NOT NULL,
  `template_id` int(11) DEFAULT NULL,
  `creador_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `appcuentas_project_1e0a3f4a` (`template_id`),
  KEY `appcuentas_project_71903877` (`creador_id`),
  CONSTRAINT `creador_id_refs_id_1f426a3e` FOREIGN KEY (`creador_id`) REFERENCES `appcuentas_client` (`id`),
  CONSTRAINT `template_id_refs_id_73bf1605` FOREIGN KEY (`template_id`) REFERENCES `appcuentas_template` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.appcuentas_project: ~22 rows (approximately)
/*!40000 ALTER TABLE `appcuentas_project` DISABLE KEYS */;
INSERT INTO `appcuentas_project` (`id`, `name`, `date_creation`, `company`, `base`, `template_id`, `creador_id`) VALUES
	(1, 'project manu', '2012-07-17 11:00:00', 'Nueva company', 0, NULL, 2),
	(3, 'Nuevo projecto', '2012-07-29 22:32:47', 'Nuevooo', 0, NULL, 2),
	(4, 'Nuevo projecto', '2012-07-29 22:34:38', 'Nuevooo', 0, NULL, 2),
	(5, 'Nuevo projecto', '2012-07-29 22:48:42', 'Nuevooo', 0, NULL, 2),
	(6, 'Nuevo projecto', '2012-07-29 22:48:44', 'Nuevooo', 0, NULL, 2),
	(7, 'Nuevo projecto', '2012-07-29 22:52:40', 'Nuevooo', 0, NULL, 2),
	(8, 'Nuevo projecto', '2012-07-29 23:12:48', 'Nuevooo', 0, NULL, 2),
	(9, 'ofisis 2012', '2012-07-30 20:12:00', 'kodevian', 0, NULL, 2),
	(10, 'eysss', '2012-07-31 03:30:15', 'eysss', 0, NULL, 2),
	(11, 'kodevian', '2012-07-31 08:33:38', 'kodevian', 0, NULL, 5),
	(12, 'oFISIS 2012', '2012-07-31 15:59:13', 'OFISIS', 0, NULL, 5),
	(13, '', '2012-07-31 16:38:39', '', 0, NULL, 5),
	(14, 'Infosoft 2012', '2012-08-20 04:08:42', 'PUCP', 0, NULL, 8),
	(15, 'Nuevo Proyecto', '2012-08-22 20:54:40', 'Nueva compania', 0, NULL, 8),
	(16, 'ofisis 2', '2012-08-22 23:02:23', 'PUCP', 0, NULL, 8),
	(17, 'nuevo proyecto Prueba', '2012-08-23 22:49:58', 'UNMSM', 0, NULL, 8),
	(18, 'ofisis 3', '2012-08-23 23:46:05', 'PUCP', 0, NULL, 8),
	(19, 'x', '2012-08-23 23:53:14', 'x', 0, NULL, 8),
	(20, 'Prueba', '2012-08-24 00:28:53', 'UNMSM', 0, NULL, 8),
	(21, 'Jose Manuel', '2012-08-25 16:05:11', 'UNMSM', 0, NULL, 8),
	(22, 'kodevian', '2012-11-09 01:02:43', 'quipu', 0, NULL, 11),
	(23, 'calidad de software', '2012-11-30 01:10:09', 'unmsm', 0, NULL, 16);
/*!40000 ALTER TABLE `appcuentas_project` ENABLE KEYS */;


-- Dumping structure for table ofisis.appcuentas_table
CREATE TABLE IF NOT EXISTS `appcuentas_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `date_creation` datetime NOT NULL,
  `columns` int(11) NOT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `appcuentas_table_499df97c` (`project_id`),
  CONSTRAINT `project_id_refs_id_14870d32` FOREIGN KEY (`project_id`) REFERENCES `appcuentas_project` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.appcuentas_table: ~33 rows (approximately)
/*!40000 ALTER TABLE `appcuentas_table` DISABLE KEYS */;
INSERT INTO `appcuentas_table` (`id`, `name`, `date_creation`, `columns`, `project_id`) VALUES
	(1, 'Primera Iteracion', '2012-07-16 11:00:00', 4, 1),
	(2, 'Segunda Iteracion', '2012-07-09 08:38:18', 5, 1),
	(3, 'manu2', '2012-07-28 22:23:02', 1, 1),
	(4, 'otro', '2012-07-28 22:25:39', 0, 1),
	(5, 'este e otro tablero', '2012-07-28 22:27:31', 0, 1),
	(6, 'jajaja', '2012-07-28 22:29:26', 0, 1),
	(7, 'jose', '2012-07-28 22:32:58', 0, 1),
	(8, 'este es nuevo', '2012-07-28 22:34:39', 0, 1),
	(9, 'este es nuevo', '2012-07-28 22:38:55', 0, 1),
	(10, 'creooo', '2012-07-28 22:39:36', 0, 1),
	(11, 'jose', '2012-07-28 22:40:22', 0, 1),
	(12, 'manu3', '2012-07-28 22:40:51', 0, 1),
	(13, 'por qqq', '2012-07-28 22:41:30', 0, 1),
	(14, '', '2012-07-28 22:41:55', 0, 1),
	(15, 'por favor que funcione', '2012-07-28 22:46:55', 0, 1),
	(16, 'XD super XD', '2012-07-28 22:48:59', 0, 1),
	(17, 'nuevo tablero', '2012-07-29 23:32:23', 0, 3),
	(18, 'nuevo tablero', '2012-07-30 20:12:19', 1, 9),
	(19, 'manu', '2012-07-31 08:33:55', 0, 11),
	(20, 'Iteracion 1', '2012-07-31 16:01:54', 0, 12),
	(21, 'nueva tablero creado ofisis', '2012-07-31 16:40:55', 2, 12),
	(22, 'Gestionar Charlas Tecnicas', '2012-08-20 04:10:43', 0, 14),
	(23, 'Gestionar Talleres', '2012-08-20 04:10:56', 0, 14),
	(24, '', '2012-08-22 00:38:11', 0, 14),
	(25, 'Nuevo tablero', '2012-08-22 20:57:33', 0, 15),
	(26, 'tablero 1', '2012-08-22 23:02:48', 0, 16),
	(27, 'Nuevo tablero', '2012-08-23 22:50:46', 0, 17),
	(28, 'Talleres', '2012-08-23 23:46:41', 0, 18),
	(29, '1', '2012-08-23 23:53:39', 0, 19),
	(30, 'Tablero 1', '2012-08-24 00:30:04', 0, 20),
	(31, 'nuevo tablero', '2012-08-25 16:05:21', 0, 21),
	(32, 'wili', '2012-11-09 01:03:31', 0, 22),
	(33, 'Crear sistema de usuarios', '2012-11-30 01:11:53', 0, 23);
/*!40000 ALTER TABLE `appcuentas_table` ENABLE KEYS */;


-- Dumping structure for table ofisis.appcuentas_task
CREATE TABLE IF NOT EXISTS `appcuentas_task` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `subtitle` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `state` varchar(50) NOT NULL,
  `column_id` int(11) DEFAULT NULL,
  `work_package_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `appcuentas_task_de8f40` (`column_id`),
  KEY `appcuentas_task_25247ba` (`work_package_id`),
  CONSTRAINT `column_id_refs_id_162a98fc` FOREIGN KEY (`column_id`) REFERENCES `appcuentas_column` (`id`),
  CONSTRAINT `work_package_id_refs_id_3f6ad16e` FOREIGN KEY (`work_package_id`) REFERENCES `appcuentas_work_package` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.appcuentas_task: ~26 rows (approximately)
/*!40000 ALTER TABLE `appcuentas_task` DISABLE KEYS */;
INSERT INTO `appcuentas_task` (`id`, `title`, `subtitle`, `description`, `state`, `column_id`, `work_package_id`) VALUES
	(1, 'Task 11', 'creada', 'creada', 'por finalizar', 3, 1),
	(2, 'tarea', 'tareaaa', 'tareaaaaa', '', 2, 1),
	(3, 'tarea agregar', 'jejejej', 'jajaja', '', 1, 1),
	(4, 'josse', 'joskssj', 'desde', '', NULL, 9),
	(6, 'hhhh', 'hhhh', 'uuuu', '1', 8, 10),
	(7, 'Nueva Tarea', 'Nueva Tarea', 'Esta es mi tarea de prueba', '1', 10, 11),
	(8, 'nueva tarea 2', 'nueva tarea 2', 'tarea 2', '1', 10, 11),
	(9, 'nueva tarea', 'nueva tarea ', 'esta es nueva', '', 13, 13),
	(10, 'traer a IGDA para un taller', 'traer a IGDA para un taller', 'descripcion de prueba', '1', 16, 14),
	(11, 'nueva tarea', 'nueva tarea', 'descripcion', '1', 17, 15),
	(12, 'tarea 1', 'tarea 1', 'tarea 1', '1', 21, 18),
	(13, 'tarea 2', 'tarea 2', 'tarea 2', '1', 20, 19),
	(14, 'tarea x', 'tarea x', 'dsfsdf', '1', 22, 18),
	(15, 'yyyyyyyy', 'yyyyyyyy', 'ygtyjh', '1', 21, 20),
	(16, 'Hacer la vista', 'Hacer la vista', 'vista detalles', '1', 23, 21),
	(17, 'Hacer el controlador', 'Hacer el controlador', 'vista detalles', '1', 24, 21),
	(18, 'contactar Jose Manuel', 'contactar Jose Manuel', 'ponente de jqMobile', '1', 28, 23),
	(19, 'comprar gaseosas', 'comprar gaseosas', 'descripcion', '1', 28, 24),
	(20, 'maquetar web', 'maquetar web', 'kasjdlkajsd', '1', 29, 25),
	(21, 'hacer algoritmo', 'hacer algoritmo', 'esfjskldfjl', '1', NULL, 25),
	(22, 'dise;ar bd', 'dise;ar bd', 'llglhjuk', '1', 30, 25),
	(23, 'nueva tarea ', 'nueva tarea ', '123', '1', 34, 28),
	(24, 'nueva tarea 2', 'nueva tarea 2', '123', '1', 32, 28),
	(25, 'nueva tarea 2.1', 'nueva tarea 2.1', '123', '1', 34, 29),
	(26, 'hacer login', 'hacer login', 'descripcion', '1', 38, 31),
	(27, 'seguridad ', 'seguridad ', 'descripcion', '1', 36, 31);
/*!40000 ALTER TABLE `appcuentas_task` ENABLE KEYS */;


-- Dumping structure for table ofisis.appcuentas_template
CREATE TABLE IF NOT EXISTS `appcuentas_template` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) NOT NULL,
  `profile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `appcuentas_template_141c6eec` (`profile_id`),
  CONSTRAINT `profile_id_refs_id_439d82c7` FOREIGN KEY (`profile_id`) REFERENCES `appcuentas_profile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.appcuentas_template: ~2 rows (approximately)
/*!40000 ALTER TABLE `appcuentas_template` DISABLE KEYS */;
INSERT INTO `appcuentas_template` (`id`, `name`, `profile_id`) VALUES
	(1, 'TEMPLATE 1', 1),
	(2, 'TEMPLATE 2', 1);
/*!40000 ALTER TABLE `appcuentas_template` ENABLE KEYS */;


-- Dumping structure for table ofisis.appcuentas_util
CREATE TABLE IF NOT EXISTS `appcuentas_util` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `date` datetime NOT NULL,
  `path` varchar(100) NOT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `appcuentas_util_499df97c` (`project_id`),
  CONSTRAINT `project_id_refs_id_7549ca1` FOREIGN KEY (`project_id`) REFERENCES `appcuentas_project` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.appcuentas_util: ~0 rows (approximately)
/*!40000 ALTER TABLE `appcuentas_util` DISABLE KEYS */;
/*!40000 ALTER TABLE `appcuentas_util` ENABLE KEYS */;


-- Dumping structure for table ofisis.appcuentas_work_package
CREATE TABLE IF NOT EXISTS `appcuentas_work_package` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` varchar(50) NOT NULL,
  `prioridad` int(11) NOT NULL,
  `table_id` int(11) DEFAULT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `appcuentas_work_package_3f3c6161` (`table_id`),
  KEY `appcuentas_work_package_499df97c` (`project_id`),
  CONSTRAINT `project_id_refs_id_7b4b2863` FOREIGN KEY (`project_id`) REFERENCES `appcuentas_project` (`id`),
  CONSTRAINT `table_id_refs_id_3745eae2` FOREIGN KEY (`table_id`) REFERENCES `appcuentas_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.appcuentas_work_package: ~31 rows (approximately)
/*!40000 ALTER TABLE `appcuentas_work_package` DISABLE KEYS */;
INSERT INTO `appcuentas_work_package` (`id`, `name`, `description`, `prioridad`, `table_id`, `project_id`) VALUES
	(1, 'Paquete_tarea prueba', 'este es nuevo', 20, 1, 1),
	(2, 'este es nuevo', 'enuevvs', 12, NULL, 1),
	(3, 'este es nuevo', 'nuevoo', 15, NULL, 1),
	(4, 'este es un nuevo paquete', 'sss', 15, NULL, 3),
	(5, 'nuevo ', 'sasa', 15, NULL, 3),
	(6, 'paquete eys', 'jejejejejeje', 20, NULL, 10),
	(7, 'paquete nuevo jeje', 'jaja', 18, NULL, 10),
	(8, 'jojo', '123', 19, NULL, 1),
	(9, 'jojolete', 'paul es feeling', 50, NULL, 10),
	(10, 'mi paquete', 'sdsfsdf', 12, 19, 11),
	(11, 'nuevo paquete', 'este es un nuevo paquete bde prueba', 25, 20, 12),
	(12, 'nuevo paquete 2', 'este es un nuevo paquete bde prueba', 25, 20, 12),
	(13, 'nuevo paquete tareas 5', 'este es nuevo', 85, 21, 12),
	(14, 'Talleres', 'esta', 14, 22, 14),
	(15, 'paquete nuevo', 'nuevo paquete', 15, 25, 15),
	(16, 'paquete nuevo', 'nuevo paquete', 15, 25, 15),
	(17, 'paquete nuevo 2', 'nuevo paquete', 15, 25, 15),
	(18, 'paquete 1', 'descripcion', 12, 26, 16),
	(19, 'paquete 2', 'descripcion', 12, 26, 16),
	(20, 'hhhh', 'lkioh', 12, 26, 16),
	(21, 'Nuevo paquete', 'descripcion', 15, 27, 17),
	(22, 'Nuevo paquete 2', 'descripcion', 14, 27, 17),
	(23, 'Traer ponentes', 'descripcion', 15, 28, 18),
	(24, 'Gestionar bocaditos', 'descripcion', 14, 28, 18),
	(25, 'askdjnaksd', 'ljhsdlfkjs', 12, 29, 19),
	(26, 'paquete 2', 'dfgdsgsd', 34, 29, 19),
	(27, 'Nuevo paquete', 'paquete', 15, 30, 20),
	(28, 'nuevo paquete', 'decripcion', 15, 31, 21),
	(29, 'nuevo paquete 2', 'decripcion', 14, 31, 21),
	(30, 'nuevo paquete 2', 'decripcion', 14, 31, 21),
	(31, 'autentificacion', 'autentificacion', 5, 33, 23);
/*!40000 ALTER TABLE `appcuentas_work_package` ENABLE KEYS */;


-- Dumping structure for table ofisis.auth_group
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.auth_group: ~0 rows (approximately)
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;


-- Dumping structure for table ofisis.auth_group_permissions
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_425ae3c4` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_5886d21f` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.auth_group_permissions: ~0 rows (approximately)
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;


-- Dumping structure for table ofisis.auth_permission
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_1bb8f392` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.auth_permission: ~75 rows (approximately)
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add permission', 1, 'add_permission'),
	(2, 'Can change permission', 1, 'change_permission'),
	(3, 'Can delete permission', 1, 'delete_permission'),
	(4, 'Can add group', 2, 'add_group'),
	(5, 'Can change group', 2, 'change_group'),
	(6, 'Can delete group', 2, 'delete_group'),
	(7, 'Can add user', 3, 'add_user'),
	(8, 'Can change user', 3, 'change_user'),
	(9, 'Can delete user', 3, 'delete_user'),
	(10, 'Can add content type', 4, 'add_contenttype'),
	(11, 'Can change content type', 4, 'change_contenttype'),
	(12, 'Can delete content type', 4, 'delete_contenttype'),
	(13, 'Can add session', 5, 'add_session'),
	(14, 'Can change session', 5, 'change_session'),
	(15, 'Can delete session', 5, 'delete_session'),
	(16, 'Can add site', 6, 'add_site'),
	(17, 'Can change site', 6, 'change_site'),
	(18, 'Can delete site', 6, 'delete_site'),
	(19, 'Can add log entry', 7, 'add_logentry'),
	(20, 'Can change log entry', 7, 'change_logentry'),
	(21, 'Can delete log entry', 7, 'delete_logentry'),
	(22, 'Can add profile', 8, 'add_profile'),
	(23, 'Can change profile', 8, 'change_profile'),
	(24, 'Can delete profile', 8, 'delete_profile'),
	(25, 'Can add template', 9, 'add_template'),
	(26, 'Can change template', 9, 'change_template'),
	(27, 'Can delete template', 9, 'delete_template'),
	(28, 'Can add client', 10, 'add_client'),
	(29, 'Can change client', 10, 'change_client'),
	(30, 'Can delete client', 10, 'delete_client'),
	(31, 'Can add project', 11, 'add_project'),
	(32, 'Can change project', 11, 'change_project'),
	(33, 'Can delete project', 11, 'delete_project'),
	(34, 'Can add client_has_ project', 12, 'add_client_has_project'),
	(35, 'Can change client_has_ project', 12, 'change_client_has_project'),
	(36, 'Can delete client_has_ project', 12, 'delete_client_has_project'),
	(37, 'Can add group', 13, 'add_group'),
	(38, 'Can change group', 13, 'change_group'),
	(39, 'Can delete group', 13, 'delete_group'),
	(40, 'Can add group_has_ client', 14, 'add_group_has_client'),
	(41, 'Can change group_has_ client', 14, 'change_group_has_client'),
	(42, 'Can delete group_has_ client', 14, 'delete_group_has_client'),
	(43, 'Can add util', 15, 'add_util'),
	(44, 'Can change util', 15, 'change_util'),
	(45, 'Can delete util', 15, 'delete_util'),
	(46, 'Can add data', 16, 'add_data'),
	(47, 'Can change data', 16, 'change_data'),
	(48, 'Can delete data', 16, 'delete_data'),
	(49, 'Can add document', 17, 'add_document'),
	(50, 'Can change document', 17, 'change_document'),
	(51, 'Can delete document', 17, 'delete_document'),
	(52, 'Can add meeting', 18, 'add_meeting'),
	(53, 'Can change meeting', 18, 'change_meeting'),
	(54, 'Can delete meeting', 18, 'delete_meeting'),
	(55, 'Can add table', 19, 'add_table'),
	(56, 'Can change table', 19, 'change_table'),
	(57, 'Can delete table', 19, 'delete_table'),
	(58, 'Can add column', 20, 'add_column'),
	(59, 'Can change column', 20, 'change_column'),
	(60, 'Can delete column', 20, 'delete_column'),
	(61, 'Can add work_ package', 21, 'add_work_package'),
	(62, 'Can change work_ package', 21, 'change_work_package'),
	(63, 'Can delete work_ package', 21, 'delete_work_package'),
	(64, 'Can add task', 22, 'add_task'),
	(65, 'Can change task', 22, 'change_task'),
	(66, 'Can delete task', 22, 'delete_task'),
	(67, 'Can add comment', 23, 'add_comment'),
	(68, 'Can change comment', 23, 'change_comment'),
	(69, 'Can delete comment', 23, 'delete_comment'),
	(70, 'Can add image', 24, 'add_image'),
	(71, 'Can change image', 24, 'change_image'),
	(72, 'Can delete image', 24, 'delete_image'),
	(73, 'Can add check', 25, 'add_check'),
	(74, 'Can change check', 25, 'change_check'),
	(75, 'Can delete check', 25, 'delete_check');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;


-- Dumping structure for table ofisis.auth_user
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.auth_user: ~16 rows (approximately)
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` (`id`, `username`, `first_name`, `last_name`, `email`, `password`, `is_staff`, `is_active`, `is_superuser`, `last_login`, `date_joined`) VALUES
	(1, 'admin', 'Gabriel', '099999', '33444444444', 'pbkdf2_sha256$10000$DVKHlfe4iP47$uKYg2ZQa9Jzsv7O8qJrZlvillWPtUQJGqCkNQkrCB4c=', 1, 1, 1, '2012-11-26 23:41:55', '2012-07-28 06:38:04'),
	(2, 'manu', 'Jose', 'vega', 'manuelriosvega@gmail.com', 'pbkdf2_sha256$10000$BSm7fWVKqrir$xWCwdd6vBJTV2vNXaGd5GW2hAoBLnDEKj2NRTNgTAGQ=', 0, 1, 0, '2012-07-31 09:28:23', '2012-07-28 06:44:10'),
	(3, 'jose', 'Javier', 'Yanao', 'josemanu@hotmail.com', 'pbkdf2_sha256$10000$JmKew6om1OMg$loahr9ufqIaumUgNxf9dd9ldCGAoZceoHoWUs8dGc84=', 0, 1, 0, '2012-07-30 23:15:00', '2012-07-30 23:15:00'),
	(4, 'dick', 'dick', 'dick', 'dick@hotmail.com', 'dick', 0, 1, 0, '2012-07-31 08:27:29', '2012-07-31 08:27:29'),
	(5, 'wili', 'fredy', 'si puede', 'josei@hotmail.com', 'pbkdf2_sha256$10000$J4QswITlkx09$AfmuPzGOqteKLx1YW1QFhOzV+SSpTkQf0wLkY9whkWA=', 0, 1, 0, '2012-07-31 16:36:57', '2012-07-31 08:30:33'),
	(6, 'Williams', 'Williams', 'Days Lam', 'williams@gmail.com', 'pbkdf2_sha256$10000$NMcWLddnvspx$GWtMgsVfZjdNvvJxsOzadKXk9WVqgKD+Rng5Hcp+TkE=', 0, 1, 0, '2012-08-20 03:15:50', '2012-08-20 03:15:50'),
	(7, 'juan', 'juan', 'medina alfaro', 'juan@hotmail.com', 'pbkdf2_sha256$10000$zLtNVFmdlaQU$H2+g016NQJb7BsLFUso5wSDyw2XhG5vG9j4vLb2Cc1Q=', 0, 1, 0, '2012-08-20 04:27:08', '2012-08-20 03:16:33'),
	(8, 'mini', 'mini', 'Vega Valverde', 'mini@gmail.com', 'pbkdf2_sha256$10000$8YvagVY3OU5Z$Op7Xs4WxpR33r31UGH+dRn9dFTCrURcYPyS2sSl3INA=', 0, 1, 0, '2012-09-03 16:38:07', '2012-08-20 03:17:18'),
	(9, 'Maria', 'Maria', 'Valenzuela', 'maria@gmail.com', 'pbkdf2_sha256$10000$FmeEmXhme9D3$2jcyZfZ5YFze41JPJvxWS22rX9RPOu8M9iHG4E9+Mjg=', 0, 1, 0, '2012-08-20 03:38:29', '2012-08-20 03:38:29'),
	(10, 'Edson', 'Edson', 'Espinoza', 'edson@gmail.com', 'pbkdf2_sha256$10000$afXPiTIFnk6z$h3GGx64eT4gVhEMR/PZtcI8iqNp8PJjktZmZzA0B47k=', 0, 1, 0, '2012-08-20 03:39:02', '2012-08-20 03:39:02'),
	(12, 'wilimarjorie', 'wilimarjorie', 'manuel', 'wili_marjorie@hotmail.com', 'pbkdf2_sha256$10000$OExAeM0LR8zo$Mg1CjV/mwZnsEupRuJTBW/j9YeT2roXOkpOrpR9WmOs=', 0, 1, 0, '2012-11-09 01:02:18', '2012-11-09 01:02:07'),
	(13, 'cdscd', 'cdscd', '', '', '!', 0, 1, 0, '2012-11-12 21:47:04', '2012-11-12 21:47:04'),
	(14, 'josemanu', 'josemanu', 'mamanmsna', 'masns', 'pbkdf2_sha256$10000$F5B2sF5LrA8s$bqBP7o1FRCxB2uxtc+9NwREYHU3UVOMk7nO05Z/WOHE=', 0, 1, 0, '2012-11-12 22:07:12', '2012-11-12 22:07:12'),
	(15, 'jorge', 'jorge', 'jorge', 'jorge', 'pbkdf2_sha256$10000$t5pbMLPQzyyy$drkn3vQP7otANxQOGUNa8C2shSoH2piE/3woU54zXPs=', 0, 1, 0, '2012-11-12 22:19:14', '2012-11-12 22:19:14'),
	(16, 'laredo', 'laredo', 'laredo', 'laredo', 'pbkdf2_sha256$10000$0Ntx4wVImoK3$Rh2l87YLz2Dlafz75jhVH3YqyZSi4z+bbCo9pLR3/R0=', 0, 1, 0, '2012-11-12 22:20:15', '2012-11-12 22:20:15'),
	(17, 'josemanuel1', 'josemanuel1', 'Rios Vega', 'manuelriosvega1@gmail.com', 'pbkdf2_sha256$10000$jpultRhzh4vo$1TROLNZfOJIadIHCCjsbV7+w07VlK/cZXxsltkI9gvI=', 0, 1, 0, '2012-11-30 01:07:09', '2012-11-30 01:06:52');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;


-- Dumping structure for table ofisis.auth_user_groups
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_403f60f` (`user_id`),
  KEY `auth_user_groups_425ae3c4` (`group_id`),
  CONSTRAINT `group_id_refs_id_f116770` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_7ceef80f` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.auth_user_groups: ~0 rows (approximately)
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;


-- Dumping structure for table ofisis.auth_user_user_permissions
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_403f60f` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_dfbab7d` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.auth_user_user_permissions: ~0 rows (approximately)
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;


-- Dumping structure for table ofisis.django_admin_log
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_403f60f` (`user_id`),
  KEY `django_admin_log_1bb8f392` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_288599e6` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c8665aa` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.django_admin_log: ~22 rows (approximately)
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` (`id`, `action_time`, `user_id`, `content_type_id`, `object_id`, `object_repr`, `action_flag`, `change_message`) VALUES
	(1, '2012-07-28 06:40:28', 1, 8, '1', 'normal', 1, ''),
	(2, '2012-07-28 06:41:46', 1, 10, '1', 'admin', 1, ''),
	(3, '2012-07-28 06:44:10', 1, 3, '2', 'manu', 1, ''),
	(4, '2012-07-28 06:46:30', 1, 3, '2', 'manu', 2, 'Changed password, first_name, last_name and email.'),
	(5, '2012-07-28 06:47:01', 1, 10, '2', 'manu', 1, ''),
	(6, '2012-07-28 07:42:17', 1, 11, '1', 'project manu', 1, ''),
	(7, '2012-07-28 08:37:45', 1, 19, '1', 'Por hacer', 1, ''),
	(8, '2012-07-28 08:38:03', 1, 19, '1', 'Primera Iteracion', 2, 'Changed name.'),
	(9, '2012-07-28 08:38:24', 1, 19, '2', 'Segunda Iteracion', 1, ''),
	(10, '2012-07-28 08:39:10', 1, 20, '1', 'Por hacer', 1, ''),
	(11, '2012-07-28 08:39:34', 1, 20, '2', 'Haciendo', 1, ''),
	(12, '2012-07-28 08:39:49', 1, 20, '3', 'terminadas', 1, ''),
	(13, '2012-07-28 08:40:01', 1, 20, '4', 'columna 1', 1, ''),
	(14, '2012-07-28 08:42:32', 1, 21, '1', 'Paquete_tarea prueba', 1, ''),
	(15, '2012-07-28 08:43:21', 1, 22, '1', 'Task 11', 1, ''),
	(16, '2012-07-29 21:06:11', 1, 11, '2', 'Plantilla basica', 1, ''),
	(17, '2012-07-30 23:15:00', 1, 3, '3', 'jose', 1, ''),
	(18, '2012-07-30 23:15:28', 1, 3, '3', 'jose', 2, 'Changed password and email.'),
	(19, '2012-07-30 23:15:53', 1, 10, '3', 'jose', 1, ''),
	(20, '2012-07-31 00:42:16', 1, 18, '1', 'nueva reunioj', 1, ''),
	(21, '2012-08-20 03:25:45', 1, 3, '1', 'admin', 2, 'Changed password, first_name and last_name.'),
	(22, '2012-08-20 03:26:09', 1, 3, '3', 'jose', 2, 'Changed password, first_name and last_name.');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;


-- Dumping structure for table ofisis.django_content_type
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.django_content_type: ~25 rows (approximately)
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
	(1, 'permission', 'auth', 'permission'),
	(2, 'group', 'auth', 'group'),
	(3, 'user', 'auth', 'user'),
	(4, 'content type', 'contenttypes', 'contenttype'),
	(5, 'session', 'sessions', 'session'),
	(6, 'site', 'sites', 'site'),
	(7, 'log entry', 'admin', 'logentry'),
	(8, 'profile', 'appcuentas', 'profile'),
	(9, 'template', 'appcuentas', 'template'),
	(10, 'client', 'appcuentas', 'client'),
	(11, 'project', 'appcuentas', 'project'),
	(12, 'client_has_ project', 'appcuentas', 'client_has_project'),
	(13, 'group', 'appcuentas', 'group'),
	(14, 'group_has_ client', 'appcuentas', 'group_has_client'),
	(15, 'util', 'appcuentas', 'util'),
	(16, 'data', 'appcuentas', 'data'),
	(17, 'document', 'appcuentas', 'document'),
	(18, 'meeting', 'appcuentas', 'meeting'),
	(19, 'table', 'appcuentas', 'table'),
	(20, 'column', 'appcuentas', 'column'),
	(21, 'work_ package', 'appcuentas', 'work_package'),
	(22, 'task', 'appcuentas', 'task'),
	(23, 'comment', 'appcuentas', 'comment'),
	(24, 'image', 'appcuentas', 'image'),
	(25, 'check', 'appcuentas', 'check');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;


-- Dumping structure for table ofisis.django_session
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_3da3d3d8` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.django_session: ~7 rows (approximately)
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
	('18604c299a94fbb4ea12516f8d62b01b', 'NDgwNmI5OTMzODhlNmUxOGNiY2IzNjg0ZDk2Mjg5NWViYWJlNjc4OTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQh1Lg==\n', '2012-09-08 16:04:03'),
	('6247b463a68ab7ef68e1efc3f7666845', 'NzU1M2I1YjVhMWM1MjJhYzNlMWU3ZWVkN2NiZDdkYTMwMzFmMzkyNzqAAn1xAShVDV9hdXRoX3Vz\nZXJfaWSKAQhVEl9hdXRoX3VzZXJfYmFja2VuZFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxAnUu\n', '2012-09-05 22:58:24'),
	('632ed2e110f35fd273ac0a94c9ac2b65', 'NzU1M2I1YjVhMWM1MjJhYzNlMWU3ZWVkN2NiZDdkYTMwMzFmMzkyNzqAAn1xAShVDV9hdXRoX3Vz\nZXJfaWSKAQhVEl9hdXRoX3VzZXJfYmFja2VuZFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxAnUu\n', '2012-09-17 16:38:07'),
	('6b4e1384d8bf0535198075266c9cd9f0', 'NTg1MzlkZDlhZGRmYjA2NmY2YWFmZjJkYTRkNDI2YmU1ZGYwYTBiMjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQV1Lg==\n', '2012-08-14 14:08:55'),
	('b9315a8da1ac6c14de0ac55d2aaef553', 'ZGEyNmUwZjAyNmIxODliMzFjOTBmYjFkNzUzNmRlZjMyZTYyMTQ3ODqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKARF1Lg==\n', '2012-12-14 01:07:09'),
	('cdc05886c20d6d5bf7deb68a8301ba7d', 'YTczMzdlMTYwMmE2OWMwYTNjM2JlM2JmMmMzNjgzMjgzZjc2NTY4OTqAAn1xAShVDV9hdXRoX3Vz\nZXJfaWSKAQVVEl9hdXRoX3VzZXJfYmFja2VuZFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxAnUu\n', '2012-08-14 16:36:57'),
	('f9f6b1424bf9fa1b706753f47d4f6985', 'NzFhZGVmM2E2ZmExMTFhMTFkYWM4ZGZjM2E2OTAzNDMwY2IxNTEyMjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmRVDV9h\ndXRoX3VzZXJfaWSKAQx1Lg==\n', '2012-11-26 22:20:16');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;


-- Dumping structure for table ofisis.django_site
CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Dumping data for table ofisis.django_site: ~1 rows (approximately)
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
	(1, 'example.com', 'example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
/*!40014 SET FOREIGN_KEY_CHECKS=1 */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
