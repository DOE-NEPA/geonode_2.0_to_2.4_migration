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

src_cur.execute("select resourcebase_ptr_id, workspace, store, \"storeType\", name, typename, popular_count, share_count, default_style_id from layers_layer")
#print str(src_cur)
for src_row in src_cur:
  assignments = []
  #resourcebase_ptr_id
  assignments.append(src_row[0])
  #title_en
  assignments.append(None)
  #abstract_en
  assignments.append(None)
  #purpose_en
  assignments.append(None)
  #constraints_other_en
  assignments.append(None)
  #supplemental_information_en
  assignments.append(None)
  #distribution_description_en
  assignments.append(None)
  #data_quality_statement_en
  assignments.append(None)
  #workspace
  assignments.append(src_row[1])
  #store
  assignments.append(src_row[2])
  #storeType
  assignments.append(src_row[3])
  #name
  assignments.append(src_row[4])
  #typename
  assignments.append(src_row[5])
  #default_style_id
  assignments.append(src_row[8])
  #charset
  assignments.append("UTF8")
  #upload_session_id
  assignments.append(None)
  #service_id
  assignments.append(None)
  
  try:
    dst_cur.execute("insert into layers_layer(resourcebase_ptr_id, title_en, abstract_en, purpose_en, constraints_other_en, supplemental_information_en, distribution_description_en, data_quality_statement_en, workspace, store, \"storeType\", name, typename, default_style_id, charset, upload_session_id, service_id) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", assignments)
    dst.commit()
  except Exception as error:
    print 
    print type(error)
    print str(error) + "select resourcebase_ptr_id, workspace, store, \"storeType\", name, typename, popular_count, share_count, default_style_id from layers_layer"
    print str(src_row)
    dst.rollback()

dst.commit()

src_cur.close()

dst_cur.close()

src.close()

dst.close()

