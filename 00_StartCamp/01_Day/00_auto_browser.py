import webbrowser

# webbrowser.open('https://google.com')

idols = ['bts', 'red velvet', 'iu', 'winner']

for idol in idols:
    print(type(idol))
    webbrowser.open('https://search.naver.com/search.naver?query='+idol)