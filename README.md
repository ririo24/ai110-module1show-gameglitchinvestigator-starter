# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
         This is a guessing numbers game. Users are given a selection of difficulty levels to choose from which corresponds to the size of the range of values they will be guessing from. The user will recieve hints, notifying them if their guess was too high or too low. 
- [ ] Detail which bugs you found.
         I found several bugs in this program. For instance, the hint is opposite of what it's supposed to be. Another bug was an incorrect hard difficulty max range value. I also noticed that the message bar always says "Guess a number between 1 and 100" and doesn't adjust for difficulty setting range.
- [ ] Explain what fixes you applied.
         I had Claude adjust the hints so that they would not be giving the opposite message to the user. Claude also changed the max range value for the hard difficulty level to be 200, instead of 50. As for the message, instead of the statement being st.info statement always be "Guess a number between 1 and 100", it now adjusts to the current low and high values that are currently set for the difficulty level.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
