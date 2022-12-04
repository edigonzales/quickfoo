import quickfoo

jack = quickfoo.Ilivalidator('jack', '21')
jack.getAge()

valid = jack.validate('tests/data/254900.itf')
print("The file is valid: {}".format(valid))