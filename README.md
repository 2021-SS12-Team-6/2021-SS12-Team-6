# 2021-SS12-Team-6

## Setup
Install node packages:
```
$ npm install
```

Install Python packages: 
```
$ pip install -r requirements.txt
```

##### Permissions
Bot permissions that are enabled:

## Concept
Our open source project encourages users to improve the project or customize their own fork of the project by adding new images/gifs to our ASL database with the bot's __!add__ command.  

- script updates the ASL dictionary for the bot to use. 
- bot's add command allows users to add images to the ASL Assets folder.

## How to use
After adding the bot to your server (with the necessary permissions), there are several commands that the bot can perform:

__!ASL__  
__!help__
__!add__


Notes: 
- commands are always prefixed with '!'
- a mistyped command brings up the help menu. 
- commands ignore case (lower/upper)

## References

#### Discord bot documentation
https://discordjs.guide/creating-your-bot/commands-with-user-input.html#basic-arguments  


## Next Steps
- Create a private backend, to separate API token authentication from the public facing repository for better security.