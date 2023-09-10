# UW Couse Scheduler
## A schedule planning agent for University of Waterloo students

## Features:
* Get your current schedule and display in calendar format or list format



  <img src="https://github.com/Sirius-Hou/UW-Course-Scheduler/assets/118148925/75c7cbad-0057-4df0-a54b-01e17ff030fe" alt="image" width="80%" height="80%" />

  <img src="https://github.com/Sirius-Hou/UW-Course-Scheduler/assets/118148925/896e7dfd-f095-4927-b133-c21df2f23354" alt="image" width="50%" height="50%" />
* Calculate and visualize all possible time-conflict-free schedules based on your selection of courses
  ![image](https://github.com/Sirius-Hou/UW-Course-Scheduler/assets/118148925/57c3b293-5fe2-4b01-b794-b288d1e76f85)

  
* Show instructions to convert from your current schedule to a desired generated schedule
* Import your friend's schedule and show instructions to convert from your current schedule to your friend's
* Adjust your schedule (show latest courses/sessions info, add/drop courses, swap sessions), changes reflected on calendar display in real time



## Setup
Step 1: Clone the project to your computer

Step 2: Download Python and set up system variable environment path to Python directory

Step 2: Direct to the *UW-Course-Scheduler* directory and run the  `setup` program as administrator, or copy-paste the following command in terminal and execute:
```
npm init -y
npm i dotenv openai
pip install openai
pip install python-dotenv
pip install -r requirements.txt
```
It will automatically install all necessary packages and libraries.

## Usage
This project is currently in beta test version and runs on terminal. To execute the program, you can follow the following steps:
#### Step 1: Copy your current schedule info from Quest
(1) Login to Quest

<img src="https://github.com/Sirius-Hou/UW-Course-Scheduler/assets/118148925/6cc5d12b-437a-4fc0-b96c-345b064224b2" alt="image" width="300" height="200" />

(2) Go to **Class Schedule**

(3) Pick your term then select all (Ctrl+A) and copy (Ctrl+C)

<img src="https://github.com/Sirius-Hou/UW-Course-Scheduler/assets/118148925/67217f0d-9197-4049-8b19-199b5b225dab" alt="image" width="300" height="200" />

(4) Go to your UW Course Scheduler folder, direct to `docs\client\`, open `client_current_schedule.txt` file, paste the copied text and save the file

<img src="https://github.com/Sirius-Hou/UW-Course-Scheduler/assets/118148925/6552189d-0e13-4040-95ae-eb5ad0936fb1" alt="image" width="300" height="200" />

#### Step 2: Run script
Open terminal and direct to UW-Course-Scheduler directory. Run `python script.py`

<img src="https://github.com/Sirius-Hou/UW-Course-Scheduler/assets/118148925/c309779f-c995-4a2c-aba0-deacefa02491" alt="image" width="300" height="200" />

Follow the instructions to proceed.






