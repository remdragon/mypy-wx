from typing import Any, Tuple, Type
import wx

class _Event ( wx.Event ):
	def __init__ (
		**kw : Any
	) -> None: ...


class _CommandEvent ( wx.CommandEvent ):
	def __init__ ( self,
		id : int,
		**kw: Any
	) -> None: ...

def NewEvent() -> Tuple[Type[_Event],wx.PyEventBinder]: ...

def NewCommandEvent() -> Tuple[Type[_CommandEvent],wx.PyEventBinder]: ...
