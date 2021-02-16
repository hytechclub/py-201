# Discord Bot Challenges

After completing the [code-along](DiscordCodeAlong.md), attempt the challenges below.

## Commands

The Discord library also allows special handling, called commands, that allow a user to send a message with arguments to the bot, just like calling a function! To add a command to the bot, use the `@bot.command()` decorator. Note that this decorator requires the parenthesis, while the `@bot.event` decorator does not. In order for your bot to work correctly with commands, the `on_message` event handler should await the `bot.process_commands` method. Let's add a command to our bot that simulates rolling a 6-sided die using the [`random`](https://docs.python.org/3/library/random.html) library!

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

In the preceding section, a couple new concepts were introduced. Specifically, the *function annotation* for the `count` variable - this is a newer Python feature that allows you to specify the type that a parameter expects. The Discord library uses this annotation to convert the message's content into whatever type you specify. You'll notice if you send a message like `$roll one`, your bot will not respond, and your Repl's console will have a large error message starting with `Ignoring exception in command roll:`. This is expected - the user did not respond with the expected parameter, so the command did not execute.

Specifically, the [`Converter`](https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html#basic-converters) for the argument was unable to parse the user's message. If you're interested in customizing and improving this behavior, you can check out the documentation for [Special Converters](https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html#special-converters) for more information. This might come in handy for some of the Challenges this week!
