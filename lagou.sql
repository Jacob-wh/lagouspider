# Host: localhost  (Version 5.5.5-10.1.19-MariaDB)
# Date: 2018-02-05 21:35:25
# Generator: MySQL-Front 6.0  (Build 2.20)


#
# Structure for table "position"
#

CREATE TABLE `position` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `companyName` varchar(255) DEFAULT NULL,
  `positionName` varchar(255) DEFAULT NULL,
  `positionIntro` varchar(255) DEFAULT NULL,
  `positionLabel` varchar(255) DEFAULT NULL,
  `workResponsibility` varchar(255) DEFAULT NULL,
  `positionWelfare` varchar(255) DEFAULT NULL,
  `workAddress` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;

#
# Data for table "position"
#

INSERT INTO `position` VALUES (24,'comp:any[Name','positi onN/ame','posi.tio~nIntro','positionLabel','workResponsibility','position-Welfare','workAddress'),(25,'comp:any[Name','positi o~nN/ame','posi.tio~nIntro','positionLabel','workResponsibility','position-Welfare','workAddress');
