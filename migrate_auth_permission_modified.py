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

src_cur.execute("select id, name, content_type_id, codename from auth_permission where id in (28,29,30,31,32,33,64,65,66,67,68,69,70,71,72,88,89,90,91,92,93,109,110,111,124,125,138,139,143,144,145,146,147,148,149,150,151,155,156,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190)")

for src_row in src_cur:
  assignments = []
  #id
  assignments.append(src_row[0]+10000)
  #name
  assignments.append(src_row[1])
  #content_type_id
  assignments.append(django_content_type_mapping.get_django_content_type_id(src_row[2]))
  #codename
  assignments.append(src_row[3])
  
  try:
    dst_cur.execute("insert into auth_permission(id, name, content_type_id, codename) values (%s, %s, %s, %s)", assignments)
    dst.commit()
  except Exception as error:
    print 
    print type(error)
    print str(error) + "select id, name, content_type_id, codename from auth_permission"
    print str(src_row)
    dst.rollback()

dst.commit()

src_cur.close()

dst_cur.close()

src.close()

dst.close()

