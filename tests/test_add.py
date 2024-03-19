from add import add_int

def test_add_int():
  """Tests add_int function with positive integers"""
  result = add_int(2, 3)
  # Two assertions: check for both the sum and data type
  assert result == 5, "Sum of 2 and 3 should be 5"
  assert isinstance(result, int), "Result should be an integer"
