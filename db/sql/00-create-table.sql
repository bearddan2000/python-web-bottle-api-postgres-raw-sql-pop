CREATE SEQUENCE pop_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1;

CREATE TABLE "public"."pop" (
    "id" integer DEFAULT nextval('pop_id_seq') NOT NULL,
    "name" text NOT NULL,
    "color" text NOT NULL
) WITH (oids = false);
