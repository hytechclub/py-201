# Discord Bot Challenges

After completing the [code-along](DiscordCodeAlong.md), attempt the challenges below.

## 1. Limit the Bot to a Single Channel

For the following challenges, it will be helpful if your bot sticks to a single channel. Modify the `on_message` event handler so that your bot only responds to messages sent in your specific channel. Then, continue working on the challenges while testing the bot in your channel.

The following documentation pages may be helpful for this challenge:

* [Message](https://discordpy.readthedocs.io/en/latest/api.html#discord.Message)
* [TextChannel](https://discordpy.readthedocs.io/en/latest/api.html#discord.TextChannel)

## 2. Add More Prompts and Responses

Add at least 3 more prompts and responses to the `prompts_and_responses` dictionary!

1. Add a comma to the end of the _last item_ in the dictionary
1. After the last item on a new line, add a string for a new prompt, followed by a `:`, and then a string for the new response
1. Repeat until there are at least 3 new items
1. Run the code, and verify that your Discord bot responds to the new prompts!

## Commands

The Discord library also allows special message handling, called commands, that allow a user to send a message with arguments to the bot, just like calling a function! To add a command to the bot, use the `@bot.command()` decorator. Note that this decorator requires the parenthesis, while the `@bot.event` decorator does not. In order for your bot to work correctly with commands, the `on_message` event handler should await the `bot.process_commands` method. Let's add a command to our bot that simulates rolling a 6-sided die using the [`random`](https://docs.python.org/3/library/random.html) library!

1. At the top of the file with the other `import` statements, add `import random`
1. At the bottom of the `on_message` function, add `await bot.process_commands(message)`
1. Below the `on_message` function, add a new async function called `roll` that takes two parameters: `ctx` and `count`
1. Add an annotation to the `count` parameter to specify that it should be an `int`: `count: int`
1. Above the new `roll` function, add the `@bot.command()` decorator
1. In the body of the `roll` function, create a new variable called `message` and set it to the string `"You rolled:\n"`
1. Use the `range` function to create a `for` loop that executes `count` times
1. In the body of the `for` loop, create a new variable called `roll` and set it to the result of `random.randint(1, 6)` to simulate a 6-sided die roll 
1. Append to the `message` variable the following string: `":game_die: {}".format(roll)` to show a dice emoji and the rolled result
1. Outside of the `for` loop, at the bottom of the `roll` function, use the `ctx.send` method to send the `message` and `await` it

### Code

```py
import random 

@bot.command()
async def roll(ctx, count: int):
  message = "You rolled:\n"

  for _ in range(count):
    roll = random.randint(1, 6)
    message += ":game_die: {}".format(roll)

  await ctx.send(message)
```

## Function Annotations and Converters

In the preceding section, a couple new concepts were introduced. Specifically, the *function annotation* for the `count` variable - this is a newer Python feature that allows you to specify the type that a parameter expects. You may also see this concept referred to as a *type hint*. The Discord library uses this annotation to convert the message's content into whatever type you specify. You'll notice if you send a message like `$roll one`, your bot will not respond, and your Repl's console will have a large error message starting with `Ignoring exception in command roll:`. This is expected - the user did not respond with the expected parameter, so the command did not execute.

Specifically, the [`Converter`](https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html#basic-converters) for the argument was unable to parse the user's message. If you're interested in customizing and improving this behavior, you can check out the documentation for [Special Converters](https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html#special-converters) for more information. This page will come in handy for some of the challenges this week!

## 3. Create a Command to Add More Prompts and Responses

Create a new command, called `add`, that will allow the user to add a new prompt and response to the dictionary. The command should take two string parameters,`prompt` and `response`, and add them to the `prompts_and_responses` dictionary.

For example, a user should be able to call the command like this:

```text
$add "Hakuna" "Matata"
```

## 4. Create a Command to Change the Command Prefix

Next, the bot should have a command that allows users to change the `command_prefix`, called `prefix`.

For example, a user should be able to call the command like this:

```text
$prefix %
```

After executing the command, the bot should only process commands with the new prefix.

## 5. Using Special Converters for the Add Command

Read this [documentation on Special Converters](https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html#special-converters), then modify the `add` command to take a third optional boolean parameter, called `overwrite`, that uses the `typing.Optional` type hint. This parameter should default to `False` and control whether or not the user can overwrite an existing prompt when using the command.

1. At the top of **main.py** add `import typing`
2. Find the `add` function and give it a new parameter `overwrite`
3. Add the optional type hint to the new parameter: `typing.Optional[bool] = False`

Then, use the new `overwrite` parameter to modify the control flow of the `add` method to either allow or disallow the overwriting of existing prompts.

## More Commands

The sky is the limit for what you can accomplish with commands! Try to think of other fun commands to implement. Here's some ideas to get you started:

1. Create a command to start a countdown timer ([`Tasks`](https://discordpy.readthedocs.io/en/latest/ext/tasks/index.html) will help with this challenge!)
2. Create some commands to manage a to-do list (Try creating subcommands with [`Group`](https://discordpy.readthedocs.io/en/latest/faq.html#how-do-i-make-a-subcommand) to make this more user-friendly!)
3. Create some commands to control a multiplayer game like Battleship
4. Create a command to schedule a reminder to tag a user in the future
