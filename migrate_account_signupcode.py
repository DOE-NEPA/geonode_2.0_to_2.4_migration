#!/usr/bin/python
import os
import psycopg2
import sys

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

src_cur.execute("select id, code, max_uses, expiry, inviter_id, email, notes, sent, created, use_count from account_signupcode")

for src_row in src_cur:
  assignments = []
  #id
  assignments.append(src_row[0])
  #code
  assignments.append(src_row[1])
  #max_uses
  assignments.append(src_row[2])
  #expiry
  assignments.append(src_row[3])
  #inviter_id
  assignments.append(src_row[4])
  #email
  assignments.append(src_row[5])
  #notes
  assignments.append(src_row[6])
  #sent
  assignments.append(src_row[7])
  #created
  assignments.append(src_row[8])
  #use_count
  assignments.append(src_row[9])
  
  try:
    dst_cur.execute("insert into account_signupcode(id, code, max_uses, expiry, inviter_id, email, notes, sent, created, use_count) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", assignments)
    dst.commit()
  except Exception as error:
    print 
    print type(error)
    print str(error) + "select id, code, max_uses, expiry, inviter_id, email, notes, sent, created, use_count from account_signupcode"
    print str(src_row)
    dst.rollback()

dst.commit()

src_cur.close()

dst_cur.close()

src.close()

dst.close()

