#!/usr/bin/python
import os
import psycopg2
import sys

file = open("/home/" + os.getlogin() + "/.pgpass", "r")
pgpasses = []
for line in file:
  pgpasses.append(line.rstrip("\n").split(":"))
file.close()

#print type(pgpasses)
#print len(pgpasses)
#print str(pgpasses[0])

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

src_cur.execute("select id, user_id, notice_type_id, medium, send from notification_noticesetting")

for src_row in src_cur:
  assignments = []
  #id
  assignments.append(src_row[0])
  #user_id
  assignments.append(src_row[1])
  #notice_type_id
  assignments.append(src_row[2])
  #medium
  assignments.append(src_row[3])
  #send
  assignments.append(src_row[4])
  
  try:
    dst_cur.execute("insert into notification_noticesetting(id, user_id, notice_type_id, medium, send) values (%s, %s, %s, %s, %s)", assignments)
    dst.commit()
  except Exception as error:
    print 
    print type(error)
    print str(error) + "select id, user_id, notice_type_id, medium, send from notification_noticesetting"
    print str(src_row)
    dst.rollback()

dst.commit()

src_cur.close()

dst_cur.close()

src.close()

dst.close()

