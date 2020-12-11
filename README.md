# Capital-One-MSF17
Capital One Summit Submission

<b>Basic Overview: </b>
This is a Flask project. I used Python for the data analysis, so it only felt fair to use a python backend for the project as well. I have used Django before, so I figured I would try something new and use Flask.

All html files are found in the templates folder and the images are found in the static folder.

The app.py handles two main requests for predicting the income and finding the best price. Both act similarly in that they read the latitude and longitude from the html files, read the appropriate pkl files with the models to predict the value, and open a new page that displays the information. For the income prediction, income.html is opened and for the best price, price.html is opened.

The home.html file contains all the forms that make the corresponding calls on the press of a submit button. I decided to open a new page for the results as it allows for more flexibility in the long run. If I wanted to include lots of graphs and more information about the given latitude and longitude like the prices of neighboring houses, past earnings over time, etc., putting the results on their own page more easily allow for this change.

The data\_analysis.ipynb file is a jupyter notebook file that I used to analyze the data. It assumes the data is in a folder called data. There, I have all the code I used to create the images, and make, test, and save different models. 

<b>Room for Improvements: </b> There are lots of places I could improve on in this project. First, the UI of the project is very basic. I was having a lot of trouble with library management as I had a very very messy hard drive, so that absorbed a lot of unnecessary time, which led me to use a simple view to focus on building the rest of the project.

The current implementations of the models could be improved. I would try to incorporate more features than just latitude and longitude. There is definitely a way to incorporate information about neighborhoods, history, and the current date with the datasets. It would be naive to assume that Airbnb listings aren't greatly influenced over time, and both my current models only use latitude and longitude and features. The current models have not undergone thorough hyper parameterizations either, greatly reducing the accuracies of the models. The models also may not necessarily be a good fit for the current data.
