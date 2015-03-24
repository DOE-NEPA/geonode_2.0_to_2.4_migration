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

src_cur.execute("select id, title, content, creator_id, creation_date, site_wide, members_only, dismissal_type, publish_start, publish_end from announcements_announcement")

for src_row in src_cur:
  assignments = []
  #id
  assignments.append(src_row[0])
  #title
  assignments.append(src_row[1])
  #level
  assignments.append(1)
  #content
  assignments.append(src_row[2])
  #creator_id
  assignments.append(src_row[3])
  #creation_date
  assignments.append(src_row[4])
  #site_wide
  assignments.append(src_row[5])
  #members_only
  assignments.append(src_row[6])
  #dismissal_type
  assignments.append(src_row[7])
  #publish_start
  assignments.append(src_row[8])
  #publish_end
  assignments.append(src_row[9])
  
  try:
    dst_cur.execute("insert into announcements_announcement(id, title, level, content, creator_id, creation_date, site_wide, members_only, dismissal_type, publish_start, publish_end) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", assignments)
    dst.commit()
  except Exception as error:
    print 
    print type(error)
    print str(error) + "select id, title, content, creator_id, creation_date, site_wide, members_only, dismissal_type, publish_start, publish_end from announcements_announcement"
    print str(src_row)
    dst.rollback()

dst.commit()

src_cur.close()

dst_cur.close()

src.close()

dst.close()

