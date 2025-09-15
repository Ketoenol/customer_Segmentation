# customer_Segmentation
Customer Segmentation using Python, RFM analysis, and K-Means clustering to identify and target key customer groups.

# Customer Segmentation Project

A Python project performing **customer segmentation** on retail data using **RFM analysis** and unsupervised learning techniques. This project helps businesses identify different types of customers and target them effectively.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [License](#license)

## Overview
The project loads an online retail dataset, cleans the data, calculates **Recency, Frequency, and Monetary (RFM) scores**, and clusters customers into meaningful segments using **K-Means clustering**.

## Features
- Data cleaning and preprocessing
- RFM scoring of customers
- Customer segmentation using K-Means clustering
- Visualization of customer segments
- Exporting segmented data for further analysis

## Technologies Used
- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ketoenol/customer_segmentation.git

## Usage  
-1. Make sure `onlineRetail.csv` is in the project folder.
-2. Run the main script:

   python3 customer_segmentation.py

-3. After running, the following will happen:
   - Data will be cleaned and preprocessed.
   - RFM scores will be calculated.
   - Customers will be clustered into segments using K-Means.
   - Output will be saved to `customer_segments.csv`.
-4. You can open `customer_segments.csv` to see the segmented customer data.

## Dataset 
- [Download onlineRetail.csv](https://drive.google.com/file/d/1gReuh5dAEF5FQv_fy78-laLd_GEyVqwk/view?usp=sharing)

##Liscence 
- This project is licensed under the MIT License.
