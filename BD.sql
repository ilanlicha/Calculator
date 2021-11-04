DROP TABLE IF EXISTS `operation`;
CREATE TABLE IF NOT EXISTS `operation` (
  `ID` INTEGER PRIMARY KEY AUTOINCREMENT,
  `formule` varchar(255) DEFAULT NULL,
  `calcul` varchar(255) DEFAULT NULL,
  `resultat` varchar(255) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `idUser` int(11),
  FOREIGN KEY (idUser) REFERENCES User(ID)
) ;

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `ID` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` varchar(50) NOT NULL DEFAULT '0',
  `password` varchar(50) NOT NULL DEFAULT '0',
  `quote` varchar(50) NOT NULL DEFAULT '0',
  `favorite_operation` varchar(50),
  CONSTRAINT fk_image_user          -- On donne un nom à notre clé    -- Colonne sur laquelle on crée la clé      
);