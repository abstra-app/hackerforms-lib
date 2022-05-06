from hackerforms import *

display("Hey, there. Right now, you're navigating through a web app built entirely on Python.", button_text = "Yeah, so?")

display("So, now you can now deploy those scripts that live in your terminal as beautiful, interactive webapps with literally no clicks.", button_text = "Oh, nice.  But what can it do?")

you = read("Hang on a sec, I'll get to that. But first, how shall I refer to *you*?")

feeling = read_multiple_choice(f"Sup, {you}. How's your day going?",["pretty good","ugh"])

if feeling == "ugh":
  display(f"Oh. I'm also kinda {feeling} today. We'll get through it together.", 
          button_text = "Uh. Ok.")
else:
  display("Nice! Mine's only gotten better since you showed up.",
         button_text = "Awkward")

display(f"Now that we're besties, let's do some math. I know right, nothing like math for a {feeling} day.", button_text = "Talk nerdy to me")

x = read("First up, set a value for x")

y = read("Cool, now set a value for y")

operation = read_multiple_choice(f"Interesting choices there, {you}. Now choose what you want me to do with x and y.", ["add", "subtract", "multiply","divide"])

if operation == "add":
  display(f"Let's go! {x} + {y} = {int(x)+int(y)}",button_text = "Right on")

if operation == "subtract":
  display(f"Alrighty then. {x} - {y} = {int(x)-int(y)}", button_text = "So smart")

if operation == "multiply":
  display(f"Then, you mean {x} * {y} = {int(x)*int(y)}", button_text = "Pretty much")

if operation == "divide":
  display(f"Tricky. Let me give it my best shot: {x} / {y} = {int(x)/int(y)}", button_text = "I guess?")

ans1 = read_multiple_choice(
  "Now one for you. 2x + 6y = 22, x + y = 5. What is x?",
  [1,2,3,"None"]
)
rightans1 = 2

if ans1 == rightans1:
  display(
    f"Great job, {you}!", 
    button_text = "Booyah"),
else:
  display(
    f"Hmm... that's not quite right, {you}. It's actually 2. Let's try another question.", 
    button_text = "Ok"
  )

ans2int = False


ans2 = read_number("Find the sum of the numbers between 1 and 10 (1 and 10 included).")
    
rightans2 = 55

if int(ans2) == rightans2:
  display(
    "I see you, smarty-pants!", 
    button_text = "Crushed it"),
else:
  display(
    "Don't think so. The right answer is 55.", 
    button_text = "Oh man..."
  )

display(f"Isn't this fun, {you}? I can feel our day getting more awesome by the minute. I'd wager your day might get even better if you tried Hackerforms for free right now.", button_text = "Wanna bet?")

display("You're on. Give me a spin. Go ahead, I dare you.", button_text = "Bring. It. On.")

display_link("https://www.hackerforms.com/app","Try Hackerforms free now", button_text = "On my way now")