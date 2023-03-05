import openai
import pyttsx3
import speech_recognition as sr
import time

# OpenAI API Key
openai.api_key = "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"

#Initialise the text-to-speech engine
engine = pyttsx3.init()

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        print('Skipping unknown error')

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperatore=0.5,
    )
    return response["choices"][0]["text"]

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        # Wait for user to say genius
        print("Say 'Genius' to start recoding your question")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "genius":
                    # Record audio
                    filename = "input.wav"
                    print("say your question...")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phase_time_limit=None, timeout=None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())

                    # Transcribe audio to text
                    text = transcribe_audio_to_text(filename)
                    if text:
                        print("You said: ", text)

                    # generate response using gpt-3
                    response = generate_response(text)
                    print("GPT-3 response: ", response)

                    # Read response out loud
                    speak_text(response)
            except Exception as e:
                print("An error occured: {}".format(e))

if __name__ == "__main__":
    main()
sdsssss