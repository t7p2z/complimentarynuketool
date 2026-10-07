import tkinter as tk
import time

root = tk.Tk()
root.title("Complimentary Nuke Tool")
root.geometry("640x480")

streets = ["Park Avenue", "Main Street", "Broadway", "Elm Street", "Maple Avenue", "Oak Street", "Pine Street", "Cedar Avenue", "Birch Street", "Walnut Avenue"]
cities = ["Springfield", "Shelbyville", "Ogdenville", "North Haverbrook", "Capital City", "Cypress Creek", "Brockway", "Waverly Hills", "Little Pwagmattasquarmsettport", "New Springfield"]
countirs = ["USA", "Canada", "Mexico", "UK", "Germany", "France", "Italy", "Spain", "Australia", "Japan"]

def on_info_click():
    name = user.get()
    length = len(name)
    street_index = length % len(streets)
    street_name = streets[street_index]
    adress = f"{length * 3} {street_name}, {cities[street_index]}, {countirs[street_index]}"
    fake_adress.config(text=f"Address: {adress}")
    fake_age.config(text=f"Age: {round(length / 3) * 7}")
    launch.config(state=tk.NORMAL)

def on_launch_click():
    launch.config(text="Nukes Launched!", state=tk.DISABLED)
    time.sleep(1)
    launch.config(text="LAUNCH NUKES", state=tk.NORMAL)

msg = tk.Label(root, text="This is just a stress relief tool. Nukes sent aren't real. Personal information about users is made up.", font=("Arial", 8))
msg.pack(pady=5)

platforms = ["Discord", "YouTube", "TikTok", "Roblox", "Other"]

selected_platform = tk.StringVar(root)
selected_platform.set(platforms[0])

dl = tk.Label(root, text="Select the platform on which the incident occurred:")
dl.pack(pady=10)
dropdown = tk.OptionMenu(root, selected_platform, *platforms)
dropdown.pack(pady=10)

ul = tk.Label(root, text="Enter the username of the problematic user:")
ul.pack(pady=10)
user = tk.Entry(root)
user.pack(pady=10)

cl = tk.Label(root, text="How many nukes would you like to send?")
cl.pack(pady=10)
nukes = tk.Entry(root)
nukes.pack(pady=10)

fake_adress = tk.Label(root, text="")
fake_adress.pack(pady=10)
fake_age = tk.Label(root, text="")
fake_age.pack(pady=10)

info = tk.Button(root, text="Locate Information About User", background="green", fg="white", font=("Arial", 8, "bold"), command=on_info_click)
info.pack(pady=10)

launch = tk.Button(root, text="LAUNCH NUKES", background="red", fg="white", font=("Arial", 24, "bold"), state=tk.DISABLED, command=on_launch_click)
launch.pack(pady=10)

root.mainloop()