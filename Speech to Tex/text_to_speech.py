import os
from flask import Flask, render_template, request

from google.cloud import texttospeech
from google.oauth2 import service_account

app = Flask(__name__)

# Configure credentials
credentials = service_account.Credentials.from_service_account_file(
    '/workspaces/codespaces-jupyter/secret.json')

# Configure text-to-speech client
client = texttospeech.TextToSpeechClient(credentials=credentials)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input
        user_input = request.form['input']

        # Configure text-to-speech synthesis input
        synthesis_input = texttospeech.SynthesisInput(text=user_input)

        # Configure voice settings
        voice = texttospeech.VoiceSelectionParams(
            language_code='en-US', ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )

        # Configure audio settings
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        # Synthesize speech and save to file
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        # Save audio file
        file_path = f'/workspaces/codespaces-jupyter/Speech to Tex/static/audio3'
        with open(file_path, 'wb') as out:
            out.write(response.audio_content)

        # Render template with user input and audio file path
        return render_template('/workspaces/codespaces-jupyter/Speech to Tex/templates/Some_spoken_words.html', user_input=user_input, audio_file=file_path)

    # Render template without user input or audio file path
    return render_template('/workspaces/codespaces-jupyter/Speech to Tex/templates/Some_spoken_words.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
