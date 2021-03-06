"""
TEST CASES START
"""

from Utilities import *

import pythonCallback

def input_pin_mode(port, pin):
	"""Set the pin mode to input"""
	try:
		PinPortVal = ValidPort[ os.environ['VARIANT'] ](port) and ValidPin[ os.environ['VARIANT'] ]( port, pin )
		ReferenceVal = pythonCallback.set_python_callback_reference(python_cb_func)
		if PinPortVal == False:
			raise RuntimeError, "Wrong pin and/or port. Please check the port and pin value!"
		elif ReferenceVal != None:
			raise RuntimeError, "Fails setting python ctype function reference!"
	except RuntimeError, arg:
		print arg
		return False
	else:
		VariantPinMode[ os.environ['VARIANT'] ] (port, pin, 'INPUT' )
		#GPIO_PUPDR( port, python_cb_func )
		#GPIO_MODER( port, python_cb_func )
		print "Pin mode set to INPUT"
		return True

def output_pin_mode(port, pin):
	"""Set the pin mode to output"""
	try:
		PinPortVal = ValidPort[ os.environ['VARIANT'] ](port) and ValidPin[ os.environ['VARIANT'] ]( port, pin )
		if PinPortVal == False:
			raise RuntimeError, "Wrong pin and/or port. Please check the port and pin value!"
	except RuntimeError, arg:
		print arg
		return False
	else:
		VariantPinMode[ os.environ['VARIANT'] ]( port, pin, 'OUTPUT' )
		#GPIO_PUPDR( port, python_cb_func )
		#GPIO_MODER( port, python_cb_func )
		print "Pin mode set to OUTPUT"
		return True

def input_pullup_mode(port, pin):
	"""Set the pin mode to input_pullup"""
	try:
		PinPortVal = ValidPort[ os.environ['VARIANT'] ](port) and ValidPin[ os.environ['VARIANT'] ]( port, pin )
		if PinPortVal == False:
			raise RuntimeError, "Wrong pin and/or port. Please check the port and pin value!"
	except RuntimeError, arg:
		print arg
		return False
	else:
		VariantPinMode[ os.environ['VARIANT'] ]( port, pin, 'INPUT_PULLUP' )
		#GPIO_PUPDR( port, python_cb_func )
		#GPIO_MODER( port, python_cb_func )
		print "Pin mode set to INPUT_PULLUP"
		return True

"""
TEST CASES END
"""
