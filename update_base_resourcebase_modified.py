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

src_cur.execute("select id, uuid, owner_id, title, date, date_type, edition, abstract, purpose, maintenance_frequency, restriction_code_type_id, constraints_other, language, category_id, spatial_representation_type_id, temporal_extent_start, temporal_extent_end, supplemental_information, distribution_url, distribution_description, data_quality_statement, bbox_x0, bbox_x1, bbox_y0, bbox_y1, srid, csw_typename, csw_schema, csw_mdsource, csw_insert_date, csw_type, csw_anytext, csw_wkt_geometry, metadata_uploaded, metadata_xml, thumbnail_id from base_resourcebase")

for src_row in src_cur:
  assignments = []
  #id
  assignments.append(src_row[0])
  #polymorphic_ctype_id
  assignments.append(None)
  #uuid
  assignments.append(src_row[1])
  #owner_id
  assignments.append(src_row[2])
  #title
  assignments.append(src_row[3])
  #date
  assignments.append(src_row[4])
  #date_type
  assignments.append(src_row[5])
  #edition
  assignments.append(src_row[6])
  #abstract
  assignments.append(src_row[7])
  #purpose
  assignments.append(src_row[8])
  #maintenance_frequency
  assignments.append(src_row[9])
  #restriction_code_type_id
  assignments.append(src_row[10])
  #constraints_other
  assignments.append(src_row[11])
  #license_id
  assignments.append(None)
  #language
  assignments.append(src_row[12])
  #category_id
  assignments.append(src_row[13])
  #spatial_representation_type_id
  assignments.append(src_row[14])
  #temporal_extent_start
  assignments.append(src_row[15])
  #temporal_extent_end
  assignments.append(src_row[16])
  #supplemental_information
  assignments.append(src_row[17])
  #distribution_url
  assignments.append(src_row[18])
  #distribution_description
  assignments.append(src_row[19])
  #data_quality_statement
  assignments.append(src_row[20])
  #bbox_x0
  assignments.append(src_row[21])
  #bbox_x1
  assignments.append(src_row[22])
  #bbox_y0
  assignments.append(src_row[23])
  #bbox_y1
  assignments.append(src_row[24])
  #srid
  assignments.append(src_row[25])
  #csw_typename
  assignments.append(src_row[26])
  #csw_schema
  assignments.append(src_row[27])
  #csw_mdsource
  assignments.append(src_row[28])
  #csw_insert_date
  assignments.append(src_row[29])
  #csw_type
  assignments.append(src_row[30])
  #csw_anytext
  assignments.append(src_row[31])
  #csw_wkt_geometry
  assignments.append(src_row[32])
  #metadata_uploaded
  assignments.append(src_row[33])
  #metadata_xml
  assignments.append(src_row[34])
  #popular_count
  assignments.append(0)
  #share_count
  assignments.append(0)
  #featured
  assignments.append(False)
  #is_published
  assignments.append(False)
  #thumbnail_url
  assignments.append(None)
  #detail_url
  assignments.append(None)
  #rating
  assignments.append(None)
  
  try:
    dst_cur.execute("insert into base_resourcebase(id, polymorphic_ctype_id, uuid, owner_id, title, date, date_type, edition, abstract, purpose, maintenance_frequency, restriction_code_type_id, constraints_other, license_id, language, category_id, spatial_representation_type_id, temporal_extent_start, temporal_extent_end, supplemental_information, distribution_url, distribution_description, data_quality_statement, bbox_x0, bbox_x1, bbox_y0, bbox_y1, srid, csw_typename, csw_schema, csw_mdsource, csw_insert_date, csw_type, csw_anytext, csw_wkt_geometry, metadata_uploaded, metadata_xml, popular_count, share_count, featured, is_published, thumbnail_url, detail_url, rating) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", assignments)
    dst.commit()
  except Exception as error:
    print 
    print type(error)
    print str(error) + "select id, uuid, owner_id, title, date, date_type, edition, abstract, purpose, maintenance_frequency, restriction_code_type_id, constraints_other, language, category_id, spatial_representation_type_id, temporal_extent_start, temporal_extent_end, supplemental_information, distribution_url, distribution_description, data_quality_statement, bbox_x0, bbox_x1, bbox_y0, bbox_y1, srid, csw_typename, csw_schema, csw_mdsource, csw_insert_date, csw_type, csw_anytext, csw_wkt_geometry, metadata_uploaded, metadata_xml, thumbnail_id from base_resourcebase"
    print str(src_row)
    dst.rollback()

dst.commit()

src_cur.close()

dst_cur.close()

src.close()

dst.close()

