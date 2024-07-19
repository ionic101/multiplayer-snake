# Multiplayer Snake Game
Classic snake game in retro style with multiplayer

*MULTIPLAYER IN DEVELOPMENT!*

## Requirements
- python==3.12.4
- pygame==2.5.2

## Launch
Run `main.py` in the folder `client`

## Architecture
The project was executed in the MVC pattern. The game_engine components help break down game development into the following components: Scene, Viewer, Controller. Scene stores information about objects. The Viewer draws objects on the screen. The controller reads the player's keyboard and mouse and interacts with objects. Viewer and Controller depend on the Scene

## Screenshots
![menu](https://github.com/user-attachments/assets/2a6e5ab3-5009-48e0-abe7-fc1e9662c86f)
![singleplayer](https://github.com/user-attachments/assets/5d7f5acc-86d5-48f5-8f1c-85d2fb16cae7)
