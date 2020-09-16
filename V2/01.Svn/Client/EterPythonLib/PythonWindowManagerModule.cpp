//Find
PyObject * wndImageGetWidth(PyObject * poSelf, PyObject * poArgs)
{
	...
}

///Add
//#if defined(ENABLE_PARTY_MATCH)
PyObject* wndResetFrame(PyObject* poSelf, PyObject* poArgs)
{
	UI::CWindow* pWindow;
	if (!PyTuple_GetWindow(poArgs, 0, &pWindow))
		return Py_BuildException();

	dynamic_cast<UI::CAniImageBox*>(pWindow)->ResetFrame();

	return Py_BuildNone();
}
//#endif

//Find
		{ "IsDown",						wndButtonIsDown,					METH_VARARGS },
		
///Add
//#if defined(ENABLE_PARTY_MATCH)
		{ "ResetFrame",					wndResetFrame,					METH_VARARGS },
//#endif