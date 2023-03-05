

import openai

def askGPT(text):
    openai.api_key = "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"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        temperature=0.6,
        max_tokens=150,
    )
    return print(response["choices"][0]["text"])

def main():
    while True: 
        print("GPT ask me a question\n")
        myQn = input()
        askGPT(myQn)
        print('\n')
main()
 