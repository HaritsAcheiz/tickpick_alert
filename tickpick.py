from httpx import Client
from selectolax.parser import HTMLParser
from dataclasses import dataclass 
from dotenv import load_dotenv
import os
from urllib.parse import urljoin

load_dotenv()

@dataclass
class TickpickScraper():
	baseUrl: str = 'https://www.tickpick.com'
	userAgent: str = 'Mozilla/5.0'
	proxyPath: str = None
	proxies: str = None

	def send_req(self, url, params):
		headers = {
            'user-agent': self.userAgent,
        }

		with Client(headers=headers, follow_redirects=True) as client:
			response = client.get(url, params=params)
			response.raise_for_status()

		return response

	def parse(self, response):
		tree = HTMLParser(response.text)
		tickets = tree.css('div.py-5 > div:nth-of-type(1) > ul > li.mb-0')
		for ticket in tickets:
			print(ticket.text(strip=True))

	def search_by_term(self, searchTerm):
		endpoint = '/search'
		url = urljoin(self.baseUrl, endpoint)
		params = {
			'q': searchTerm
		}

		response = self.send_req(url, params)
		self.parse(response)


@dataclass
class TickpickApi():
	baseUrl: str = 'https://www.tickpick.com'
	clientId: str = None
	clientSecret: str = None
	accessToken: str = None

	def authenticate(self):
		endpoint = ''
		url = urljoin(self.baseUrl, endpoint)
		
		response = send_req(url)
		jsonData = response.json()
		self.accessToken = jsonData['']['']

	def send_req(self, url):
		headers = {
            'user-agent': self.user_agent,
        }

		with Client(headers=headers) as client:
			response = client.get(url)
			response.raise_for_status()

		return url, response


	def search_by_term(self, searchTerm):
		endpoint = ''
		url = url.urljoin(self.baseUrl, endpoint)
		response = send_req(url)
		
		return response
		


if __name__ == '__main__':
	# clientId = os.getenv('TICKPICK_CLIENT_ID')
	# clientSecret = os.getenv('TICKPICK_CLIENT_SECRET')
	api = TickpickScraper()

	# authentication
	# api.authenticate()

	# search by term
	searchTerm = 'ncaa-mens-basketball-tournament-east-regional-alabama-vs-byu--duke-vs-arizona-session-1'
	response = api.search_by_term(searchTerm=searchTerm)

