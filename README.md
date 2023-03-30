# LA Crime Awareness and Weather

## Motivation
The daily crime total in Los Angeles is 1.11 times the California average and 1.22 times the national average.
As students in the University of Southern California, it is not a strange thing to receive various criminal alerts from the Department of Public Safety.
Considering the safety of social beings, This platform presents various information about the past crimes and the weather conditions at the time when the crime happened to help people make choices and necessary precautions for their travel and commutes, minimizing the occurrence of crimes as much as possible.

## Dataflow
We write two crawlers to scrape the crime and weather data and upload the raw data to the Firebase.

Data ETL stage (extract, transform, load) would be implemented in Spark after which the cleaned data be injected into Mysql database.

For our UI-based website, we utilize Flask to connect mysql server, transmit the request data to the Front-end, and visualize the crime and weather data in our web page based on BootStrap and Google Map Api.

Finally we deployed our whole project on an AWS EC2 instance.

![framework](https://user-images.githubusercontent.com/113748465/228740014-c1daf63a-e734-4ff6-9438-0ab671be388d.png)
