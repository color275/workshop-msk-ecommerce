# workshop-ecommerce

# .env
```
ENGINE='django.db.backends.mysql'
NAME='ecommerce'
DBUSER='testuser'
PASSWORD='testuser'
HOST='0.0.0.0'
PORT='3306'
PERSONALIZE_ARN=''
```
# MySQL Insert
```
INSERT INTO `customer` VALUES 
(101,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=','2023-04-13 01:45:01.250024',1,'AWS01','AWS01','AWS01','aws@gmail.com',1,1,'2023-04-09 03:15:42.000000','010-1234-5678',21,'남','서울시 강남구','2023-04-12 00:34:33.167432','AWS01'),
(102,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=','2023-04-13 01:45:01.250024',1,'AWS02','AWS02','AWS02','aws@gmail.com',1,1,'2023-04-09 03:15:42.000000','010-1234-5678',21,'남','서울시 강남구','2023-04-12 00:34:33.167432','AWS02'),
(103,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=','2023-04-13 01:45:01.250024',1,'AWS03','AWS03','AWS03','aws@gmail.com',1,1,'2023-04-09 03:15:42.000000','010-1234-5678',21,'남','서울시 강남구','2023-04-12 00:34:33.167432','AWS03'),
(104,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=','2023-04-13 01:45:01.250024',1,'AWS04','AWS04','AWS04','aws@gmail.com',1,1,'2023-04-09 03:15:42.000000','010-1234-5678',21,'남','서울시 강남구','2023-04-12 00:34:33.167432','AWS04'),
(105,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=','2023-04-13 01:45:01.250024',1,'AWS05','AWS05','AWS05','aws@gmail.com',1,1,'2023-04-09 03:15:42.000000','010-1234-5678',21,'남','서울시 강남구','2023-04-12 00:34:33.167432','AWS05'),
(106,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=','2023-04-13 01:45:01.250024',1,'AWS06','AWS06','AWS06','aws@gmail.com',1,1,'2023-04-09 03:15:42.000000','010-1234-5678',21,'남','서울시 강남구','2023-04-12 00:34:33.167432','AWS06'),
(107,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=','2023-04-13 01:45:01.250024',1,'AWS07','AWS07','AWS07','aws@gmail.com',1,1,'2023-04-09 03:15:42.000000','010-1234-5678',21,'남','서울시 강남구','2023-04-12 00:34:33.167432','AWS07'),
(108,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=','2023-04-13 01:45:01.250024',1,'AWS08','AWS08','AWS08','aws@gmail.com',1,1,'2023-04-09 03:15:42.000000','010-1234-5678',21,'남','서울시 강남구','2023-04-12 00:34:33.167432','AWS08'),
(109,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=','2023-04-13 01:45:01.250024',1,'AWS09','AWS09','AWS09','aws@gmail.com',1,1,'2023-04-09 03:15:42.000000','010-1234-5678',21,'남','서울시 강남구','2023-04-12 00:34:33.167432','AWS09'),
(110,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=','2023-04-13 01:45:01.250024',1,'AWS10','AWS10','AWS10','aws@gmail.com',1,1,'2023-04-09 03:15:42.000000','010-1234-5678',21,'남','서울시 강남구','2023-04-12 00:34:33.167432','AWS10'),
(111,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=','2023-04-13 01:45:01.250024',1,'AWS11','AWS11','AWS11','aws@gmail.com',1,1,'2023-04-09 03:15:42.000000','010-1234-5678',21,'남','서울시 강남구','2023-04-12 00:34:33.167432','AWS11'),
(112,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=','2023-04-13 01:45:01.250024',1,'AWS12','AWS12','AWS12','aws@gmail.com',1,1,'2023-04-09 03:15:42.000000','010-1234-5678',21,'남','서울시 강남구','2023-04-12 00:34:33.167432','AWS12'),
(113,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=','2023-04-13 01:45:01.250024',1,'AWS13','AWS13','AWS13','aws@gmail.com',1,1,'2023-04-09 03:15:42.000000','010-1234-5678',21,'남','서울시 강남구','2023-04-12 00:34:33.167432','AWS13'),
(114,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=','2023-04-13 01:45:01.250024',1,'AWS14','AWS14','AWS14','aws@gmail.com',1,1,'2023-04-09 03:15:42.000000','010-1234-5678',21,'남','서울시 강남구','2023-04-12 00:34:33.167432','AWS14'),
(115,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=','2023-04-13 01:45:01.250024',1,'AWS15','AWS15','AWS15','aws@gmail.com',1,1,'2023-04-09 03:15:42.000000','010-1234-5678',21,'남','서울시 강남구','2023-04-12 00:34:33.167432','AWS15'),
(116,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=','2023-04-13 01:45:01.250024',1,'AWS16','AWS16','AWS16','aws@gmail.com',1,1,'2023-04-09 03:15:42.000000','010-1234-5678',21,'남','서울시 강남구','2023-04-12 00:34:33.167432','AWS16'),
(117,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=','2023-04-13 01:45:01.250024',1,'AWS17','AWS17','AWS17','aws@gmail.com',1,1,'2023-04-09 03:15:42.000000','010-1234-5678',21,'남','서울시 강남구','2023-04-12 00:34:33.167432','AWS17'),
(118,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=','2023-04-13 01:45:01.250024',1,'AWS18','AWS18','AWS18','aws@gmail.com',1,1,'2023-04-09 03:15:42.000000','010-1234-5678',21,'남','서울시 강남구','2023-04-12 00:34:33.167432','AWS18'),
(119,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=','2023-04-13 01:45:01.250024',1,'AWS19','AWS19','AWS19','aws@gmail.com',1,1,'2023-04-09 03:15:42.000000','010-1234-5678',21,'남','서울시 강남구','2023-04-12 00:34:33.167432','AWS19'),
(120,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=','2023-04-13 01:45:01.250024',1,'AWS20','AWS20','AWS20','aws@gmail.com',1,1,'2023-04-09 03:15:42.000000','010-1234-5678',21,'남','서울시 강남구','2023-04-12 00:34:33.167432','AWS20');
``````

# Oracle Insert
```
INSERT INTO customer VALUES (101,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=',sysdate,1,'aws01','aws01','aws01','aws@gmail.com',1,1,sysdate,'010-1234-5678',21,'남','서울시 강남구',sysdate,'AWS01');
INSERT INTO customer VALUES (102,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=',sysdate,1,'aws02','aws02','aws02','aws@gmail.com',1,1,sysdate,'010-1234-5678',21,'남','서울시 강남구',sysdate,'AWS02');
INSERT INTO customer VALUES (103,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=',sysdate,1,'aws03','aws03','aws03','aws@gmail.com',1,1,sysdate,'010-1234-5678',21,'남','서울시 강남구',sysdate,'AWS03');
INSERT INTO customer VALUES (104,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=',sysdate,1,'aws04','aws04','aws04','aws@gmail.com',1,1,sysdate,'010-1234-5678',21,'남','서울시 강남구',sysdate,'AWS04');
INSERT INTO customer VALUES (105,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=',sysdate,1,'aws05','aws05','aws05','aws@gmail.com',1,1,sysdate,'010-1234-5678',21,'남','서울시 강남구',sysdate,'AWS05');
INSERT INTO customer VALUES (106,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=',sysdate,1,'aws06','aws06','aws06','aws@gmail.com',1,1,sysdate,'010-1234-5678',21,'남','서울시 강남구',sysdate,'AWS06');
INSERT INTO customer VALUES (107,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=',sysdate,1,'aws07','aws07','aws07','aws@gmail.com',1,1,sysdate,'010-1234-5678',21,'남','서울시 강남구',sysdate,'AWS07');
INSERT INTO customer VALUES (108,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=',sysdate,1,'aws08','aws08','aws08','aws@gmail.com',1,1,sysdate,'010-1234-5678',21,'남','서울시 강남구',sysdate,'AWS08');
INSERT INTO customer VALUES (109,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=',sysdate,1,'aws09','aws09','aws09','aws@gmail.com',1,1,sysdate,'010-1234-5678',21,'남','서울시 강남구',sysdate,'AWS09');
INSERT INTO customer VALUES (110,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=',sysdate,1,'aws10','aws10','aws10','aws@gmail.com',1,1,sysdate,'010-1234-5678',21,'남','서울시 강남구',sysdate,'AWS10');
INSERT INTO customer VALUES (111,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=',sysdate,1,'aws11','aws11','aws11','aws@gmail.com',1,1,sysdate,'010-1234-5678',21,'남','서울시 강남구',sysdate,'AWS11');
INSERT INTO customer VALUES (112,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=',sysdate,1,'aws12','aws12','aws12','aws@gmail.com',1,1,sysdate,'010-1234-5678',21,'남','서울시 강남구',sysdate,'AWS12');
INSERT INTO customer VALUES (113,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=',sysdate,1,'aws13','aws13','aws13','aws@gmail.com',1,1,sysdate,'010-1234-5678',21,'남','서울시 강남구',sysdate,'AWS13');
INSERT INTO customer VALUES (114,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=',sysdate,1,'aws14','aws14','aws14','aws@gmail.com',1,1,sysdate,'010-1234-5678',21,'남','서울시 강남구',sysdate,'AWS14');
INSERT INTO customer VALUES (115,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=',sysdate,1,'aws15','aws15','aws15','aws@gmail.com',1,1,sysdate,'010-1234-5678',21,'남','서울시 강남구',sysdate,'AWS15');
INSERT INTO customer VALUES (116,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=',sysdate,1,'aws16','aws16','aws16','aws@gmail.com',1,1,sysdate,'010-1234-5678',21,'남','서울시 강남구',sysdate,'AWS16');
INSERT INTO customer VALUES (117,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=',sysdate,1,'aws17','aws17','aws17','aws@gmail.com',1,1,sysdate,'010-1234-5678',21,'남','서울시 강남구',sysdate,'AWS17');
INSERT INTO customer VALUES (118,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=',sysdate,1,'aws18','aws18','aws18','aws@gmail.com',1,1,sysdate,'010-1234-5678',21,'남','서울시 강남구',sysdate,'AWS18');
INSERT INTO customer VALUES (119,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=',sysdate,1,'aws19','aws19','aws19','aws@gmail.com',1,1,sysdate,'010-1234-5678',21,'남','서울시 강남구',sysdate,'AWS19');
INSERT INTO customer VALUES (120,'pbkdf2_sha256$260000$mexj7X6zszC2iBHFSkaZAS$Yn0sBX2MVaZzrDi5KWH5WONNDb31m3AwGNshJmv4waI=',sysdate,1,'aws20','aws20','aws20','aws@gmail.com',1,1,sysdate,'010-1234-5678',21,'남','서울시 강남구',sysdate,'AWS20');
```