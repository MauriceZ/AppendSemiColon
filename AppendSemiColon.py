import sublime_plugin

class AppendSemiColonCommand(sublime_plugin.TextCommand):
  def run(self, edit):

    def insert_semicolon(point):
      self.view.insert(edit, point, ';')

    def is_semicolon(point):
      return self.view.substr(point) == ';'

    for region in self.view.sel():
      line = self.view.line(region)
      line_begin = line.begin()
      line_end = line.end()

      while(self.view.substr(line_end - 1).isspace() and line_end != line_begin): # go to the first character from the end that isn't whitespace
        line_end -= 1

      if line_end == line_begin:
        continue

      if self.view.match_selector(line_end - 1, 'comment'):
        point = self.view.extract_scope(line_end - 1).a - 1

        if point < line_begin:
          continue
          
        while(self.view.substr(point).isspace() and point != line_begin): # go to the first character before the comment that isn't whitespace
          point -= 1

        if not self.view.substr(point).isspace() and not is_semicolon(point):
          insert_semicolon(point + 1)

      elif not is_semicolon(line_end - 1):
        insert_semicolon(line_end)
