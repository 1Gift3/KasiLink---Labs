01/10/25
I started with Kasilab - which i am revising Py4e with kasilink in mind excercises. The thing is ive been learning and stopping when i get to big bugs or a negative mental attitude.

So with changing that since mental change that it is God that has given me this so what so ever i come accross i will persist and concourer because it is mine for the taking.

Today i worked on Input prompts with, list based prompts and a bit of conditional statements.

I must no start applying the test once done writting file - or habits as Dr chuck does, also not forgetting what Gama said Silid principles, fundamentals and design pattern.

02/10/25

Yes i keep on stumbling on and off so What ? am i learning yeah might it take time yeah - does it matter not when when im honest on it. Yes it might not reflect a perfect work guy but im applying to kasilink as i should be. Youll never know

Traceback might be on the line or the line above it.

Create your folders from Vscode then navigate with shell - and also check code with Shell.

Worked on py4e conditionals and man was i challenged , well 2morow we up to deepseek then kasilink.

03/10/25

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

