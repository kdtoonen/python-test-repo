drop table if exists tblUser;
CREATE TABLE tblUser (
 userid  integer primary key autoincrement,
 emailusername text NOT NULL unique ,
 firstname text NOT NULL,
 lastname text NOT NULL,
 password text NOT NULL,
 resetcode text,
 confirmationcode text NOT NULL,
 confirmed integer NOT NULL DEFAULT 0,
 pic text NOT NULL DEFAULT 'spock.png',
 confmsgsent integer NOT NULL DEFAULT 0,
 orglastusedasadmin integer NOT NULL DEFAULT 0);
