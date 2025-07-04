from tickpick import TickPickApi

if __name__ == '__main__':
	api = TickPickApi()
	api.authenticate()
	response = api.search_by_term()