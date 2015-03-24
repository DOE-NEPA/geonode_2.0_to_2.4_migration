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

src_cur.execute("select id, actor_content_type_id, actor_object_id, verb, description, target_content_type_id, target_object_id, action_object_content_type_id, action_object_object_id, timestamp, public, data from actstream_action")

for src_row in src_cur:
  assignments = []
  #id
  assignments.append(src_row[0])
  #actor_content_type_id
  assignments.append(django_content_type_mapping.get_django_content_type_id(src_row[1]))
  #actor_object_id
  assignments.append(src_row[2])
  #verb
  assignments.append(src_row[3])
  #description
  assignments.append(src_row[4])
  #target_content_type_id
  assignments.append(django_content_type_mapping.get_django_content_type_id(src_row[5]))
  #target_object_id
  assignments.append(src_row[6])
  #action_object_content_type_id
  assignments.append(django_content_type_mapping.get_django_content_type_id(src_row[7]))
  #action_object_object_id
  assignments.append(src_row[8])
  #timestamp
  assignments.append(src_row[9])
  #public
  assignments.append(src_row[10])
  #data
  assignments.append(src_row[11])
  
  try:
    dst_cur.execute("insert into actstream_action(id, actor_content_type_id, actor_object_id, verb, description, target_content_type_id, target_object_id, action_object_content_type_id, action_object_object_id, timestamp, public, data) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", assignments)
    dst.commit()
  except Exception as error:
    print 
    print type(error)
    print str(error) + "select id, actor_content_type_id, actor_object_id, verb, description, target_content_type_id, target_object_id, action_object_content_type_id, action_object_object_id, timestamp, public, data from actstream_action"
    print str(src_row)
    dst.rollback()

dst.commit()

src_cur.close()

dst_cur.close()

src.close()

dst.close()

