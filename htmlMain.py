import random 
import os

usedImgs = [] 
num_lines = sum(1 for line in open('deadsongs.txt'))


def main():
    """
    executes all methods in order
    :return: none
    :author: Lucy Happ
    """
    #clear old images 
   

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
    <title>twitterBot</title>
</head>
<body class = "mainBody">
    <div class="myWrapper">
        <div id="generalInfo">
            <h1>
                Welcome To My Grateful Dead HTML Generating TwitterBot!
            </h1>
            <p>
                This bot was made both as a personal project to familiarize myself with the twitter api
                and out of a deep irrational love for Grateful Dead. I'm a cat mom, deadhead, Taco Bell enthusiast, and a computer engineer.
                This project was developed using python with the tweepy library  and using tools such as Git and Visual Studio.
                The intended purpose of this bot was host a monthly CSS competition through twitter by providing pseudorandom
                generated HTML files. The HTML file is not to be edited and only the CSS file (style.css) is to be submitted.
            </p>
            <a href="https://www.tacobell.com/">Visit The Offical TacoBell Website </a>
            <a href="myTest.HTML" download>Download the HTML & Image Files</a>
            <a href="https://www.cs.cmu.edu/~mleone/dead-lyrics.html"> Images and Content Sources</a>
            <a href="http://www.csszengarden.com/">This bot was inspired by CSS Zen Garden</a>
            <a href="https://github.com/happlb/htmlGenerator">View my GitHub for this Project </a>
            <a href="https://www.linkedin.com/in/lucy-happ-647684153">View my Linkdien</a>
            <a href="https://happlb.github.io/personal-portfolio-v1.1/index">View My Personal Webpage</a>
        </div>
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
                4:create_ul(),
                5:create_ol(),
             }
    return switcher.get(i,"")

def create_h():
    headingValue = str(random.randint(1, 4))
    heading = """
            <h""" + headingValue+""">
                """ + create_content() + """
            </h""" + headingValue+">"
    return heading

def create_content():
    line_to_grab = random.randint(0, num_lines-1)
    songFile = open("deadsongs.txt", "r")
    line = songFile.readlines()[line_to_grab].rstrip() 
    return line

def create_lg_content():
    path ='deadSongsLyrics/'
    files = os.listdir(path)
    index = random.randrange(0, len(files))
    path +=files[index]
    songFile = open(path, "r")
    Lines = songFile.readlines()
    myLyrics=""
    for line in Lines: 
        myLyrics+=line.rstrip() + " " 
    return myLyrics

def getImg_src():
    path ='photos/'
    files = os.listdir(path)
    index = random.randrange(0, len(files))
    path +=files[index]
    return path

def create_p():
    p = """
            <p>
                """ + create_lg_content() + """
            </p>"""
    return p

def create_img():
    img = """
            <img src=" """ + getImg_src() + """" >"""
    return img



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


def create_ul():
    ul = """
            <ul>""" + create_li() + """
            </ul>"""
    return ul

def create_ol():
    ol = """
            <ol>""" + create_li() + """
            </ol>"""
    return ol

def create_li():
    listItem=""
    numOfLi = random.randint(1, 20)
    for x in range(0, numOfLi):
        listItem += """
               <li>""" + create_content() + """</li>"""
    
    return listItem

def create_footer_lines():
    footer = """    </div>
</body>
</html>
    """
    return footer


main()
