import random 

def main():
    """
    executes all methods in order
    :return: none
    :author: Lucy Happ
    """
    Html_file= open("myTest.html","w+")
    Html_file.write(create_header_lines() + create_body_lines() + create_footer_lines())
    Html_file.close()

    

def create_header_lines():
    """
    Read the header using the next byte message
    :return: number of lines in the message
    :author: Lucy Happ
    """
    header = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>twitterBot</title>
</head>
<body class = "mainBody">
    <div class="myWrapper">"""
    print(header);
    return header
   

def create_body_lines():
    body = """"""
    numOfDivs = random.randint(1, 10)
    for x in range(0, numOfDivs):
        body+= create_div() 
    print(body)
    return body

def create_div():
     return """
        <div>

        </div>
"""    

def create_footer_lines():
    footer = """    </div>
</body>
</html>
    """
    print(footer);
    return footer


main()
