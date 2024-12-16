# Instagram Bot

This bot is designed to perform automated tasks on Instagram, such as tracking unfollowers, using Python and Selenium. By following the steps outlined in this document, you can set up, configure, and run the bot.

---

## Features

- Detects unfollowers on Instagram.
- Automates login and navigation using Selenium.
- Dynamically scrolls through followers and unfollowers lists.
- Adjustable `time.sleep()` delays to accommodate different internet and system speeds.

---

## Prerequisites

Before you begin, ensure you have the following installed on your system:

1. **Python**: Version 3.6 or later is recommended.
2. **Google Chrome**: Ensure you have a compatible version with ChromeDriver.
3. **ChromeDriver**: Required to interact with the browser via Selenium.
4. **Selenium**: Install it using `pip install selenium`.

Refer to the [official Selenium documentation](https://selenium-python.readthedocs.io/installation.html) for further details on installation and compatibility.

---

## Installation

1. **Install Python Dependencies**
   ```bash
   pip install selenium
   ```

2. **Download ChromeDriver**
   - Visit the [ChromeDriver downloads page](https://chromedriver.chromium.org/downloads).
   - Download the version that matches your Google Chrome version.
   - Add ChromeDriver to your system PATH or place it in the project directory.

3. **Clone or Create Project Files**
   - Save the `instagram.py` script in your working directory.
   - Create a file named `instagramUserInfo.py` with the following structure:
     ```python
     username = "your_instagram_username"
     password = "your_instagram_password"
     ```

---

## Configuration

### Adjusting `time.sleep()` Delays

The bot uses `time.sleep()` to pause between actions. If the bot encounters errors or timeouts, these delays might need adjustment based on your:
- **Internet Speed**: Increase the delay for slower connections.
- **System Performance**: Longer delays might help on slower machines.

To adjust delays, modify the `time.sleep()` values in `instagram.py`.

---

## Usage

1. **Set Up User Info**
   - Add your Instagram login credentials to the `instagramUserInfo.py` file.

2. **Run the Bot**
   - Open the terminal or your preferred IDE (e.g., Visual Studio Code).
   - Navigate to the directory containing `instagram.py`.
   - Run the bot:
     ```bash
     python instagram.py
     ```

3. **Analyze Results**
   - The bot will output the detected unfollowers directly in the terminal.

---

## Troubleshooting

1. **Common Issues**
   - **Errors related to timeouts or missing elements**: These are often caused by insufficient or excessive `time.sleep()` delays. Adjust these values as needed.
   - **ChromeDriver version mismatch**: Ensure that the version of ChromeDriver matches your installed Google Chrome version.

2. **Debugging Tips**
   - Check the structure of Instagram's web elements. Updates to Instagram's layout may require changes to the bot's XPath or CSS selectors.
   - Use the browser's developer tools (F12) to inspect element classes and paths.

---

## Additional Notes

- **Security Reminder**: Avoid sharing your `instagramUserInfo.py` file to prevent exposing your login credentials.
- **Account Safety**: Overusing the bot may lead to temporary action blocks or account bans by Instagram. Use the bot responsibly.
- **Future Updates**: Monitor Instagram's UI changes to ensure compatibility.

---

## Resources

- Selenium Python Documentation: [https://selenium-python.readthedocs.io/](https://selenium-python.readthedocs.io/)
- ChromeDriver Downloads: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
