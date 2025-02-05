import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import sys

print('Initalizing...')

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def read_chromedriver_path():
    config_path = os.path.expandvars(r"%AppData%\Local\DiamondFinder\config.txt")
    if os.path.exists(config_path):
        with open(config_path, 'r') as file:
            path = file.readline().strip()
            return path
    return None

def kill_all_threads():
    clear_console()
    print("Error: App hasn't been setup")
    time.sleep(5)
    sys.exit(1)

chromedriver_path = read_chromedriver_path()
if not chromedriver_path or not os.path.exists(chromedriver_path):
    kill_all_threads()

def diamond_finder():
    clear_console()
    print("Diamond Finder v1.4")
    print("Select a Version")
    print("[1] Java 1.17")
    print("[2] Java 1.18")
    print("[3] Java 1.19")
    print("[4] Java 1.20")
    print("[5] Java 1.20.2")

    version_choice = input("Enter the number corresponding to your version: ")
    versions = {
        "1": "java_1_17",
        "2": "java_1_18",
        "3": "java_1_19",
        "4": "java_1_20",
        "5": "java_1_20_2"
    }
    platform = versions.get(version_choice)

    if not platform:
        return

    seed = input("Input your seed: ").strip()
    coords = input("Input your coordinates (X, Y, Z): ").strip()
    try:
        x, y, z = [c.strip() for c in coords.split(',')]
    except ValueError:
        return

    url = f"https://www.orefinder.gg/ores?filter=big&ores[]=diamond&platform={platform}&position[]={x}&position[]={y}&position[]={z}&seed={seed}"
    clear_console()

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--log-level=3")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    service = Service(chromedriver_path)
    service.creation_flags = 0x08000000

    try:
        driver = webdriver.Chrome(service=service, options=options)
    except:
        kill_all_threads()

    driver.get(url)
    time.sleep(5)

    diamonds = driver.find_elements(By.XPATH, "//span[contains(@class, 'text-sm font-semibold')]")
    coordinates = driver.find_elements(By.XPATH, "//div[contains(@class, 'col-[2] row-span-2')]//p")

    diamond_coords = []
    for diamond, coord in zip(diamonds, coordinates):
        print(f"Diamonds: {diamond.text}, Coordinates: {coord.text}")
        coord_values = coord.text.split('/')
        if len(coord_values) == 3:
            diamond_coords.append((diamond.text, coord_values))

    driver.quit()

    export_choice = input("Would you like to export this data to Xaero's Minimap Waypoints? [Y or N]: ").strip().upper()
    if export_choice == 'Y':
        with open(os.path.expanduser("~/Desktop/waypoints.txt"), 'w') as f:
            for index, (diamond, coords) in enumerate(diamond_coords, start=1):
                x, y, z = [c.strip() for c in coords]
                f.write(f"waypoint:diamonds{index}:D:{x}:{y}:{z}:0:false:0:gui.xaero_default:false:0:0:false\n")
        print('waypoints.txt saved to desktop')

    input("Press any key to exit...")

if __name__ == "__main__":
    diamond_finder()
