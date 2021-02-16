from dataclasses import dataclass # pip install dataclasses
import webview # pip install pywebview


@dataclass
class API:
    name: str
    _window = None

    def triggerSomeJS(self):
        print("Trigger is working")
        print("run some long process")
        self._window.evaluate_js("helloWorldFromPy()")
        return 

    def sayName(self, arg_name=None):
        if arg_name is not None:
            print("arg_name", arg_name)
        return self.name

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
window = webview.create_window("PyDesktop", "templates/base.html", **window_args)
js_api._window = window
webview.start(debug=True)