from pytubefix import YouTube
from pytubefix.cli import on_progress
import os

def baixar_audio_youtube(url, output_path="."):
    """Baixa o áudio de um vídeo do YouTube em formato MP3."""
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"Baixando o áudio de: {yt.title}")

        audio_stream = yt.streams.filter(only_audio=True).first()

        if audio_stream:
            print("Encontrando a melhor qualidade de áudio...")
            audio_stream.download(output_path=output_path, filename=f"{yt.title}.mp3")
            print(f"Download do áudio de '{yt.title}' concluído com sucesso!")
        else:
            print(f"Nenhuma stream de áudio disponível para este vídeo: {url}")

    except Exception as e:
        print(f"Ocorreu um erro ao processar {url}: {e}")

if __name__ == "__main__":
    lista_de_links = []
    print("Digite os links dos vídeos do YouTube para baixar o áudio (um por linha).")
    print("Deixe uma linha em branco para finalizar a entrada de links.")

    while True:
        link = input("> ").strip()
        if not link:
            break
        lista_de_links.append(link)

    output_directory = "audio_baixado"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for url in lista_de_links:
        baixar_audio_youtube(url, output_directory)

    print("Processo de download de áudio em lote concluído.")