# Text Classification on Reddit Comments with TensorFlow Deep Learning
Predicting the political compass quadrant of Reddit user comments using a deep learning classification model trained on comments from [r/PoliticalCompassMemes](https://www.reddit.com/r/PoliticalCompassMemes/). 

The model is built using TensorFlow. See the .ipynb file for the data pre-processing and the model building process.

Nearly all users in the subreddit select a [user flair](https://mods.reddithelp.com/hc/en-us/articles/360010541651-User-Flair). The flairs are pre-defined to represent each sector in the political compass. It is assumed in this project that the flair represents the user's political orientation. Each comment from this community is retrieved along with the user's flair. These flairs make the perfect target variable for the model.


[Check out the app!](https://political-compass-reddit-test.herokuapp.com/)

This web app takes in a Reddit username as an input and predicts the political compass sector of each of the user's comments using the saved TensorFlow model. It will return the comment count of each sector as well as each comment with its sector prediction. The web app is built with Streamlit and deployed using Heroku.
