#!/usr/bin/python
import os
import psycopg2

def parents(cur, tab):
  sql = """
    select distinct
           fkc.table_name as pk_table_name
    from   information_schema.table_constraints       as fkt,
           information_schema.constraint_column_usage as fkc
    where  fkt.constraint_catalog = fkc.constraint_catalog        
    and    fkt.constraint_schema  = fkc.constraint_schema
    and    fkt.constraint_name    = fkc.constraint_name     
    and    fkt.constraint_type    = 'FOREIGN KEY'
    and    fkt.table_name         = %s
"""
  results = []
  cur.execute(sql, (tab,))
  for cur_row in cur:
    results.append(cur_row[0])
  return results


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

dst = psycopg2.connect(host=dst_pgpass[0], database="geonode", user=dst_pgpass[3], password=dst_pgpass[4])

src_cur = src.cursor()

src_cur.execute("select table_name from information_schema.tables where table_schema = 'geonode' order by table_name")

src_tables = src_cur.fetchall()

#print type(src_tables)
#print len(src_tables)
#print str(src_tables[0])

dst_cur = dst.cursor()

#dst_cur.execute("set search_path = geonode,public")
dst_cur.execute("select table_name from information_schema.tables where table_schema = 'public' order by table_name")

dst_tables = dst_cur.fetchall()

#print type(dst_tables)
#print len(dst_tables)
#print str(dst_tables[0])

print "Tables in src not in dst:"
print "-------------------------"
src_not_in_dst = 0
for src_table in src_tables:
  not_found = True
  for dst_table in dst_tables:
  	if src_table[0] == dst_table[0]:
  	  not_found = False
  	  break
  if not_found:
  	print src_table[0]
  	src_not_in_dst = src_not_in_dst + 1
print str(src_not_in_dst)

print "\nTables in both:"
print "---------------"
both_tables = []
in_both = 0
for src_table in src_tables:
  for dst_table in dst_tables:
  	if src_table[0] == dst_table[0]:
  	  both_tables.append(src_table[0])
  	  print src_table[0]  
  	  in_both = in_both + 1
  	  break
print str(in_both)

print "\nTables in dst not in src:"
print "-------------------------"
dst_not_in_src = 0
for dst_table in dst_tables:
  not_found = True
  for src_table in src_tables:
  	if dst_table[0] == src_table[0]:
  	  not_found = False
  	  break
  if not_found:
  	print dst_table[0]
  	dst_not_in_src = dst_not_in_src + 1
print str(dst_not_in_src)

# write migration programs
for both_table in both_tables:
  #print "type(both_table)=" + str(type(both_table))
  file = open("migrate_" + both_table + ".py", "w")
  src_cur.execute("select column_name from information_schema.columns where table_name = %s order by ordinal_position", (both_table,))
  src_columns = src_cur.fetchall()
  #print type(src_columns)
  #print len(src_columns)
  #print str(src_columns[0])
  dst_cur.execute("select column_name from information_schema.columns where table_name = %s order by ordinal_position", (both_table,))
  dst_columns = dst_cur.fetchall()
  #print type(dst_columns)
  #print len(dst_columns)
  #print str(dst_columns[0])
  both_columns = []
  for src_column in src_columns:
    for dst_column in dst_columns:
      if src_column[0] == dst_column[0]:
        both_columns.append(src_column[0])
        #print src_column[0]  
    	break

  select = "select "
  column_number = 0
  for src_column in src_columns:
    column_number = column_number + 1
    if column_number > 1:
      select = select + ', '
    select = select + src_column[0]
  select = select + " from " + both_table

  assignments = "  "
  for dst_column in dst_columns:
    assignments = assignments + "#" + dst_column[0] + "\n  "
    if dst_column in src_columns:
      assignments = assignments + "assignments.append(src_row[" + str(src_columns.index(dst_column)) + "])\n  "
    else:
      assignments = assignments + "assignments.append(None)\n  "

  insert = "insert into " + both_table + "("
  values = ") values ("
  column_number = 0
  for dst_column in dst_columns:
    column_number = column_number + 1
    if column_number > 1:
      insert = insert + ', '
      values = values + ', '
    insert = insert + dst_column[0]
    values = values + "%s"
  insert = insert + values + ")"

  file.write("""#!/usr/bin/python
import os
import psycopg2
import sys

file = open("/home/" + os.getlogin() + "/.pgpass", "r")
pgpasses = []
for line in file:
  pgpasses.append(line.rstrip("\\n").split(":"))
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

""")
  file.write("src_cur.execute(\"" + select + "\")\n\n")
  file.write("for src_row in src_cur:\n")
  file.write("  assignments = []\n")
  file.write(assignments + "\n")
  file.write("  try:\n")
  file.write("    dst_cur.execute(\"" + insert + "\", assignments)\n")
  file.write("    dst.commit()\n")
  file.write("  except Exception as error:\n")
  file.write("    print \n")
  file.write("    print type(error)\n")
  file.write("    print str(error) + \"" + select + "\"\n")
  file.write("    print str(src_row)\n")
  file.write("    dst.rollback()\n")
  file.write("""
dst.commit()

src_cur.close()

dst_cur.close()

src.close()

dst.close()

""")  
  file.close()

# get dependency order
dependencies = []
for both_table in both_tables:
  for parent in parents(dst_cur, both_table):
    dependency = []
    dependency.append(both_table)
    dependency.append(parent)     
    dependencies.append(dependency)
#print str(dependencies)
#print len(dependencies)
for dependency_level in range(1, 20):
  for dependency in dependencies:
    if (len(dependency) - 1) == dependency_level:
      dependency_count = 0
      for parent in parents(dst_cur, dependency[dependency_level]):
        if parent != dependency[dependency_level]:
          if dependency_count == 0:
            dependency.append(parent)
          else:
            additional = []
            for additional_dependency in range(0, dependency_level):
              additional.append(dependency[additional_dependency])
            additional.append(parent)
            dependencies.append(additional)
          dependency_count= dependency_count + 1
          
print "\nTables in FK to PK order:"
print "-------------------------"
for dependency in dependencies:
  print str(dependency)
#  print len(dependency)
	
print len(dependencies)

flipped = []
dependency_level = 20
#print dependency_level
while dependency_level > -1:
  for dependency in dependencies:
    if (len(dependency) - 1) >= dependency_level:
      #print dependency[dependency_level]
      if not dependency[dependency_level] in flipped:
        flipped.append(dependency[dependency_level])
  dependency_level = dependency_level - 1
  #print dependency_level
for both_table in both_tables:
  if not both_table in flipped:
    flipped.append(both_table)

print "\nTables in dependency order:"
print "---------------------------"
for flip in flipped:
  print flip
  
print len(flipped)

dst.commit()

src_cur.close()

dst_cur.close()

src.close()

dst.close()
