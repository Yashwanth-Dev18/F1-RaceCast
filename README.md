**[F1: RaceCast](https://f1-racecast-hybrid-era.streamlit.app/)**



<img width="397" height="203" alt="RaceCast Thumbnail" src="https://github.com/user-attachments/assets/fd60adc1-070f-4906-8b90-fe18af99b764" />


**Formula 1: Pinnacle of Motorsport**



***The project began with an ambitious, yet pragmatic goal: to build a PoC to predict Formula 1 racing's grid results using machine learning.*** 


This was particularly challenging given F1's inherent unpredictability. Each race contains countless variables that defy pure performance metrics: 
first-lap collisions, DNFs, unexpected mechanical/engine failures, strategic gambles on safety cars, and sudden weather changes can instantly rewrite 
a team's destiny. The core challenge was building a model that could see through this chaos to identify the true underlying performance hierarchy.

***Initial Phase***


The initial phase involved bringing the thought to an idea with buisiness value. This model is intended to provide a quantifiable framework for assessing 
driver & car performance, with applications in fan engagement platforms, media analysis, and team strategy simulation. With this value proposition defined, 
the crucial task of feature engineering began. I started with including lot of features such as Qualifying results, FP driver pace, driver statistics, four
different weather consitions impacting tyre degredation and grip on the track. Then, I deduced the complexity to having 4 crucial features including drivers,
cars, circuits and track conditions using feature selection. After that, began the monumental task of data collection & processing and creaed my own dataset. 
I designed and built a custom script to scrape, structure, and process historical F1 data into a comprehensive CSV file, creating a dataset spanning from 2014 
to 2025 with almost 200 one-hot encoded features including 40+ drivers, 100+ cars, 30+ circuits, and 2 weather-based track conditions. My first modeling 
attempts were a rigorous process of experimentation, testing everything from basic Linear Regression to advanced ensembles like LightGBM and XGBoost.

<img width="476" height="367" alt="Model Evalutation Scatter Plot" src="https://github.com/user-attachments/assets/1f0b965a-9007-4e2e-b99d-19785f5e1841" />

To make a logical, data-driven decision on the best model, I employed extensive diagnostic data visualizations. I generated confusion matrices, feature 
importance charts, scatter plots of predicted vs. actual values, and error distribution plots to compare each model's performance and behavior deeply. 
This analysis revealed that Gradient Boosting was the most balanced, offering superior consistency and inherent regularization that made it less prone to 
overfitting. After selecting it, I dove deeper into noise reduction by performing a thorough feature analysis: I split features from the target, checked 
each feature's variance, and measured its correlation with the race result. This process of noise cancellation was crucial, as it helped refine the model's 
focus on the most predictive signals, leading to improved consistency and accuracy in predicting race pace and final results.

<img width="905" height="424" alt="Noice Analysis Result after removal of Unnecessary Features " src="https://github.com/user-attachments/assets/4a368ced-eb3a-43e6-b593-6e0876a6c150" />

***Recent Data Prediction Phase***


Driven to further improve accuracy, I hypothesized that more recent data would be more relevant. I created a second dataset focused solely on the 
2020-2025 seasons, believing the modern era's regulations would provide a cleaner signal. Surprisingly, this refinement backfired; reducing the dataset's 
size and variety removed crucial historical patterns that the model needed to understand performance hierarchies, ultimately making predictions worse. 
This was a critical learning moment. 

***Final Phase***


I returned to the full 2014-2025 dataset and shifted my strategy to meticulous hyperparameter tuning. By optimizing the Gradient Boosting model's 
parameters and ensuring it could learn the fundamental relationship that the car matters more than the driver—which it successfully did, 
assigning 56% of importance to cars—I finally achieved a breakthrough, reducing the MAE to a more respectable 3.4 positions. With a robust model in hand, 
the final phase was about creating a tangible product. I developed and deployed an interactive web application using Streamlit, bringing the "F1: RaceCast" 
predictor to life and demonstrating a complete machine learning lifecycle. The model serves its prupose to provide a quantifiable framework for assessing 
driver vs. car performance on various scenarios, with potential applications in fan engagement, media analysis, and team strategy simulation
in the Formula 1 Motorsport.

<img width="741" height="359" alt="RaceCast Prediction" src="https://github.com/user-attachments/assets/cdfd9c66-abb5-4b7e-8605-daaac20fb098" />



**Example Execution**:


Predicted Position of Lewis Hamilton in the 2025 Azerbaijan GP in the Ferrari-SF25 car: P6, Actual Result: P8 

**Conclusion**


While the model's Mean Absolute Error of 3.55 positions might initially seem high, this performance must be contextualized within F1's 
extreme unpredictability—a sport where even the fastest car has only a 65% historical probability of winning from pole position. The model's 
true value lies not in predicting exact finishing orders, but in quantifying the performance hierarchy between drivers and cars. This provides 
tangible business value for media companies seeking data-driven race previews, fantasy sports platforms needing performance projections, 
and team strategists analyzing competitor strengths across different circuit types, transforming subjective racing expertise into 
objective, quantifiable insights.


***Developed by: [Yashwanth Krishna Devanaboina](www.linkedin.com/in/yashwanth-krishna-devanaboina-66ab83212)***


***AI/ML Engineer | Software Developer | CS student at Lnu | AWS Certified Cloud Practitioner | Cisco Certified Data Analyst***

