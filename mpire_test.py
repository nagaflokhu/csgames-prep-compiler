from mpire import *

def test_eval_if_true():
  res = eval_ast(
    Node(
      type = 'if',
      children = [
        Node(
          type = '==',
          children = [
            Node(
              type = 'number',
              children = [5]
            ),
            Node(
              type = 'number',
              children = [5]
            )
          ]
        ),
        Node(
          type = 'string',
          children = ['hi']
        )
      ]
    )
  )

  expected = 'hi'
  check_expected(expected, res)

def test_eval_number():
  res = eval_ast(Node(type = 'number', children = [5]))
  expected = 5
  check_expected(expected, res)

def test_eval_string():
  res = eval_ast(Node(type = 'string', children = ['hi']))
  expected = 'hi'
  check_expected(expected, res)

def check_expected(expected, actual):
  if not expected == actual:
    print('Expected {}, got {}'.format(expected, actual))
  else:
    print('Success!')

if __name__ == '__main__':
  for fn_or_var_name in dir():
    if fn_or_var_name.startswith('test_'):
      eval(fn_or_var_name)()