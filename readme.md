# Flet Demo App



This is a simple demo application built with **Flet**. This is a simple and fun number guessing game built with Flet. The player tries to guess a secret number between 0 and 100. After each guess, the game provides hints whether the secret number is higher or lower. The game tracks the number of attempts and celebrates with a congratulatory message when the player guesses correctly. Features include:

Interactive input for guesses

Hints after each attempt (higher/lower)

Attempt counter

Option to start a new game

Fun emojis for a lively user experience 🎉



## Installation



1\. Make sure you have **Python** installed.

2\. Install the required package using **pip**. In your terminal or PyCharm terminal, run:



```bash

pip install "flet\[all]"

```



## How to Use



1\. Open the project in **PyCharm** (or any Python IDE).

2\. Run the Python file that contains your app (for example, `index.py`). This will open a window showing the button.

3\. Click the button to increase the counter. The text on the screen will update with the number of times the button has been clicked.


## Running with Docker🐳

You can also run the app using **Docker**:

Build the Docker image:


```bash

docker build -t game .

```

Run the Docker container:

```bash

docker run -p 8500:8500 game

```



Open your browser and go to http://localhost:8500 to see the app running.



## About Flet



**Flet** is a Python framework that allows you to build interactive web, desktop, and mobile applications \*\*without needing to write JavaScript, HTML, or CSS\*\*. It provides a set of UI components (widgets) that you can use directly in Python, making it easier and faster to create GUI applications.



With Flet, you can:



\* Build desktop and web apps using Python only.

\* Handle UI events and updates in a reactive way.

\* Focus on Python code without worrying about front-end technologies.



## Example Screenshot



![App Screenshot](screenshot.png)





