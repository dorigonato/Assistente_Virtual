# pip install gTTS SpeechRecognition playsound pyjokes wikipedia pygame pyaudio

import speech_recognition as sr
from gtts import gTTS
import os
from datetime import datetime
import playsound
import pyjokes
import wikipedia
import webbrowser

# Endereço do executável do Word
word_path = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
music_path = r"Sade-The Sweetest Taboo.mp3"


# Listar os microfones disponíveis
print("Microfones disponíveis:")
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Microfone {index}: {name}")

# Configurar o índice do microfone
selected_microphone_index = 0  # Use o índice do microfone que deseja utilizar

# Função para capturar áudio do microfone
def get_audio():
    r = sr.Recognizer()
    try:
        with sr.Microphone(device_index=selected_microphone_index) as source:
            print("Ajustando ao ruído ambiente. Aguarde...")
            r.adjust_for_ambient_noise(source, duration=1)
            print("Estou ouvindo, fale algo...")
            audio = r.listen(source)
            print("Processando...")
            said = r.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {said}")
            return said.lower()
    except Exception as e:
        print(f"Erro: {e}")
        speak("Desculpe, não consegui entender o que você disse.")
        return ""

# Função para converter texto em fala
def speak(text):
    tts = gTTS(text=text, lang='pt-br')
    filename = "voice.mp3"
    try:
        os.remove(filename)  # Remover o arquivo anterior, se existir
    except OSError:
        pass
    tts.save(filename)
    playsound.playsound(filename)

# Loop principal para executar os comandos
while True:
    print("\nEstou ouvindo...")
    command = get_audio()

    if "youtube" in command:
        speak("Abrindo Youtube.")
        webbrowser.open("https://www.youtube.com/")
    
    elif "google" in command:
        speak("Google busca.")
        webbrowser.open("https://www.google.com.br/")
    
    elif "word" in command:
        try:
            speak("Abrindo o Microsoft Word.")
            os.startfile(word_path)
        except Exception as e:
            print(f"Erro ao tentar abrir o Word: {e}")
            speak("Desculpe, não consegui abrir o Word. Verifique o caminho do arquivo.")

    elif "buscar" in command:
        speak("Buscando no Wikipédia...")
        query = command.replace("buscar", "").strip()
        try:
            result = wikipedia.summary(query, sentences=2, lang="pt")
            speak("De acordo com a Wikipédia:")
            print(result)
            speak(result)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("Encontrei várias opções para sua busca. Seja mais específico.")
        except wikipedia.exceptions.PageError:
            speak("Não encontrei resultados para sua busca.")
        except Exception as e:
            print(f"Erro: {e}")
            speak("Desculpe, ocorreu um erro ao buscar no Wikipédia.")

    elif "piada" in command or "joke" in command:
        joke = pyjokes.get_joke(language="pt")
        speak("Aqui vai uma piada:")
        print(joke)
        speak(joke)

    elif "música" in command or "abrir música" in command:
        try:
            speak("Tocando sua música.")
            os.startfile(music_path)
        except Exception as e:
            print(f"Erro ao tentar abrir a música: {e}")
            speak("Desculpe, não consegui tocar a música. Verifique o caminho do arquivo.")


    elif "sair" in command or "fechar" in command:
        speak("Até a próxima!")
        break

    else:
        speak("Desculpe, não reconheci o comando. Tente novamente.")
