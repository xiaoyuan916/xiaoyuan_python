from urllib import robotparser

parser = robotparser.RobotFileParser()
parser.set_url('https://www.taobao.com/robots.txt')
parser.read()
str=parser.can_fetch('Hellokitty', 'http://www.taobao.com/article')

print(str)