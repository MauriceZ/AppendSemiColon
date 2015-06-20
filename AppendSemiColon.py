import sublime_plugin;

class AppendSemiColonCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			line_end = self.view.line(region).end()
			self.view.insert(edit, line_end, ';')
