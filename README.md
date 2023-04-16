# Hacknite23 - Team Segmentation Fault

Aim: Our goal was to develop an IPL data analysis application that can provide valuable insights into player performance and team selection. The application generates the following outputs:

  1) Best Playing XI (Team-wise): The application will analyze the performance of players in a specific team for a particular year and generate a recommendation for the best playing XI for that team. The output will be based on various performance metrics such as batting average, bowling average, strike rate, economy rate, etc.
  
  2) Best Playing XI (In a given season, all teams combined) : The application will analyze the performance of all players across all teams and all years and generate a recommendation for the best overall playing XI. The output will be based on various performance metrics such as batting average, bowling average, strike rate, economy rate, etc.
  
  3) Prediction for the best Daily Fantasy Team : The application will analyse the performance of all players across the 2 teams of an upcoming match using fantasy points available on the fantasy.iplt20 page, and generate a recommendation for the best playing XI. The team will consist of players from both teams, and captain, vice-captain, based on performance. Upcoming match data is updated everytime the page is refreshed.
 
  4) Radar charts for top players: Using matplotlib the app constructs a radar chart based on parameters(eg:runs,wickets etc) for the top batsman and top Bowler.
 
To achieve these objectives, we used various data scraping(using selenium), processing and analysis techniques (using pandas).The final output will be presented in an easy-to-understand format for users to make informed decisions about team selection and player performance.

Scraping was done from the official iplt20 website.

### **Installation process:**
  -->Download the zip file of the project from the github repo and extract the file.
  
  -->Pre-requesites: Django,numpy,pandas,selenium,matplotlib. To install use "pip3 install 'module name'"
  
### **To Run the app:**
  -->Navigate to the Pyfiles/ipl_frontend folder and run "python3 manage.py runserver" in terminal
  
[!["IPLAnalysis Screen Recording"](http://img.youtube.com/vi/A_aWvGXSAw4/0.jpg)](http://www.youtube.com/watch?v=A_aWvGXSAw4 "IPLAnalysis Screen Recording")

### ** Future Scope
Fantasy ipl requires you to login to fetch the fantasy points of all the players. An otp that is sent through SMS is to be entered before we scrape the details. So before the scrapping is done we have to manually login and enter the otp to fetch the fantasy points. We plan to improve the scraping by making it completely automated without manual intervention.
  
