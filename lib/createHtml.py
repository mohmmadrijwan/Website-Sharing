def createHtmlFile(caption, link_url,):
    """
        Creates Html file for showing image and caption with shortened link
    """

    # Generate HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Image with Caption</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                margin: 50px;
            }}
            img {{
                max-width: 100%;
                height: auto;
            }}
            .caption {{
                margin-top: 10px;
                font-size: 18px;
            }}
            .caption a {{
                text-decoration: none;
                color: blue;
            }}
            .caption a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <img src="img/image.jpg" alt="Image">
        <div class="caption">
            <a href="{link_url}" target="_blank">{caption}</a>
        </div>
    </body>
    </html>
    """

    # Save the HTML content to a file
    with open("index.html", "w") as file:
        file.write(html_content)

    print("HTML file generated: index.html")
