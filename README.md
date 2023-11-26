# ml_assign_Democritos
ML assign for Democritos Msc in AI

  This is a project that has been created as a task for the Machine Learning lesson
of the Inter-Institutional MSc entitled "Artificial Intelligence" that is organized by 
The Department of Digital Systems, School of Informatics and Communication Technologies, 
of University of Piraeus, and the Institute of Informatics and Telecommunications of NCSR "Demokritos".
url: "https://msc-ai.iit.demokritos.gr/en".

  This project is a web service where a user can calculate the fuel consumption of a certain ship (for a specific
trip) by importing the values that specify it. An ML model predicting the main engine's fuel consumption has been fitted to 
hystorical data that consist the dataset.csv (attached). The total number of instaces is 263511 and the
number of attributes is 65.

The code has been created with the use of python version 3.9.13. In order to recreate the same working enviroment (and to ensure trouble-free code execusion) it is advised to run under virtual enviroment that should be created with the use of requirements.txt
 
 Two Machine Learning regression algorithms (SVR and GradientBoosting) were used in order to predict a ship's main engine fuel consumption (label = ME FUEL CONSUMPTION). The other 66 column names (displayed in dataset_attributes.txt) represent the training attributes. 

The ml_training.py script is used in order to determine the best algorithm and tune its hyperparameters. The most suitable "tuned" algorithn is saved and then used in django framework in order to predict the main engine fuel consumption.
User input values of interest in the django's front end form and the CUMULATIVE model's prediction is returned.
