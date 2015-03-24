#!/usr/bin/python
import os
import psycopg2
import sys
import django_content_type_mapping

file = open("/home/" + os.getlogin() + "/.pgpass", "r")
pgpasses = []
for line in file:
  pgpasses.append(line.rstrip("\n").split(":"))
file.close()

for pgpass in pgpasses:
  #print str(pgpass)
  if pgpass[0] == "54.236.235.110" and pgpass[3] == "geonode":
    src_pgpass = pgpass
  if pgpass[0] ==  "54.197.226.56"  and pgpass[3] == "geonode":
    dst_pgpass = pgpass

src = psycopg2.connect(host=src_pgpass[0], database="geonode2", user=src_pgpass[3], password=src_pgpass[4])

dst = psycopg2.connect(host=dst_pgpass[0], database="geonode",  user=dst_pgpass[3], password=dst_pgpass[4])

src_cur = src.cursor()

dst_cur = dst.cursor()

src_cur.execute("select id, name, app_label, model from django_content_type where id in (10,11,22,23,24,30,31,37,47,48,49,53,54,55,56,57,58,59,60)")

for src_row in src_cur:
  assignments = []
  #id
  assignments.append(django_content_type_mapping.get_django_content_type_id(src_row[0]))
  #name
  assignments.append(src_row[1])
  #app_label
  assignments.append(src_row[2])
  #model
  assignments.append(src_row[3])
  
  try:
    dst_cur.execute("insert into django_content_type(id, name, app_label, model) values (%s, %s, %s, %s)", assignments)
    dst.commit()
  except Exception as error:
    print 
    print type(error)
    print str(error) + "select id, name, app_label, model from django_content_type"
    print str(src_row)
    dst.rollback()

dst.commit()

src_cur.close()

dst_cur.close()

src.close()

dst.close()

