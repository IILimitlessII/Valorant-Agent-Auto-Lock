import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Dictionary of agents
agents = {
    "breach": 1, "brimstone": 2, "jett": 3, "neon": 4, "phoenix": 5,
    "reyna": 6, "sage": 7, "sova": 8, "viper": 9, "astra": 10,
    "chamber": 11, "clove": 12, "cypher": 13, "deadlock": 14, "fade": 15,
    "gekko": 16, "harbor": 17, "iso": 18, "kayo": 19, "killjoy": 20,
    "omen": 21, "raze": 22, "skye": 23, "yoru": 24
}

class ValorantAutoAgentSelectGUI:
    def __init__(self, master):
        self.master = master
        master.title("Valorant Auto Agent Select")
        master.geometry("1045x550")  # Set window size
        master.resizable(False, False)

        # Frame for images
        self.image_frame = tk.Frame(master)
        self.image_frame.pack(side="top", fill="both", expand=True)

        # Create image buttons for agent selection
        self.image_buttons = []
        for idx, agent_name in enumerate(agents.keys()):
            image_path = f"images/{agent_name}.png"  # Assuming images are named as agent_name.png in the images folder
            if os.path.exists(image_path):
                image = Image.open(image_path)
                image = image.resize((100, 100))  # Resize the image to 100x100 pixels
                photo = ImageTk.PhotoImage(image)
                button = tk.Button(self.image_frame, image=photo, command=lambda name=agent_name: self.select_agent(name))
                button.image = photo
                row = idx // 9  # Calculate row (cycle through 0 to 2)
                col = idx % 9  # Calculate column (cycle through 0 to 8)
                button.grid(row=row, column=col, padx=5, pady=5)
                self.image_buttons.append(button)

        # Frame for file path label and browse button
        self.browse_frame = tk.Frame(master)
        self.browse_frame.pack(side="bottom", fill="x")

        # Add label above the tip
        self.agent_label = tk.Label(self.browse_frame, text="Selected Agent: None", font=("Arial", 14, "bold"))
        self.agent_label.pack(side="top", padx=10, pady=(10, 5))
        
        # Load lock images
        self.lock_grey_img = Image.open("images/lock_grey.jpg")
        self.lock_grey_img = self.lock_grey_img.resize((160, 50))
        self.lock_grey_img = ImageTk.PhotoImage(self.lock_grey_img)

        self.lock_blue_img = Image.open("images/lock_blue.jpg")
        self.lock_blue_img = self.lock_blue_img.resize((160, 50))
        self.lock_blue_img = ImageTk.PhotoImage(self.lock_blue_img)

        self.lock_in_button = tk.Button(self.browse_frame, image=self.lock_grey_img, command=self.lock_in_agent, state="disabled")
        self.lock_in_button.pack(side="top", padx=(0, 10), pady=5)

        self.tip = tk.Label(self.browse_frame, text="Find the GameUserSettings.ini file in folder with mixed characters under Windows folder. Eg:3f9bd-c4f6e-8ba7d-4c8f9-ef6ab-eu/Windows", wraplength=1000)
        self.tip.pack(side="top", padx=10, pady=5)

        self.browse_button = tk.Button(self.browse_frame, text="Browse", command=self.browse_file)
        self.browse_button.pack(side="left", padx=(10, 0), pady=5)

        

        self.current_file_label = tk.Label(self.browse_frame, text="Current GameUserSettings.ini FilePath: None")
        self.current_file_label.pack(side="left", padx=(0, 10), pady=5)

    def browse_file(self):
        valorant_path = os.path.join(os.environ['LOCALAPPDATA'], 'VALORANT', 'Saved', 'Config')
        filename = filedialog.askopenfilename(title="Select GameUserSettings.ini File", initialdir=valorant_path)
        if filename:
            self.current_file_label.config(text=f"Current GameUserSettings.ini FilePath: {filename}")
            self.lock_in_button.config(image=self.lock_blue_img, state="normal")
        print("Selected file:", filename)  # You can use this file path to read GameUserSettings.ini

    def select_agent(self, agent_name):
        agent_number = agents.get(agent_name)
        if agent_number:
            print(f"Agent {agent_name} selected with number {agent_number}")
            self.agent_label.config(text=f"Selected Agent: {agent_name}")
            # Call the function to perform the auto-clicking logic here
        else:
            print("Agent not found!")

    def lock_in_agent(self):
        selected_agent = self.agent_label.cget("text")
        if selected_agent != "Selected Agent: None":
            print(f"Locking in agent: {selected_agent}")
            # Add your logic here to lock in the selected agent
        else:
            print("No agent selected!")

if __name__ == "__main__":
    root = tk.Tk()
    gui = ValorantAutoAgentSelectGUI(root)
    root.mainloop()
