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

src_cur.execute("select id, map_id, stack_order, format, name, opacity, styles, transparent, fixed, \"group\", visibility, ows_url, layer_params, source_params, local from maps_maplayer")

for src_row in src_cur:
  assignments = []
  #id
  assignments.append(src_row[0])
  #map_id
  assignments.append(src_row[1])
  #stack_order
  assignments.append(src_row[2])
  #format
  assignments.append(src_row[3])
  #name
  assignments.append(src_row[4])
  #opacity
  assignments.append(src_row[5])
  #styles
  assignments.append(src_row[6])
  #transparent
  assignments.append(src_row[7])
  #fixed
  assignments.append(src_row[8])
  #group
  assignments.append(src_row[9])
  #visibility
  assignments.append(src_row[10])
  #ows_url
  assignments.append(src_row[11])
  #layer_params
  assignments.append(src_row[12])
  #source_params
  assignments.append(src_row[13])
  #local
  assignments.append(src_row[14])
  
  try:
    dst_cur.execute("insert into maps_maplayer(id, map_id, stack_order, format, name, opacity, styles, transparent, fixed, \"group\", visibility, ows_url, layer_params, source_params, local) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", assignments)
    dst.commit()
  except Exception as error:
    print 
    print type(error)
    print str(error) + "select id, map_id, stack_order, format, name, opacity, styles, transparent, fixed, \"group\", visibility, ows_url, layer_params, source_params, local from maps_maplayer"
    print str(src_row)
    dst.rollback()

dst.commit()

src_cur.close()

dst_cur.close()

src.close()

dst.close()

