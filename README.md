# LaunchMate

**LaunchMate** is a smart automation script designed to streamline your daily workflow by automatically launching your essential websites and applications. It features intelligent frequency control to prevent redundant launches and maintains a detailed usage log.

## 🚀 Purpose & Problem Solving

In a daily routine, manually opening the same set of websites (news, email, project boards) and applications (IDEs, communication tools) can be repetitive and time-consuming. **LaunchMate** solves this by:

1.  **Automating Routine**: Launches all your required tools with a single execution.
2.  **Smart Frequency Control**: Unlike simple batch scripts, LaunchMate checks the last time it ran. If you accidentally trigger it or restart your computer shortly after the first run, it respects a configurable "cooldown" period (e.g., 4 hours) and won't open everything again.
3.  **Usage Tracking**: Keeps a local log (`log.csv`) of when and how often you use your setup, tracking both daily and lifetime usage.

## ✨ Core Features

*   **Multi-Platform Support**: Works seamlessly on **Windows**, **macOS** and **Linux**.
*   **Configurable Launch List**: Easily define a list of URLs and Application Shortcuts to open via a simple `.env` file.
*   **Smart Timer**: Prevents spamming windows by checking the time elapsed since the last run. Configurable via `repeat_time`.
*   **Silent Execution**: The script uses `.pyw` extension to run in the background without a distracting console window.
*   **Activity Logging**: Automatically logs every successful run with timestamps and counters in `log.csv`.

## 🛠️ Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/sadmanhsakib/LaunchMate.git
    cd LaunchMate
    ```

2.  **Install Dependencies**
    This project requires Python installed. Install the required package:
    ```bash
    pip install python-dotenv
    ```

3.  **Configuration**
    Create a `.env` file in the root directory (or edit the existing one) with the following variables:

    ```env
    # Minimum time (in hours) to wait before running again
    repeat_time=4

    # Comma-separated list of URLs to open
    URLS=https://google.com,https://github.com

    # Comma-separated list of Application Shortcuts/Paths
    # Windows Example:
    SHORTCUTS=C:\Users\Public\Desktop\Notepad++.lnk,C:\Path\To\App.lnk
    # macOS Example:
    # SHORTCUTS=/Applications/Spotify.app,/Applications/Slack.app
    ```

## 🚀 Usage

### Manual Run
Simply double-click the `main.pyw` file.
*   If the `repeat_time` has passed since the last run, your apps and sites will open.
*   If not, the script will exit silently.

### Automatic Run (Startup)
To have this run automatically when you turn on your computer:

#### **Windows (Task Scheduler)**
For a more reliable startup experience than the Startup folder:
1.  Press `Win + R`, type `taskschd.msc`, and press Enter.
2.  In the right pane, click **Create Basic Task...**.
3.  **Name**: "LaunchMate" (or your preferred name). Click Next.
4.  **Trigger**: Select **When I log on**. Click Next.
5.  **Action**: Select **Start a program**. Click Next.
6.  **Program/script**: Browse and select your `pythonw.exe` (usually in your Python installation folder) or simply select the `main.pyw` file if `.pyw` is associated with Python correctly.
    *   *Tip*: To be safe, point to `pythonw.exe` and put the full path to `main.pyw` in the **Add arguments** box.
7.  Click **Finish**.

#### **macOS**
Add the script to your **Login Items** in System Settings or use `automator` to create an application that runs the script.

#### **Linux**
You can use the `autostart` directory.
1.  Create a `.desktop` file in `~/.config/autostart/` (e.g., `launchmate.desktop`).
2.  Add the following content (adjust paths as needed):
    ```ini
    [Desktop Entry]
    Type=Application
    Exec=/usr/bin/python3 /path/to/your/LaunchMate/main.pyw
    Hidden=false
    NoDisplay=false
    X-GNOME-Autostart-enabled=true
    Name=LaunchMate
    Comment=Start daily routine
    ```

## 📊 Logging

The script generates a `log.csv` file automatically:
```csv
Lifetime-Counter,Today-Counter,Date,Time
1,1,2023-10-27,09:00:00
2,2,2023-10-27,14:00:00
```
*   **Lifetime-Counter**: Total times the script has run.
*   **Today-Counter**: Times the script has run today.

## 🤝 Contributing

This project is solely developed and maintained by **[Sadman Sakib](https://github.com/sadmanhsakib)**.

If you have suggestions or find bugs, please feel free to open an issue or submit a Pull Request.