Remote system media controls
Controls any active media player on your system remotely

Features
• System-wide media controls
• Play/Pause playback
• Next/Previous track
• Stop playback
• Volume controls
• Universal compatibility
• Clean interface, modern and responsive design
• No need to configure specific media players
• Works regardless of which app is currently playing music
• The system automatically routes media key commands to the active media player
• Cross-platform compatible (Windows, macOS, Linux)
• Provides visual feedback through Django messages

How It Works
The app uses the pynput library to send standard system media keys:
• Media Play/Pause Key - Toggles playback in the active media player
• Media Stop Key - Stops playback
• Media Next/Previous Keys - Skip tracks
• Volume Keys - Control system volume

Compatibility
The app works with any media player that responds to system media keys, including:
• Spotify (desktop app and web player)
• iTunes/Apple Music
• Windows Media Player
• VLC Media Player
• YouTube (in web browsers)
• Pandora, SoundCloud, etc.
• Most other media applications


Setup Instructions:

Download the project and add the Django secret key in playerconfig/settings.py file in SECRET_KEY = 'add-your-secret-key-here' inside the quotes
You can generate one at https://djecrety.ir

1. Create and activate a virtual environment:
```bash
python -m venv venv
```
On Linux:
```bash
source venv/bin/activate
```
On Windows:
```bash
venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Start the server:
```bash
python manage.py runserver yourIPaddress:8000
```

5. Access the app at:
http://127.0.0.1:8000 on your local device
or
http://yourIPaddress:8000 remotely on another device


Project Structure:

media_control_app/
├── manage.py
├── requirements.txt
├── media_player_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── player/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│       └── __init__.py
├── templates/
    └── player/
        └── index.html