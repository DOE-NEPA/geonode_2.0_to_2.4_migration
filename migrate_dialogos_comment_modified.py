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

src_cur.execute("select id, author_id, name, email, website, content_type_id, object_id, comment, submit_date, ip_address, public from dialogos_comment")

for src_row in src_cur:
  assignments = []
  #id
  assignments.append(src_row[0])
  #author_id
  assignments.append(src_row[1])
  #name
  assignments.append(src_row[2])
  #email
  assignments.append(src_row[3])
  #website
  assignments.append(src_row[4])
  #content_type_id
  assignments.append(django_content_type_mapping.get_django_content_type_id(src_row[5]))
  #object_id
  assignments.append(src_row[6])
  #comment
  assignments.append(src_row[7])
  #submit_date
  assignments.append(src_row[8])
  #ip_address
  assignments.append(src_row[9])
  #public
  assignments.append(src_row[10])
  
  try:
    dst_cur.execute("insert into dialogos_comment(id, author_id, name, email, website, content_type_id, object_id, comment, submit_date, ip_address, public) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", assignments)
    dst.commit()
  except Exception as error:
    print 
    print type(error)
    print str(error) + "select id, author_id, name, email, website, content_type_id, object_id, comment, submit_date, ip_address, public from dialogos_comment"
    print str(src_row)
    dst.rollback()

dst.commit()

src_cur.close()

dst_cur.close()

src.close()

dst.close()

