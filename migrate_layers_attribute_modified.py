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

src_cur.execute("select id, layer_id, attribute, description, attribute_label, attribute_type, visible, display_order, count, min, max, average, median, stddev, sum, unique_values, last_stats_updated from layers_attribute")

for src_row in src_cur:
  assignments = []
  #id
  assignments.append(src_row[0])
  #layer_id
  assignments.append(src_row[1])
  #attribute
  assignments.append(src_row[2])
  #description
  assignments.append(src_row[3])
  #attribute_label
  assignments.append(src_row[4])
  #attribute_type
  assignments.append(src_row[5])
  #visible
  assignments.append(src_row[6])
  #display_order
  assignments.append(src_row[7])
  #count
  assignments.append(src_row[8])
  #min
  assignments.append(src_row[9])
  #max
  assignments.append(src_row[10])
  #average
  assignments.append(src_row[11])
  #median
  assignments.append(src_row[12])
  #stddev
  assignments.append(src_row[13])
  #sum
  assignments.append(src_row[14])
  #unique_values
  assignments.append(src_row[15])
  #last_stats_updated
  assignments.append(src_row[16])
  
  try:
    dst_cur.execute("insert into layers_attribute(id, layer_id, attribute, description, attribute_label, attribute_type, visible, display_order, count, min, max, average, median, stddev, sum, unique_values, last_stats_updated) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", assignments)
    dst.commit()
  except Exception as error:
    print 
    print type(error)
    print str(error) + "select id, layer_id, attribute, description, attribute_label, attribute_type, visible, display_order, count, min, max, average, median, stddev, sum, unique_values, last_stats_updated from layers_attribute"
    print str(src_row)
    dst.rollback()

dst.commit()

src_cur.close()

dst_cur.close()

src.close()

dst.close()

