import os
import pyautogui
import keyboard
import time
import pyfiglet
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich import box

# Initialize Rich console
console = Console()

# Dictionary of agents
agents = {
    "breach": 1,
    "brimstone": 2,
    "jett": 3,
    "neon": 4,
    "phoenix": 5,
    "reyna": 6,
    "sage": 7,
    "sova": 8,
    "viper": 9,
    "astra": 10,
    "chamber": 11,
    "clove": 12,
    "cypher": 13,
    "deadlock": 14,
    "fade": 15,
    "gekko": 16,
    "harbor": 17,
    "iso": 18,
    "kay/o": 19,
    "killjoy": 20,
    "omen": 21,
    "raze": 22,
    "skye": 23,
    "yoru": 24
}

# Global variables for coordinates of agent and lock-in agent
start_x = None
start_y = None
new_increment = None
lock_in = None

def find_resolution_values(file_path):
    resolution_values = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip().startswith("ResolutionSizeX="):
                resolution_values["ResolutionSizeX"] = int(line.split("=")[1])
            elif line.strip().startswith("ResolutionSizeY="):
                resolution_values["ResolutionSizeY"] = int(line.split("=")[1])
    return resolution_values.get("ResolutionSizeX"), resolution_values.get("ResolutionSizeY")

def calculate_aspect_ratio(resolution_x, resolution_y):
    aspect_ratio = resolution_x / resolution_y
    return aspect_ratio

def get_aspect_ratio_category(aspect_ratio):
    if aspect_ratio >= 1.7:
        return {
            "width": 1366,
            "height": 768,
            "start_x": 445,
            "start_y": 600,
            "lock_in": (680, 520),
            "increment": 60
        }
    elif aspect_ratio >= 1.66:
        return {
            "width": 1280,
            "height": 768,
            "start_x": 400,
            "start_y": 600,
            "lock_in": (640, 520),
            "increment": 60
        }
    elif aspect_ratio >= 1.6:
        return {
            "width": 1280,
            "height": 800,
            "start_x": 390,
            "start_y": 625,
            "lock_in": (640, 540),
            "increment": 60
        }
    elif aspect_ratio >= 1.33:
        return {
            "width": 1280,
            "height": 960,
            "start_x": 340,
            "start_y": 750,
            "lock_in": (640, 650),
            "increment": 75
        }
    elif aspect_ratio >= 1.25:
        return {
            "width": 1280,
            "height": 1024,
            "start_x": 320,
            "start_y": 800,
            "lock_in": (640, 700),
            "increment": 80
        }
    else:
        return None

def find_game_settings_file(root_dir):
    for root, dirs, files in os.walk(root_dir):
        if "GameUserSettings.ini" in files:
            return os.path.join(root, "GameUserSettings.ini")
    return None

def main():
    
    global start_x, start_y, new_increment, lock_in
    app_name = "\nAuto Lock"
    crawford_art = pyfiglet.figlet_format(app_name, font="crawford")
    console.print(crawford_art, style="bold blue")
    localappdata_folder = os.environ['LOCALAPPDATA']
    valorant_config_path = os.path.join(localappdata_folder, "VALORANT", "Saved", "Config")
    game_settings_file = find_game_settings_file(valorant_config_path)

    if game_settings_file:
        resolution_x, resolution_y = find_resolution_values(game_settings_file)
        console.print(f'\nResolution : [bold]{resolution_x}[/bold] x [bold]{resolution_y}[/bold]')
        aspect_ratio = calculate_aspect_ratio(resolution_x, resolution_y)
        aspect_ratio_dict = get_aspect_ratio_category(aspect_ratio)
        if aspect_ratio_dict:
            width = aspect_ratio_dict["width"]
            height = aspect_ratio_dict["height"]
            xscale = resolution_x / width
            yscale = resolution_y / height
            start_x = aspect_ratio_dict["start_x"] * xscale
            start_y = aspect_ratio_dict["start_y"] * yscale
            lock_in_x = aspect_ratio_dict["lock_in"][0] * xscale
            lock_in_y = aspect_ratio_dict["lock_in"][1] * yscale
            lock_in = (lock_in_x, lock_in_y)
            mean_scale = (xscale + yscale) / 2
            new_increment = aspect_ratio_dict["increment"] * mean_scale
        else:
            console.print("[bold red]Error:[/bold red] Aspect ratio category not found.")
    else:
        console.print("[bold red]Error:[/bold red] GameUserSettings.ini not found.")

    start_key = 'a'  # Press 'a' to start clicking
    stop_key = 's'   # Press 's' to stop clicking

    console.print("[bold cyan]\nAvailable agents:\n[bold cyan]")
    table = Table(show_header=True, header_style="bold magenta", box=box.HEAVY_HEAD)
    table.add_column("Agent Name", style="cyan")
    for agent_name in agents:
        table.add_row(agent_name)
    console.print(table)

    agent_name = Prompt.ask("\nEnter Agent Name:")
    agent = calculate_coordinates(agent_name)

    if agent is None:
        return

    console.print("Press [bold green]'a'[/bold green] to start hold [bold red]'s'[/bold red] to stop")
    click_flag = False  # Flag to control clicking

    while True:
        if keyboard.is_pressed(start_key) and not click_flag:
            console.print("[bold green]Clicking started.[bold green]")
            click_flag = True
            click_between_positions(agent, lock_in, click_flag)
        elif keyboard.is_pressed(stop_key):
            console.print("[bold red]Stopping...[bold red]")
            click_flag = False
            break

def calculate_coordinates(agent_name):
    agent_number = agents.get(agent_name)
    if not agent_number:
        console.print("[bold red]Error:[/bold red] Agent not found!")
        return None
    if agent_number <= 9:
        return start_x + (agent_number - 1) * new_increment, start_y
    elif agent_number <= 18:
        return start_x + (agent_number - 9 - 1) * new_increment, start_y + new_increment
    else:
        return start_x + (agent_number - 18 - 1) * new_increment, start_y + (new_increment * 2)

def wiggle_mouse(position):
    x, y = position
    pyautogui.moveTo(x - 5, y, duration=0.02)  # Move left by 5 pixels
    pyautogui.moveTo(x + 5, y, duration=0.02)  # Move right by 5 pixels
    pyautogui.moveTo(x, y, duration=0.02)      # Return to original position

def click_between_positions(agent, lock_in, click_flag):
    current_position = agent
    while click_flag:
        wiggle_mouse(current_position)
        pyautogui.click(current_position[0], current_position[1])
        time.sleep(0.03)
        current_position = lock_in if current_position == agent else agent
        if keyboard.is_pressed('s'):  # Press 's' to stop clicking
            break

if __name__ == "__main__":
    main()
