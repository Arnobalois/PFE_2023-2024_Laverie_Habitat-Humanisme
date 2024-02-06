# PFE_2023-2024_Laverie_Habitat-Humanisme
Final project of my engineering school 
During this project I had to create a system for a rpivate laundry where users can select a laundry machine and than pay for what the consume ( only the electrical cosumption is colected)
# How it work
## Senor
For this project I had to find a sensor folowing multiple specification. I made a study to select the best match for the specs , and at the end I've choosen the sonoff PowR3 6A.
You can find it on the link below : 

link 1 
link 2 
link 3

## HomeAssistant 
This sensor is commonly used with a internet connection because it need to upload the data on Sonoff's cloud but in my project I need to use this sensor in a Lan mode. That's where home assistant make it's entry , home Assistant allow me to use the sensor in lan mode , it collect data from the sensor and store them instead of sending them to the cloud.
To do so I need to install a specific service made by the community available on the following link : 

link service sonoff 

## WebApp in DJango 
We have the sensor , we have a solution for the lan mode and now we need a app that can comunicate with home assitant and store date. After discussion with the client , we decide to create a WebApp available a dedicated network. With this solution users can use the app from anywhere in the bulding with the only restriction , be connected to the network.
To create this WebApp I decided to create a prototype in Django becasue althought it is dense and most of the proposed package are useless for the project , It simplify a lot of things and with those simplification I can create a App faster 

# How to use it ? 
## Preparation
For this project you need 4 things :
-A router (It can be your internet provider router)
-A network with internet access (it is needed for the first 2 part )
-A computer with a network card (to connect to the router)
-1 sonoff Pow R3 Sensor 

This project use docker , therefor you need a windows 10 or 11 at least to be able to install docker. You also need to install WSL2 on your computer 


For Information, this project was created using a raspberry pi 4 2go with a OpenWrt OS installed which come with docker. For the entire projet I use docker to host the HomeAssistant server and the WebApp

## Installation Steps 
To use this project you have to folow all the steps below 
### First : Home Assistant
This step require a pc with Linux os or a Windows with WSL 2 installed

#### Docker for Windows 

#### Docker for Linux 

Update
```sh
$ sudo apt update 
```

```sh
$ sudo apt isntall 
```


### Second : Connect a sensor to Home Assisant

### Third : install the web app

### Optional : install WSL 2 on Windows
