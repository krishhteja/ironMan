from googletrans import Translator
import json

def translation(word, destination):
    languages = {"afrikaans": "af", "irish": "ga", "albanian": "sq", "italian": "it", "arabic": "ar", "japanese": "ja",
                 "azerbaijani": "az", "kannada": "kn", "basque": "eu", "korean": "ko", "bengali": "bn", "latin": "la",
                 "belarusian": "be", "latvian": "lv", "bulgarian": "bg", "lithuanian": "lt", "catalan": "ca",
                 "macedonian": "mk", "chinese": "zh-CN", "malay": "ms", "chinese": "zh-TW", "maltese": "mt",
                 "croatian": "hr", "norwegian": "no", "czech": "cs", "persian": "fa", "danish": "da", "polish": "pl",
                 "dutch": "nl", "portuguese": "pt", "english": "en", "romanian": "ro", "esperanto": "eo",
                 "russian": "ru", "estonian": "et", "serbian": "sr", "filipino": "tl", "slovak": "sk", "finnish": "fi",
                 "slovenian": "sl", "french": "fr", "spanish": "es", "galician": "gl", "swahili": "sw",
                 "georgian": "ka", "swedish": "sv", "german": "de", "tamil": "ta", "greek": "el", "telugu": "te",
                 "gujarati": "gu", "thai": "th", "haitian": "ht", "turkish": "tr", "hebrew": "iw", "ukrainian": "uk",
                 "hindi": "hi", "urdu": "ur", "hungarian": "hu", "vietnamese": "vi", "icelandic": "is", "welsh": "cy",
                 "indonesian": "id", "yiddish": "yi"}

    if destination.lower() in languages:
        destinationCode = languages[destination.lower()]
    else:
        out = "Unable to find the said language {}".format(destination)
        return out

    translator = Translator()
    translation = (translator.translate(word, dest=destinationCode))
    extraData = translation.extra_data['translation']
    pronuncation = translation.pronunciation
    temporary = extraData[-1]
    for element in temporary:
        if element != None:
            pronuncation = element
            break
    out = "The word you said is {}. It is identified that the language is {}. It's translated as {} in {}".format(word, translation.src, pronuncation, destination)
    print(out)
    return out

#translation("Neevu ekkada", "english")