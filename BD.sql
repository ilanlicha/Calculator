DROP TABLE IF EXISTS `operation`;
CREATE TABLE IF NOT EXISTS `operation` (
  `ID` INTEGER PRIMARY KEY AUTOINCREMENT,
  `formule` varchar DEFAULT NULL,
  `resultat` varchar DEFAULT NULL,
  `idUser` int,
  FOREIGN KEY (idUser) REFERENCES User(ID)
) ;

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `ID` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` varchar NOT NULL DEFAULT '0',
  `password` varchar NOT NULL DEFAULT '0',
  `quote` varchar NOT NULL DEFAULT '0',
  `favorite_operation` varchar,
  CONSTRAINT fk_image_user
);

DROP TABLE IF EXISTS `mathematician`;
CREATE TABLE IF NOT EXISTS `mathematician` (
  `ID` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` varchar,
  `description` varchar,
  `born` varchar,
  `died` varchar,
  `contributions` varchar
);

INSERT INTO mathematician (name, description, born, died, contributions)
VALUES (
"Euclid"
,"Euclid, sometimes called Euclid of Alexandria to distinguish him from Euclid of Megara, was a Greek mathematician, often referred to as the ""founder of geometry"" or the ""father of geometry"". He was active in Alexandria during the reign of Ptolemy I (323–283 BC)."
,"Mid-4th century BC"
,"Mid-3rd century BC"
,"His Elements is one of the most influential works in the history of mathematics, serving as the main textbook for teaching mathematics (especially geometry) from the time of its publication until the late 19th or early 20th century. In the Elements, Euclid deduced the theorems of what is now called Euclidean geometry from a small set of axioms. Euclid also wrote works on perspective, conic sections, spherical geometry, number theory, and mathematical rigor."
);

INSERT INTO mathematician (name, description, born, died, contributions)
VALUES (
"Pythagoras"
,"Pythagoras of Samos was an ancient Ionian Greek philosopher and the eponymous founder of Pythagoreanism. His political and religious teachings were well known in Magna Graecia and influenced the philosophies of Plato, Aristotle, and, through them, Western philosophy."
,"570 BC"
,"495 BC"
,"According to Aristotle, the Pythagoreans used mathematics for solely mystical reasons, devoid of practical application. They believed that all things were made of numbers. The number one (the monad) represented the origin of all things and the number two (the dyad) represented matter. The number three was an ""ideal number"" becauseit had a beginning, middle, and end and was the smallest number of points that could be used to define a plane triangle, which they revered as a symbol of the god Apollo. The number four signified the four seasons and the four elements. The number seven was also sacred because it was the number of planets and the number of strings on a lyre, and because Apollo's birthday was celebrated on the seventh day of each month.They believed that odd numbers were masculine, that even numbers were feminine, and that the number five represented marriage, because it was the sum of two and three."
);

INSERT INTO mathematician (name, description, born, died, contributions)
VALUES (
"Thales of Miletus"
,"Thales of Miletus was a Greek mathematician, astronomer and pre-Socratic philosopher from Miletus in Ionia, Asia Minor. He was one of the Seven Sages of Greece. Many, most notably Aristotle, regarded him as the first philosopher in the Greek tradition, and he is otherwise historically recognized as the first individual known to have entertained and engaged in scientific philosophy. He is often referred to as the Father of Science."
,"626/623 BC"
,"548/545 BC"
,"Thales was known for his innovative use of geometry. His understanding was theoretical as well as practical. For example, he said: Megiston topos: apanta gar chorei (Μέγιστον τόπος· ἄπαντα γὰρ χωρεῖ.) The greatest is space, for it holds all things. Topos is in Newtonian-style space, since the verb, chorei, has the connotation of yielding before things, or spreading out to make room for them, which is extension. Within this extension, things have a position. Points, lines, planes and solids related by distances and angles follow from this presumption. Thales understood similar triangles and right triangles, and what is more, used that knowledge in practical ways. The story is told in Diogenes Laërtius (loc. cit.) that he measured the height of the pyramids by their shadows at the moment when his own shadow was equal to his height. A right triangle with two equal legs is a 45-degree right triangle, all of which are similar. The length of the pyramid's shadow measured from the center of the pyramid at that moment must have been equal to its height. This story indicates that he was familiar with the Egyptian seked, or seqed, the ratio of the run to the rise of a slope (cotangent). The seked is at the base of problems 56, 57, 58, 59 and 60 of the Rhind papyrus — an ancient Egyptian mathematical document. More practically Thales used the same method to measure the distances of ships at sea, said Eudemus as reported by Proclus ('in Euclidem'). According to Kirk & Raven (reference cited below), all you need for this feat is three straight sticks pinned at one end and knowledge of your altitude. One stick goes vertically into the ground. A second is made level. With the third you sight the ship and calculate the seked from the height of the stick and its distance from the point of insertion to the line of sight (Proclus, In Euclidem, 352)."
);

INSERT INTO mathematician (name, description, born, died, contributions)
VALUES (
"Al-Khwarizmi"
,"Muhammad Ibn Musa al-Khuwarizmi, généralement appelé Al-Khwarismi (latinisé en Algoritmi ou Algorizmi), est un mathématicien, géographe, astrologue et astronome persan, membre de la Maison de la sagesse de Bagdad. Ses écrits, rédigés en langue arabe, puis traduits en latin à partir du XIIe siècle, ont permis l'introduction de l'algèbre en Europe. Sa vie s'est déroulée en totalité à l'époque de la dynastie abbasside."
,"780"
,"850"
,"Al-Khwârismî est l'auteur de plusieurs ouvrages de mathématiques. Le plus célèbre, intitulé Kitābu 'l-mukhtaṣar fī ḥisābi 'l-jabr wa'l-muqābalah,  ou Abrégé du calcul par la restauration et la comparaison, publié sous le règne d'Al-Ma’mūn (813-833), « est considéré comme le premier manuel d'algèbre7 ». Ce livre contient six chapitres. Il ne contient aucun chiffre. Toutes les équations sont exprimées avec des mots. Le carré de l'inconnue est nommé « le carré » ou mâl, l'inconnue est « la chose » ou shay (šay), la racine est le jidhr, la constante est le dirham ou adǎd. Al-Khwârismî définit ainsi six équations canoniques auxquelles peuvent être ramenés les problèmes concrets d'héritage, d'arpentage des terres, ou de transactions commerciales. Par exemple, l'équation « des biens sont égaux aux racines » équivaudrait de nos jours à une équation de la forme. Le terme al-jabr est repris par les Européens et devient plus tard le mot algèbre."
);