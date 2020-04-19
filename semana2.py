import streamlit as st

def main():
    st.title('Hello World')
    st.header('Esse é o header')
    st.subheader('Esse é o subheader')
    st.text('Isto é um texto')
    st.image('triquetra.png')
    st.subheader('Audio')
    #st.audio('record.wav')
    st.subheader('Video')
    #st.video('nomevideo.mov')

if __name__ == '__main__':
    main()