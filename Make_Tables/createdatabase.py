import mysql.connector
import os
from dotenv import load_dotenv

directory = os.getcwd()
envindex = directory.find('Make_Tables')
load_dotenv(directory[:envindex]+"/.env")

mydb = mysql.connector.connect(
        host = os.environ.get("DATABASE_HOST"),
        user = os.environ.get("DATABASE_USER"),
        password = os.environ.get("DATABASE_PASSWORD"),
        port = os.environ.get("DATABASE_PORT")
	)

mycursor = mydb.cursor()

try:  #drop the database if it already existss
	mycursor.execute("drop database sac_data")
except:
	print("Database does not exist")

#Creating the databases
mycursor.execute("create database sac_data")
print("Database sac_data created successfully")	
mycursor.execute("use sac_data")

#Creating the tables
mycursor.execute("CREATE TABLE Users(userID char(6) primary key, email varchar(30) unique, password varchar(64), name varchar(64), admin boolean);")
print("Successfully Created Table Users ")   #To Store the login details

mycursor.execute("CREATE TABLE Clubs(clubID char(6) primary key, clubName varchar(64) NOT NULL, about varchar(600), type set('open','close'));")
print("Successfully Created Table Clubs ")   #To store the details of the number of clubs

mycursor.execute("CREATE TABLE ClubMembers(userID char(6), clubID char(6), FOREIGN KEY (userID) REFERENCES Users(userID), FOREIGN KEY (clubID) REFERENCES Clubs(clubID));")
print("Successfully Created Table ClubMembers ")  #To find the students are in which group

mycursor.execute("CREATE TABLE Coordinators(clubID char(6), userID char(6), FOREIGN KEY (userID) REFERENCES Users(userID), FOREIGN KEY (clubID) REFERENCES Clubs(clubID))")
print("Successfully Created Table Coordinators ")  #To store who is the coordie of a group

mycursor.execute("CREATE TABLE Events(eventID Integer(4) PRIMARY KEY, eventName varchar(30), about varchar(600), eventDate date, clubID char(6), registered varchar(3000), attended varchar(3000), FOREIGN KEY (clubID) REFERENCES Clubs(clubID));")
print("Successfully Created Events Table")  #To store all the events

print("Done Creating Tables")
mycursor.close()
mydb.close()
print()
