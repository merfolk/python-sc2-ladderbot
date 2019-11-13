# Python-sc2 Ladder Bot Example
This is a StarCraft 2 example bot coded using Burny's fork of [python-sc2](https://github.com/BurnySc2/python-sc2/) that has the ability to integrate with the [LadderManager](https://github.com/Cryptyc/Sc2LadderServer) so that it can run against other bots on [SC2 AI Ladder](http://sc2ai.net) and [AI-Arena](http://ai-arena.net).

This bot can be run either locally against a computer opponent, or through the [LadderManager](https://github.com/Cryptyc/Sc2LadderServer). The file "run.py" is used for both variants, which loads ExampleBot from example_bot.py, and starts the appropriate game type.

## Requirements
* [Python 3.6+](https://www.python.org/downloads/), preferable 64-bit
* Burny's fork of [python-sc2](https://github.com/BurnySc2/python-sc2/)
    * note the use of Burny's fork instead of Dentosal's.

## Usage

### Run a basic game 
```
python run.py
```
You can modify run.py to load your own bot or change the computer opponent.

### Installing Ladder Manager (LM)

[Ladder Manager](https://github.com/Cryptyc/Sc2LadderServer) can be used to run matches between bots or even to play against a bot as human.

#### Installing

1. Download and extract a [binary release of Ladder Manager](https://drive.google.com/file/d/18lmZEzzZEP1VhqmHKsiSn9g7P2BDutNJ/view)
    1. it should contain example bots and also a compiled version of [LadderGUI](https://github.com/NikEyX/LadderGUI).  

#### Compiling from source

1. You can find source code from the [Ladder Manager Github repository](https://github.com/Cryptyc/Sc2LadderServer).
1. You have to also compile the [LadderGUI](https://github.com/NikEyX/LadderGUI).

#### Requirements for a bot

Basically LM needs to know these things from a bot:
* the bot's name and race
* how to start the bot (`run_ladder.py`)
* All the bot's requirements either bundled with the bot or installed in the runtime
    * in Python, usually with `pip install`
    * Use `pip list` to see all installed packages.

#### Running bot vs. bot matches

1. Copy the relevant files from this repo into /Bots/**[YourBotName]**/ inside the Ladder Manager directory.
1. Bot directory should contain a **LadderBots.json** file. Make sure to replace the [placeholders] with your bot's info.

    ```
    {
      "Bots": {
        "[YourBotName]": {
          "Race": "[Terran/Protoss/Zerg/Random]",
          "Type": "Python",
          "RootPath": "./",
          "FileName": "run_ladder.py",
          "Debug": false
        }
      }
    }
    ``` 

1. Start **LadderGUI.exe**
1. select your bot as a player
1. Click **generate & run**

As always, it is advisable to automate this process as much as possible and add it to version control. Most bot authors have a script that creates a zip archive from the bot.

#### Running bot vs. human matches

A human bot is simply a bot launches but does nothing. For Starcraft 2 to register the player's input, the human "bot" must be player 1.

#### Troubleshooting

A bot may not work with LM because... 

1. The bot directory name differs from the bot name in LadderBots.json
1. The bot name is invalid
    1. it seems LM does not like eg. an underscore `_` in the name. Best to stick to just a-z, A-Z.
1. LM can not find the run script specified in LadderBots.json
1. Python runtime does not have all all the required dependencies
    1. Check the error log.
    1. It is possible to bundle bot with your own library to make sure it is available on the running machine. For example, python-sc2 can be bundled with your bot by just copying the complete library code in /sc2 folder.

Error log is written under the bot's **data** folder and can help in debugging.

## Bot coding
See [python-sc2](https://github.com/BurnySc2/python-sc2/) for more example bots and documentation.
