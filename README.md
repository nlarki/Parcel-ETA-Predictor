# ParcelLab-Task - 📦

## The purpose of the project

- Develop 2 different ML Models for the estimation of the Delivery Date (EDD)
  1. Data exploration and preparation: understanding, cleaning, variable retention/Feature selection, etc.
  2. Model Selection
  3. Data Partitioning: Training and testing
  4. Model Comparison /Evaluation:
  5. Parameter tuning.
  6. Develop a simple API for the deployment of the output, feel free to use the framework which suits the best for this task.

## Methods used - 💻

1. Utalised jupyter notebook so that i could do some pre analysis of the data
2. Performed some transformation e.g. changing individual dates to epoch times for regression
3. Decided to use Gradient boosting and Random Forest as my two models. Both are robust and produce good results.
4. Found a paper discussing methods used for EDD estimation, they suggested boosting models as well as the forest model. link: https://arxiv.org/pdf/2009.11598.pdf
5. Once the models had been produced and checked, they were then exported using pickle.
6. A simple website was created using Flask, a python framework. The models were hosted in the backend of the website and were accesed through a REST API.

## Report based Analysis

I used SAS VA which is a tool similar to PowerBI. The report allows the user too look at deliveries at
a courier based level. Have a look here: https://viyawaves.sas.com/SASVisualAnalytics/?reportUri=%2Freports%2Freports%2Ffb24327b-4213-42e5-8ca6-2d4363b93ab2&sectionIndex=0&sso_guest=true&sas-welcome=false

## How to use the program

1. In order to use the program you must first clone the repo.
2. After cloning the repo ensure you install the requirements.txt
3. change directory to EDT-wbsite and then run: python app.py
4. website should host on: http://127.0.0.1:5000/
5. Enter information into the text boxes.
6. Due to the values being encoded during the prep stages, values such as GBR now have numerical values.
7. I recommend using these values as an example for the time being (obviously mess around with these values at the same time)
   Delivery Region: 44, Courier: 3, Return Tracking: 0, Delivery Location: 3, Transit Date: 2020-09-02 13:19:00, Pick up date: 2020-09-02 00:00:00
