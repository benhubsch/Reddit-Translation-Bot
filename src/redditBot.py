import praw
from praw.models import Comment
from praw.models import Submission
from googletrans import Translator
import secret

engd = {"afrikaans": "af", "albanian": "sq", "arabic": "ar", "azerbaijani": "az",
"basque": "eu", "bengali": "bn", "belarusian": "be", "bulgarian":"bg", "catalan": "ca",
"chinese": "zh-CN", "chinese simplified": "zh-CN", "chinese traditional": "zh-TW",
"croatian": "hr", "czech": "cs", "danish": "da", "dutch": "nl", "english": "en",
"esperanto": "eo", "estonian": "et", "filipino": "tl", "finnish": "fi", "french": "fr",
"galician": "gl", "georgian": "ka", "german": "de", "greek": "el", "gujarati": "gu",
"haitian creole": "ht", "hebrew": "iw", "hindi": "hi", "hungarian": "hu", "icelandic": "is",
"indonesian": "id", "irish": "ga", "italian": "it", "japanese": "ja", "kannada": "kn",
"korean": "ko", "latin": "la", "latvian": "lv", "lithuanian": "lt", "macedonian": "mk",
"malay": "ms", "maltese": "mt", "norwegian": "no", "persian": "fa", "polish": "pl",
"portuguese": "pt", "romanian": "ro", "russian": "ru", "serbian": "sr", "slovak": "sk",
"slovenian": "sl", "spanish": "es", "swahili": "sw", "swedish": "sv", "tamil": "ta",
"telugu": "te", "thai": "th", "turkish": "tr", "ukrainian": "uk", "urdu": "ur",
"vietnamese": "vi", "welsh": "cy", "yiddish": "yi"}

def translate(text, target):
    translator = Translator()
    translation = translator.translate(text, dest=target)
    return translation.text

def main():
    unread = []
    for item in reddit.inbox.unread(limit=None):
        # ignores messages in the inbox
        if isinstance(item, Comment):
            lang = item.body.split()[1]
            parent = reddit.comment(item.id).parent()

            # checks for parent being submission or comment, and handles accordingly
            if isinstance(parent, Comment):
                try:
                    lang_code = engd[lang.lower()]
                    translated = translate(parent.body.strip(), lang_code)
                except Exception as e:
                    translated = "No translation was found for this language :/. Sorry to have failed you, human.\
                                  I can translate comments and submissions when requested of the form '/u/BotTranslator <language>'. Try again in another language!"
                item.reply(translated)
            elif isinstance(parent, Submission):
                try:
                    lang_code = engd[lang.lower()]
                    post_title = translate("Title: " + parent.title.strip(), lang_code)
                    post_description = translate("Content: " + parent.selftext.strip(), lang_code)
                    translated = post_title + "\n \n" + post_description
                except Exception as e:
                    translated = "No translation was found for this language :/. Sorry to have failed you, human.\
                                  I can translate comments and submissions when requested of the form '/u/BotTranslator <language>'. Try again in another language!"
                item.reply(translated)
            unread.append(item)
    reddit.inbox.mark_read(unread)



if __name__ == '__main__':
    reddit = praw.Reddit(client_id = secret.client_id, \
                         client_secret = secret.client_secret, \
                         user_agent = secret.user_agent, \
                         username = secret.reddit_user, \
                         password = secret.reddit_password)
    main()
