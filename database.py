
import sqlite3

connection = sqlite3.connect('data.db')  #file name

TABLE_NAME = "student_table"
STUDENT_ID="student_id"
STUDENT_NAME="student_name"
STUDENT_COLLEGE="student_collage"
STUDENT_ADDRESS="student_sddress"
STUDENT_PHONE="student_phone"





connection.execute(" CREATE TABLE IF  NOT EXISTS " +TABLE_NAME +
                    "(" + STUDENT_ID +
                    " INTEGER PRIMARY KEY AUTOINCREMENT," +
                    STUDENT_NAME + " TEXT," + STUDENT_COLLEGE + " TEXT," +
                    STUDENT_ADDRESS + " TEXT," + STUDENT_PHONE + " INTEGER);" )

def insert(name,college,address,phone):
    connection.execute("INSERT INTO " + TABLE_NAME + " ( " +
                       STUDENT_NAME + "," +
                       STUDENT_COLLEGE + "," + STUDENT_ADDRESS +
                       "," + STUDENT_PHONE +
                       ") VALUES ( '" + name + "','" + college + "'," +
                       "'" + address + "','" + phone + "');")
    connection.commit()
def show():
    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + ";")

    for row in cursor:
        print("Student id is:", row[0])
        print("Student name is:", row[1])
        print("Student collage is", row[2])
        print("address is",row[3])
        print("phone no. is:",row[4])
    connection.commit()
