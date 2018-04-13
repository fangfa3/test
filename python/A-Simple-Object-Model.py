def test_read_write_field():
	# Python code
	class A(object):
		pass
	obj = A()
	obj.a = 1
	assert obj.a == 1

	obj.b = 5
	assert obj.a == 1
	assert obj.b == 5

	obj.a = 2
	assert obj.a == 2
	assert obj.b == 5

	# Object model code 
#	A = Class(name="A", base_class=OBJECT, fields={}, metaclass=TYPE)
#	obj = Instance(A)
#	obj.write_attr("a", 1)
#	assert obj.read_attr("a") == 1
#
#	obj.write_attr("b", 5)
#	assert obj.read_attr("a") == 1
#	assert obj.read_attr("b") == 5
#
#	obj.write_attr("a", 2)
#	assert obj.read_attr("a") == 2
#	assert obj.read_attr("b") == 5

class Base(object)

	def __init__(self, cls, fields):
		self.cls = cls
		self.fields = fields

	def read_attr(self, fieldname):
		return self._read_dict(fieldname)

	def write_attr(self, fieldname, value):
		self._write_dict(fieldname, value)

	def isinstance(self, cls):
		return self.cls.issubclass(cls)

	def callmethod(self, methname, *args):
		meth = self.cls._read_from_class(methname)
		return meth(self, *args)

	def _read_dict(self, fieldname):
		return self._fields.get(fieldname, MISSING)

	def _write_dict(self, fieldname, value):
		self._fields[fieldname] = value

MISSING = object()

