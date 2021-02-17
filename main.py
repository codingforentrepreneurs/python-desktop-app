from dataclasses import dataclass # pip install dataclasses
import pathlib
import jinja2

import webview # pip install pywebview

def render_jinja2_html(entrypoint, context={}, base_dir='.'):
    base_dir = pathlib.Path(base_dir).resolve() # root dir
    loader = jinja2.FileSystemLoader(searchpath= base_dir / "templates")
    template_env = jinja2.Environment(loader=loader)
    template = template_env.get_template(entrypoint)
    return template.render(**context)

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
rendered_html_str = render_jinja2_html("home.html", context={"name": "PyDesktop App"})
window_args = {
    "js_api": js_api,
    "width": 1200
}
window = webview.create_window("PyDesktop", html=rendered_html_str, **window_args)
js_api._window = window
webview.start(debug=True)