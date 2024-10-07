import re

def extract_strings_between_tags(html_string):
    # This pattern matches any content between HTML tags
    pattern = r'<[^>]+>(.*?)</[^>]+>'
    
    # Find all matches in the HTML string
    matches = re.findall(pattern, html_string, re.DOTALL)
    
    # Strip whitespace from the beginning and end of each match
    return [match.strip() for match in matches if match.strip()]

# Example usage
html_content = """
<html>
    <head>
        <title>Sample Page</title>
    </head>
    <body>
        <h1>Welcome to my website</h1>
        <p>This is a paragraph.</p>
        <div>
            <p>This is another paragraph inside a div.</p>
        </div>
        <p>Here's a paragraph with <strong>bold text</strong> inside.</p>
    </body>
</html>
"""

extracted_strings = extract_strings_between_tags(html_content)

print("Extracted strings:")
for i, string in enumerate(extracted_strings, 1):
    print(f"{i}. {string}")
