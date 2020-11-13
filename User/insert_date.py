from datetime import datetime
import sublime
import sublime_plugin


class InsertDatetimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel()
        for s in sel:
            self.view.replace(edit, s, datetime.now().strftime("%a, %b %-d %Y; %-I:%M%p"))
