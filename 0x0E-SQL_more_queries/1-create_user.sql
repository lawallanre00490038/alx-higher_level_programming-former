CREATE USER
  IF NOT EXITS  'user_0d_1'@'localhost'
  IDENTIFIED BY 'user_0d_1_pwd';
 GRANT ALL PRIVILEDGES
  ON "."
  TO 'user_0d_1'@'localhost'
  IDENTIFIED BY 'user_0d_1_pwd';
 FLUSH PRIVILEDGES;
