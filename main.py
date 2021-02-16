import webview # pip install pywebview

html_str = """
<h1>Hello World </h1>
"""
webview.create_window("PyDesktop", html=html_str)
webview.start(debug=True)