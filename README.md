# Atlas Diamond Finder

## Overview
Atlas Diamond Finder is a tool that helps Minecraft players locate diamond ore veins using seed-based world generation.

## Features
- Supports **Java Edition** versions:
  - 1.17
  - 1.18
  - 1.19
  - 1.20
  - 1.20.2

## Prerequisites (For Python Users)
- Python 3.x installed
- Google Chrome installed
- [Chromedriver](https://sites.google.com/chromium.org/driver/) (Ensure it matches your Chrome version)
- Required Python packages:
  ```sh
  pip install selenium
  ```

## Installation
### Using the EXE Release
1. Download the latest **EXE release** from [GitHub Releases](https://github.com/yourusername/Atlas-Diamond-Finder/releases).
2. Extract the ZIP file.
3. Run **setup.bat** to configure Chromedriver.
4. Launch **AtlasDiamondFinder.exe** and follow the on-screen instructions.

### Using Python
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/Atlas-Diamond-Finder.git
   cd Atlas-Diamond-Finder
   ```
2. Install dependencies:
   ```sh
   pip install selenium
   ```
3. Setup **Chromedriver**:
   - Run **setup.bat** (included in the repository) to configure Chromedriver automatically.
   - Alternatively, manually place the `chromedriver.exe` file in a known location and create a configuration file at:
     ```
     %AppData%\Roaming\Local\DiamondFinder\config.txt
     ```
   - Add the full path to `chromedriver.exe` in the file.

## Usage
1. Run the tool:
   - **EXE Version**: Double-click `AtlasDiamondFinder.exe`.
   - **Python Version**: Run the script manually:
     ```sh
     python source.py
     ```
2. Select your **Minecraft version**.
3. Enter your **world seed**.
4. Input **X, Y, Z coordinates**.
5. The tool will scrape **orefinder.gg** and display diamond locations.
6. Optionally, export waypoints for **Xaero's Minimap**.
7. The waypoints will be saved to `waypoints.txt` on your **desktop**.

## Example Output
```
Diamond Finder v1.4
Select a Version
[1] Java 1.17
[2] Java 1.18
[3] Java 1.19
[4] Java 1.20
[5] Java 1.20.2
Enter the number corresponding to your version: 3
Input your seed: 123456789
Input your coordinates (X, Y, Z): -124, 12, 340

Diamonds: 4, Coordinates: -130 / 10 / 345
Diamonds: 2, Coordinates: -120 / 11 / 335

Would you like to export this data to Xaero's Minimap Waypoints? [Y or N]: Y
waypoints.txt saved to desktop
```

## Troubleshooting
### "App hasn't been setup" Error
- Run **setup.bat** to configure Chromedriver automatically.
- Ensure you have the correct **chromedriver path** set in:
  ```
 %AppData%\Roaming\Local\DiamondFinder\config.txt
  ```

### Chromedriver Issues
- Make sure **chromedriver.exe** matches your installed **Chrome version**.
- Download the latest version from [here](https://sites.google.com/chromium.org/driver/).

## Contributions
Feel free to submit **issues** or **pull requests** to improve the tool!

## Disclaimer
Atlas Diamond Finder is **not affiliated** with Mojang or Minecraft. Use this tool at your own discretion.

