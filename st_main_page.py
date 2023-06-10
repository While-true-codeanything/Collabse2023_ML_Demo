import requests
import streamlit as st

st.set_page_config(page_title="Discopus ML")


def request_tags(url: str, text: str) -> str:
    params = {"text": text}
    response = requests.get(url, params=params)
    data = response.json()
    return data['data']


st.title("Collabse 2023 ML Demonstration")
st.subheader("Напишите Вашу идею/описание проекта или опыта и мы выделим ключевые навыки")

tags_str = ""

TEXT_TONE = "http://89.232.160.227:8080/api/v0/ml/text-tone"
KEY_WORDS = "http://89.232.160.227:8080/api/v0/ml/key-words"
SKILLS_URL = "http://89.232.160.227:8080/api/v0/ml/categories"
NEWS_URL = "http://89.232.160.227:8080/api/v0/ml/news"

text = st.text_area("Tags", label_visibility="hidden")
detected_tags = st.empty()
if st.button("Отправить"):
    if text != "":
        with st.spinner("🤖 Наш ИИ подбирает Вам навыки и тематику..."):
            if len(text) > 1500:
                text = text[:1500]
            if len(text) < 150:
                st.error("Ваша идея/описание слишком короткое :( Опишите подробнее, иначе мы не сможем правильно определить тематику. Введите не меньше 150 символо")
            else:
                res = request_tags(SKILLS_URL, text)
                s = "**Теги:**\n"
                for item in res:
                    s += ("- **{}**\n".format(item))

                detected_tags.write(s)
                st.success("Готово!")
st.title("")
st.subheader("Напишите текст и мы выделим ключевые фразы из него")


news = st.text_area("Ключевые фразы", key="KEY_WORDS_area", label_visibility="hidden")
detected_key_words = st.empty()
if st.button("Отправить", key="KEY_WORDS"):
    if news != "":
        with st.spinner("🤖 Наш ИИ подбирает оптимальные ключевые слова/фразы..."):
            if len(news) > 1500:
                news = news[:1500]
            if len(news) < 150:
                st.error(
                    "Текст слишком короткий :( Напишите подробнее, иначе выделение ключевых элементов не будет иметь смысла. Введите не меньше 150 символо")
            else:
                res = request_tags(KEY_WORDS, news)
                s = "**Ключевые слова:**\n"
                for item in res:
                    s += ("- **{}**\n".format(item))

                detected_key_words.write(s)
                st.success("Готово!")

st.subheader("Напишите отзыв и мы определим его семантику Положительный/Отрицательный")

semantic = st.text_area("Семантика", key="Semantic_area", label_visibility="hidden")
detected_semantic = st.empty()
if st.button("Отправить", key="Semantic"):
    if semantic != "":
        with st.spinner("🤖 Наш ИИ подбирает Семантику..."):
            if len(semantic) > 1500:
                semantic = semantic[:1500]
            if len(semantic) < 150:
                st.error(
                    "Текст слишком короткий :( Напишите подробнее, иначе выделение семантики не будет работать. Учтите, что чем больше  обьем текста, тем точнее будет работать данная модель. Введите не меньше 150 символов")
            else:
                detected_semantic.subheader(request_tags(TEXT_TONE, semantic))
                st.success("Готово!")

st.subheader("Напишите текст новости и мы определим ее общую тематику")

news_theme = st.text_area("Тематика новости", key="News_theme_area", label_visibility="hidden")
detected_news_theme = st.empty()
if st.button("Отправить", key="News_theme"):
    if news_theme != "":
        with st.spinner("🤖 Наш ИИ подбирает тему новости..."):
            if len(news_theme) > 1500:
                news_theme = news_theme[:1500]
            if len(news_theme) < 150:
                st.error(
                    "Текст слишком короткий :( Напишите подробнее, иначе выделение тематики новости не будет работать.  Введите не меньше 150 символо")
            else:
                detected_news_theme.subheader(request_tags(NEWS_URL, news_theme)[0])
                st.success("Готово!")