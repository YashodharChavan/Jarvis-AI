import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
from bs4 import BeautifulSoup
from openai import OpenAI

client = OpenAI(api_key = '<your openai api key>')


# Initialize recognizer
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def record_audio_and_return():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source)   
        text = recognizer.recognize_google(audio)  
        return text



def get_first_search_result(query): 
    search_url = f"https://www.google.com/search?q={query}"
     
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }
    response = requests.get(search_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find the <a> tag with class 'UWckNb"'
        a_tag = soup.find("a", attrs={"jsname": "UWckNb"})
        if a_tag and a_tag.has_attr('href'): 
            return a_tag["href"]
        else:
            print("No result found with the specified class.")
    else:
        print(f"Failed to fetch search results. HTTP Status Code: {response.status_code}")
    return None


def handle_command(command):
    print("the command is: ", command)
    action = ' '.join(command.split()[1:])
    if (get_first_search_result(action) is None):
        speak("some error occured")
    else:
        webbrowser.open(get_first_search_result(action))
            
def generate_openai_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a virtual assistant names JARVIS, you help if some general tasks. "},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return completion.choices[0].message.content

def process_command():
    text = record_audio_and_return()

    if(text.lower()=='jarvis'):
        speak("yes sir")
        text = record_audio_and_return()
        print(f"the command: {text}")
        handle_command(text)
    
    elif(text.lower()=='hey jarvis'):
        speak("yes sir")
        text = record_audio_and_return()   
        print(f"the command: {text}")
        response = generate_openai_response(text)
        speak(response)
    
    if text.lower() == 'exit':
        speak("goodbye")
        exit()


if __name__ == "__main__":
    speak("initializing jarvis...")
    while True:
        try:
            process_command()
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")