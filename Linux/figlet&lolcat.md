# Colorful Terminal Banner with Figlet & Lolcat

Enhance your terminal experience by creating a vibrant and eye-catching banner using Figlet and Lolcat. Follow these simple steps to install the required tools and customize your terminal banner.

### Step 1: Update Package Lists
```bash
sudo apt update
```

### Step 2: Install Figlet and Lolcat
```bash
sudo apt install figlet lolcat
```

### Step 3: Clone Figlet Fonts
```bash
git clone https://github.com/xero/figlet-fonts
```

### Step 4: Copy Fonts to Figlet Directory
```bash
sudo cp figlet-fonts/* /usr/share/figlet/.
```

### Step 5: Create and Display Colorful Banner
```bash
figlet -f slant "eSparkBiz" -c | lolcat && figlet -f digital "Tag Line" -c | lolcat
```

### Step 6: Update Bashrc Configuration
```bash
nano ~/.bashrc
```
Scroll to the end of the file and add the following line:
```bash
# Print colorful banner on terminal startup
figlet -f slant "eSparkBiz" -c | lolcat && figlet -f digital "Tag Line" -c | lolcat
```
Save the changes (Ctrl + O) and exit (Ctrl + X).

Now, every time you open a new terminal, your custom banner will greet you in a colorful and stylish way. Enjoy your enhanced terminal experience with Figlet and Lolcat!