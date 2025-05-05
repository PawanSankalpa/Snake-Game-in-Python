🐍 Snake Game (Built with Python Turtle)
Hey! I'm Pawan 👋
This is one of the first real Python projects I built — a fully working Snake Game using Python’s built-in turtle module.

It’s simple, fun, and was a great way for me to practice object-oriented programming (OOP) and improve my Python skills!

🛠 How I Made This (My Process)
So let me walk you through how I built this project, step by step — just like I did it:

1. I planned it out first (in my head 😅)
I knew I needed:

A snake that moves

Food that appears in random places

A way to detect collisions

A scoreboard that keeps track of score and high score

2. I created the snake 🐍
I made a Snake class that stores the snake segments as a list of turtles.
Each segment is a square, and they follow the head as it moves.
Then I added movement controls (Up, Down, Left, Right) using keyboard inputs.

3. I added the food 🍽️
Created a Food class by inheriting from Turtle.
The food appears randomly on the screen using random.randint().
When the snake eats it (gets close), it disappears and reappears elsewhere — and the snake gets longer!

4. I created the scoreboard 🎯
I made a Scoreboard class that displays the current score on top.
I also created a data.txt file to save the highest score, so it doesn’t reset when you restart the game.

5. I wrote the game loop in main.py 🔁
This is the brain of the whole game.
It constantly updates the screen, moves the snake, checks for food collisions, wall collisions, and tail collisions.
If you crash, the game resets (but your high score stays safe!).

6. I styled it a bit
Set the background color to black

Gave the snake a white color

Made the food small and blue

Set screen size to 600x600

🖥 How to Run It (Step-by-Step)
🔧 Requirements
Python 3.x

That’s it! No need to install external libraries. turtle and random come built-in.

🚀 Run Instructions
Download the files or clone the repo:

bash
Copy
Edit
git clone https://github.com/PawanSankalpa/turtle_projects.git
cd turtle_projects
Create a file named data.txt in the same folder (if not already there), and just put a 0 in it:

txt
Copy
Edit
0
This file stores the high score.

Run the game

bash
Copy
Edit
python main.py
🎮 How to Play
Use the arrow keys to move the snake:

Up → Go up

Down → Go down

Left → Turn left

Right → Turn right

Eat the blue food to grow longer.

Don’t crash into the walls or your own tail — or your score resets!

Beat your own high score stored in data.txt.

📂 What's Inside
File	What it does
main.py	Runs the game loop and connects all components
snake.py	Handles snake segments, movement, and growing
food.py	Manages food behavior and random positioning
scoreboard.py	Displays and tracks score + high score
data.txt	Stores your highest score

💡 Extra Ideas I Might Try Later
Add sound effects

Add levels with increasing speed

Add a start/restart screen

Style it more with custom shapes or colors

🙌 Final Thoughts
This was a really fun and useful project for me to learn Python.
I finally understood how classes, inheritance, OOP, and modular code all come together in a real game.
If you're new to Python, try this out. It teaches you a lot!

Built by me — Pawan 👾
If you have questions or wanna show me your version, hit me up!