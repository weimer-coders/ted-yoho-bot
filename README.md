# Ted Yoho Bot
## Acknowledgement
* First, we would like to acknowledge Chris Amico and his [propublica-congress repo](https://github.com/eyeseast/propublica-congress). Without this repo, it would have been significantly more work, and for that we are eternally grateful.
## Getting Started
### Getting API Access
* Before starting any code, you need to create a new email and Twitter account for your bot.
* Then you must set up a new Twitter app and get Twitter API access. You can follow this [walk-through](https://github.com/weimer-coders/twitter-bots#your-twitter-api-key).
* Next you need to request access for ProPublica's Congress API. Here's where [to go](https://www.propublica.org/datastore/api/propublica-congress-api).
### Setting up Your Environment
* Open terminal.
* pip install virtualenv if you have not already.
`sudo -H pip install virtualenv`.
* Clone or download this repo. Move it somewhere you won't forget.
* `cd` into that directory.
* Create a virtual environment in that directory. Type or paste this in: `virtualenv --python=/usr/local/bin/python3 env`
* Activate your virtual environment by typing or pasting this in: `source env/bin/activate`.
### Install ted-yoho-bot's Dependencies
* While still in your virtual environment, you need to install the python-congress client. Type in or paste this line into your terminal window: `pip install python-congress`. Then run the setup script: `python setup.py install`.
* You're still in your virtual environment right? Cool. Install tweepy by typing in: `pip install tweepy`.

## Code
* Before deploying this to Heroku, you will want to make sure that our Python script that is running everything, `make_tweet.py`, is working locally. To do that, open the `ted-yoho-bot` folder in your text editor and paste in your access keys and secrets that you got from Twitter and your access key from ProPublica into `make_tweet.py`. So for example, you would replace  `the_consumer_key` on line 15 with the consumer key you got from Twitter in string format: `'YOUR_ACCESS_KEY'`. Ignore the key variables on lines 8 through 12 for now. That is for Heroku and only if you want to keep your variables hidden for when you publish your code on GitHub.
* You should be ready to see your very own Ted Yoho Twitter bot running from your machine. Back in terminal, type `python make_tweet.py`. If there were any votes for that day, it will tweet them from the account that you set up to tweet from. If there were not votes, it will do nothing. So don't panic.

## Deployment
* For deploying to Heroku, we followed along with this video. You can find it [here](https://www.youtube.com/watch?v=DwWPunpypNA).
* To set up when you want the bot to run –– such as daily, hourly and every 10 minutes and at what time –– you can use Heroku Scheduler. It is a Heroku add-on, and you can find instructions for setting it up [here](https://devcenter.heroku.com/articles/scheduler). You will have to verify your account by giving Heroku your credit card information.

## Things to Note
* The code in this repo is only for Ted Yoho's votes. There will be a new repo named `keeping-up-with-congress` coming in the future that will make it easier for others to follow House representatives or State senators that they are interested in.
