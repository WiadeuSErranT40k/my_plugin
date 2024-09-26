import sublime
import sublime_plugin

class SaludarCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.message_dialog("¡Hola! Este es un saludo desde SaludarCommand.")
