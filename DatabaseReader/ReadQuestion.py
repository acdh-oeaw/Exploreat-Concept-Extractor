# import MySQLdb
import mysql.connector
import mysql.connector
import datetime
import re

class QuestionReader:
    records=[]

    def readQuestionByID(self, id):
        counter = 0
        records = []

        try:
            cnx = mysql.connector.connect(user='root', password='ExploreAt!dbo2018'
                                          , host='127.0.0.1',
                                          database='dboe2018')
            cursor = cnx.cursor()
            query=("select  id,originalfrage from frage where fragebogen_id= " +str(id))
            # print(str(topic[0]))
            cursor.execute(query)

            for rec in cursor:
                rec = (str(rec[0]), rec[1])
                self.records.append(rec)

            cursor.close()
            cnx.close
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cnx.close()
        return records

