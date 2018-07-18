import webapp2
import jinja2
import os
import random

jinja_current_directory = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)

positive_responses = [
  'It is certain',
  'It is decidedly so',
  'Without a doubt',
  'Yes, definitely',
  'You may rely on it',
  'As I see it',
  'yes',
  'Most Likely',
  'Outlook good',
  'Yes',
  'Signs point to yes.'
]

negative_responses = [
    'Don\'t count on it',
    'My reply is no',
    'My sources say no',
    'Outlook not so good',
    'very doubtful.'
]

noncommittal_responses = [
    'Reply hazy',
    'try again',
    'Ask again later',
    'Better not tell you now',
    'Cannot predict now',
    'Concentrate and ask again'
]

response_list_list = [
    positive_responses,
    negative_responses,
    noncommittal_responses
]

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        welcome_template = \
                jinja_current_directory.get_template('templates/welcome.html')
        self.response.write(welcome_template.render())

    def post(self):
        welcome_template = \
                jinja_current_directory.get_template('templates/welcome.html')

        user_feeling = self.request.get('user_feeling')

        responses = None
        if user_feeling == 'positive':
            if random.random() > 0.25:
                responses = positive_responses
            else:
                responses = random.choice(response_list_list)
        elif user_feeling == 'negative':
            if random.random() > 0.25:
                responses = negative_responses
            else:
                responses = random.choice(response_list_list)
        elif user_feeling == 'noncommittal':
            if random.random() > 0.25:
                responses = noncommittal_responses
            else:
                responses = random.choice(response_list_list)
        else:
            responses = random.choice(response_list_list)

        template_dict = {
            'answer': random.choice(responses)
        }

        self.response.write(welcome_template.render(template_dict))

app = webapp2.WSGIApplication([
    ('/', WelcomePage),
], debug=True)
