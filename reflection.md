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

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
