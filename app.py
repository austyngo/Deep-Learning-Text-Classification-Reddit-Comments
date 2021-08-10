import praw
import config
import streamlit as st
from os import listdir
from Tokenize import Comment
from make_predictions import Prediction

st.markdown("<h1 style='text-align: center;'>Reddit Comment Political Compass Test</h1>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1,1,1])

with col2:
    st.image(r'images/Centrist.jpg', width=250)

st.markdown('''
Find out where your Reddit comments fall in the political compass!\n
This app uses a deep learning model trained on comments from **r/politicalcompassmemes** 
to predict where each of your comments lie in the political compass based on the language and words used.''')

#config contains reddit authentication tokens
reddit = praw.Reddit(client_id= config.clientid,  
                    client_secret= config.secret,
                    user_agent = config.useragent,
                    username= config.username,
                    password= config.password)

user = st.text_input("Enter your reddit username", value='')

@st.cache
def get_comments(uname):
    
    redditor = reddit.redditor(uname)
    all_comments = [i.body for i in redditor.comments.new()]
    return all_comments

@st.cache
def predict_user_comments():
    comments_with_predict = {}
    for i in get_comments(user): 
        tokenized = Comment(i).tokenize()
        prediction_each_comment = Prediction(tokenized).predict()
        comments_with_predict.update({i:prediction_each_comment})
        
    return comments_with_predict

@st.cache
def flair_counts(dict_):  
    predicted_flairs = list(dict_.values())
    return dict((x,predicted_flairs.count(x)) for x in set(predicted_flairs)) 

from os import listdir
img_names = [f.strip('.jpg') for f in listdir(r'images')]

button = st.button('Predict!')

if button:
    try:
        st.write('Comment count by quadrant')
        for k, v in flair_counts(predict_user_comments()).items():
            for i in img_names:
                if k.lower() == i.lower():
                    col1, mid, col2 = st.columns([1,1,20])
                    with col1:
                        st.image(fr'images/{i}.jpg', width=30)
                    with col2:
                        st.write(f'{k}: {v}')
    except:
        st.write('Username does not exist')

button_2 = st.button('Show Comments')

if button_2:
    try:
        st.write('Comments:')
        for c, f in predict_user_comments().items():
            st.markdown(f'{c} - **{f}**') 
    except:
        st.write('Username does not exist')

st.markdown('See the code in my [GitHub Repository](https://github.com/austyngo/Political-Compass-Deep-Learning-Text-Classification).')