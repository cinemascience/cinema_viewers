import webbrowser


# open several instances of URL to test
webbrowser.open_new("http://127.0.0.1:8000/cinema_explorer.html")
webbrowser.open_new_tab("http://127.0.0.1:8000/cinema_explorer.html?databases=testing/explorer/small.json")
webbrowser.open_new_tab("http://127.0.0.1:8000/cinema_explorer.html?databases=data/sphere.cdb")
webbrowser.open_new_tab("http://127.0.0.1:8000/cinema_explorer.html?databases=data/sphere_multi-image.cdb,data/sphere.cdb")

