
template = """
Dear {name}
As you may know, 2010 marks our {year} years of doing business. Over the last decade, AdWorks has grown from a tiny startup into a robust company with over 200 employees throughout the Southeast. Our growth would not have been possible without loyal customers like you. Therefore, we would like to extend to you a {discount}% discount on your next order. It’s our way of saying “thanks" for your continued business. We’ll keep working hard to provide the best possible customer service along with innovative products, just as we’ve always done. Thanks again for choosing AdWorks!
Sincerely,

Liz Doe
President and CEO
"""	#	Taken from https://edu.gcfglobal.org/en/word2010/using-mail-merge/1/

recipients = [
	{
		"name": "Someone",
		"year": 5,
		"discount": 10
	},
	{
		"name": "Some other one",
		"year": 8,
		"discount": 20
	}
]

def	create(info):
	return template.format(name=info["name"], year=info["year"], discount=info["discount"])

if __name__ == "__main__":
	for info in recipients:
		print(create(info))
