# Valorant Auto Agent Select

Automatically selects agents in Valorant based on the resolution of your screen. Currently have 24 Agents (Valorant Version 8.05). Uses Valorant user config file to get the current resolution then calculates the necessary co-ordinates of the agent and lock-in button.

## This script works with any resolution that has an aspect ratio of:
### - 16:9
### - 16:10
### - 5:4
### - 5:3
### - 4:3

## !! Note !!
### If you have multiple accounts you will need to set the GameUserSettings.ini manually as you may have multiple Config folders

Change on line 125:
```python
game_settings_file = find_game_settings_file(valorant_config_path)
```
to
```python
game_settings_file = "C:\\Users\\{YourUsername}\\AppData\Local\\VALORANT\\Saved\\Config\\{long string of random characters}\\Windows\\GameUserSettings.ini"
```
Tip: 
The Windows folder contains 2 files GameUserSettings.ini and RiotUserSettings.ini to check your account search your in-game username in RiotUserSettings.ini

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/Valorant-Agent-Auto-Lock.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Valorant-Agent-Auto-Lock
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure that your Valorant game is running and in the main menu.

2. Run the script:

    ```bash
    python autolock.py
    ```

3. Follow the on-screen instructions to select an agent and start the auto-clicking process.
   
4. Start search in-game.
   
5. Press 'a' to start clicking and hold 's' to stop.

## Compatibility

This script is compatible with Windows, macOS, and Linux.

## Disclaimer

This script is intended for educational purposes only. Use it responsibly and respect the terms of service of Valorant.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
