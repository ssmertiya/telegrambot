<h3>Telegram Bot Data Logger</h3>
<br>
<h5>Project Goal</h5>
The goal of this project is to create a Telegram bot that can log and store messages, commands, and other data sent by users. This data stored in MongoDB database or cloud storage for later analysis or automation.
<h5>How It Works</h5>
<h6>1.User Interaction</h6>
A user sends a message to the Telegram bot. The bot receives and processes the message.
<h6>2.Logging Data</h6>
The bot saves the message details (e.g., text, sender info, timestamp) to the database.
<h6>3.Response</h6>
The bot reply with a confirmation message to the user.
<h5>Technology Stack</h5>
Programming Language: Python
<br>
Database: MongoDB Atlas
<br>
<br>
<h5>Actions perform to create this Project</h5><br>
1.Create a new Bot and its username: - For this i searched BotFather in telegram and put /start command in BotFather then create new Bot and its username though follow the BotFather guidelines, after then BotFather provides TOKEN.<br>
<br>
•	Bot Name: - “Your_Bot_Name”<br>
•	Bot username: - “Your_Bot_username”<br>
•	TOKEN: - “Put_Your_Tokeid_which_provided_by_BotFather”<br>
<br>
2.Disable the privacy of MyTestBot: - Again I go with BotFather put /setprivacy command than choose bot username and disable the setting. Now bot can access all the messages from a Channel or group.<br>
<br>
3.Install telegram-bot and MongoDB libraries: - Both libraries are installed locally using this command (pip install python-telegram-bot pymongo) these are installed connection established between python and telegram as well as python and MongoDB.<br>
<br>
4.Signup MongoDB Atlas account and create free cluster of 512 MB storage then create username and password for this cluster additionally configure IP addresses to allow access for authorized person after that it provides connection string to connect this cluster.<br>
<br>
•	Username: - “Put_Cluster_username”<br>
•	Password: - “Put_Cluster_password”<br>
•	Connection String: - “mongodb+srv://<username>:<db_password>@<cluster_name>.fy4hf.mongodb.net/?retryWrites=true&w=majority&appName=<cluster_name>”<br>
•	In this string we have to put db_password and authSource=admin, if we get authentication error.<br>
•	Revised String: - “mongodb+srv://<username>:<db_password>@<cluster_name>.fy4hf.mongodb.net/?retryWrites=true&w=majority&appName=<cluster_name>”&authSource=admin<br>
<br>
•	If we use special character in username_db and password_db then we have to encode then put encoded value into string. <br>
<br>
import urllib.parse<br>
username = "myUser@"<br>
password = "myP@ssw#rd!"<br>
encoded_username = urllib.parse.quote_plus(username)<br>
encoded_password = urllib.parse.quote_plus(password)<br>
<br>
5.Finally write a python code for this project (Telegram Bot Data Logger)

