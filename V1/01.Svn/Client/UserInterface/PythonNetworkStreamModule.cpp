//Find
PyObject* netSendExchangeElkAddPacket(PyObject* poSelf, PyObject* poArgs)
{
	int iElk;
	if (!PyTuple_GetInteger(poArgs, 0, &iElk))
		return Py_BuildException();

	CPythonNetworkStream& rkNetStream=CPythonNetworkStream::Instance();
	rkNetStream.SendExchangeElkAddPacket(iElk);
	return Py_BuildNone();
}

///Add
#ifdef GROUP_MATCH
PyObject* netSendGroupMatchPacket(PyObject* poSelf, PyObject* poArgs)
{
	int index;
	if (!PyTuple_GetInteger(poArgs, 0, &index))
		return Py_BuildException();
	int ayar;
	if (!PyTuple_GetInteger(poArgs, 1, &ayar))
		return Py_BuildException();

	CPythonNetworkStream& rkNetStream=CPythonNetworkStream::Instance();
	rkNetStream.GroupMatchh(index, ayar);
	return Py_BuildNone();
}
#endif

//Find
		{ "SendExchangeStartPacket",			netSendExchangeStartPacket,				METH_VARARGS },

///Add
		#ifdef GROUP_MATCH
		{ "SendGroupMatch",						netSendGroupMatchPacket,				METH_VARARGS },
		#endif