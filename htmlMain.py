import random 

usedImgs = [] 


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
    <link rel="stylesheet" href="style.css">
    <script type="text/javascript" src="script.js"></script>
    <title>twitterBot</title>
</head>
<body class = "mainBody">
    <div class="myWrapper">
"""
    return header
   

def create_body_lines():
    body = """"""
    numOfDivs = random.randint(1, 20)
    for x in range(0, numOfDivs):
        body+= create_div(x) 
    return body

def create_div(i):
    myDivid = """ id = "myDiv""" + str(i)
    div="""        <div"""+myDivid +"""" >"""
    div+=create_elements(random.randint(0, 5))
    div+="""
        </div>
"""
    return (div)

def create_elements(i):
    switcher={
                0:create_h(),
                1:create_p(),
                2:create_img(),
                3:create_table(),
                4:create_table(),
                5:create_table(),
             }
    return switcher.get(i,"""""")

def create_h():
    headingValue = str(random.randint(1, 4))
    heading = """
            <h""" + headingValue+""">
                """ + create_content() + """
            </h""" + headingValue+">"
    return heading

def create_content():
    return "oh hey im some content"

def create_p():
    p = """
            <p>
                """ + create_content() + """
            </p>"""
    return p

def create_img():
    img = """
            <img src=" """ + getImg_src() + """" >"""
    return img

def getImg_src():
    #this will have to be randomized and then mark which image was taken to prevent repeats
    return "kittySmalls.JPG"

def create_table():
    table = """
            <table>""" + create_table_tr() + """
            </table>"""
    return table

def create_table_tr():
    numOftr = random.randint(1, 20)
    numOfth = random.randint(1, 10)
    tableTr = """
               <tr>""" + create_table_th(numOfth) + """
               </tr>"""
    for x in range(0, numOftr):
        tableTr += """
               <tr>""" + create_table_td(numOfth) + """
               </tr>"""
    
    return tableTr


def create_table_th(numOfth):
    tableTh = """"""
    for x in range(0, numOfth):
        tableTh += """
                   <th>""" + create_content() + """</th>"""
    return tableTh

def create_table_td(numOfth):
    tableTd = """"""
    for x in range(0, numOfth):
        tableTd += """
                   <td>""" + create_content() + """</td>"""
    return tableTd


def create_footer_lines():
    footer = """    </div>
</body>
</html>
    """
    return footer


main()
