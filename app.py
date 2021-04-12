import streamlit as st
import emoji
from textblob import TextBlob
import pyjokes


sad = emoji.emojize(":disappointed:")
laugh = emoji.emojize(" :laughing:")
smiley = emoji.emojize(" :smiley:")
cry = emoji.emojize(":cry:")
jokes = pyjokes.get_joke(category='all')
joy = emoji.emojize(":joy:")


def main():
    st.title("Mood detector")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Sentiment detector app</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    feeling = st.text_input("How was your day?", "Type Here")
    analysisPol = TextBlob(feeling).polarity
    analysisSub = TextBlob(feeling).subjectivity
    result = ""
    if analysisPol > 0 and analysisPol <= 0.8:
        result = f'Great to hear that {smiley}'
    elif analysisPol > 0.8:
        result = f'Great you look quit happy {laugh}'
    else:
        result = f' sad to hear that {sad} \n I hope this will make you feel happy.\n {jokes} {joy} {joy}'
    if st.button("Predict"):
        st.success('{}'.format(result))
    if st.button("About"):
        st.text("This is a simple emotion detector detector")
        st.text("Built with Streamlit")


if __name__ == '__main__':
    main()
