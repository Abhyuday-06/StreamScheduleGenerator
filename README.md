# Stream Schedule Generator

This is a simple web application built with Flask that helps you generate formatted Discord messages for your stream schedules.

## Features

- **Generate Discord Timestamps:** Easily convert your local time to a Discord timestamp that will display correctly for users in different timezones.
- **Multi-platform Support:** Generate messages for Twitch, Kick, and multi-platform streams (Twitch + YouTube).
- **Dynamic Form:** Add or remove multiple stream entries in a single form.
- **Dark Mode:** Toggle between light and dark mode for a better user experience.
- **Feature Requests:** Submit feature requests or bug reports directly through the application.

## Setup and Usage

### Prerequisites

- Python 3.x
- Flask
- pytz

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/stream-schedule-generator.git
   cd stream-schedule-generator
   ```

2. **Install the dependencies:**
   ```bash
   pip install Flask pytz
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```

4. **Open your web browser and navigate to:**
   ```
   http://127.0.0.1:5000
   ```

### How to Use

1. **Fill in the Stream Details:**
   - Select the timezone for your stream.
   - Choose the date and time of your stream using the datetime picker.
   - Enter the stream information (e.g., "Playing Valorant with viewers").
   - Select the platform(s) you will be streaming on.

2. **Add More Streams (Optional):**
   - Click the "Add Another Stream" button to add another stream to your schedule.

3. **Generate the Messages:**
   - Click the "Generate" button to create the formatted Discord messages.

4. **Copy to Clipboard:**
   - Click the "Copy to Clipboard" button to copy the generated messages.

5. **Paste in Discord:**
   - Paste the copied messages into your Discord channel. The timestamps will be automatically formatted by Discord.

## Feature Requests and Bug Reporting

If you have a feature request or want to report a bug, please use the "Feature Request/Bug Reporting" page in the application.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or improvements, feel free to open an issue or create a pull request.
