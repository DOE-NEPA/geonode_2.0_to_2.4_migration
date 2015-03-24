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

#src_cur.execute("select id, user_id, name, organization, profile, position, voice, fax, delivery, city, area, zipcode, country, email from people_profile")

select = """select auth_user.id,         
       auth_user.password,   
       auth_user.last_login, 
       auth_user.is_superuser,
       auth_user.username,   
       auth_user.first_name, 
       auth_user.last_name,  
       auth_user.email auth_user_email,      
       auth_user.is_staff,   
       auth_user.is_active,  
       auth_user.date_joined,
       people_profile.id people_profile_id,          
       people_profile.user_id,     
       people_profile.name,        
       people_profile.organization,
       people_profile.profile,     
       people_profile.position,    
       people_profile.voice,       
       people_profile.fax,         
       people_profile.delivery,    
       people_profile.city,        
       people_profile.area,        
       people_profile.zipcode,     
       people_profile.country,     
       people_profile.email people_profile_email
from   people_profile 
join   auth_user 
on     people_profile.user_id = auth_user.id
order by auth_user.id"""

#print select + "\n"

src_cur.execute(select)

for src_row in src_cur:
  assignments = []
  #id
  assignments.append(src_row[0])
  #password
  assignments.append(src_row[1])
  #last_login
  assignments.append(src_row[2])
  #is_superuser
  assignments.append(src_row[3])
  #username
  assignments.append(src_row[4])
  #first_name
  assignments.append(src_row[5])
  #last_name
  assignments.append(src_row[6])
  #email
  if src_row[7]:
    assignments.append(src_row[7])
  else:
    assignments.append(src_row[24])
  #is_staff
  assignments.append(src_row[8])
  #is_active
  assignments.append(src_row[9])
  #date_joined
  assignments.append(src_row[10])
  #organization
  assignments.append(src_row[14])
  #profile
  assignments.append(src_row[15])
  #position
  assignments.append(src_row[16])
  #voice
  assignments.append(src_row[17])
  #fax
  assignments.append(src_row[18])
  #delivery
  assignments.append(src_row[19])
  #city
  assignments.append(src_row[20])
  #area
  assignments.append(src_row[21])
  #zipcode
  assignments.append(src_row[22])
  #country
  assignments.append(src_row[23])
  
  try:
    dst_cur.execute("insert into people_profile(id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, organization, profile, position, voice, fax, delivery, city, area, zipcode, country) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", assignments)
    dst.commit()
  except Exception as error:
    print 
    print type(error)
    print str(error) + select
    print str(src_row)
    dst.rollback()

dst.commit()

src_cur.close()

dst_cur.close()

src.close()

dst.close()

