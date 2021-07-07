knights = {"gallahand": "the pure", "robin": "the brave"}

for k, v in knights.items():
	print(k, v)

knights["Hex"] = "the Mighty"

if "Hex" in knights:
	knights.pop("gallahand")
	for k, v in knights.items():
		print(k, v)
