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
    3. Decided to use Gradient boosting and Random Forest as my two models. Both are robust and produce good results. Found a paper discussing methods used for EDD estimation, they suggested boosting models as well as the forest model. link: https://arxiv.org/pdf/2009.11598.pdf
    4. Once the models had been produced and checked, they were then exported using pickle.
    5. A simple website was created using Flask, a python framework. The models were hosted in the backend of the website and were accesed through a REST API.
