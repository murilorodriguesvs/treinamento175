import webbrowser

f = open('Treinamento 175.html','w')

message = """<html>
<head></head>
<body><p>Olá mundo!</p></body>
</html>"""

f.write(message)
f.close()

webbrowser.open_new_tab('helloworld.html')
