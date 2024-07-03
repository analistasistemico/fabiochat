from googletrans import Translator

def translate_text(text, source_lang, target_lang): """ Traduz um texto de um idioma de origem para um idioma de destino.

Args:
    text (str): O texto a ser traduzido.
    source_lang (str): O código do idioma de origem (ex: 'pt', 'en', 'es').
    target_lang (str): O código do idioma de destino (ex: 'pt', 'en', 'es').

Returns:
    str: O texto traduzido.
"""
translator = Translator()
translation = translator.translate(text, src=source_lang, dest=target_lang)
return translation.text
