# Discord bot 'Legion'
## by DaveMitHut

### Preface
I wrote this little discord bot for my own private server in april 2019.
In April 2020 we moved this bot to the server for our streaming community
"Helden Auf Papier". In July/August 2020 I rewrote the bot in Python and
added additional functions for twitch integration and more. After another
code review in may 2021, this bot got a major update concerning its code.

The bot has basic functions related to *Magic: The Gathering*, *Dungeons & Dragons*
and RPGs in general. It is named after the character 'Legion' from the Mass Effect
game series.

### Commands
All commands are described in the following table:

**Name** | **Description**
---- | ----
**!help** | display all available commands
**!coinflip** | flip a coin
**!roll xdx+x** or **!roll xdx-x** | roll the specified number of a dice with an optional +/- modifier
**!card cardname** | display the image of the requested card
**!rulings cardname** | display all available rulings for the requested card and their source
**!legality cardname** | display the legality of the requested card for the standard, modern & commander formats

### Community-specific commands
All community-specific commands and their respective communities are described in the following table:

**Name** | **Description** | **Community**
---- | ---- | ----
**!cassandra** | story-specific command | HeldenAufPapier

### Additional functions
In addition to the specified functions above, this bot will also greet all new
server members. Furthermore, the bot will grant a specific role to every new member of
the server.

### Disclaimer
The literal and graphical information presented by this bot about Magic: The Gathering,
including card images, the mana symbols, and Oracle text, is copyright Wizards of the Coast,
LLC, a subsidiary of Hasbro, Inc. This bot is not produced by, endorsed by, supported by,
or affiliated with Wizards of the Coast. The same holds true for literal and graphical
information about Dungeons & Dragons.
