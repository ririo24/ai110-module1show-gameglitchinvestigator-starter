# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

      - When I first ran the game, I noticed that when I input a number lower than the secret number, I recieved a hint that said go lower. When I did the opposite, input a number higher than the secret number, the hint said to go higher. 
      - Another bug I noticed was in the difficulty selection. The range for the hard difficulty mode was smaller than in the normal difficulty mode. The range for normal was 1-100 meanwhile, the range for hard was 1-50. So either those ranges should be swapped or the hard range should be expanded. 
      - A third bug I noticed was that a new game doesn't reset the status or the score. 
      - The message bar always says "Guess a number between 1 and 100" and doesn't adjust for difficulty setting range.
      - Lets you input negative numbers and 0.
      - Truncates decimal to whole number.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
      Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
      Claude suggested that certain code be refactored from app.py into logic_utils.py. I verified that Claude's suggestion was working as intended several times by running the app and seeing the changes it made work live.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
      One example of an missleading suggestion given by Claude was what to do when a player switches difficulty mid-game. Claude said that an issue of the program was that the secret stays from the old difficulty range and that the input key resets but the secret, attempts, and score does not. During mid-game, if a player switches difficulty, it somewhat makes sense not to reset the whole game in the instance that the player wants to keep playing. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    - I decided a bug was really fixed if one, I thought Claude's solution was reasonable. Two, it passed the pytest test cases. And most importantly, three, it worked when I ran streamlit and tested it for myself.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
      I ran pytest and it showed me that the test cases Claude created produced no errors. The only errors that popped up were in the test cases already in the test_game_logic.py file.
- Did AI help you design or understand any tests? How?
      Yes, AI helped design the test cases in my code. I had asked Claude to generate relevant test cases that would test the bugs it had fixed in my code. I then reviewed them to make sure I agreed with it's solution and that it made sense for my code before accepting any changes.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
    Streamlit "reruns" basically reruns the entire Python script upon every interaction the user has with the code. For instance, any time the user clickes a buttom or enters and input, your whole python script gets rerun by Streamlit. Session state is essentially Streamlit's memory between each of the reruns. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
      One habit would be my testing habit. I make sure to test at every stage and with every edit Claude adds to the code. I plan to use it in future projects in order to make sure I don't allow for changes that don't work to be permenantly commited to the code. I also want to minimize errors in my code and doing increment testing helps prevent that.
- What is one thing you would do differently next time you work with AI on a coding task?
      One thing I would do differently is commit my changes more and ask AI to justify its coding changes more.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
      This project made me see how useful AI can be in helping programmers create meaningful code and debug faster. AI's quick production of test cases is a valueable tool to any coder interested in testing their work.
