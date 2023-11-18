glossary = {
    'variable': 'A name that refers to a value.',
    'list': 'A collection of items in a particular order.',
    'dictionary': 'A collection of key-value pairs.',
}

for term, definition in glossary.items():
    print(f"{term}: {definition}")


glossary['tuple'] = 'An immutable, ordered collection of elements.'
glossary['function'] = 'A reusable block of code.'
glossary['module'] = 'A file containing Python code.'
glossary['class'] = 'A blueprint for creating objects.'
glossary['method'] = 'A function that is associated with an object.'


for term, definition in glossary.items():
    print(f"{term}: {definition}")
