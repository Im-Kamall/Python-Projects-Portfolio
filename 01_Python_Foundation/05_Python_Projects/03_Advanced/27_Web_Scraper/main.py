html = """
<html>
<head><title>My Website</title></head>
<body>
<h1>Welcome to Python Web Scraper</h1>
<p>This is a sample paragraph.</p>
</body>
</html>
"""

start = html.find("<h1>") + 4
end = html.find("</h1>")

heading = html[start:end]

print("Extracted Heading:", heading)