--
-- Création de la base de données :
--

DROP DATABASE IF EXISTS Association;

CREATE DATABASE Association CHARACTER SET 'utf8';

USE Association;

--
-- Création des tables :
--

CREATE TABLE Eleve (
	elv_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	elv_nom VARCHAR(30) NOT NULL,
    elv_prenom VARCHAR(30) NOT NULL,
	elv_dans_quelle_annee int UNSIGNED NOT NULL,
	elv_sexe CHAR(1),
	elv_present_asso VARCHAR(50),
	PRIMARY KEY (elv_id)
)
ENGINE=INNODB;



CREATE TABLE Evenement (
	evm_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	evm_nom VARCHAR(30) NOT NULL,
	evm_date DATE,
	evm_dsc VARCHAR(100),
	evm_lieu VARCHAR(30),
	PRIMARY KEY (evm_id)
)
ENGINE=INNODB;


CREATE TABLE Association (
	asc_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	asc_nom VARCHAR(50) NOT NULL,
    asc_nom_president varchar(50),
    asc_eleve_appartient varchar(50),
	asc_dsc VARCHAR(50),
	asc_local VARCHAR(10),
	PRIMARY KEY (association_id),
	CONSTRAINT fk_asc_eleve_appartient FOREIGN KEY (asc_eleve_appartient) REFERENCES Association(asc_id) ON DELETE SET NULL
)
ENGINE=INNODB;


CREATE TABLE Participer_a (
	prt_eleve int UNSIGNED NOT NULL,
	prt_association INT UNSIGNED NOT NULL,
	CONSTRAINT pk_Participer_a PRIMARY KEY(prt_eleve, prt_association),
	CONSTRAINT fk_prt_eleve FOREIGN KEY (prt_eleve) REFERENCES Elève(elv_id),
	CONSTRAINT fk_prt_association FOREIGN KEY (prt_association) REFERENCES Association(asc_id)
)
ENGINE=INNODB;


--
-- Insertion de valeurs dans les tables :
--

INSERT INTO Eleve
VALUES	(1, 'FONDA', 'Henry', 1, 'M', 'CLUB VOILE'),
	(2, 'LEIGH', 'Viven', 1, 'F', 'ESIG''ELECTRONIX'),
	(3, 'FORD', 'Harrison', 5, 'M', 'BSBG_DE SUSTAINABLE'),
	(4, 'HAMIL', 'Mark', 5, 'M', 'BDE OLYMPE'),
	(5, 'WINSLET', 'Kate', 4, 'F', 'BDE OLYMPE'),
	(6, 'DI CAPRIO', 'Leonardo', 3, 'M', 'LA TORTUE DECHAINEE'),
	(7, 'CONNERY', 'Sean', 3, 'M', 'ESIG''4L'),
	(8, 'BRONSON', 'Charles', 2, 'M', 'KICK & BEAT'),
	(9, 'FONDA', 'Jane', 1, 'F', 'ESIG''BOUTIK'),
	(10, 'FONDA', 'Peter', 1, 'M', 'J2E'),
	(11, 'COPPOLA', 'Sofia', 5, 'F', 'ESIG''SOLIDAIRE'),
	(12, 'ALLEN', 'Woody', 4, 'M', 'J2E'),
	(13, 'FONDA', 'Bridget', 2, 'F', 'Bureau des Elèves'),
	(14, 'DUJARDIN', 'Jean', 3, 'M', 'ESIG''COMPUTER'),
	(15, 'DELON', 'Alain', 5, 'M', 'GSIG''TIR'),
	(16, 'DEPARDIEU', 5, '1948-12-27', 'M', 'LA CUISINE DES MOUSQUETAIRES'),
	(17, 'DELON', 'Anthony', 2, 'M', 'GSIG''TIR'),
	(18, 'DEPARDIEU', 'Guillaume', 3, 'M', 'FREEDOM'),
	(19, 'DEPARDIEU', 'Julie', 1, 'F', 'LE GALA'),
    (0,'nomtest','prénomtest',0,'F','assotest');




INSERT INTO Evenement
VALUES	(1, 'Course de l''Aventure', 'Le samedi matin de 8h à 10h', 'Exploration en courant', 'Réserve naturelle à proximité'),
	(2, 'Fête de la Connaissance', 'Tous les jeudis après-midi de 15h à 17h', 'Partage et découverte', 'Hall de l''école'),
	(3, 'Soirée Créative', 'Le dernier vendredi de chaque mois de 19h à 22h', 'Expression artistique', 'Centre communautaire'),
	(4, 'Nuit Étoilée', 'Tous les trimestres, le samedi soir de 20h à minuit', 'Célébration et divertissement', 'Salle de réception du centre-ville'),
	(5, 'Chant Harmonieux', 'Tous les mercredis soir de 19h à 21h', 'Partage de la musique','Salle de musique'),
	(6, 'Rythmes Urbains', 'Tous les vendredis après-midi de 16h à 18h','Exploration des paroles', 'Centre d''activités étudiantes'),
	(7, 'Exploration Africaine', 'Tous les lundis soir de 18h30 à 20h30', 'Découverte de la diversité culturelle', 'Salle polyvalente'),
	(8, 'Exploration Culturelle', 'Tous les jeudis après-midi de 15h à 17h', 'Découverte de différentes cultures', 'Salle de réunion de la bibliothèque'),
	(9, 'Rythmes Endiablés', 'Tous les mardis soir de 20h à 22h', 'Exploration de la danse', 'Gymnase'),
	(10, 'Esprit d''Équipe', 'Tous les mercredis après-midi de 16h à 18h', 'Encouragement et énergie','Gymnase'),
	(11, 'Jeu Passionnant', 'Tous les mercredis soir de 19h à 21h', 'Exploration des jeux', 'Salle de détente étudiante'),
	(12, 'Études Renforcées', 'Tous les mardis après-midi de 15h à 17h', 'Soutien académique', 'Salle d''étude de la bibliothèque'),
	(13, 'Aventure en Plein Air', 'Le deuxième week-end de chaque mois', 'Exploration de la nature', 'Terrain de camping en périphérie'),
	(14, 'Balade à Deux Roues', 'Tous les samedis matin de 10h à 12h', 'Exploration de la région', 'Place devant l''école'),
	(15, 'Course Palpitante', 'Une fois par mois, le dimanche après-midi de 14h à 16h', 'Compétition amicale', 'Circuit de karting'),
	(16, 'Navigation Aquatique', 'Tous les mercredis après-midi de 16h à 18h', 'Découverte de la voile', 'Ponton au bord du lac'),
	(17, 'Études Préparatoires', 'Tous les vendredis soir de 17h à 19h', 'Préparation aux études supérieures', 'Centre d''études'),
	(18, 'Robotique Innovante', 'Tous les mercredis soir de 19h à 21h', 'Exploration de la technologie', 'Laboratoire de technologie'),
	(19, 'Dégustation Gourmande', 'Tous les vendredis soir de 18h à 20h', 'Exploration culinaire', 'Cuisine gastronomique'),
	(20, 'Vol en Haute Altitude', 'Tous les samedis matin de 9h à 11h', 'Découverte de l''aviation', 'Terrain d''aviation'),	
    (21, 'Journalisme Actif', 'Tous les lundis après-midi de 16h à 18h', 'Exploration de l''actualité', 'Centre médiatique étudiant'),
	(22, 'Exploration Maritime', 'Tous les mercredis après-midi de 15h à 17h', 'Découverte de la navigation', 'Quai au bord de la mer'),
	(23, 'Écologie Engagée', 'Tous les jeudis matin de 10h à 12h', 'Protection de l''environnement', 'Réserve naturelle'),
    (24, 'Solidarité Ensemble', 'Tous les mardis après-midi de 14h à 16h', 'Aide communautaire', 'Centre communautaire'),
	(25, 'Relations Étudiantes', 'Tous les vendredis soir de 19h à 21h', 'Socialisation étudiante', 'Centre d''activités étudiantes'),
	(26, 'Stratégie d''Échecs', 'Tous les mercredis soir de 18h à 20h', 'Exploration du jeu d''échecs', 'Salle de jeux d''échecs'),
    (27, 'Informatique Avancée', 'Tous les lundis après-midi de 15h à 17h', 'Exploration de la technologie informatique', 'Laboratoire d''informatique'),
	(28, 'Prévention Ensemble', 'Une fois par mois, le vendredi soir de 19h à 21h', 'Sensibilisation à la prévention', 'Auditorium de l''école'),	
    (29, 'Égalité Sociale', 'Tous les jeudis après-midi de 17h à 19h', 'Lutte contre les inégalités', 'Salle de débat des sciences sociales'),
	(30, 'Capture Artistique', 'Tous les vendredis après-midi de 16h à 18h', 'Exploration de la photographie', 'Studio de photographie'),
	(31, 'Spectacle de Rouleau', 'Tous les mercredis soir de 19h à 21h', 'Exploration du théâtre de rouleau', 'Centre des arts de la scène'),
    (32, 'Aide Solidaire', 'Selon besoin', 'Support aux groupes scolaires', 'Dans différents endroits de l''école'),
	(33, 'Théâtre Créatif', 'Tous les mardis soir de 18h à 20h', 'Exploration du théâtre', 'Théâtre de l''école'),
	(34, 'Tir Précis', 'Tous les samedis matin de 10h à 12h', 'Exploration du tir', 'Stand de tir') ;


INSERT INTO Association
VALUES	(1, 'BDE OLYMPE', 'LANDAU Jon',932, ' BDS', 3, 'Drame', ' H110'),
	(2,'Bureau des Elèves ', 'LUMET Sidney', 65, 'BDE CPIi', 'H111'),
	(3, 'Bureau des Animations', 'SPIELBERG Steven', 54, 'BDA', 'H113'),
	(4, 'LE GALA','DILLER Barry', 120, 'organisation du gala annuel', 'H114'),
	(5, 'CLUB ZIK', 'LUCAS George',100, 'musique et chant', 'H115'),
	(6, 'KICK & BEAT', 'VARDA Agnès', 89, 'rap','C124'),
	(7, 'ESI''AFRIK','FORD Harrison', 140,' découverte culturelle',  'C135'),
	(8, 'FREEDOM','KUROSAWA Akira', 67, 'découverte culturelle ', 'C136'),
	(9, 'ESI''CREW', 'MIYAZAKI Hayao', 110, 'danse',  NULL),
	(10, 'POM-POM ESIGELEC', 'TAKAHATA Isao', 50,' danse', 'D103'),
	(11, 'ESI''GAMES', 'COPPOLA Francis Ford', 75, ' jeux vidéos',  'C116'),
	(12, 'ESIGELEC ALUMNI', 'FONDA Peter', 30, 'promouvoir le diplome',  'B310'),
	(13, 'ESIG''4L', 'COPPOLA Sofia', 43,'rallye humanitaire',  'USA'),
	(14, 'ESIG''BIKERS', 'ALLEN Woody', 67, 'motards',  NULL),
	(15, 'ESIG''KARTING','HAZANAVICIUS Michel', 94, 'sorties kart',NULL),
	(16, 'TEAM DEFI 24H ESIGELEC', 'STURGES John', 56, 'courses motonautiques', NULL),
	(17, 'J2E', 'KENNEDY Burt',88, 'Junior Etude',  'B307'),
	(18, 'ESIG''TRONIX', 'JACKSON Peter', 62, 'apprendre de choses robotique',  'H206'),
	(19, 'LA CUISINE DES MOUSQUETAIRES','LELOUCH Claude' , 67, 'gastronomie','H109'),
	(20, 'ESIG''AERO', 'Dubois Lucas', 33, 'aéronautique',  'C138'),
	(21, 'LA TORTUE DECHAINEE', 'Lefevre Camille', 88,' journal', NULL),
	(22, 'CLUB VOILE', 'Martin Leo', 38,'navigation',  'H108'),
	(23, 'BSBG_DE SUSTAINABLE', 'Dupont Clara', 78, 'écologie et solidarité',NULL),
	(24, 'ESIG''SOLIDAIRE', 'Laurent Maxime', 55, 'solidarité', NULL),
	(25, 'RESEAU DE PI','Garcia Emma', 48, 'relationnel étudiants', 'B305'),
	(26, 'ESIG''CHESS', 'Leroy Nathan', 33, 'échecs', NULL),
	(27, 'ESIG''COMPUTER','Moreau Chloe', 77, 'informatique', 'M104'),
	(28, 'STOP','Fournier Thomas', 63, ' prévention soirées', 'M103'),
	(29, 'SOIS FIER.E ET OSE','Rousseau Antoine', 67, 'lutte contre les discriminations', 'M102'),
	(30, 'CAPTIVE',' Fontaine Eva', 32,'vidéo et photographie', 'M01'),
	(31, 'ESIG''BOULES',' Chevalier Louis', 78, 'pétanque ',  NULL),
	(32, 'ESIG SUPPORTERS','Bernard Léa', 87, 'soutien lors des compétitions',  NULL),
	(33, 'ESIG''THEATRE','Michel Hugo',78, 'théâtre', 'H201'),
	(34, 'GSIG''TIR', 'Girard Manon', 49, 'sorties autour du tir',  NULL),
	(0, 'assotest', 'présidtest', 1, 'dsctest',  NULL);
	
	



INSERT INTO Joue_dans
VALUES	(1, 1),
	(2, 2),
	(3, 3),
	(3, 8),
	(6, 4),
	(5, 4),
	(3, 5),
	(3, 6),
	(7, 6),
	(3, 11),
	(8, 12),
	(8, 14),
	(7, 17),
	(12, 23),
	(11, 24),
	(13, 26),
	(14, 27),
	(14, 28),
	(7, 29);


-- 
-- Requêtes :
--

