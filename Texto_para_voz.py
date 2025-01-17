# Certifique-se de instalar as dependências antes de executar o código:
# No terminal do VSCode, execute:
# pip install gTTS

from gtts import gTTS
import os
import tkinter as tk
from tkinter import simpledialog

# Função para obter entrada de texto do usuário
def get_user_text():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    user_text = simpledialog.askstring("Entrada de Texto", "Digite o texto que deseja converter para áudio:")
    return user_text

# Função para converter texto em fala e abrir o reprodutor de mídia
def text_to_speech():
    text = get_user_text()
    if text:
        # Configuração do idioma
        language = "pt-br"

        try:
            # Converte texto em áudio
            gtts_object = gTTS(text=text, lang=language, slow=False)

            # Caminho do arquivo de áudio gerado
            audio_file = "output_audio.mp3"

            # Salva o arquivo de áudio
            gtts_object.save(audio_file)

            # Abre o reprodutor de mídia padrão do sistema
            print("Abrindo o reprodutor de mídia para reproduzir o áudio...")
            os.startfile(audio_file)  # Para Windows
            # No Linux ou macOS, use o comando abaixo:
            # os.system(f"xdg-open {audio_file}")  # Linux
            # os.system(f"open {audio_file}")  # macOS

        except Exception as e:
            print(f"Erro ao gerar ou abrir o áudio: {e}")
    else:
        print("Nenhum texto foi inserido.")

# Executa o programa
if __name__ == "__main__":
    text_to_speech()
