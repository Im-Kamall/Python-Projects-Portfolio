url = input("Enter long URL: ")

short_code = "py" + str(len(url))

short_url = "https://short.ly/" + short_code

print("Short URL:", short_url)
