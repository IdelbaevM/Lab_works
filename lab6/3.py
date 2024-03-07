def true(tuple_elements):
    return all(tuple_elements)
tuple1 = (True, True, True)
tuple2 = (True, False, True)
result1 = true(tuple1)
result2 = true(tuple2)
print(f"All elements in tuple1 are true: {result1}")
print(f"All elements in tuple2 are true: {result2}")
