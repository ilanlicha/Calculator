DROP TABLE IF EXISTS `operation`;
CREATE TABLE IF NOT EXISTS `operation` (
  `ID` int(11) NOT NULL ,
  `formule` varchar(255) DEFAULT NULL,
  `calcul` varchar(255) DEFAULT NULL,
  `resultat` varchar(255) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ;

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `ID` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` varchar(50) NOT NULL DEFAULT '0',
  `password` varchar(64) NOT NULL DEFAULT '0',
  `quote` varchar(50) NOT NULL DEFAULT '0',
  `idUser` int(11),
  CONSTRAINT fk_image_user          -- On donne un nom à notre clé
        FOREIGN KEY (idUser)             -- Colonne sur laquelle on crée la clé
        REFERENCES User(ID)
);
