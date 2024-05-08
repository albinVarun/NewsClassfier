import joblib
import streamlit as st

model = joblib.load("news-classification-model.pkl")

news_labels={"0":"Techincal","1":"Business","2":"Sports","3":"Entertain","4":"Politics"}

st.title("News Classification")

user_input=st.text_area("Enter news here:")

if st.button("Predict"):

    predicted_label=model.predict([user_input])[0]
    #print("Prediced Label:"+str(prediced_label))
    predicted_news_label = news_labels[str(predicted_label)]

    st.info(f"Predicted Sentiment: {predicted_news_label}")