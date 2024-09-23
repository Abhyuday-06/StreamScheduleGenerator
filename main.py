import pytz
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

timezone_offsets = {
    "AEST": 10,    
    "AEDT": 11,    
    "CEST": 2,     
    "CET": 1,      
    "SGT": 8,      
}

feature_requests = []

def to_discord_timestamp(datetime_str, timezone):
    stream_time = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
    offset_hours = timezone_offsets[timezone]
    timezone_obj = pytz.FixedOffset(offset_hours * 60)
    stream_time = timezone_obj.localize(stream_time)
    discord_timestamp = int(stream_time.timestamp())
    return discord_timestamp, stream_time.date()  

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        timezones = request.form.getlist('timezones')
        datetime_strs = request.form.getlist('datetime')
        stream_infos = request.form.getlist('stream_info')
        platforms = request.form.getlist('platform')

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

            if previous_date and previous_date != stream_date:
                output_messages.append("")  # Add a line break if dates are different

            output_messages.append(message)
            previous_date = stream_date  

        platforms_info = "\n\n 🟪 = Twitch \n 🟩 = Kick \n 🟪 🟥 = Twitch + YouTube"
        output_messages.append(platforms_info)

        return render_template('index.html', output_messages=output_messages)

    return render_template('index.html')

@app.route('/feature_request', methods=['GET', 'POST'])
def feature_request():
    if request.method == 'POST':
        username = request.form.get('username', '').strip() or "Anonymous"
        feature_request_text = request.form['feature_request']
        feature_requests.append(f"{username}: {feature_request_text}")

    return render_template('feature_request.html', requests=feature_requests)


if __name__ == '__main__':
    app.run(debug=True)
