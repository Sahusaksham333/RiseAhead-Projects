"""PDF Text Extractor & Study Audiobook Script"""
from pathlib import Path

def extract_pdf_text(pdf_path: str) -> str:
    from pypdf import PdfReader
    reader = PdfReader(pdf_path)
    return "\n\n".join((page.extract_text() or "").strip() for page in reader.pages)

def speak_text(text: str, rate: int = 165):
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("rate", rate)
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    print("Install pypdf & pyttsx3, then call speak_text(extract_pdf_text('notes.pdf')).")
