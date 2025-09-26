import webbrowser

f = open('treinamento175.html','w')

message = """<html>
<head></head>
<body><p>Olá mundo!</p></body>
</html>"""

f.write(message)
f.close()

webbrowser.open_new_tab('helloworld.html')
