
import MySQLdb as my

db = my.connect("localhost", "root","roottoor","dbs")

cursor = db.cursos()

cursor.execute("SELECT VERSION()")

data = cursor.fletchone()

print "Database version : %s " % data
 

