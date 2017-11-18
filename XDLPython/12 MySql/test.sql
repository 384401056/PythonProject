/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50619
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50619
File Encoding         : 65001

Date: 2017-11-18 14:05:26
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for tb_account
-- ----------------------------
DROP TABLE IF EXISTS `tb_account`;
CREATE TABLE `tb_account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account` varchar(20) NOT NULL,
  `overage` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_account
-- ----------------------------
INSERT INTO `tb_account` VALUES ('1', 'jack', '800');
INSERT INTO `tb_account` VALUES ('2', 'rose', '1200');

-- ----------------------------
-- Table structure for tb_college
-- ----------------------------
DROP TABLE IF EXISTS `tb_college`;
CREATE TABLE `tb_college` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_tb_College_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_college
-- ----------------------------
INSERT INTO `tb_college` VALUES ('1', '云南大学');
INSERT INTO `tb_college` VALUES ('2', '北京大学');

-- ----------------------------
-- Table structure for tb_color
-- ----------------------------
DROP TABLE IF EXISTS `tb_color`;
CREATE TABLE `tb_color` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `color_name` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_color
-- ----------------------------
INSERT INTO `tb_color` VALUES ('1', '红色');
INSERT INTO `tb_color` VALUES ('2', '黄色');
INSERT INTO `tb_color` VALUES ('3', '蓝色');
INSERT INTO `tb_color` VALUES ('4', '绿色');
INSERT INTO `tb_color` VALUES ('5', '紫色');
INSERT INTO `tb_color` VALUES ('6', '粉色');
INSERT INTO `tb_color` VALUES ('7', '彩虹色');
INSERT INTO `tb_color` VALUES ('8', '彩虹色');
INSERT INTO `tb_color` VALUES ('9', '神谷科技');

-- ----------------------------
-- Table structure for tb_dept
-- ----------------------------
DROP TABLE IF EXISTS `tb_dept`;
CREATE TABLE `tb_dept` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dept_name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_dept
-- ----------------------------
INSERT INTO `tb_dept` VALUES ('1', '产品部');
INSERT INTO `tb_dept` VALUES ('2', '研发部');
INSERT INTO `tb_dept` VALUES ('3', '销售部');
INSERT INTO `tb_dept` VALUES ('4', '工程部');
INSERT INTO `tb_dept` VALUES ('5', '行政部');
INSERT INTO `tb_dept` VALUES ('6', '总经办');
INSERT INTO `tb_dept` VALUES ('7', '董事会');
INSERT INTO `tb_dept` VALUES ('8', '财务部');
INSERT INTO `tb_dept` VALUES ('9', '彩虹色');
INSERT INTO `tb_dept` VALUES ('10', '神谷科技');

-- ----------------------------
-- Table structure for tb_group
-- ----------------------------
DROP TABLE IF EXISTS `tb_group`;
CREATE TABLE `tb_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_tb_group_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_group
-- ----------------------------

-- ----------------------------
-- Table structure for tb_learner
-- ----------------------------
DROP TABLE IF EXISTS `tb_learner`;
CREATE TABLE `tb_learner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `college_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `age` (`age`),
  KEY `college_id` (`college_id`),
  KEY `ix_tb_learner_name` (`name`),
  CONSTRAINT `tb_learner_ibfk_1` FOREIGN KEY (`college_id`) REFERENCES `tb_college` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_learner
-- ----------------------------
INSERT INTO `tb_learner` VALUES ('1', '小明', '20', '2');
INSERT INTO `tb_learner` VALUES ('2', '小红', '30', '1');

-- ----------------------------
-- Table structure for tb_myuser
-- ----------------------------
DROP TABLE IF EXISTS `tb_myuser`;
CREATE TABLE `tb_myuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_myuser
-- ----------------------------

-- ----------------------------
-- Table structure for tb_server
-- ----------------------------
DROP TABLE IF EXISTS `tb_server`;
CREATE TABLE `tb_server` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_tb_server_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_server
-- ----------------------------

-- ----------------------------
-- Table structure for tb_servertogroup
-- ----------------------------
DROP TABLE IF EXISTS `tb_servertogroup`;
CREATE TABLE `tb_servertogroup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) DEFAULT NULL,
  `server_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `group_id` (`group_id`),
  KEY `server_id` (`server_id`),
  CONSTRAINT `tb_servertogroup_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `tb_group` (`id`),
  CONSTRAINT `tb_servertogroup_ibfk_2` FOREIGN KEY (`server_id`) REFERENCES `tb_server` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_servertogroup
-- ----------------------------

-- ----------------------------
-- Table structure for tb_student
-- ----------------------------
DROP TABLE IF EXISTS `tb_student`;
CREATE TABLE `tb_student` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `age` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_student
-- ----------------------------

-- ----------------------------
-- Table structure for tb_tch_stu_relation
-- ----------------------------
DROP TABLE IF EXISTS `tb_tch_stu_relation`;
CREATE TABLE `tb_tch_stu_relation` (
  `id` int(11) NOT NULL,
  `tch_id` int(11) NOT NULL,
  `stu_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tch_id` (`tch_id`),
  KEY `stu_id` (`stu_id`),
  CONSTRAINT `tb_tch_stu_relation_ibfk_1` FOREIGN KEY (`tch_id`) REFERENCES `tb_teacher` (`id`),
  CONSTRAINT `tb_tch_stu_relation_ibfk_2` FOREIGN KEY (`stu_id`) REFERENCES `tb_student` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_tch_stu_relation
-- ----------------------------

-- ----------------------------
-- Table structure for tb_teacher
-- ----------------------------
DROP TABLE IF EXISTS `tb_teacher`;
CREATE TABLE `tb_teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `age` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_teacher
-- ----------------------------

-- ----------------------------
-- Table structure for tb_user
-- ----------------------------
DROP TABLE IF EXISTS `tb_user`;
CREATE TABLE `tb_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `age` int(10) NOT NULL,
  `department` int(11) DEFAULT NULL,
  `color` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department` (`department`),
  KEY `color` (`color`),
  CONSTRAINT `tb_user_ibfk_1` FOREIGN KEY (`department`) REFERENCES `tb_dept` (`id`),
  CONSTRAINT `tb_user_ibfk_2` FOREIGN KEY (`color`) REFERENCES `tb_color` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_user
-- ----------------------------
INSERT INTO `tb_user` VALUES ('13', 'aaa', '10', '1', '6');
INSERT INTO `tb_user` VALUES ('14', 'bbb', '20', '1', '6');
INSERT INTO `tb_user` VALUES ('15', 'ccc', '30', '2', '5');
INSERT INTO `tb_user` VALUES ('16', 'ddd', '40', '3', '6');
INSERT INTO `tb_user` VALUES ('17', 'eee', '50', null, '6');
INSERT INTO `tb_user` VALUES ('19', 'fff', '60', '5', '3');

-- ----------------------------
-- Table structure for tb_user_other
-- ----------------------------
DROP TABLE IF EXISTS `tb_user_other`;
CREATE TABLE `tb_user_other` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nam` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_user_other
-- ----------------------------
INSERT INTO `tb_user_other` VALUES ('13', 'd');
INSERT INTO `tb_user_other` VALUES ('14', 'd');

-- ----------------------------
-- View structure for v1
-- ----------------------------
DROP VIEW IF EXISTS `v1`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost`  VIEW `v1` AS SELECT * from tb_user ;

-- ----------------------------
-- Procedure structure for proc_p1
-- ----------------------------
DROP PROCEDURE IF EXISTS `proc_p1`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `proc_p1`()
BEGIN
	SELECT * FROM tb_user;
END
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for proc_p2
-- ----------------------------
DROP PROCEDURE IF EXISTS `proc_p2`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `proc_p2`(in il int)
BEGIN
	DECLARE d1 int;
	DECLARE d2 int DEFAULT 4;
	set d1 = il+d2;
	SELECT * from tb_user WHERE id = d1;
END
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for proc_p3
-- ----------------------------
DROP PROCEDURE IF EXISTS `proc_p3`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `proc_p3`(
	in i1 int,
	out i2 int, -- 存储过程的返回变量
	inout i3 int  -- 既可以当返回值，又可传入参数
)
BEGIN
	set i2 = i1 + 100; -- out结果
	SELECT * from tb_user; -- 查询结果
END
;;
DELIMITER ;

-- ----------------------------
-- Function structure for func_f1
-- ----------------------------
DROP FUNCTION IF EXISTS `func_f1`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `func_f1`(
	i1 int, -- 参数
	i2 int
) RETURNS int(11)
BEGIN
	DECLARE num int;
	set num = i1 + i2;
	RETURN(num);
END
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `tri_before_insert_tb_color`;
DELIMITER ;;
CREATE TRIGGER `tri_before_insert_tb_color` BEFORE INSERT ON `tb_color` FOR EACH ROW BEGIN
	INSERT INTO tb_dept(dept_name) VALUES(NEW.color_name); -- NEW是指在tb_color中插入的数据。
END
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `tri_before_insert_tb_user`;
DELIMITER ;;
CREATE TRIGGER `tri_before_insert_tb_user` BEFORE INSERT ON `tb_user` FOR EACH ROW BEGIN
	INSERT INTO tb_color(color_name) VALUES('彩虹色');
END
;;
DELIMITER ;
