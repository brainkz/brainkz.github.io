
HOME = '/Users/brainkz/Coding/brainkz.github.io'

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
<!-- <h2>Ph.D. candidate, University of Rochester</h2> -->
'''

ADDRESS = '''
<address>
  Ph.D. candidate<br>
  Department of Electrical and Computer Engineering<br>
  University of Rochester<br>
  501 Computer Studies Building<br>
  Rochester, NY 14627<br>
  <img width="100em" src="images/part1.png" alt="part1">
  <img width="190em" src="images/part2.png" alt="part2">
</address>
'''

BIO = '''
<p>Rassul Bairamkulov was born in August 1994 in Karaganda, Kazakhstan.<br>
He received a Bachelor of Engineering degree in Electrical and Electronic Engineering from Nazarbayev University in Astana, Kazakhstan in 2016, and a Master of Science degree in Electrical and Computer Engineering from the University of Rochester in Rochester, NY in 2018.
In the summers of 2018 and 2020, he interned with Qualcomm in San Diego, CA.
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
'iscas': 'Proceedings of the IEEE International Symposium on Circuits and Systems',
'dac'  : 'Proceedings of the ACM/IEEE Design Automation Conference',
'pemc' : 'Proceedings of the IEEE International Power Electronics and Motion Control Conference'
}
JC = {**JOURNALS,**CONFERENCES}

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
}

PRESENTATIONS = '''
<h2 id="presentation">Talks</h2><a href=#up>Return to top</a>
<p>
<strong>R. Bairamkulov</strong>, "Graph Algorithms for VLSI Power and Clock Networks," University of Rochester, Rochester, New York, April 27, 2022.<br>
<a href="talks/Defense.pdf">PDF</a> <a href="talks/maps.pptx">Maps</a> <a href="talks/Defense_Supplemental.zip">Supplemental Materials</a>
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
