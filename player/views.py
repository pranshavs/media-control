from pynput.keyboard import Key, Controller
import time
from django.shortcuts import render, redirect
from django.contrib import messages

# Initialize the system keyboard controller
keyboard = Controller()

def index(request):
    """Main media controls interface."""
    context = {
        'title': 'Remote System Media Controls',
        'description': 'Control media playback of your system'
    }
    return render(request, 'player/index.html', context)

def play_pause(request):
    """Send play/pause media key."""
    try:
        # Send media play/pause key
        keyboard.press(Key.media_play_pause)
        keyboard.release(Key.media_play_pause)
        messages.success(request, 'Play/Pause')
    except Exception as e:
        # Catch any errors with the request and store it in the variable 'e'
        messages.error(request, f'Error playing/pausing playback: {e}')
    # After trying to send the key, redirect the user to the route named 'player:index'
    return redirect('player:index')

def stop(request):
    """Send stop media key."""
    try:
        # Send media stop key
        keyboard.press(Key.media_stop)
        keyboard.release(Key.media_stop)
        messages.success(request, 'Stopped playing')
    except Exception as e:
        # Catch any errors with the request and store it in the variable 'e'
        messages.error(request, f'Error stopping playback: {e}')
    # After trying to send the key, redirect the user to the route named 'player:index'
    return redirect('player:index')

def next_track(request):
    """Send next track media key."""
    try:
        # Send media next key
        keyboard.press(Key.media_next)
        keyboard.release(Key.media_next)
        messages.success(request, 'Next track played')
    except Exception as e:
        # Catch any errors with the request and store it in the variable 'e'
        messages.error(request, f'Error playing next track: {e}')
    # After trying to send the key, redirect the user to the route named 'player:index'
    return redirect('player:index')

def previous(request):
    """Send previous track media key."""
    try:
        # Send media previous key
        keyboard.press(Key.media_previous)
        keyboard.release(Key.media_previous)
        messages.success(request, 'Previous track played')
    except Exception as e:
        # Catch any errors with the request and store it in the variable 'e'
        messages.error(request, f'Error playing previous track: {e}')
    # After trying to send the key, redirect the user to the route named 'player:index'
    return redirect('player:index')

def volume_up(request):
    """Send volume up key."""
    try:
        # Send volume up key
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        messages.success(request, 'Volume turned up')
    except Exception as e:
        # Catch any errors with the request and store it in the variable 'e'
        messages.error(request, f'Error turning volume up: {e}')
    # After trying to send the key, redirect the user to the route named 'player:index'
    return redirect('player:index')

def volume_down(request):
    """Send volume down key."""
    try:
        # Send volume down key
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        messages.success(request, 'Volume turned down')
    except Exception as e:
        # Catch any errors with the request and store it in the variable 'e'
        messages.error(request, f'Error turning volume down: {e}')
    # After trying to send the key, redirect the user to the route named 'player:index'
    return redirect('player:index')

def mute(request):
    """Send mute key."""
    try:
        # Send volume mute key
        keyboard.press(Key.media_volume_mute)
        keyboard.release(Key.media_volume_mute)
        messages.success(request, 'Muted/Unmuted playback')
    except Exception as e:
        # Catch any errors with the request and store it in the variable 'e'
        messages.error(request, f'Error muting playback: {e}')
    # After trying to send the key, redirect the user to the route named 'player:index'
    return redirect('player:index')