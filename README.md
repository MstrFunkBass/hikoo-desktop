# Hikoo Desktop
A python application to display an AI-generated image and Haiku as a Windows background.

1. [How Does It Work?](#how-does-it-work)
1. [How To Install](#how-to-install)
1. [Problems and Things To Do](#problems-and-things-to-do)


# How Does It Work?

### Querying Chat-GPT
This project contains python code to query OpenAI's Chatgpt to generate a Haiku, and generate an image based on the Haiku.  
The OpenAI API is used for this which needs a secret key. This secret key is stored on the Windows device's environment variables.  
I use chat-gpt 3.5 turbo, and each wallpaper refresh costs about $0.02.

### Processing the image and text
These elements are then processed - using the Pillow python library - to create an image that can be used as a desktop wallpaper.  
The aspect ratio can be adapted in-code for different sized displays.

### Chaning the Wallpaper
Finally, the windows api is used via python to change the device wallpaper to the processed image.

### Execution
The code can be executed manually, however for ease there are two execution files (a .bat and a .vbs).  
The .bat file contains command prompt prompts to activate the virtual environment, and run the main script.  
The .vbs file can be execued to run the .bat file without opening the command prompt.  

# How To Install

To use this on your Windows computer, you will need:
- python 3.11
- a virtual enviroment called '.venv' at the same directory that the 'hikoo-desktop' directory sits in
- to install all of the packages on the venv from the requirements.txt file
- access to OpanAI API (to get secret key) - use 'chat-gpt 3.5 turbo'
- to set up an environment variable for the OpenAI secret

`[Add to here!]`


# Problems and Things To Do
