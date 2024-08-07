# ml_assign_Democritos
ML assign for Democritos Msc in AI

  This is a project that has been created as a task for the Machine Learning lesson
of the Inter-Institutional MSc entitled "Artificial Intelligence" that is organized by 
The Department of Digital Systems, School of Informatics and Communication Technologies, 
of University of Piraeus, and the Institute of Informatics and Telecommunications of NCSR "Demokritos".
url: "https://msc-ai.iit.demokritos.gr/en".

  This project is a web service where a user can calculate the fuel consumption of a certain ship (for a specific
trip) by importing the values that specify it. An ML model predicting the main engine's fuel consumption has been fitted to 
hystorical data that consist the dataset.csv (attached). The total number of rows is 65868 and the
number of columns is 46.

The test_dataset.csv is a seperate dataset used for testing and represents a complete different trip of the ship that took place in a later period of time.

The code has been created with the use of python version 3.9.13. In order to recreate the same working enviroment (and to ensure trouble-free code execusion) it is advised to run under virtual enviroment that should be created with the use of requirements.txt (attached).

The web interface has been constructed with the use of django framework from python.In the section A of text file "Django_commands.txt" (attached) there are instructions in order to bring the development server to life.

The ml_training.py script is used in order to determine the best algorithm and tune its hyperparameters. The tuning process has been performed with the use of cross-validated grid-search over a parameter grid (splitting the dataset in 10 folds).The most suitable "tuned" algorithn is saved and then used in django framework in order to predict the main engine fuel consumption.

User can input Trip duration (in days), Engine_RPM, Aft draft of ship, Fore draft of ship and Ship Heading. The service uses the saved trained model in order to return the cumulative fuel oil consuption and a diagramm of the ships daily fuel oil consumption.

The result_scores.py script can be used by the user to visualize the results of the tuning process of all algorithms (which can also be seen in result.txt file), in order to justify the final selection of "best" algorithm.
