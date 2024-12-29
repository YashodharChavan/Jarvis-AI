# JARVIS AI

JARVIS AI is a Python-based voice-activated personal assistant that performs web searches, answers general questions, and provides responses using audio output. By leveraging speech recognition, text-to-speech, and the ChatGPT API, JARVIS offers an interactive experience for users.

---

## Features
- **Voice Search**: Perform web searches using voice commands.
- **Question Answering**: Receive answers to general questions via voice interaction.
- **Text-to-Speech Output**: Responds with clear, loud audio.
- **Integration with ChatGPT API**: Provides intelligent and context-aware answers.

---

## Prerequisites
Ensure the following are installed:
- Python 3.7 or higher
- A stable internet connection

---

## Installation


1. Clone the repository:
   ```bash
   git clone https://github.com/YashodharChavan/Jarvis-AI.git
   cd jarvis-ai
   ```

2. Use the virtual enviroment (optional):
   ```bash
   .\env\Scripts\activate.ps1
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your ChatGPT API key:
   - Ensure you have access to OpenAI's API and save the API key in a `.env` file or in code as:
     ```
     CHATGPT_API_KEY=<your-api-key>
     ```

---

## Modules Used

The following Python modules are used in this project:

| Module               | Version    | Purpose                                    |
|----------------------|------------|--------------------------------------------|
| `beautifulsoup4`     | 4.12.3     | Parsing and scraping web pages            |
| `bs4`                | 0.0.2      | Simplified import for BeautifulSoup       |
| `certifi`            | 2024.12.14 | SSL certificate validation                 |
| `charset-normalizer` | 3.4.1      | Encoding detection and normalizer          |
| `comtypes`           | 1.4.8      | Windows COM client automation              |
| `idna`               | 3.10       | Internationalized Domain Names handling    |
| `PyAudio`            | 0.2.14     | Audio input/output via the microphone      |
| `pypiwin32`          | 223        | Python bindings for Windows API            |
| `pyttsx3`            | 2.98       | Text-to-speech conversion                  |
| `pywin32`            | 308        | Windows API functions and interfaces       |
| `requests`           | 2.32.3     | HTTP requests for API communication        |
| `soupsieve`          | 2.6        | Filtering HTML/XML for BeautifulSoup       |
| `SpeechRecognition`  | 3.12.0     | Recognizing speech from audio              |
| `typing_extensions`  | 4.12.2     | Enhancements for type hinting              |
| `urllib3`            | 2.3.0      | HTTP library for Python                    |

---

## Usage

1. Launch the application:
   ```bash
   python main.py
   ```

2. Use voice commands to ask questions or initiate searches.

---

## Future Improvements
- Integration with more APIs for extended functionality.
- Support for multiple languages.
- Enhanced error handling and logging.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contribution
We welcome contributions to enhance JARVIS AI. Feel free to submit a pull request or open an issue.

---

## Acknowledgments
- [OpenAI](https://openai.com) for the ChatGPT API.
- The developers and maintainers of the Python modules used.

---

**Happy Coding!**

