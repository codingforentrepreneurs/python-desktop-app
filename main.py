from dataclasses import dataclass # pip install dataclasses
import webview # pip install pywebview


@dataclass
class API:
    name: str

    def helloWorld(self):
        """
        pywebview.api.helloWorld()
        """
        if not self.name:
            return "Hello world"
        return f"Hello world {self.name}"

js_api = API(name='Justin')

window_args = {
    "js_api": js_api,
    "width": 1200
}
webview.create_window("PyDesktop", "templates/base.html", **window_args)
webview.start(debug=True)