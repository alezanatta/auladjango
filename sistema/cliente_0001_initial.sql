BEGIN;
--
-- Create model Cidade
--
CREATE TABLE "cliente_cidade" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nm_cidade" varchar(20) NOT NULL, "nm_estado" varchar(15) NOT NULL, "sg_estado" varchar(2) NOT NULL, "nm_pais" varchar(10) NOT NULL, "sg_pais" varchar(3) NOT NULL);
--
-- Create model Endereco
--
CREATE TABLE "cliente_endereco" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "tp_logradouro" varchar(15) NOT NULL, "nm_logradouro" varchar(40) NOT NULL, "nm_bairro" varchar(20) NOT NULL, "cd_cidade_id" integer NOT NULL REFERENCES "cliente_cidade" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Cliente
--
CREATE TABLE "cliente_cliente" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nm_cliente" varchar(45) NOT NULL, "nr_cpf" varchar(14) NOT NULL, "dt_nascimento" date NOT NULL, "idade" integer NOT NULL, "nr_endereco" integer NOT NULL, "dsc_complemento" text NOT NULL, "cd_endereco_id" integer NOT NULL REFERENCES "cliente_endereco" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "cliente_endereco_cd_cidade_id_398bf95f" ON "cliente_endereco" ("cd_cidade_id");
CREATE INDEX "cliente_cliente_cd_endereco_id_20bfdae6" ON "cliente_cliente" ("cd_endereco_id");
COMMIT;
