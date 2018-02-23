from congress import Congress
from today_success import practice_todayData
import re
import tweepy
import os

# Heroku Variables. You define these in Heroku's dashboard.
the_consumer_key = os.environ.get('the_consumer_key')
the_consumer_secret = os.environ.get('the_consumer_secret')
the_access_key = os.environ.get('the_access_key')
the_access_secret = os.environ.get('the_access_secret')
congress_key = os.environ.get('congress_key')

# Access keys from Twitter and ProPublica's API
consumer_key = the_consumer_key
consumer_secret = the_consumer_secret
access_key = the_access_key
access_secret = the_access_secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
congress = Congress(congress_key)

api = tweepy.API(auth)

# Returns votes that happend on the day that the function is called. 
todays_votes = congress.votes.today('house')

# This function accepts 3 arguments: The chamber, either 'house' or 'senate'; roll_call_num, which is the roll call number for each vote, and a session.
def get_info(chamber, roll_call_num, sess):
	today_yoho_vote = congress.votes.get(chamber, roll_call_num, sess)['votes']['vote']['positions'][426]['vote_position']
	shortTitle = congress.votes.get(chamber, roll_call_num, sess)['votes']['vote']['bill']['short_title']
	billNum = congress.votes.get(chamber, roll_call_num, sess)['votes']['vote']['bill']['number']
	bill_desc = congress.votes.get(chamber, roll_call_num, sess)['votes']['vote']['description']
	which_congress = str(congress.votes.get(chamber, roll_call_num, sess)['votes']['vote']['congress'])
	iso_bill = congress.votes.get(chamber, roll_call_num, sess)['votes']['vote']['bill']['bill_id']
	cleaned_bill = re.sub("[^0-9\-.]", '', iso_bill)
	congress_dot_gov = 'https://www.congress.gov/bill/' + which_congress + 'th-congress/house-bill/' + cleaned_bill
	api.update_status('Ted Yoho voted ' + today_yoho_vote + ' on "' + bill_desc + '," in '+ billNum + ' "' + shortTitle + '." ' + congress_dot_gov)

#  This function goes through every vote that took place in the argument that is passed through in the form of d. It keeps going until there is no more (that's where except IndexError comes in). It gets the roll call number, session and chamber in each vote and then passes it into the get_info function.
def practice_today_roll(d):
	z = 0
	for i in d:
		try:
			rollCall = d['votes'][z]['roll_call']
			sess = d['votes'][z]['session']
			chamber = d['chamber']
			get_info(chamber, rollCall, sess)
			z += 1
			pass
		except IndexError:
			break

practice_today_roll(todays_votes)