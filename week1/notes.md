Week 1

01/October/25
I started with Kasilab - which i am revising Py4e with kasilink in mind excercises. The thing is ive been learning and stopping when i get to big bugs or a negative mental attitude.

So with changing that since mental change that it is God that has given me this so what so ever i come accross i will persist and concourer because it is mine for the taking.

Today i worked on Input prompts with, list based prompts and a bit of conditional statements.

I must no start applying the test once done writting file - or habits as Dr chuck does, also not forgetting what Gama said Silid principles, fundamentals and design pattern.

02/October/25

Yes i keep on stumbling on and off so What ? am i learning yeah might it take time yeah - does it matter not when when im honest on it. Yes it might not reflect a perfect work guy but im applying to kasilink as i should be. Youll never know

Traceback might be on the line or the line above it.

Create your folders from Vscode then navigate with shell - and also check code with Shell.

Worked on py4e conditionals and man was i challenged , well 2morow we up to deepseek then kasilink.

03/October/25

Lol turns out that my long named folder of excercises 3.0 conditionals and exercises variables - when shelling into them i would need cd "name " not just cd name of folder ahahha.

So next time when naming folder its better to avoid spaces in folder names -> using _ or - instead: exercises_3.0_conditionals or exercises-3.0-conditionals

## Customer Auto Responder Work
- Fixed issue where input was hardcoded to "delivery" - learned that when you assign a variable twice, the second assignment overwrites the first!
- Removed redundant nested if statement in else block - if you're already in else, you don't need to check the opposite condition again
- Added .lower() method to make input case-insensitive (DELIVERY = delivery = Delivery)
- Created input validation using a list of valid options and checking if user input is in that list
- Learned about clean conditional logic: check for invalid input first, then handle valid cases


## Key Lessons Today:
1. Always test your conditionals with different inputs - don't hardcode test values
2. Keep conditional logic simple and avoid redundant checks
3. Input validation is crucial - always handle unexpected user input
4. Case sensitivity matters in user input - always consider using .lower() or .upper()

Key "Function" Concepts You're Practicing:

✅ Parameters - passing data into functions

✅ Return values - getting results back

✅ Logic inside functions - conditional thinking

✅ Reusability - same function, different inputs

What Was Wrong:
Infinite Loop: The function was calling itself indefinitely, which would crash your program
Wrong Function Name: You were calling a function that didn't exist (rate_seller instead of server)
Structure Issue: Test code was mixed inside the function instead of being separate

Fixed Issues:
✅ Removed Infinite Recursion: Deleted the served = server(120, 52, 30) call inside the function
✅ Fixed Function Names: Changed rate_seller() calls to server() to match the actual function name
✅ Moved Test Code: Put the function calls outside the function definition where they belong
✅ Cleaned Up Output: Removed the confusing intermediate print statements inside the function

Week 2 

October/06/225

Wow man function for a service request system - here was i calling my function before even finishing the tot and even printing - Interesting thou was it.

Worked on loops today and a service booking to kasilink


October/07/25
Continued on service_booking.py.

Had problems.
Root cause: the service-choice and budget-validation loops were written so they could exit prematurely (wrong use of break) and had a few flow/indentation issues that made the code behave incorrectly at runtime.

Effects before fix:
If a user entered an unavailable service the code used break, which would exit the validation loop and let execution continue with undefined variables (or end incorrectly).
Budget validation had unreachable break statements after raising a ValueError and could accept invalid inputs.
The script invoked book_service() unconditionally at module import, which is fine for a script but less safe for reuse/imports.

Fixes applied:
For the service choice loop:
Replaced the erroneous break on invalid choice with continue so the loop prompts again until a valid service is entered.
Explicit break only when a valid choice is provided.
Made the exception handler specific and continue on bad input.

For the budget loop:
Read input into budget_input then converted to float(budget_input) to avoid confusing prompts.
Removed unreachable break after raises and instead raise the ValueError so the except block handles re-prompting.
Only break the loop after a valid budget is parsed and passes checks.

Module protection: wrapped the final call in if __name__ == "__main__": and moved service, budget = book_service() there, so importing the module doesn't run interactive prompts.

ii. Location based service - well i ddnt know to give a string title first letter, .title(): converts the string to title case — capitalizes the first letter of each word and makes the rest lowercase.

', '.join(...) takes the transformed list and joins its elements into a single string with ", " as the separator.

Week 3 

October /14/25

So from the 8th of october to the 10th i was unable to push nothing but that doesnt mean nothing was happening.

I attended PyconAfrica 25 for the 3 days and maan did i really learna dn was exposed to much - from a whole python community brilliant minds, great sponsors and great reception.

This week as bit by bit ill be writting on such  with no rush - but overral it was amazing as the idea of Kasilink to be a platform was ignited there and also that i understand better from visuals rathers than terms.

 7.2.py to correctly extract the numeric substring after "X-DSPAM-Confidence:" and convert it to float, add basic file-not-found handling, and print an average;

 Was faced with alot of mental battle today:

- Drowsiness unable to apply mysself deeper into things until mid day i realised that i didn't call my Lord to the scene or askHim to be with me. I then relaxed slept abit then when i woke went on my knees.
- So i rememebered that i learned something last week at the conference about how my brain works - i then went back to Pseaudo codes or diagrams to put the logic and flow first.

- im still on the files diagram not done yet but im thankful.

October / 15th/ 25

Wow only now the slice [:] and index do i get[]

When a split is being done like the X-DSPASM : you get a list with up to 2 elements (idexing is 0=first 1=second)

- Ooh yes so above you are correct but i believ what you were reffering to was the (':
', 1)
- So the one is the maxsplit as in how many splits are performed.

Wow im not saying that i like Pseuado or diagrams but they made me be able to look into code kinda break it down with 7.2.py

As i journey on im learning to be precise in my coding and sticking to one language one stack - Python.PostgreSql and Django.

October / 16/ 25

- Loops loops loops was working on 7.2 diagram and learned that loops are designed to run forever(while true) until we the user signal we want it to stop by entering 'done'. break is a standard way to exit such input loop immediately.

- So ive read the logic but somehow its only getting to me now the difference between loops and statements.

- statement tests a condition once at the spot where it appears.
If the condition is true, the indented block under the if runs exactly once (unless inside a loop, in which case it may run multiple times because the loop repeats).

- while loop does repeatedly tests a condition and runs its block as long as the condition is true.
The condition is checked before each iteration; when it becomes false (or a break executes), the loop ends and execution continues after the loop.

October/17/25

Was on lists today but Guardians were introduced to me - guarding a blowing part of the code. Another version of try and except but the reason we didn't use try/except on excercise is because - if it comes thru that line and finds not what it seeks it will skip...using if (continue)

- So i think when the code works and gives us something but then retraces (Traceback) thats when we intoduce guardian.

- So i noticed that even if i use chatgpt to confirm my psaeudo its however not entirely accurate.

Week 3 
October /20/25

Still continueing with my plan - python, postgresql and django.

Yeeesh just learned that a for loop has no options yes or no in 8.5 diagram. it processes the loop.

-  also learned that , Parallelogram: input / output (e.g., "Read file", "Print").

- SO flow charts are really helping me get the logic, bit by bit.

October/21/25

- Dictionaries,  im learning that this line many.get(w, 0) especially the zero is for - If w is not found (first time the word appears), it returns 0. Now in the dictionary many, If w is found, it returns its current count.

This is called dictionary based frequency - A histogram (in programming, a mapping of items to their counts) Defensive dictionary lookup (using .get(key, default) to avoid KeyError)

- a classic way to count how many times each item (word) appears in a collection.

- when i was flowcharting something ddnt make sens to me and i ask chat of vscode then it outlayd it. filename being empty - means: Did the user press Enter without typing anything when prompted for the file name? and the user just presses Enter, fname will be an empty string ("").
So, len(fname) < 1 checks if the string has zero length (no characters).

If it’s empty, the program sets fname to 'clown.txt' so it has a default file to use.

- im learning that my use of time needs attention - im distracted when i work 9-12 annd 15H00 - 18H00. This need re adjustment.

October /22/25

So Both lists and dictionaries are a way to store up data in a pc, same symbol [] but the other stores it in key, value pairs while list as asn array storing all types both.

- yeessh loops , "if is false" → skip the if-block → continue at the next statement (still inside the same loop body if you are inside a loop).
"for loop" → after the loop body finishes for one item, the loop gets the next item and runs the body again.

- if statement only decides whether to run the indented block right there. So its the condition that will determine

- for loop repeats its body for each item in the iterable.

- Loops playing games with me but im not giving in , "For each line - Yes/No" represents a loop condition checks if there are more lines to process in a file. 

- Ooh initializing dictionary and lists lol {} []

October/ 23/25

- Came across again with raise that i now had to understand it. So a bare minimum one inside an except block re-raises the same exception that was caught - meaning after printing "File not found: …", Python will continue raising the original FileNotFoundError and the program will terminate (unless some outer code catches it). The original traceback is preserved.

- ooh yes and learned that tuples are a sequence of list but in key value pairs. Theres a difference when i read it and when i finally understand it.

October/24/25

 - So when flowcharing be cautious to flow what the code says cause at times something might be created and just be redundant.

 - So Flowcharts should show meaningful actions/decisions; unused/redundant statements add noise and confuse a reader.

 - Idk whether it takes time but i keep on coming to this - that a for loop repeats only its own body. if we have another loop nested, each loop repeats the statement inside its own block..so code inside the inner loop returns the inner lop header not the outer loop header.

 - been running from this a min now but today had to put myself out there...on powershel to open file cat filename and command prompt is type filename.

 

Week 4

October/27/25
- So i realised that python is broad and for me awhile ago i chose backend, so today checked what on python im more on then automation with backend came up so those too. More like automation and web dev.

-  So to start with what i've realised im for ever doing on auto is git adding then push. i can start there and also wanted a while ago to automate my notes to formate build log and social media post. or automate that by 5 thirty always as for a review maybe to log in.

- Lets start there.

- When working on automation, you need to specify where on your directory youd run the script.
 Ran script to take my jpg files to pictures in my dir.
 

October/28/25

- Python has upgrade changing 'The exists_ok' keyword in Python 3.2+. If you run the script on an older Python (or on an environment where os.makedirs is overridden), calling (exists_ok=True) raises TypeError because that keyword isn't recognized anymore.

So "errno" module that exposes platform error numbers (the same symbolic names from POSIX errno.h) was brought in.

- So i ran an automation that picks up all images that i download into one folder from webp, jpeg,jpg and png.

- And did one also for my pdf files - all in order now.

- I started on webscraping : scraping data from sites for first tymers for my ground breakers show. But i soon realised that my commitment wasntthere and normally maybe after sum finish script my drive less. so then onnce this kicks i will review code write notes and comments etc

- October/30th/25
- I didnt work yesterday and maan did it not feel ohk..im glad im here today

- Ive slept enough Ive played enough my time in now the opportunity is now. Now or Never!

- October/02/2025
- Was curious what is a parser - A parser is a program or library that reads raw text (or bytes) and turns it into a structured representation you can work with in code. For HTML that structure is usually a tree of nodes (DOM-like): elements, attributes, and text nodes.
How that applies to HTML scraping

When you fetch a web page you get raw HTML bytes. An HTML parser:
Tokenizes the bytes/characters (tags, attributes, text).
Builds a tree of nodes (elements nested inside other elements).
Normalizes/fixes common mistakes in real-world HTML (missing end tags, misnested tags).
After parsing you can query the tree (find elements, extract text, follow links).

Week 5

- Novermber/03/25

- Yeesh ive been on sum soul searching i guess when  i seem to struggle with putting much focus on my programming. Well i guess thats what happens when you trying to juggle alot in order to stay afloat in life - but ive put all to rest only me and programming now will see where it takes us.

- manged to launch database today sql3 and struggle to see it on my power shell etc but eventually managed. can see the table but cant see the contents even the script runs for firsttyimeers, will have to go thru it again...im a fan of postgre bytheway.

- November/03/25

- Man for the first time i really had fun, just playing around with code. No deadline, project, or solving problem just playing around with it seeing what it does how i can also do something with it.

-So my firsttymers script work but now its collecting othing i need to change approach to find that which i can scrape from.

- Wow struggled through sites and the script to print out or show me first timers until i used wiki but now its all mixed up needing sum attention to detail sorting also.

- i Think the mentality of playing around with code seeing what it can do or show me or what i need - might be a great mentality going into things.

November/05/25

- Bit by bit im getting into shortcuts more on navigating through vs code and other applications powershell too.

- So im learning that not being able to play around with code limits me in a way and blocks my engagement, im creative by nature and being able to play around with code as i noticed this week is my fortay. So i guess i have to do that deepseek more first to a place i can be able to just play code then continue with my automations and webscrapings etc before api python which then will be met with postgre connections then django later.

