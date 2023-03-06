from flask import Flask, render_template, request
import openai

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_text', methods=['POST'])
def process_text():
    # Get the value from the input box
    input_text = request.form['inputBox']
    print(input_text)

    # Generate text using OpenAI API
    openai.api_key = "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"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input_text,
        temperature=0.5,
        max_tokens=250,
    )
    output_text = response["choices"][0]["text"]
    print(output_text)    
    return render_template('index.html', output_text=output_text)

if __name__ == '__main__':
    app.run(debug=True)

