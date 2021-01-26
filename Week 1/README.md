# Week 1

## Table of Contents

## Exercise goals, enviroment

The goal was to create a bootable USB drive for Linux, launch it, use the terminal to list working hardware and finally try out some applications.

As I am already rocking Ubuntu 20.14 on my work laptop, more precisely dual-booting Windows 10 and Ubuntu 20.14, I was already more or less familiar with the procedure having completed it on multiple occasions.

I completed the exercise at home in Alppila, Helsinki. I initially started working around 23.00, slowly completing tasks alongside other activities. I used my work laptop with dual-boot to create the USB boot drive, then tested it on my moderately powerful gaming PC. I'd say the whole ordeal took me around 3 hours in total.

## Prerequisities

To replicate this exercise you will need a computer without any specific hardware, an Internet connection to download Linux Ubuntu and an USB drive with roughly 2.6 GB storage capability. Note that the USB drive will be wiped clean during the procedure.

## Downloading OS & other software

### Ubuntu

For this exercise I chose Ubuntu 20.14 as my Linux distribution. Download for free is available [here](https://ubuntu.com/#download).

![]

### Rufus

Rufus is a free application for creating bootable USB drives. Download for free is available [here](https://rufus.ie/).

![]

## Creating bootable USB drive using Rufus

### Rufus setup

Once I had downloaded & installed everything needed the actual procedure turned out to be quite simple. Using Rufus UI I selected USB drive, browsed for Ubuntu ISO image file and simply hit 'START'. The process took approximately 10 minutes to finish. Once done I unplugged the USB drive from laptop, inserted in PC and navigated to PC's BIOS.

![](https://github.com/JoonasKulmala/Linux-Server-course/blob/main/Week%201/Screenshots/Rufus%20UI.PNG)

### Logs

Going through the logs I could see the moment USB drive was inserted; no restarting or manually selecting was required.

![](https://github.com/JoonasKulmala/Linux-Server-course/blob/main/Week%201/Screenshots/Rufus%20log.PNG)

### Booting USB drive from BIOS

![](https://github.com/JoonasKulmala/Linux-Server-course/blob/main/Week%201/Screenshots/BIOS.png)

## Launching Ubuntu & downloading applications

### Ubuntu desktop

My boot was successful and Ubuntu was up and running!

![](https://github.com/JoonasKulmala/Linux-Server-course/blob/main/Week%201/Screenshots/Desktop.png)

Using terminal command ```sudo lshw -short -sanitize``` I listed the hardware of my PC.

![](https://github.com/JoonasKulmala/Linux-Server-course/blob/main/Week%201/Screenshots/Terminal.png)

## Installing & comparing software

Now it was time to try out software running on Linux. I tested installing some using both Terminal & Software GUI

![](https://github.com/JoonasKulmala/Linux-Server-course/blob/main/Week%201/Screenshots/TerminalDownloading.png)
&nbsp;&nbsp;&nbsp;&nbsp;
![](https://github.com/JoonasKulmala/Linux-Server-course/blob/main/Week%201/Screenshots/SoftwareGUI.png)

### Mines. KMines

The iconic Minesweeper comes in many forms, and as it turns out, operating systems!

![](https://github.com/JoonasKulmala/Linux-Server-course/blob/main/Week%201/Screenshots/Mines.png)
![](https://github.com/JoonasKulmala/Linux-Server-course/blob/main/Week%201/Screenshots/KMines.png)

### Rhytmbox, VLC media player

Rhytmbox comes preinstalled with this Linux distro, but I prefer my trusty VLC media player. Sadly I had no music tracks so I skipped testing for these two. I did however try OS sound effects to make sure all my drivers were working.

![](https://github.com/JoonasKulmala/Linux-Server-course/blob/main/Week%201/Screenshots/Rhytmbox.png)
![](https://github.com/JoonasKulmala/Linux-Server-course/blob/main/Week%201/Screenshots/VLC.png)

### Calculator, Qalculator!

I'm fairly sure every OS out there comes with a calculator. In Ubuntu 20.14 it was called, well, Calculator. I wanted to install more advanced software for my imaginary math problems, though. Qalculator! seemed to be a good choice.

![](https://github.com/JoonasKulmala/Linux-Server-course/blob/main/Week%201/Screenshots/Calculator.png)
![](https://github.com/JoonasKulmala/Linux-Server-course/blob/main/Week%201/Screenshots/Qalculator!.png)