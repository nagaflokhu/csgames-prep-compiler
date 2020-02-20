
class Node:
  def __init__(self, type, children):
    self.type = type
    self.children = children

def eval_(program):
  for line in program:
    eval_line(line)

def eval_line(line):
  eval_ast(to_ast(tokenize(line)))

def tokenize(line):
  return line.split()

def to_ast(tokens):
  pass

def eval_ast(node):
  if node.type == 'if':
    condition = eval_ast(node.children[0])
    if condition:
      return eval_ast(node.children[1])
    elif len(node.children) == 3:
      return eval_ast(node.children[2])
  elif node.type == '==':
    return eval_ast(node.children[0]) == eval_ast(node.children[1])
  elif node.type == 'number' or node.type == 'string':
    return node.children[0]

def parse(stream):
  stream = stream.split()
  token, stream = next_token(stream)
  while token is not None:
    pass

# if a = 5 print "ok" else print "fail"
# if a = 5 print "ok" print "fail"