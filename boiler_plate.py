import os

HOME = os.getcwd()

HEADER = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html>
<head>
  <title>Rassul Bairamkulov</title>
  <link rel="stylesheet" href="css/style.css">
  <!-- based on https://cdn.simplecss.org/simple.css -->
</head>
'''

NAVBAR = '''
<nav>
  <a href="index.html">Home        </a>
  <a href="pub.html"  >Publications</a>
  <a href="Rassul_Bairamkulov_CV_2023.pdf"  > CV    </a>
</nav>
'''

FOOTER = '''
</p>
</body>
</html>
'''

BODY_HEADER = '''
<!-- Main content -->
<h1>Rassul Bairamkulov</h1>
<h3>Advancing EDA tools for next-generation computing systems</h3>
'''
# <h2>Postdoctoral Scholar at EPFL</h2>
# <h3>Advancing EDA for next-generation computing systems</h3>

ADDRESS = '''
<address>
  <br><br><br>
  Integrated Systems Laboratory LSI<br>
  EPFL, Building INF 339<br>
  Lausanne 1015, Switzerland<br>
  rassul.bairamkulov@epfl.ch<br>
</address>
'''
  # <img width="100em" src="images/part1.png" alt="part1">
  # <img width="190em" src="images/part2.png" alt="part2">

WELCOME = '''
<p>Hello and welcome to my webpage.</p>

<p>I am a postdoctoral scholar in the&nbsp;<a href="https://www.epfl.ch/labs/lsi/">Integrated Systems Laboratory</a>&nbsp;(LSI) at&nbsp;EPFL, Lausanne, Switzerland, working alongside <a href="https://si2.epfl.ch/~demichel/">Professor Giovanni De Micheli</a>&nbsp;developing electronic design automation tools for the emerging VLSI technologies.&nbsp;</p>

<p>I completed my Ph.D. in Electrical and Computer Engineering at the&nbsp;<a href="https://www.hajim.rochester.edu/ece/">University of Rochester</a>, Rochester, New York, under the supervision of <a href="http://www2.ece.rochester.edu/users/friedman/">Professor E. G. Friedman</a>.</p>

<p>I was an intern at Qualcomm Inc., San Diego, California, during the summers of 2018 and 2020.</p>

<p>Prior to my doctoral studies, I received my B.Eng. in Electrical and Electronic Engineering at <a href="https://nu.edu.kz">Nazarbayev University</a>, Astana, Kazakhstan.</p>

<p>For more information, please see the <a href="pub.html">publications</a> section or my profile at <a href="https://scholar.google.com/citations?hl=en&user=RgDE-cIAAAAJ">Google Scholar</a>.</p>
'''

BIO = '''
<p>Rassul Bairamkulov was born in August 1994 in Karaganda, Kazakhstan.<br>
He received a Bachelor of Engineering degree in Electrical and Electronic Engineering from Nazarbayev University in Astana, Kazakhstan in 2016, and a Master of Science degree in Electrical and Computer Engineering from the University of Rochester in Rochester, NY in 2018.
I was an intern at Qualcomm in San Diego, California, during the summers of 2018 and 2020
He is currently completing the Ph.D. degree in Electrical and Computer Engineering from the University of Rochester in Rochester, NY under the supervision of Prof. Eby G. Friedman.
His current research interests include graph theory, physical design of integrated circuits, and electronic design automation of conventional and emerging VLSI technologies.</p>
'''

SKIP = '''
<h3 id="up">Skip to</h3>
<p>
<a href="#conference">Conference papers</a><br>
<a href="#presentation">Talks</a><br>
<a href="#dissertation">Dissertation</a>
</p>
'''

JOURNALS = {
'tcad' : 'IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems',
'tcasi': 'IEEE Transactions on Circuits and Systems I: Regular Papers',
}
CONFERENCES = {
'glsvlsi': 'Proceedings of the ACM Great Lakes Symposium on VLSI',
'iscas': 'Proceedings of the IEEE International Symposium on Circuits and Systems',
'dac'  : 'Proceedings of the ACM/IEEE Design Automation Conference',
'pemc' : 'Proceedings of the IEEE International Power Electronics and Motion Control Conference'
}
BOOKS = {
'springer_cham' : 'Springer, Cham, Switzerland'
}


JC = {**JOURNALS,**CONFERENCES, **BOOKS}

FANCY_NAMES = {
'me'	: '<strong>R. Bairamkulov</strong>',
'EGF'	: '<a href="http://www2.ece.rochester.edu/~friedman/">E. G. Friedman</a>',
'AR'	: 'A. Ruderman',
'YLF'	: 'Y. L. Familiant',
'ARoy'	: 'A. Roy',
'JSO'	: 'J. S. Ochoa',
'KX'	: 'K. Xu',
'MN'	: 'M. Nagarajan',
'MP'	: 'M. Popovich',
'TJ'	: 'T. Jabbari',
'VS'	: 'V. Srinivas',
'GDM'	: '<a href="https://si2.epfl.ch/~demichel/">G. De Micheli</a>',
}

PLAIN_NAMES = {
'me'	: 'R. Bairamkulov',
'EGF'	: 'E. G. Friedman',
'AR'	: 'A. Ruderman',
'YLF'	: 'Y. L. Familiant',
'ARoy'	: 'A. Roy',
'JSO'	: 'J. S. Ochoa',
'KX'	: 'K. Xu',
'MN'	: 'M. Nagarajan',
'MP'	: 'M. Popovich',
'TJ'	: 'T. Jabbari',
'VS'	: 'V. Srinivas',
'GDM'	: 'G. De Micheli',
}

PRESENTATIONS = '''
<h2 id="presentation">Talks</h2><a href=#up>Return to top</a>
<p>
<strong>R. Bairamkulov</strong>, "Graph Algorithms for VLSI Power and Clock Networks," University of Rochester, Rochester, New York, April 27, 2022.<br>
<a href="talks/Defense.pdf">PDF</a> <a href="talks/maps.pptx">Maps</a> <a href="talks/Defense_Supplemental.zip">Supplemental Material</a>
</p>
'''

DISSERTATION = '''
<h2 id="dissertation">Dissertation</h2><a href=#up>Return to top</a>
<p>
<strong>R. Bairamkulov</strong>, "Graph Algorithms for VLSI Power and Clock Networks," University of Rochester, Rochester, New York, April 2022.
<details>
<summary>
<u>Bibtex</u>
</summary>
<span>@phdthesis{bairamkulov_2022_thesis,<br>&emsp;author = "R. Bairamkulov",<br>&emsp;title = "Graph Algorithms for VLSI Power and Clock Networks",<br>&emsp;school = "University of Rochester",<br>&emsp;year = "2022",<br>}
</span>
</details>
</p>
'''

MONTHS = { 'Jan': 'January', 'Feb': 'February', 'Mar': 'March', 'Apr': 'April', 'May': 'May', 'Jun': 'June', 'Jul': 'July', 'Aug': 'August', 'Sep': 'September', 'Oct': 'October', 'Nov': 'November', 'Dec': 'December', 1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December',}


PROJECTS = '''
'''