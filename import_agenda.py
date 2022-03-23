from db_table import db_table
import xlrd
import sys


file_name = sys.argv[1]
print "This is the name of the script: ", sys.argv[1]
agenda = xlrd.open_workbook(file_name).sheet_by_index(0)
schema = [x for x in agenda.row_values(12)]
print schema

users = db_table("agenda", { "id": "integer PRIMARY KEY", 
                            "date": "string NOT NULL", 
                            "time_start": "string NOT NULL",
                            "time_end": "string NOT NULL", 
                           "title":"string NOT NULL",
                           "location": "string",
                           "description":"string"})

id = 1
for rx in xrange(13,agenda.nrows):
    content = [c for c in agenda.row_values(rx)]
    if "'" in content[3] :
        content[3] = content[3].replace("'","''")
        
    users.insert({"id": id , 
                  "date": content[0],
                  "time_start":content[1],
                  "time_end":content[2],
                  "title":content[3],
                  "location": content[4] if len(content) >= 5 else None,
                 "description": content[5] if len(content) == 5 else None})
    id = id + 1


users.close()