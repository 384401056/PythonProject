/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50619
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50619
File Encoding         : 65001

Date: 2017-11-13 09:20:22
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for tb_color
-- ----------------------------
DROP TABLE IF EXISTS `tb_color`;
CREATE TABLE `tb_color` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `color_name` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_color
-- ----------------------------
INSERT INTO `tb_color` VALUES ('1', '红色');
INSERT INTO `tb_color` VALUES ('2', '黄色');
INSERT INTO `tb_color` VALUES ('3', '蓝色');
INSERT INTO `tb_color` VALUES ('4', '绿色');
INSERT INTO `tb_color` VALUES ('5', '紫色');
INSERT INTO `tb_color` VALUES ('6', '粉色');

-- ----------------------------
-- Table structure for tb_dept
-- ----------------------------
DROP TABLE IF EXISTS `tb_dept`;
CREATE TABLE `tb_dept` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dept_name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

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
