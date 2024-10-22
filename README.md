
<h1 align="center">SchoolPrepGenie</h1>
<h2 align="center">"Pack Smart, Stay Informed - The School App Every Parent Needs"</h2>
<p align="center">


# Technologies Used:
![Django](https://img.shields.io/badge/-Django-white?style=for-the-badge&logo=django&logoColor=white&logoWidth=20&color=092E20)
![Python](https://img.shields.io/badge/-Python-white?style=for-the-badge&logo=python&logoColor=white&logoWidth=20&color=3776AB)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-white?style=for-the-badge&logo=postgresql&logoColor=white&logoWidth=20&color=4169E1)
![iOS](https://img.shields.io/badge/-iOS-white?style=for-the-badge&logo=apple&logoColor=white&logoWidth=20&color=000000)
![SwiftUI](https://img.shields.io/badge/-SwiftUI-white?style=for-the-badge&logo=swift&logoColor=white&logoWidth=20&color=F05138)
![Xcode](https://img.shields.io/badge/-Xcode-white?style=for-the-badge&logo=xcode&logoColor=white&logoWidth=20&color=1575F9)


# Mission Statement:

" Connect teachers, parents and students and maintain their data that will make this connection reliable, effective and smooth "

# Mission Objectives:

- **Timetable**: View class-specific timetables.
- **Lunch Menu**: Stay updated with the daily/weekly school lunch  menu.
- **Announcements**: Check upcoming school events and important announcements.
- **Attendance Tracking**: View attendance history of the student.
- **Teacher Feedback**: Directly communicate with teachers through feedback and messages.
- **Course Calendar**: Track important course milestones and holidays.
- **Leave Requests**: Submit leave applications directly through the app.

# Instructions to run program:

- Open a terminal.
- Run following commands:

1. **Set Up the Database:**

```bash
psql -U postgres
CREATE DATABASE schoolprep_django;
\q
```


2. **Install Dependencies:**
###### Please note that the commands for setting up the development environment, creating migrations, and applying them to the database are written in the Makefile for convenience.

```bash
make dev-install
```

3. **Start the Development Server:**
###### The command starts the Django development server using the settings defined in the config/settings/dev.py file. After starting the server, Django typically outputs a message indicating the URL where you can access your application.

```bash
make start
```
4. **You should see output like:**


```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 16, 2024 - 03:34:56
Django version X.Y.Z, using settings 'config.settings.dev'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

5. **Stop the Server:**
```
 To stop the server, press CONTROL-C in  the terminal where it's running.

```



 
