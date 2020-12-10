# Pollution-Tracker

It is a program that tells the API(Air Pollution Index) and further pollutants level in air of any city in the world.

## Introduction
So this is the Python program that uses Python as a programming language. I have to use the API of [AQCIN](https://aqicn.org/city/all/) website to fetch information about the pollution level of the city. So I have used an API key to get access to website data. Here we first fetch the data in the form of a Dictionary and the according to the key we display the output of that field. If the field is not available we show a message with "Not available". And after that using Matplotlib, we plot the pie chart of various pollutants in the air.

## Installation
```bash
https://github.com/sagarmude7/Pollution-Tracker.git
cd Pollution-Tracker
```

## Packages

I have used three packages 
* Tkinter : For the GUI of window
```bash
pip install Tkinter
```
* Matplotlib : To plot the pie chart which shows the percentage of different pollution levels in the air of the city.
```bash
pip install matplotlib
```
* Request : To fetch the information from the website.
```bash
pip install requests
```



## Output
* Main Window which ask the name of the city to user

![Main Window](https://github.com/sagarmude7/Pollution-Tracker/blob/main/Output/Nagpur.png)
* Output window which show the distribution of pollutants in the air of the city

![Nagpur](https://github.com/sagarmude7/Pollution-Tracker/blob/main/Output/Window.png)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Improvement Required
* Position of City on Map.
* Must show past 15 days API.
* Must show an error if the city name does not exist.
* Not to include the parameter whose information is currently not available.

## License
[MIT](https://github.com/sagarmude7/Pollution-Tracker/blob/main/LICENSE)
