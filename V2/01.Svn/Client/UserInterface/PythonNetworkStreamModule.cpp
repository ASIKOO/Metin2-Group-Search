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
#if defined(ENABLE_PARTY_MATCH)
#include "PythonPlayer.h"
PyObject* netSendPartyMatchSearch(PyObject* poSelf, PyObject* poArgs)
{
	int index;
	if (!PyTuple_GetInteger(poArgs, 0, &index))
		return Py_BuildException();

	CPythonNetworkStream::Instance().PartyMatch(index, CPythonPlayer::PARTY_MATCH_SEARCH);
	return Py_BuildNone();
}
PyObject* netSendPartyMatchCancel(PyObject* poSelf, PyObject* poArgs)
{
	int index;
	if (!PyTuple_GetInteger(poArgs, 0, &index))
		return Py_BuildException();

	CPythonNetworkStream::Instance().PartyMatch(index, CPythonPlayer::PARTY_MATCH_CANCEL);
	return Py_BuildNone();
}
#endif

//Find
		{ "SendExchangeStartPacket",			netSendExchangeStartPacket,				METH_VARARGS },

///Add
#if defined(ENABLE_PARTY_MATCH)
		{ "SendPartyMatchSearch",				netSendPartyMatchSearch,				METH_VARARGS },
		{ "SendPartyMatchCancel",				netSendPartyMatchCancel,				METH_VARARGS },
#endif