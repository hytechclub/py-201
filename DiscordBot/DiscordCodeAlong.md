# Discord Chat Bot

In this activity, create a Discord chat bot that can respond to messages in a Discord server. How the chat bot responds and what it says is for you to decide! The chat bot could respond to common phrases, or respond to commands with useful features like rolling dice, posting pictures, or acting as a calculator.

## Setting Up

1. Go to [repl.it](https://repl.it)
1. Log in
1. Clone the [HyTechClub-Robot-Start repl](https://repl.it/@brebory/HyTechClub-Robot-Start)
1. Make sure you have a Discord account so you can create and registor your bot

## Creating and Registering the Bot

The first step is to navigate to the [Discord Developer Portal](https://discord.com/developers/applications). You'll be prompted to log in, so use your Discord account that you created during set up.

1. Make sure that you're on the Applications tab, and then click the blue "New Application" button in the top right
1. The "Create An Application" dialog will appear, so give your appliction a name, then click Create
1. You will be taken to your new application's General Information page. In the left-hand sidebar, click on "Bot"
1. On the Bot page, click the "Add Bot" button

If you get an error about "Too many users share this name", then you will need to change your application's name on the General Information page first, then try again with the new name.

## Saving the Bot Token in the .env File
Repl.it has a special feature that allows you to create environment variables for your Repl application. In your Repl, create a new file called `.env`. In this plaintext file, you can create environment variables by making key-value pairs like this:

```text
ENVIRONMENT_VARIABLE_NAME=Value
ANOTHER_VARIABLE=anothervalue
```

Each environment variable should be on it's own line within this file.

1. In the .env file, create a new variable called `DISCORD_BOT_SECRET`
1. Back in the Discord Developer Portal, navigate to your Bot's page, and find the "Copy" button for your bot's "Token"
![Discord Bot Settings](discord-bot-settings-cropped.jpg)
1. Click the copy button and paste the Bot Token into your Repl's `.env` file

### Code

```text
DISCORD_BOT_SECRET=ABCD.EFGHIJKLMNOPQR.STUVWXYZ
```

### Testing the Bot

With the starter code from the Repl, and your Bot Token in the `.env` file, you should now be able to run your Repl and see your bot successfully log in! CLick the Run button at the top of the repl and you should see output similar to the following, except the username should match the username that you gave your bot.

```text
Logged in as: HyTechClub Robot#9248
Command prefix is: !
```

## Responding to the on_message Event

The next step is to allow your bot to respond to messages in servers that it has joined. In order to accomplish this, you will use the `@bot.event` decorator. This decorator will take a function and add it to your bot as an "event handler". Event handlers allow you to write code that executes in response to something that happens.

1. Create an async function called `on_message`
1. Add the `@bot.event` decorator above your new function