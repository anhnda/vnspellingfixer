from preprocess_data import *
def get_news_sentence_reader():
    return open("%s/%s"%(DATA_DIR,NEWS_SENTENCES_DATA),encoding="utf-8")
def get_subtitle_reader():
    return open("%s/%s"%(DATA_DIR,SUBTITLES_EXPORT_DATA),encoding="utf-8")