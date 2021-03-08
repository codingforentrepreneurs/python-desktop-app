from dataclasses import dataclass # pip install dataclasses
import pathlib
import jinja2
import json

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

    def selectFile(self):
        file_types = ("Images (*.png;*.jpg)", )
        return self._window.create_file_dialog(webview.OPEN_DIALOG, file_types=file_types)

    def selectFolder(self):
        return self._window.create_file_dialog(webview.FOLDER_DIALOG)

    def saveFile(self):
        file_types = ("Text (*.txt)", )
        return self._window.create_file_dialog(webview.SAVE_DIALOG, save_filename='abc.txt')
    
    def saveProjectFile(self):
        file_types = ("PyDestkop (*.pydesktop)", )
        return self._window.create_file_dialog(webview.SAVE_DIALOG, save_filename='abc.pydesktop')

    def myAPIRequest(self, jsonData):
        data  = json.loads(jsonData)
        destFilePath = data.get('filePath')
        print("my api request", jsonData, )
        if destFilePath:
            path = pathlib.Path(destFilePath).resolve()
            if path.exists():
                with open(path, 'w+') as f:
                    f.write(jsonData)


    def thisIsMyPyHandler(self, jsonData):
        print('this is my handler working', jsonData)

    def defaultHandleForm(self, jsonData):
        print("raw json data", jsonData)
        data = {}
        try:
            data = json.loads(jsonData)
        except:
            pass
        print("python data", data)
        print('myinputvalue', data.get('myinputname'))

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