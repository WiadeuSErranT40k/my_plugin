import sublime
import sublime_plugin

class MiPluginCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.message_dialog("Hola desde MiPlugin!")

