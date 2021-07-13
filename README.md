# Item Stock Notifier

This is a python script in order to see if an item you want is back in stock. This makes it much easier for those who are trying to find something online that just never seems to be in stock! This bot can be modified to check the site every 10 minutes, 5 minutes or more or less, while notifying you on slack on your phone, or desktop. Making it so much easier then checking the website manually every day, every hour.

## How to set up

1. Type <code>git clone https://github.com/mathewsjoyy/StockNotifier.git</code> in your cmd.
2. cd into the project directory and type <code>pip install -r requirements.txt</code> in your cmd.
3. Read through comments and adjust code to your needs.
4. Set up a slack bot and obtain its api / token key.
5. Use repl.it's [UpTime Robot](https://replit.com/talk/learn/How-to-use-and-setup-UptimeRobot/9003) or any other methods to keep script running in background while you carry on with your day!

## Additional info

If you run into any errors with the code double check you have selected the correct css_selector <code>(Inspect element the page > find the tag with the stock text > right click > copy > copy selector)</code> in the website you're using, you have chrome installed and also that you are using latest version of python and the necessary packages. If you still run into errors feel free to contact me, and I can sort it out for you!
