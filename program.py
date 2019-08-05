def main():
	print_header()
	folder = get_folder_from_user
	if not folder:
		print("Sorry, we can't search that location.")
		return

	text = get_search_text_from_user()
	if not text:
		print("We can't search for nothing!")
		return

	search_folders(folder, text)

def print_header():
	print("-----------------------------")
	print("--------TEXT SEARCHER--------")
	print("-----------------------------")

def get_folder_from_user():
	folder = input('What folder do you want to search?')
	if not folder or not folder.strip()
		return None
	if not os.path.isdir(folder):
		return None

	return os.path.abspath(folder)

def get_search_text_from_user():
	text = input('What are you searching for [single phrases only]?')
	return text

def search_folders(folder, text):

	all_matches = []
	items = os.listdir(folder)

	for item in items:
		full_item = os.path.join(folder,item)
		if os.path.isdir(full_item)
			continue

		matches = search_file(full_item, text)
		all_matches.extend(matches)

	return all_matches


def search_file(filename, search_text):


if __name__ == '__main__':
	main()