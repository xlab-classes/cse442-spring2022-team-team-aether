# cse442-spring2022-team-team-aether
cse442-spring2022-team-team-aether created by GitHub Classroom   
**Steps to run this application:**  
1. You must have mySQL installed on your system. In order to do so, go to this link: https://dev.mysql.com/downloads/installer/, and download the latest version of mySQL which your system supports. 
2. You will require the following libraries to be installed in your system:<br/>
   - flask
   - hashlib
   - bcrypt</br>
3. To download these, go into your terminal and run the following commands in your terminal individually:
   - pip install Flask
   - pip install hashlib<br/>
   - pip install bcrypt<br/>
4. You will also need to install mysqlconnector. To do so, run the following command in your terminal: 
   - pip install mysql-connector-python<br/>
(if pip doesn't work, try pip3 since your system might have a Python 3 version)
5. After installing the libraries, go into server.py and change certificate and key to certify the site for the hosted IP address.
6. In server.py, change the server port according to the ports available for the system.
7. In authController.py, change the existing database to connect to the machine’s respective database.
8. Run server.py. 
  


