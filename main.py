import pytz
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

# Dictionary to store GMT offsets for timezones
timezone_offsets = {
    "AEST": 10,    # GMT +10
    "AEDT": 11,    # GMT +11
    "CEST": 2,     # GMT +2
    "CET": 1,      # GMT +1
    "SGT": 8,      # GMT +8
}

def to_discord_timestamp(datetime_str, timezone):
    # Parse the input date and time (in "Y-m-d H:i" format from Flatpickr)
    stream_time = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
    
    # Get the offset for the selected timezone
    offset_hours = timezone_offsets[timezone]
    
    # Create a timezone-aware datetime object based on the selected timezone
    timezone_obj = pytz.FixedOffset(offset_hours * 60)
    stream_time = timezone_obj.localize(stream_time)
    
    # Convert the timezone-aware datetime to a Discord timestamp
    discord_timestamp = int(stream_time.timestamp())
    
    return discord_timestamp, stream_time.date()  # Returning both timestamp and date

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        timezones = request.form.getlist('timezones')  # Get all timezone inputs
        datetime_strs = request.form.getlist('datetime')  # Get all date-time inputs
        stream_infos = request.form.getlist('stream_info')  # Get all stream info inputs
        platforms = request.form.getlist('platform')  # Get all platform inputs

        output_messages = []
        previous_date = None

        for timezone, datetime_str, stream_info, platform in zip(timezones, datetime_strs, stream_infos, platforms):
            timestamp, stream_date = to_discord_timestamp(datetime_str, timezone)

            if platform == "Kick":
                icon = "🟩"
                message = f"{icon} **<t:{timestamp}:F>** {stream_info} on Kick {icon}"
            elif platform == "Twitch":
                icon = "🟪"
                message = f"{icon} **<t:{timestamp}:F>** {stream_info} {icon}"
            elif platform == "Twitch + YouTube":
                icon = "🟪 🟥"
                message = f"{icon} **<t:{timestamp}:F>** {stream_info} 🟥 🟪"

            # If this stream is on a different date from the previous stream, add a line gap
            if previous_date and previous_date != stream_date:
                output_messages.append("")  # Add a line break if dates are different

            output_messages.append(message)
            previous_date = stream_date  # Update the previous date

        platforms_info = "\n\n 🟪 = Twitch \n 🟩 = Kick \n 🟪 🟥 = Twitch + YouTube"
        output_messages.append(platforms_info)

        return render_template('index.html', output_messages=output_messages)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
