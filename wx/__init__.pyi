# imports:
import six
from six import text_type as unicode, binary_type as bytes
from types import TracebackType
from typing import Any, Callable, Iterator, Optional, overload, Sequence, Tuple, Type, TypeVar, Union
Text = Union[unicode,str]
TextType = Text

if not six.PY2: long = int

# simple type declarations and aliases:

AcceleratorEntryFlags = int
BackgroundStyle = int
BackgroundStyleType = BackgroundStyle
BitmapType = int
Border = int
BorderType = int
BrushStyle = int
ClientData = Any
Coord = int
EventCategory = int
FontEncoding = int
FontFamily = int
FontFlag = int
FontStyle = int
FontWeight = int
ItemKind = int
KeyCode = int
LayoutDirection = int
LayoutDirectionType = LayoutDirection
MappingMode = int
MouseButton = int
MouseWheelAxis = int
StandardID = int
PyUserData = Union[Any] # TODO FIXME is this correct?
PyWindow = Window
RasterOperationMode = int
SystemColour = int
SystemFont = int
TextPos = long # TODO FIXME: the documentation claims this exists, but it doesn't appear to, this is a guess
Uint32 = int
UIntPtr = int
WindowID = int
WindowVariant = int
WindowVariantType = WindowVariant

# constants:

ACCEL_NORMAL : AcceleratorEntryFlags = ...
ACCEL_SHIFT : AcceleratorEntryFlags = ...
ALL : int = ...
BG_STYLE_PAINT : BackgroundStyle = ...
BITMAP_TYPE_INVALID : BitmapType = ...
BITMAP_TYPE_BMP : BitmapType = ...
BITMAP_TYPE_ICO : BitmapType = ...
BITMAP_TYPE_CUR : BitmapType = ...
BITMAP_TYPE_XBM : BitmapType = ...
BITMAP_TYPE_XBM_DATA : BitmapType = ...
BITMAP_TYPE_XPM : BitmapType = ...
BITMAP_TYPE_XPM_DATA : BitmapType = ...
BITMAP_TYPE_TIFF : BitmapType = ...
BITMAP_TYPE_TIF : BitmapType = ...
BITMAP_TYPE_GIF : BitmapType = ...
BITMAP_TYPE_PNG : BitmapType = ...
BITMAP_TYPE_JPEG : BitmapType = ...
BITMAP_TYPE_PNM : BitmapType = ...
BITMAP_TYPE_PCX : BitmapType = ...
BITMAP_TYPE_PICT : BitmapType = ...
BITMAP_TYPE_ICON : BitmapType = ...
BITMAP_TYPE_ANI : BitmapType = ...
BITMAP_TYPE_IFF : BitmapType = ...
BITMAP_TYPE_TGA : BitmapType = ...
BITMAP_TYPE_MACCURSOR : BitmapType = ...
BITMAP_TYPE_ANY : BitmapType = ...
BG_STYLE_CUSTOM : BackgroundStyle = ...
BORDER_DEFAULT : Border = ...
BORDER_DOUBLE : Border = ...
BORDER_MASK : Border = ...
BORDER_NONE : Border = ...
BORDER_RAISED : Border = ...
BORDER_SIMPLE : Border = ...
BORDER_STATIC : Border = ...
BORDER_SUNKEN : Border = ...
BORDER_THEME : Border = ...
BOTH : int = ...
ButtonNameStr : Text = ...
CANCEL : long = ...
CANCEL_DEFAULT : long = ...
CB_DROPDOWN : long = ...
CB_READONLY : long = ...
CB_SIMPLE : long = ...
CB_SORT : long = ...
CENTRE : long = ...
ComboBoxNameStr : Text = ...
DEFAULT_DIALOG_STYLE : long = ...
DEFAULT_FRAME_STYLE : long = ...
DefaultCoord : Coord = ...
EmptyString : Text = ...
EVT_CATEGORY_UI : EventCategory = ...
EVT_CATEGORY_USER_INPUT : EventCategory = ...
EVT_CATEGORY_SOCKET : EventCategory = ...
EVT_CATEGORY_TIMER : EventCategory = ...
EVT_CATEGORY_THREAD : EventCategory = ...
EVT_CATEGORY_ALL : EventCategory = ...
EXPAND : int = ...
FrameNameStr : Text = ...
FONTENCODING_CP437 : FontEncoding = ...
FONTENCODING_CP1252 : FontEncoding = ...
FONTENCODING_DEFAULT : FontEncoding = ...
FONTENCODING_ISO8859_1 : FontEncoding = ...
FONTENCODING_SYSTEM : FontEncoding = ...
FONTENCODING_UTF8 : FontEncoding = ...
FONTENCODING_UTF16 : FontEncoding = ...
FONTENCODING_UTF16BE : FontEncoding = ...
FONTENCODING_UTF16LE : FontEncoding = ...
FONTENCODING_UTF32 : FontEncoding = ...
FONTENCODING_UTF32BE : FontEncoding = ...
FONTENCODING_UTF32LE : FontEncoding = ...
FONTENCODING_UNICODE : FontEncoding = ...
FONTFAMILY_DEFAULT : FontFamily = ...
FONTFAMILY_DECORATIVE : FontFamily = ...
FONTFAMILY_ROMAN : FontFamily = ...
FONTFAMILY_SCRIPT : FontFamily = ...
FONTFAMILY_SWISS : FontFamily = ...
FONTFAMILY_MODERN : FontFamily = ...
FONTFAMILY_TELETYPE : FontFamily = ...
FONTFAMILY_MAX : FontFamily = ...
FONTFAMILY_UNKNOWN : FontFamily = ...
FONTFLAG_DEFAULT : FontFlag = ...
FONTFLAG_ITALIC : FontFlag = ...
FONTFLAG_SLANT : FontFlag = ...
FONTFLAG_LIGHT : FontFlag = ...
FONTFLAG_BOLD : FontFlag = ...
FONTFLAG_ANTIALIASED : FontFlag = ...
FONTFLAG_NOT_ANTIALIASED : FontFlag = ...
FONTFLAG_UNDERLINED : FontFlag = ...
FONTFLAG_STRIKETHROUGH : FontFlag = ...
FONTFLAG_MASK : FontFlag = ...
FONTSTYLE_NORMAL : FontStyle = ...
FONTSTYLE_ITALIC : FontStyle = ...
FONTSTYLE_SLANT : FontStyle = ...
FONTSTYLE_MAX : FontStyle = ...
FONTWEIGHT_NORMAL : FontWeight = ...
FONTWEIGHT_LIGHT : FontWeight = ...
FONTWEIGHT_BOLD : FontWeight = ...
FONTWEIGHT_MAX : FontWeight = ...
HELP : long = ...
HORIZONTAL : int = ...
HSCROLL : long = ...
ICON_AUTH_NEEDED : long = ...
ICON_ERROR : long = ...
ICON_EXCLAMATION : long = ...
ICON_HAND : long = ...
ICON_INFORMATION : long = ...
ICON_NONE : long = ...
ICON_QUESTION : long = ...
ICON_WARNING : long = ...
ID_ANY : WindowID = ...
ID_CANCEL : StandardID = ...
ID_NO : StandardID = ...
ID_OK : StandardID = ...
ID_YES : StandardID = ...
ITEM_SEPARATOR : ItemKind = ...
ITEM_NORMAL : ItemKind = ...
ITEM_CHECK : ItemKind = ...
ITEM_RADIO : ItemKind = ...
LB_SINGLE : long = ...
LC_ICON : long = ...
LC_REPORT : long = ...
LC_VIRTUAL : long = ...
LC_SINGLE_SEL : long = ...
LEFT : int = ...
LIST_AUTOSIZE_USEHEADER : int = ...
LIST_FORMAT_LEFT : long = ...
LIST_NEXT_ABOVE : int = ...
LIST_NEXT_ALL : int = ...
LIST_NEXT_BELOW : int = ...
LIST_NEXT_LEFT : int = ...
LIST_NEXT_RIGHT : int = ...
LIST_STATE_DONTCARE : int = ...
LIST_STATE_DROPHILITED : int = ...
LIST_STATE_FOCUSED : int = ...
LIST_STATE_SELECTED : int = ...
LIST_STATE_CUT : int = ...
ListCtrlNameStr : Text = ...
MAXIMIZE_BOX : long = ...
NB_BOTTOM : long = ...
NB_FIXEDWIDTH : long = ...
NB_LEFT : long = ...
NB_MULTILINE : long = ...
NB_NOPAGETHEME : long = ...
NB_RIGHT : long = ...
NB_TOP : long = ...
NO_BORDER : long = ...
NO_DEFAULT : long = ...
NOT_FOUND : int = ...
ODDEVEN_RULE : int = ...
OK : long = ...
OK_DEFAULT : long = ...
PanelNameStr : Text = ...
RESIZE_BORDER : long = ...
SearchCtrlNameStr : Text = ...
SIZE_ALLOW_MINUS_ONE : int = ...
SIZE_AUTO : int = ...
SIZE_AUTO_WIDTH : int = ...
SIZE_AUTO_HEIGHT : int = ...
SIZE_FORCE : int = ...
SIZE_USE_EXISTING : int = ...
SOLID : int = ...
STAY_ON_TOP : long = ...
STB_SIZEGRIP : long = ...
SYS_COLOUR_APPWORKSPACE : SystemColour = ...
SYS_COLOUR_BTNFACE : SystemColour = ...
SYS_COLOUR_BTNSHADOW : SystemColour = ...
SYS_COLOUR_BTNTEXT : SystemColour = ...
SYS_COLOUR_GRAYTEXT : SystemColour = ...
SYS_COLOUR_HIGHLIGHT : SystemColour = ...
SYS_COLOUR_HIGHLIGHTTEXT : SystemColour = ...
SYS_COLOUR_WINDOW : SystemColour = ...
SYS_COLOUR_WINDOWTEXT : SystemColour = ...
SYS_ANSI_FIXED_FONT : SystemFont = ...
SYS_ANSI_VAR_FONT : SystemFont = ...
SYS_DEFAULT_GUI_FONT : SystemFont = ...
SYS_DEVICE_DEFAULT_FONT : SystemFont = ...
SYS_OEM_FIXED_FONT : SystemFont = ...
SYS_SYSTEM_FONT : SystemFont = ...
TAB_TRAVERSAL : long = ...
TE_MULTILINE : long = ...
TE_PASSWORD : long = ...
TE_PROCESS_ENTER : long = ...
TE_PROCESS_TAB : long = ...
TE_READONLY : long = ...
TextCtrlNameStr : Text = ...
TextEntryDialogStyle : long = ...
TRANSPARENT : int = ...
VERTICAL : int = ...
VSCROLL : long = ...
WANTS_CHARS : long = ...
WINDING_RULE : int = ...
WXK_ADD : KeyCode = ...
WXK_BACK : KeyCode = ...
WXK_DELETE : KeyCode = ...
WXK_DOWN : KeyCode = ...
WXK_END : KeyCode = ...
WXK_ESCAPE : KeyCode = ...
WXK_F1: KeyCode = ...
WXK_F2: KeyCode = ...
WXK_F3: KeyCode = ...
WXK_F4: KeyCode = ...
WXK_F5: KeyCode = ...
WXK_F6: KeyCode = ...
WXK_F7: KeyCode = ...
WXK_F8: KeyCode = ...
WXK_F9: KeyCode = ...
WXK_F10: KeyCode = ...
WXK_F11: KeyCode = ...
WXK_F12: KeyCode = ...
WXK_HOME : KeyCode = ...
WXK_INSERT : KeyCode = ...
WXK_LEFT : KeyCode = ...
WXK_NUMPAD_ENTER : KeyCode = ...
WXK_PAGEDOWN : KeyCode = ...
WXK_PAGEUP : KeyCode = ...
WXK_RETURN : KeyCode = ...
WXK_RIGHT : KeyCode = ...
WXK_SUBTRACT : KeyCode = ...
WXK_TAB : KeyCode = ...
WXK_UP : KeyCode = ...
XOR : int = ...
YES_DEFAULT : long = ...
YES_NO : long = ...


# pre-defined objects:

DefaultPosition : Point = ...
DefaultSize : Size = ...
DefaultValidator : Validator = ...
EVT_BUTTON : PyEventBinder = ...
EVT_CHAR : PyEventBinder = ...
EVT_CHAR_HOOK : PyEventBinder = ...
EVT_CHECKBOX : PyEventBinder = ...
EVT_CLOSE : PyEventBinder = ...
EVT_COMBOBOX : PyEventBinder = ...
EVT_COMBOBOX_CLOSEUP : PyEventBinder = ...
EVT_COMBOBOX_DROPDOWN : PyEventBinder = ...
EVT_ERASE_BACKGROUND : PyEventBinder = ...
EVT_KEY_DOWN : PyEventBinder = ...
EVT_LEFT_DCLICK : PyEventBinder = ...
EVT_LEFT_DOWN : PyEventBinder = ...
EVT_LEFT_UP : PyEventBinder = ...
EVT_LIST_COL_CLICK : PyEventBinder = ...
EVT_LIST_ITEM_ACTIVATED : PyEventBinder = ...
EVT_LIST_ITEM_SELECTED : PyEventBinder = ...
EVT_MENU : PyEventBinder = ...
EVT_MIDDLE_DOWN : PyEventBinder = ...
EVT_MIDDLE_UP : PyEventBinder = ...
EVT_MOTION : PyEventBinder = ...
EVT_MOUSEWHEEL : PyEventBinder = ...
EVT_NAVIGATION_KEY : PyEventBinder = ...
EVT_NOTEBOOK_PAGE_CHANGED : PyEventBinder = ...
EVT_NOTEBOOK_PAGE_CHANGING : PyEventBinder = ...
EVT_PAINT : PyEventBinder = ...
EVT_RIGHT_DOWN : PyEventBinder = ...
EVT_RIGHT_UP : PyEventBinder = ...
EVT_SEARCHCTRL_SEARCH_BTN: PyEventBinder = ...
EVT_SCROLLWIN_BOTTOM : PyEventBinder = ...
EVT_SCROLLWIN_LINEDOWN : PyEventBinder = ...
EVT_SCROLLWIN_LINEUP : PyEventBinder = ...
EVT_SCROLLWIN_PAGEDOWN : PyEventBinder = ...
EVT_SCROLLWIN_PAGEUP : PyEventBinder = ...
EVT_SCROLLWIN_THUMBRELEASE : PyEventBinder = ...
EVT_SCROLLWIN_THUMBTRACK : PyEventBinder = ...
EVT_SCROLLWIN_TOP : PyEventBinder = ...
EVT_SET_FOCUS : PyEventBinder = ...
EVT_SIZE : PyEventBinder = ...
EVT_TEXT : PyEventBinder = ...
EVT_TEXT_ENTER : PyEventBinder = ...
EVT_TIMER : PyEventBinder = ...
EVT_TOOL : PyEventBinder = ...
EVT_TOOL_ENTER : PyEventBinder = ...
EVT_WINDOW_DESTROY : PyEventBinder = ...
NullBrush : Brush = ...
NullPen : Pen = ...
TRANSPARENT_BRUSH : Brush = ...
TRANSPARENT_PEN : Pen = ...

# functions:

def CallAfter (
	callableObj : Any, # TODO FIXME: no real way to specify type info here
	*args : Any,
	**kwargs : Any
) -> None: ...

def GetMousePosition() -> Point: ...

def GetTopLevelParent ( window : Window ) -> Optional[Window]: ...

def MessageBox (
	message : Text,
	caption : Text = ...,
	style : long = ...,
	parent : Optional[Window] = ...,
	x : Coord = ...,
	y : Coord = ...,
) -> int: ...

def PostEvent (
	dest : EvtHandler,
	event : Event,
) -> None: ...

def version() -> Text: ...

# classes:

class Object ( object ):
	pass


class WindowIDRef ( object ):
	def GetValue ( self ) -> int: ...


def NewIdRef() -> WindowIDRef: ...


class StreamBase ( object ):
	pass


class InputStream ( StreamBase ):
	pass


class OutputStream ( StreamBase ):
	pass


class Colour ( object ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		red : int,
		green : int,
		blue : int,
		alpha : int = ...,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		coIRGB : long,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		colour : Colour,
	) -> None: ...


class PyEventBinder ( object ):
	typeId : int


class SingleInstanceChecker ( object ): # TODO FIXME: sip.wrapper?
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self, name : Text, path : Text = ... ) -> None: ...
	
	def IsAnotherRunning ( self ) -> bool: ...


class DCClipper ( object ): # TODO FIXME: sip.wrapper?
	@overload
	def __init__ ( self,
		dc : DC,
		region : Region,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		dc : DC,
		rect : Rect,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		dc : DC,
		x : int,
		y : int,
		w : int,
		h : int,
	) -> None: ...
	
	def __enter__ ( self ) -> DCClipper: ...
	
	def __exit__ ( self, exc_type : Optional[Type[BaseException]], exc_val : Optional[Exception], exc_tb : Optional[TracebackType] ) -> bool: ...


class AffineMatrix2DBase ( object ):
	pass


class AffineMatrix2D ( AffineMatrix2DBase ):
	pass


class DC ( Object ):
	AsBitmap : Bitmap
	Background : BrushType
	BackgroundMode: int
	BoundingBox : Tuple[int,int,int,int]
	Brush : BrushType
	CGContext : UIntPtr
	CharHeight : Coord
	CharWidth : int
	ClippingRect : Rect
	Depth : int
	DeviceOrigin : Point
	Font : FontType
	FontMetrics : FontMetricsType
	GdkDrawable : UIntPtr
	HDC : long
	Handle : Optional[UIntPtr]
	LayoutDirection : LayoutDirectionType
	LogicalFunction : RasterOperationMode
	MapMode : MappingMode
	#MultiLineTextExtent : XXX # can't figure out how to use this
	PPI : SizeType
	Pen : PenType
	#Pixel : XXX # can't figure out how to use this
	Size : SizeType
	SizeMM : SizeType
	TextBackground : Colour
	#TextExtent : XXX
	TextForeground : Colour
	TransformMatrix : AffineMatrix2D
	
	def __enter__ ( self ) -> DC: ...
	
	def __exit__ ( self, exc_type : Optional[Type[BaseException]], exc_val : Optional[Exception], exc_tb : Optional[TracebackType] ) -> bool: ...
	
	def Clear ( self ) -> None: ...
	
	@overload
	def DrawCircle ( self,
		x : int,
		y : int,
		radius : int,
	) -> None: ...
	
	@overload
	def DrawCircle ( self,
		pt : Point,
		radius : int,
	) -> None: ...
	
	@overload
	def DrawLine ( self,
		x1 : int,
		y1 : int,
		x2 : int,
		y2 : int,
	) -> None: ...
	
	@overload
	def DrawLine ( self,
		pt1 : Point,
		pt2 : Point,
	) -> None: ...
	
	def DrawLineList ( self,
		lines : Sequence[Tuple[int,int,int,int]],
		pens : Union[None,PenType,Sequence[PenType]] = ...,
	) -> None: ...
	
	def DrawPolygon ( self,
		points: Sequence[Union[Point,Tuple[int,int]]],
		xoffset : int = ...,
		yoffset : int = ...,
		fill_style : int = ...,
	) -> None: ...
	
	@overload
	def DrawRectangle ( self,
		x : int,
		y : int,
		width : int,
		height : int,
	) -> None: ...
	
	@overload
	def DrawRectangle ( self,
		pt : Point,
		sz : SizeType,
	) -> None: ...
	
	@overload
	def DrawRectangle ( self,
		rect : Rect,
	) -> None: ...
	
	@overload
	def DrawRoundedRectangle ( self,
		x : int,
		y : int,
		width : int,
		height : int,
		radius : float,
	) -> None: ...
	
	@overload
	def DrawRoundedRectangle ( self,
		pt : Point,
		sz : SizeType,
		radius : float,
	) -> None: ...
	
	@overload
	def DrawRoundedRectangle ( self,
		rect : Rect,
		radius : float,
	) -> None: ...
	
	@overload
	def DrawText ( self,
		text : Text,
		x : int,
		y : int,
	) -> None: ...
	
	@overload
	def DrawText ( self,
		text : Text,
		pt : Point,
	) -> None: ...
	
	def GetBoundingBox ( self ) -> Tuple[int,int,int,int]: ...
	
	def GetLogicalFunction ( self ) -> RasterOperationMode: ...
	
	def GetMultiLineTextExtent ( self, st : Text ) -> SizeType: ...
	
	def GetPixel ( self, x : int, y : int ) -> Colour: ...
	
	def GetTextExtent ( self, st : Text ) -> SizeType: ...
	
	def SetBackground ( self, brush : BrushType ) -> None: ...
	
	def SetBackgroundMode ( self, mode : int ) -> None: ...
	
	def SetBrush ( self,
		brush : BrushType,
	) -> None: ...
	
	def SetFont ( self, font : FontType ) -> None: ...
	
	def SetLogicalFunction ( self,
		function : RasterOperationMode,
	) -> None: ...
	
	def SetPen ( self,
		pen : PenType,
	) -> None: ...
	
	def SetTextBackground ( self,
		colour : Colour,
	) -> None: ...
	
	def SetTextForeground ( self,
		colour : Colour,
	) -> None: ...


class WindowDC ( DC ):
	def __init__ ( self, window : Window ) -> None: ...


class ClientDC ( WindowDC ):
	def __init__ ( self, window : Window ) -> None: ...


class ScreenDC ( DC ):
	def __init__ ( self ) -> None: ...
	
	@staticmethod
	def EndDrawingOnTop() -> bool: ...
	
	@overload
	@staticmethod
	def StartDrawingOnTop ( window : Window ) -> bool: ...
	
	@overload
	@staticmethod
	def StartDrawingOnTop ( rect : Optional[Rect] = ... ) -> bool: ...


class MemoryDC ( DC ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		dc : DC,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		bitmap : Bitmap,
	) -> None: ...


class BufferedDC ( MemoryDC ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		dc : DC,
		area : Size,
		style : int = ...,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		dc : DC,
		buffer : Bitmap = ...,
		style : int = ...,
	) -> None: ...


class BufferedPaintDC ( BufferedDC ):
	@overload
	def __init__ ( self,
		window : Window,
		buffer : Bitmap,
		style : int = ...,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		window : Window,
		style : int = ...,
	) -> None: ...


class AutoBufferedPaintDC ( BufferedPaintDC ):
	def __init__ ( self,
		window : Window,
	) -> None: ...


class DCPenChanger ( object ): # TODO FIXME: sip.wrapper?
	def __init__ ( self,
		dc : DC,
		pen : Pen,
	) -> None: ...
	
	def __enter__ ( self ) -> DCPenChanger: ...
	
	def __exit__ ( self, exc_type : Optional[Type[BaseException]], exc_val : Optional[Exception], exc_tb : Optional[TracebackType] ) -> bool: ...


class DCBrushChanger ( object ): # TODO FIXME: sip.wrapper?
	def __init__ ( self,
		dc : DC,
		brush : Brush,
	) -> None: ...
	
	def __enter__ ( self ) -> DCBrushChanger: ...
	
	def __exit__ ( self, exc_type : Optional[Type[BaseException]], exc_val : Optional[Exception], exc_tb : Optional[TracebackType] ) -> bool: ...


class GDIObject ( Object ):
	def Destroy ( self ) -> None: ...


class Pen ( GDIObject ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		colour : Colour,
		width : int = ...,
		style : int = ...,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		pen : Pen,
	) -> None: ...
PenType = Pen


class Brush ( GDIObject ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		colour : Colour,
		style : BrushStyle = ...,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		stippleBitmap : Bitmap,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		brush : Brush,
	) -> None: ...
BrushType = Brush


class Cursor ( GDIObject ):
	pass
CursorType = Cursor


class FontInfo ( object ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self, pointSize : int ) -> None: ...
	
	@overload
	def __init__ ( self, pixelSize : Size ) -> None: ...
	
	def AllFlags ( self, flags : FontFlag ) -> FontInfo: ...
	
	def AntiAliased ( self, antiAliased : bool = ... ) -> FontInfo: ...
	
	def Bold ( self, bold : bool = ... ) -> FontInfo: ...
	
	def Encoding ( self, encoding : FontEncoding ) -> FontInfo: ...
	
	def FaceName ( self, faceName : Text ) -> FontInfo: ...
	
	def Family ( self, family : FontFamily ) -> FontInfo: ...
	
	def Italic ( self, italic : bool = ... ) -> FontInfo: ...
	
	def Light ( self, light : bool = ... ) -> FontInfo: ...
	
	def Slant ( self, slant : bool = ... ) -> FontInfo: ...
	
	def Strikethrough ( self, strikethrough : bool = ... ) -> FontInfo: ...
	
	def Underlined ( self, underlined : bool = ... ) -> FontInfo: ...


class NativeFontInfo ( object ): # TODO FIXME: sip.wrapper?
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self, info : NativeFontInfo ) -> None: ...
	
	def FromString ( self, s : Text ) -> bool: ...
	
	def FromUserString ( self, s : Text ) -> bool: ...
	
	def GetEncoding ( self ) -> FontEncoding: ...
	
	def GetFaceName ( self ) -> Text: ...
	
	def GetFamily ( self ) -> FontFamily: ...
	
	def GetPointSize ( self ) -> int: ...
	
	def GetStyle ( self ) -> FontStyle: ...
	
	def GetUnderlined ( self ) -> bool: ...
	
	def GetWeight ( self ) -> FontWeight: ...
	
	def Init ( self ) -> None: ...
	
	def InitFromFont ( self, font : Font ) -> None: ...
	
	def SetEncoding ( self, encoding : FontEncoding ) -> None: ...
	
	@overload
	def SetFaceName ( self, facename : Text ) -> bool: ...
	
	@overload
	def SetFaceName ( self, facenames : Sequence[Text] ) -> None: ...
	
	def SetFamily ( self, family : FontFamily ) -> None: ...
	
	def SetPointSize ( self, pointsize : int ) -> None: ...
	
	def SetStyle ( self, style : FontStyle ) -> None: ...
	
	def SetUnderlined ( self, underlined : bool ) -> None: ...
	
	def SetWeight ( self, weight : FontWeight ) -> None: ...
	
	def ToString ( self ) -> Text: ...
	
	def ToUserString ( self ) -> Text: ...
	
	def __str__ ( self ) -> str: ...


class FontMetrics ( object ):
	ascent : int
	averageWidth : int
	descent : int
	externalLeading : int
	height : int
	internalLeading : int
	
	def __init__ ( self ) -> None: ...
FontMetricsType = FontMetrics


class Font ( GDIObject ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		font : Font,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		fontInfo : FontInfo,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		pointSize : int,
		family : FontFamily,
		style : FontStyle,
		weight : FontWeight,
		underline : bool = ...,
		faceName : Text = ...,
		encoding : FontEncoding = ...,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		pixelSize : Size,
		family : FontFamily,
		style : FontStyle,
		weight : FontWeight,
		underline : bool = ...,
		faceName : Text = ...,
		encoding : FontEncoding = ...,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		nativeInfoString : Text,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		nativeInfo : NativeFontInfo,
	) -> None: ...
FontType = Font


class IconLocation ( object ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		filename : Text,
		num : int = ...,
	) -> None: ...


class Icon ( GDIObject ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		icon : Icon,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		name : Text,
		type : BitmapType = ...,
		desiredWidth : int = ...,
		desiredHeight : int = ...,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		loc : IconLocation,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		bmp : Bitmap,
	) -> None: ...


class Region ( GDIObject ):
	pass


class Bitmap ( GDIObject ):
	Depth : int
	Handle : long
	Height : int
	#Mask : Mask
	#Palette : Palette
	Size : SizeType
	Width : int
	
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		bitmap : Bitmap,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		bits : bytes,
		width: int,
		height : int,
		depth : int = ...,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		width : int,
		height : int,
		depth : int = ...,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		sz : SizeType,
		depth : int = ...,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		name : Text,
		type : BitmapType = ...,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		img : Image,
		depth : int = ...,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		listOfBytes : Sequence[bytes],
	) -> None: ...
	
	@staticmethod
	def FromBufferRGBA (
		width : int,
		height : int,
		data : Any, # TODO FIXME: no way to specify an object that supports the buffer interface in mypy
	) -> Bitmap: ...


class Image ( Object ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		width : int,
		height : int,
		clear : bool = ...,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		sz : Size,
		clear: bool = ...,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		name : Text,
		type : BitmapType = ...,
		index : int = ...,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		name : Text,
		mimetype : Text,
		index : int = ...,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		stream : InputStream,
		type : BitmapType = ...,
		index : int = ...,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		stream : InputStream,
		mimetype : Text,
		index : int = ...,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		width : int,
		height : int,
		data : bytes,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		width : int,
		height : int,
		data : bytes,
		alpha : bytes, # TODO FIXME: is this right???
	) -> None: ...
	
	@overload
	def __init__ ( self,
		size : Size,
		data : bytes,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		size : Size,
		data : bytes,
		alpha : bytes, # TODO FIXME: is this right???
	) -> None: ...
	
	def ConvertToBitmap ( self,
		depth : int = ...,
	) -> Bitmap: ...
	
	def HasAlpha ( self ) -> bool: ...
	
	def HasMask ( self ) -> bool: ...
	
	def InitAlpha ( self ) -> None: ...


class ImageList ( Object ):
	ImageCount : int
	
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		width : int,
		height : int,
		mask : bool = ...,
		initialCount : int = ...,
	) -> None: ...
	
	@overload
	def Add ( self, bitmap : Bitmap, mask : Bitmap = ... ) -> int: ...
	
	@overload
	def Add ( self, bitmap : Bitmap, maskColour : Colour ) -> int: ...
	
	@overload
	def Add ( self, icon : Icon ) -> int: ...
	
	def Create ( self,
		width : int,
		height : int,
		mask : bool = ...,
		initialCount : int = ...,
	) -> bool: ...
	
	def Draw ( self,
		index : int,
		dc : DC,
		x : int,
		y : int,
		flags : int = ...,
		solidBackground : bool = ...,
	) -> bool: ...
	
	def GetBitmap ( self, index : int ) -> Bitmap: ...
	
	def GetIcon ( self, index : int ) -> Icon: ...
	
	def GetImageCount ( self ) -> int: ...
	
	def GetSize ( self, index : int ) -> Tuple[int,int]: ...
	
	def Remove ( self, index : int ) -> bool: ...
	
	def RemoveAll ( self ) -> bool: ...
	
	@overload
	def Replace ( self, 
		index : int, 
		bitmap : Bitmap, 
		mask : Bitmap = ...,
	) -> bool: ...
	
	@overload
	def Replace ( self, index : int, icon : Icon ) -> bool: ...


class MenuBar ( Window ):
	def __init__ ( self, style : long = ... ) -> None: ...
	
	def Append ( self,
		menu : Menu,
		title : Text,
	) -> bool: ...
	
	def Attach ( self,
		frame : Frame,
	) -> bool: ...
	
	def Check ( self,
		id : int,
		check : bool,
	) -> None: ...
	
	def Detach ( self ) -> None: ...
	
	def Enable ( self, id : int, enable : bool ) -> None: ... # type: ignore
	
	def EnableTop ( self,
		pos : int,
		enable : bool,
	) -> None: ...
	
	def FindItem ( self,
		id : int,
	) -> Tuple[Any,...]: ... # TODO FIXME: test to see if we can be more specific...
	
	def FindItemById ( self,
		id : int,
	) -> MenuItem: ... # TODO FIXME: invalid id raises or returns None?
	
	def FindMenu ( self,
		title : Text,
	) -> int: ... # TODO FIXME: invalid id raises or returns None / -1?
	
	def FindMenuItem ( self,
		menuString : Text,
		itemString : Text,
	) -> int: ... # TODO FIXME: invalid id raises or returns None / -1?
	
	def GetFrame ( self ) -> Frame: ...
	
	def GetHelpString ( self,
		id : int,
	) -> Text: ... # TODO FIXME: invalid id raises or returns None / empty string?
	
	def GetLabel ( self,
		id : int,
	) -> Text: ... # TODO FIXME: invalid id raises or returns None / empty string?
	
	# def GetLabelTop # DEPRECATED
	
	def GetMenu ( self,
		menuIndex : int,
	) -> Menu: ... # TODO FIXME: invalid index raises or returns None?
	
	def GetMenuCount ( self ) -> int: ...
	
	def GetMenuLabel ( self,
		pos : int,
	) -> Text: ... # TODO FIXME: failure conditions?
	
	def GetMenuLabelText ( self,
		pos : int,
	) -> Text: ... # TODO FIXME: failure conditions?
	
	def GetMenus ( self ) -> Sequence[Tuple[Menu,Text]]: ...
	
	def Insert ( self,
		pos : int,
		menu : Menu,
		title : Text,
	) -> bool: ...
	
	def IsAttached ( self ) -> bool: ...
	
	def IsChecked ( self,
		id : int,
	) -> bool: ...
	
	def IsEnabled ( self, # type: ignore
		id : int,
	) -> bool: ...
	
	def IsEnabledTop ( self,
		pos : int,
	) -> bool: ...
	
	@staticmethod
	def MacGetCommonMenuBar() -> MenuBar: ...
	
	@staticmethod
	def MacSetCommonMenuBar (
		menubar : MenuBar,
	) -> None: ...
	
	def OSXGetAppleMenu ( self ) -> Menu: ...
	
	def Refresh ( self,
		eraseBackground : bool = ...,
		rect : Optional[Rect] = ...,
	) -> None: ...
	
	def Remove ( self,
		pos : int,
	) -> Menu: ...
	
	def Replace ( self,
		pos : int,
		menu : Menu,
		title : Text,
	) -> Menu: ...
	
	def SetHelpString ( self,
		id : int,
		helpString : Text,
	) -> None: ...
	
	def SetLabel ( self,
		id : int,
		label : Text,
	) -> None: ...
	
	# SetLabelTop - DEPRECATED
	
	def SetMenuLabel ( self,
		pos : int,
		label : Text,
	) -> None: ...
	
	def SetMenus ( self,
		items : Sequence[Tuple[Menu,Text]],
	) -> None: ...
	


class Menu ( EvtHandler ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		style : long,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		title : Text,
		style : long = ...,
	) -> None: ...
	
	@overload
	def Append ( self,
		id : int,
		item : Text = ...,
		helpString : Text = ...,
		kind : ItemKind = ...,
	) -> MenuItem: ...
	
	# the following is DEPRECATED, use AppendSubMenu() instead
	#@overload
	#def Append ( self,
	#	id : int,
	#	item : Text,
	#	subMenu : Menu,
	#	helpString : Text = ...,
	#) -> MenuItem: ...
	
	@overload
	def Append ( self,
		menuItem : MenuItem,
	) -> MenuItem: ...
	
	def AppendSubMenu ( self,
		submenu : Menu,
		text : Text,
		help : Text = ...,
	) -> MenuItem: ...
	
	def Enable ( self,
		id : int,
		enable : bool,
	) -> None: ...


class MenuItem ( Object ):
	def __init__ ( self,
		parentMenu : Optional[Menu] = ...,
		id : StandardID = ...,
		text : Text = ...,
		helpString : Text = ...,
		kind : ItemKind = ...,
		subMenu : Optional[Menu] = ...,
	) -> None: ...
	
	def Enable ( self,
		enable : bool = ...,
	) -> None: ...


class SizerItem ( Object ):
	@overload
	def __init__ ( self,
		window : Window,
		flags : SizerFlags,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		window : Window,
		proportion : int = ...,
		flag : int = ...,
		border : int = ...,
		userData : PyUserData = ...,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		sizer : Sizer,
		flags : SizerFlags,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		sizer : Sizer,
		proportion : int = ...,
		flag : int = ...,
		border : int = ...,
		userData : PyUserData = ...,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		width : int,
		height : int,
		proportion : int = ...,
		flag : int = ...,
		border : int = ...,
		userData : PyUserData = ...,
	) -> None: ...


class Sizer ( Object ):
	@overload
	def Add ( self,
		window : Window,
		flags : SizerFlags,
	) -> SizerItem: ...
	
	@overload
	def Add ( self,
		window : Window,
		proportion: int = ...,
		flag : int = ...,
		border : int = ...,
		userData : PyUserData = ...,
	) -> SizerItem: ...
	
	@overload
	def Add ( self,
		sizer : Sizer,
		flags : SizerFlags,
	) -> SizerItem: ...
	
	@overload
	def Add ( self,
		sizer : Sizer,
		proportion : int = ...,
		flag : int = ...,
		border : int = ...,
		userData : PyUserData = ...,
	) -> SizerItem: ...
	
	@overload
	def Add ( self,
		width : int,
		height : int,
		proportion : int = ...,
		flag : int = ...,
		border : int = ...,
		userData : PyUserData = ...,
	) -> SizerItem: ...
	
	@overload
	def Add ( self,
		width : int,
		height : int,
		flags : SizerFlags,
	) -> SizerItem: ...
	
	@overload
	def Add ( self, item : SizerItem ) -> SizerItem: ...
	
	@overload
	def Add ( self,
		size : Size = ...,
		proportion : int = ...,
		flag : int = ...,
		border : int = ...,
		#/Transfer/ : None = ..., # TODO FIXME: dunno how to define this one properly
	) -> SizerItem: ...
	
	@overload
	def Add ( self,
		size : Size,
		flags : int,
	) -> SizerItem: ...
SizerType = Sizer


class SizerFlags ( object ):
	def __init__ ( self,
		proportion : int = ...,
	) -> None: ...


class BoxSizer ( Sizer ):
	def __init__ ( self,
		orient : int = ...,
	) -> None: ...


class GridSizer ( Sizer ):
	pass


class FlexGridSizer ( GridSizer ):
	@overload
	def __init__ ( self, cols : int, vgap : int, hgap : int ) -> None: ...
	
	@overload
	def __init__ ( self, cols : int, gap : Size = ... ) -> None: ...
	
	@overload
	def __init__ ( self,
		rows : int,
		cols : int,
		vgap : int,
		hgap : int,
	) -> None: ...
	
	@overload
	def __init__ ( self, rows : int, cols : int, gap : Size ) -> None: ...
	
	def AddGrowableCol ( self, idx : int, proportion : int = ... ) -> None: ...
	
	def AddGrowableRow ( self, idx : int, proportion : int = ... ) -> None: ...


class Point ( object ):
	x : int
	y : int
	
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self, x : int, y : int ) -> None: ...
	
	@overload
	def __init__ ( self, pt : Point ) -> None: ...
	
	@overload
	def __getitem__ ( self, idx : int ) -> int: ...
	
	@overload
	def __getitem__ ( self, idx : slice ) -> Sequence[int]: ...
	
	def __iter__ ( self ) -> Iterator[int]: ... # it doesn't really have an __iter__ but mypy is confused
	
	def __len__ ( self ) -> int: ...
PointType = Point


class Size ( object ):
	Height : int
	Width : int
	height : int
	width : int
	x : int
	y : int
	
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self, width : int, height : int ) -> None: ...
	
	@overload
	def __getitem__ ( self, idx : int ) -> int: ...
	
	@overload
	def __getitem__ ( self, idx : slice ) -> Sequence[int]: ...
	
	def __iter__ ( self ) -> Iterator[int]: ... # it doesn't really have an __iter__ but mypy is confused
	
	def __len__ ( self ) -> int: ...
	
	def GetHeight ( self ) -> int: ...
	
	def GetWidth ( self ) -> int: ...
SizeType = Size


class Rect ( object ):
	Bottom : int
	BottomLeft : Point
	BottomRight : Point
	Height : int
	Left : int
	Position : Point
	Right : int
	Size : SizeType
	Top : int
	TopLeft : Point
	TopRight : Point
	Width : int
	X : int
	Y : int
	bottom : int
	bottomLeft : Point
	bottomRight : Point
	height : int
	left : int
	right : int
	top : int
	topLeft : Point
	topRight : Point
	width : int
	x : int
	y : int
	
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		x : int,
		y : int,
		width : int,
		height : int,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		pos : Point,
		size : SizeType,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		size: SizeType,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		topLeft : Point,
		bottomRight : Point,
	) -> None: ...
	
	@overload
	def __getitem__ ( self, idx : int ) -> int: ...
	
	@overload
	def __getitem__ ( self, idx : slice ) -> Sequence[int]: ...
	
	def __iter__ ( self ) -> Iterator[int]: ... # it doesn't really have an __iter__ but mypy is confused
	
	def __len__ ( self ) -> int: ...
RectType = Rect


class TimeSpan ( object ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		hours : int,
		min : int = ...,
		sec : int = ...,
		msec : int = ...,
	) -> None: ...
	
	# Abs	Returns the absolute value of the timespan: does not modify the object.
	# Add	Adds the given wx.TimeSpan to this wx.TimeSpan and returns a reference to itself.
	# Day	Returns the timespan for one day.
	
	@staticmethod
	def Days ( days : long ) -> TimeSpan: ... # Returns the timespan for the given number of days.
	
	def Format ( self,
		format : Text = ...,
	) -> Text: ... # Returns the string containing the formatted representation of the time span.
	
	def GetDays ( self ) -> int: ... # Returns the difference in number of days.
	def GetHours ( self ) -> int: ... # Returns the difference in number of hours.
	def GetMilliseconds ( self ) -> long: ... # Returns the difference in number of milliseconds.
	def GetMinutes ( self ) -> int: ... # Returns the difference in number of minutes.
	def GetSeconds ( self ) -> long: ... # Returns the difference in number of seconds.
	
	# GetValue	Returns the internal representation of timespan.
	# GetWeeks	Returns the difference in number of weeks.
	# Hour	Returns the timespan for one hour.
	
	@staticmethod
	def Hours ( hours : long ) -> TimeSpan: ... # Returns the timespan for the given number of hours.
	
	# IsEqualTo	Returns True if two timespans are equal.
	# IsLongerThan	Compares two timespans: works with the absolute values, i.e. -2 hours is longer than 1 hour.
	# IsNegative	Returns True if the timespan is negative.
	# IsNull	Returns True if the timespan is empty.
	# IsPositive	Returns True if the timespan is positive.
	# IsShorterThan	Compares two timespans: works with the absolute values, i.e. 1 hour is shorter than -2 hours.
	# Millisecond	Returns the timespan for one millisecond.
	
	@staticmethod
	def Milliseconds ( ms : long ) -> TimeSpan: ... # Returns the timespan for the given number of milliseconds.
	
	# Minute	Returns the timespan for one minute.
	
	@staticmethod
	def Minutes ( min : long ) -> TimeSpan: ... # Returns the timespan for the given number of minutes.
	
	# Multiply	Multiplies this time span by n.
	# Neg	Negate the value of the timespan.
	# Negate	Returns timespan with inverted sign.
	# Second	Returns the timespan for one second.
	
	@staticmethod
	def Seconds ( sec : long ) -> TimeSpan: ... # Returns the timespan for the given number of seconds.
	
	# Subtract	Subtracts the given wx.TimeSpan to this wx.TimeSpan and returns a reference to itself.
	# Week	Returns the timespan for one week.
	
	@staticmethod
	def Weeks ( weeks : long ) -> TimeSpan: ... # Returns the timespan for the given number of weeks.


class DateTime ( object ):
	DayOfYear : int
	JDN : float
	JulianDayNumber : float
	LastMonthDay : DateTime
	MJD : float
	ModifiedJulianDayNumber : float
	RataDie : float
	Ticks : int
	WeekOfMonth : int
	WeekOfYear : int
	day : int
	hour : int
	millisecond : int
	minute : int
	month : int
	second : int
	year : int
	
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		date : DateTime,
	) -> None: ...
	
	@overload
	def __init__ ( self,
		day : int,
		month : int,
		year : int = ...,
		hour : int = ...,
		minute : int = ...,
		second : int = ...,
		millisec : int = ...,
	) -> None: ...


class EventFilter ( object ):
	def __init__ ( self ) -> None: ...
	
	def FilterEvent ( self, event : Event ) -> int: ...


class AppConsole ( EventFilter, EvtHandler ):
	pass


class App ( AppConsole ):
	def __init__ ( self,
		redirect : bool = ...,
		filename : Text = ...,
		useBestVirtual : bool = ...,
		clearSigInt : bool = ...
	) -> None: ...
	
	def ExitMainLoop ( self ) -> None: ...
	
	def MainLoop ( self ) -> None: ...
	
	def SetTopWindow ( self, frame : Frame ) -> None: ...


class Trackable ( object ):
	pass


__EvtHandlerSource = Union[Menu,MenuItem,Timer,Window]
class EvtHandler ( Trackable, Object ):
	def Bind ( self,
		event : PyEventBinder,
		handler : Any, # TODO FIXME: Callable[[Event],None] doesn't work... :(
		source : Optional[__EvtHandlerSource] = ...,
		id : WindowID = ...,
		id2 : WindowID = ...,
	) -> None: ...
	
	def Unbind ( self,
		event : PyEventBinder,
		source : Optional[__EvtHandlerSource] = ...,
		id : WindowID = ...,
		id2 : WindowID = ...,
		handler : Any = ...,
	) -> bool: ...


class Validator ( EvtHandler ):
	pass
ValidatorType = Validator


class Timer ( EvtHandler ):
	Id : int
	Interval : int
	Owner : EvtHandler
	
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		owner : EvtHandler,
		id : int = ...,
	) -> None: ...
	
	def GetId ( self ) -> int: ...
	
	def GetInterval ( self ) -> int: ...
	
	def GetOwner ( self ) -> EvtHandler: ...
	
	def IsOneShot ( self ) -> bool: ...
	
	def IsRunning ( self ) -> bool: ...
	
	def Notify ( self ) -> None: ...
	
	def SetOwner ( self,
		owner : EvtHandler,
		id : int = ...,
	) -> None: ...
	
	def Start ( self,
		milliseconds : int = ...,
		oneShot : bool = ...
	) -> bool: ...
	
	def StartOnce ( self,
		milliseconds : int = ...,
	) -> bool: ...
	
	def Stop ( self ) -> None: ...


class Caret ( object ):
	pass
CaretType = Caret


class VisualAttributes ( object ):
	pass


class DropTarget ( object ):
	pass
DropTargetType = DropTarget


class LayoutConstraints ( Object ):
	pass


class ToolTip ( Object ):
	pass
ToolTipType = ToolTip


class WindowBase ( EvtHandler ):
	def AddChild ( self, child : WindowBase ) -> None: ...
	
	def RemoveChild ( self, child : WindowBase ) -> None: ...


class Window ( WindowBase ):
	AcceleratorTable : AcceleratorTableType
	AutoLayout : bool
	BackgroundColour : Colour
	BackgroundStyle : BackgroundStyleType
	BestSize : SizeType
	BestVirtualSize : SizeType
	Border : BorderType
	Caret : CaretType
	CharHeight : int
	CharWidth : int
	Children : Sequence[Window]
	ClassName : Text
	ClientAreaOrigin : Point
	ClientRect : RectType
	ClientSize : SizeType
	Constraints : LayoutConstraints
	ContainingSizer : Sizer
	Cursor : CursorType
	DefaultAttributes : VisualAttributes
	DropTarget : DropTargetType
	EffectiveMinSize : SizeType
	Enabled : bool
	EventHandler : EvtHandler
	ExtraStyle : long
	Font : FontType
	ForegroundColour : Colour
	GrandParent : Optional[Window]
	Handle : Optional[UIntPtr]
	HelpText : Text
	Id : WindowID
	Label : Text
	LayoutDirection : LayoutDirectionType
	MaxClientSize : SizeType
	MaxHeight : int
	MaxSize : SizeType
	MaxWidth : int
	MinClientSize : SizeType
	MinHeight : int
	MinSize : SizeType
	MinWidth : int
	Name : Text
	Parent : Optional[Window]
	Position : Point
	Rect : RectType
	ScreenPosition : Point
	ScreenRect : RectType
	Shown : bool
	Size : SizeType
	Sizer : SizerType
	ThemeEnabled : bool
	ToolTip : ToolTipType
	TopLevel : bool
	TopLevelParent : Optional[Window]
	UpdateClientRect : RectType
	UpdateRegion : Region
	Validator : ValidatorType
	VirtualSize : SizeType
	WindowStyle : long
	WindowStyleFlag : long
	WindowVariant : WindowVariantType
	
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		parent : Optional[Window],
		id : WindowID = ...,
		pos : Point = ...,
		size : SizeType = ...,
		style : long = ...,
		name : Text = ...,
	) -> None: ...
	
	def CaptureMouse ( self ) -> None: ...
	
	def Center ( self, dir : int = ... ) -> None: ...
	
	def CenterOnParent ( self, dir : int = ... ) -> None: ...
	
	def Centre ( self, dir : int = ... ) -> None: ...
	
	def CentreOnParent ( self, dir : int = ... ) -> None: ...
	
	def Close ( self, force : bool = ... ) -> bool: ...
	
	def Destroy ( self ) -> bool: ...
	
	def DestroyLater ( self ) -> None: ...
	
	def Disable ( self ) -> bool: ...
	
	def Enable ( self,
		enable : bool = ...,
	) -> bool: ...
	
	def Fit ( self ) -> None: ...
	
	def Freeze ( self ) -> None: ...
	
	def GetClientRect ( self ) -> RectType: ...
	
	def GetFont ( self ) -> FontType: ...
	
	def GetId ( self ) -> WindowID: ...
	
	def GetParent ( self ) -> Optional[Window]: ...
	
	def GetPosition ( self ) -> Point: ...
	
	def GetRect ( self ) -> RectType: ...
	
	def GetScrollPos ( self,
		orientation : int,
	) -> int: ...
	
	def GetScrollRange ( self,
		orientation : int,
	) -> int: ...
	
	def GetScrollThumb ( self,
		orientation : int,
	) -> int: ...
	
	def GetSize ( self ) -> SizeType: ...
	
	def GetVirtualSize ( self ) -> SizeType: ...
	
	def HandleAsNavigationKey ( self,
		event : KeyEvent,
	) -> bool: ...
	
	def Hide ( self ) -> bool: ...
	
	def IsEnabled ( self ) -> bool: ...
	
	def IsFrozen ( self ) -> bool: ...
	
	def Layout ( self ) -> bool: ...
	
	def Navigate ( self,
		flags : int = ...,
	) -> bool: ...
	
	@overload
	def PopupMenu ( self,
		menu : Menu,
		pos : Point = ...,
	) -> bool: ...
	
	@overload
	def PopupMenu ( self,
		menu : Menu,
		x : int,
		y : int,
	) -> bool: ...
	
	def Refresh ( self,
		eraseBackground : bool = ...,
		rect : Optional[RectType] = ...,
	) -> None: ...
	
	def ReleaseMouse ( self ) -> None: ...
	
	@overload
	def ScreenToClient ( self,
		x : int,
		y : int,
	) -> Tuple[int,int]: ...
	
	@overload
	def ScreenToClient ( self,
		pt : Point,
	) -> Point: ...
	
	def SetAcceleratorTable ( self,
		accel : AcceleratorTableType,
	) -> None: ...
	
	def SetAutoLayout ( self,
		autoLayout : bool,
	) -> None: ...
	
	def SetBackgroundColour ( self, colour : Colour ) -> bool: ...
	
	def SetBackgroundStyle ( self,
		style : BackgroundStyleType,
	) -> bool: ...
	
	def SetFocus ( self ) -> None: ...
	
	def SetFont ( self,
		font : FontType,
	) -> bool: ...
	
	def SetForegroundColour ( self, colour : Colour ) -> bool: ...
	
	def SetPosition ( self, pt : Point ) -> None: ...
	
	def SetRect ( self,
		rect : RectType,
	) -> None: ...
	
	def SetScrollbar ( self,
		orientation : int,
		position : int,
		thumbSize : int,
		range : int,
		refresh : bool = ...,
	) -> None: ...
	
	def SetScrollPos ( self,
		orientation : int,
		pos : int,
		refresh : bool = ...,
	) -> int: ...
	
	@overload
	def SetSize ( self,
		x : int,
		y : int,
		width : int,
		height : int,
		sizeFlags : int = ..., # SIZE_AUTO_WIDTH|SIZE_AUTO_HEIGHT|SIZE_AUTO|SIZE_USE_EXISTING|SIZE_ALLOW_MINUS_ONE|SIZE_FORCE
	) -> None: ...
	
	@overload
	def SetSize ( self,
		rect : RectType,
	) -> None: ...
	
	@overload
	def SetSize ( self,
		size : SizeType,
	) -> None: ...
	
	@overload
	def SetSize ( self,
		width : int,
		height : int,
	) -> None: ...
	
	def SetSizer ( self,
		sizer : SizerType,
		deleteOld : bool = ...,
	) -> None: ...
	
	def SetSizerAndFit ( self,
		sizer : SizerType,
		deleteOld : bool = ...,
	) -> None: ...
	
	@overload
	def SetVirtualSize ( self,
		width : int,
		height : int,
	) -> None: ...
	
	@overload
	def SetVirtualSize ( self,
		size : SizeType,
	) -> None: ...
	
	def Show ( self,
		show : bool = ...,
	) -> bool: ...
	
	def Thaw ( self ) -> None: ...
	
	def TransferDataFromWindow ( self ) -> bool: ...
	
	def TransferDataToWindow ( self ) -> bool: ...
	
	def Update ( self ) -> None: ...
	
	def Validate ( self ) -> bool: ...
WindowType = Window


class NonOwnedWindow ( Window ):
	pass


class TopLevelWindow ( NonOwnedWindow ):
	def GetTitle ( self ) -> Text: ...
	
	def Maximize ( self,
		maximize : bool = ...,
	) -> None: ...
	
	def SetIcon ( self,
		icon : Icon,
	) -> None: ...
	
	def SetTitle ( self, title : Text ) -> None: ...


class Frame ( TopLevelWindow ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		parent : Optional[Window] = ...,
		id : WindowID = ...,
		title : Text = ...,
		pos : Point = ...,
		size : Size = ...,
		style : long = ...,
		name : Text = ...,
	) -> None: ...
	
	def SetMenuBar ( self,
		menuBar : MenuBar,
	) -> None: ...


class Dialog ( TopLevelWindow ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		parent : Optional[Window],
		id : WindowID = ...,
		title : Text = ...,
		pos : Point = ...,
		size : Size = ...,
		style : long = ...,
		name : Text = ...,
	) -> None: ...
	
	def CreateButtonSizer ( self,
		flags : long,
	) -> Sizer: ...
	
	def EndModal ( self,
		retCode : int,
	) -> None: ...
	
	def IsModal ( self ) -> bool: ...
	
	def SetReturnCode ( self,
		retCode : int,
	) -> None: ...
	
	def ShowModal ( self ) -> int: ...


class MessageDialog ( Dialog ):
	def __init__ ( self,
		parent : Optional[Window],
		message : Text,
		caption : Text = ...,
		style : long = ...,
		pos : Point = ...,
	) -> None: ...
	
	def SetYesNoLabels ( self, yes : Text, no : Text ) -> bool: ...


class TextEntryDialog ( Dialog ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		parent : Optional[Window],
		message : Text,
		caption : Text = ...,
		value : Text = ...,
		style : long = ...,
		pos : Point = ...,
	) -> None: ...
	
	def GetValue ( self ) -> Text: ...
	
	def SetMaxLength ( self,
		len : long,
	) -> None: ...
	
	def SetValue ( self,
		value : Text,
	) -> None: ...
	
	def ShowModal ( self ) -> int: ...


class Panel ( Window ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		parent : Window,
		id : WindowID = ...,
		pos : Point = ...,
		size : Size = ...,
		style : long = ...,
		name : Text = ...,
	) -> None: ...


class SplitterWindow ( Window ):
	SashPosition : int
	
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		parent : Window,
		id : WindowID = ...,
		pos : Point = ...,
		size : Size = ...,
		style : long = ...,
		name : Text = ...,
	) -> None: ...
	
	def SplitHorizontally ( self,
		window1 : Window,
		window2 : Window,
		sashPosition : int = ...,
	) -> bool: ...
	
	def SplitVertically ( self,
		window1 : Window,
		window2 : Window,
		sashPosition : int = ...,
	) -> bool: ...
	
	def Unsplit ( self, toRemove : Optional[Window] = ... ) -> bool: ...


class Scrolled ( object ):
	# AdjustScrollbars
	
	@overload
	def CalcScrolledPosition ( self, x : int, y : int ) -> Point: ...
	
	@overload
	def CalcScrolledPosition ( self, pt : Point ) -> Point: ...
	
	@overload
	def CalcUnscrolledPosition ( self, x : int, y : int ) -> Point: ...
	
	@overload
	def CalcUnscrolledPosition ( self, pt : Point ) -> Point: ...
	
	# Create
	# DisableKeyboardScrolling
	
	def DoPrepareDC ( self, dc : DC ) -> None: ...
	
	# EnableScrolling
	# GetScaleX
	# GetScaleY
	# GetScrollLines
	# GetScrollPageSize
	
	def GetScrollPixelsPerUnit ( self ) -> Tuple[int,int]: ...
	
	# GetSizeAvailableForScrollTarget
	# GetTargetRect
	# GetTargetWindow
	
	def GetViewStart ( self ) -> Tuple[int,int]: ...
	
	# IsAutoScrolling
	# IsRetained
	
	def OnDraw ( self, dc : DC ) -> None: ...
	
	# PrepareDC
	
	@overload
	def Scroll ( self, x : int, y : int ) -> None: ...
	
	@overload
	def Scroll ( self, pt : Point ) -> None: ...
	
	# SendAutoScrollEvents
	# SetScale
	# SetScrollPageSize
	
	def SetScrollRate ( self, xstep : int, ystep : int ) -> None: ...
	
	# SetScrollbars
	# SetTargetRect
	# SetTargetWindow
	# ShowScrollbars
	# StopAutoScrolling


class ScrolledPanel ( Scrolled, Panel ):
	pass

ScrolledWindow = ScrolledPanel


class ScrolledCanvas ( Window, Scrolled ):
	pass


class ItemContainerImmutable ( object ):
	def FindString ( self,
		string : Text,
		caseSensitive : bool = ...,
	) -> int: ...
	
	def GetCount ( self ) -> int: ...
	
	def GetSelection ( self ) -> int: ...
	
	def GetString ( self,
		n : int,
	) -> Text: ...
	
	def GetStringSelection ( self ) -> Text: ...
	
	def GetStrings ( self ) -> Sequence[Text]: ...
	
	def IsEmpty ( self ) -> bool: ...
	
	def Select ( self,
		n : int,
	) -> None: ...
	
	@overload
	def SetSelection ( self,
		n : int,
	) -> None: ...
	
	@overload
	def SetSelection ( self,
		from_ : long,
		to_ : long,
	) -> None: ...
	
	def SetString ( self,
		n : int,
		string : Text,
	) -> None: ...
	
	def SetStringSelection ( self,
		string : Text,
	) -> bool: ...


class ItemContainer ( ItemContainerImmutable ):
	@overload
	def Append ( self, item : Text ) -> int: ...
	
	@overload
	def Append ( self,
		item : Text,
		clientData : ClientData,
	) -> int: ...
	
	@overload
	def Append ( self,
		items : Sequence[Text],
	) -> int: ...
	
	def AppendItems ( self,
		items : Sequence[Text],
	) -> None: ...
	
	def Clear ( self ) -> None: ...
	
	def Delete ( self,
		n : int,
	) -> None: ...
	
	def DetachClientObject ( self,
		n : int,
	) -> ClientData: ...
	
	def GetClientData ( self,
		n : int,
	) -> ClientData: ...
	
	def GetClientObject ( self,
		n : int,
	) -> ClientData: ...
	
	def GetItems ( self ) -> Sequence[Text]: ...
	
	def HasClientData ( self ) -> bool: ...
	
	def HasClientObjectData ( self ) -> bool: ...
	
	def HasClientUntypedData ( self ) -> bool: ...
	
	@overload
	def Insert ( self,
		item : Text,
		pos : int,
	) -> int: ...
	
	@overload
	def Insert ( self,
		item : Text,
		pos : int,
		clientData : ClientData,
	) -> int: ...
	
	@overload
	def Insert ( self,
		items: Sequence[Text],
		pos : int,
	) -> int: ...
	
	def Set ( self,
		items : Sequence[Text],
	) -> None: ...
	
	def SetClientData ( self,
		n : int,
		data : ClientData,
	) -> None: ...
	
	def SetClientObject ( self,
		n : int,
		data : ClientData,
	) -> None: ...
	
	def SetItems ( self,
		items : Sequence[Text],
	) -> None: ...
	

class Control ( Window ):
	def SetLabel ( self, label : Text ) -> None: ...


class StaticText ( Control ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		parent : Window,
		id : WindowID = ...,
		label : Text = ...,
		pos : Point = ...,
		size : Size = ...,
		style : long = ...,
		name : Text = ...,
	) -> None: ...


class TextEntry ( object ):
	def AppendText ( self, text : Text ) -> None: ...
	
	#@overload
	def AutoComplete ( self, choices : Sequence[Text] ) -> bool: ...
	
	#@overload
	#def AutoComplete ( self, completer : TextCompleter ) -> bool: ... # commented out because not pure python and not (currently) Linux
	
	def AutoCompleteDirectories ( self ) -> bool: ...
	
	def AutoCompleteFileNames ( self ) -> bool: ...
	
	def CanCopy ( self ) -> bool: ...
	
	def CanCut ( self ) -> bool: ...
	
	def CanPaste ( self ) -> bool: ...
	
	def CanRedo ( self ) -> bool: ...
	
	def CanUndo ( self ) -> bool: ...
	
	def ChangeValue ( self, value : Text ) -> None: ...
	
	def Clear ( self ) -> None: ...
	
	def Copy ( self ) -> None: ...
	
	def Cut ( self ) -> None: ...
	
	def GetHint ( self ) -> Text: ...
	
	def GetInsertionPoint ( self ) -> long: ...
	
	def GetLastPosition ( self ) -> TextPos: ...
	
	def GetMargins ( self ) -> Point: ...
	
	def GetRange ( self, from_ : long, to_ : long ) -> Text: ...
	
	def GetSelection ( self ) -> Tuple[int,int]: ...
	
	def GetStringSelection ( self ) -> Text: ...
	
	def GetValue ( self ) -> Text: ...
	
	def IsEditable ( self ) -> bool: ...
	
	def IsEmpty ( self ) -> bool: ...
	
	def Paste ( self ) -> None: ...
	
	def Redo ( self ) -> None: ...
	
	def Remove ( self, from_ : long, to_ : long ) -> None: ...
	
	def Replace ( self, from_ : long, to_ : long, value : Text ) -> None: ...
	
	def SelectAll ( self ) -> None: ...
	
	def SelectNone ( self ) -> None: ...
	
	def SetEditable ( self, editable : bool ) -> None: ...
	
	def SetHint ( self, hint : Text ) -> bool: ...
	
	def SetInsertionPoint ( self, pos : long ) -> None: ...
	
	def SetInsertionPointEnd ( self ) -> None: ...
	
	@overload
	def SetMargins ( self, pt : Point ) -> bool: ...
	
	@overload
	def SetMargins ( self, left : int, top : int = ... ) -> bool: ...
	
	def SetMaxLength ( self, len : long ) -> None: ...
	
	def SetSelection ( self, from_: long, to_ : long ) -> None: ...
	
	def SetValue ( self, value : Text ) -> None: ...
	
	def Undo ( self ) -> None: ...
	
	def WriteText ( self, text : Text ) -> None: ...


class TextCtrl ( TextEntry, Control ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		parent : Window,
		id : WindowID = ...,
		value : Text = ...,
		pos : Point = ...,
		size : Size = ...,
		style : long = ...,
		validator : Validator = ...,
		name : Text = ...,
	) -> None: ...


class SearchCtrl ( TextCtrl ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		parent : Window,
		id : WindowID = ...,
		value : Text = ...,
		pos : Point = ...,
		size : Size = ...,
		style : long = ...,
		validator : Validator = ...,
		name : Text = ...,
	) -> None: ...


class ListBox ( Control, ItemContainer ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		parent : Window,
		id : WindowID = ...,
		pos : Point = ...,
		size : Size = ...,
		choices : Sequence[Text] = ...,
		style : long = ...,
		validator : Validator = ...,
		name : Text = ...,
	) -> None: ...
	
	@overload
	def SetFirstItem ( self, n : int ) -> None: ...
	
	@overload
	def SetFirstItem ( self, string : Text ) -> None: ...


class ListItem ( Object ):
	pass


class ListCtrl ( Control ):
	#Column : ListItem
	ColumnCount : int
	ColumnsOrder : Sequence[int]
	CountPerPage : int
	EditControl : Optional[TextCtrl]
	FocusedItem : int
	#Item : XXX
	ItemCount : int
	#ItemPosition : XXX
	#ItemRect : XXX
	#ItemSpacing : XXX
	MainWindow : Window
	SelectedItemCount : int
	TextColour : Colour
	TopItem : long
	ViewRect : Rect
	
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		parent : Window,
		id : WindowID = ...,
		pos : Point = ...,
		size : Size = ...,
		style : long = ...,
		validator : Validator = ...,
		name : Text = ...,
	) -> None: ...
	
	def Append ( self,
		entry : Sequence[Text],
	) -> int: ...
	
	def DeleteAllItems ( self ) -> None: ...
	
	def EnsureVisible ( self,
		item : long,
	) -> bool: ...
	
	def Focus ( self,
		idx : int,
	) -> None: ...
	
	def GetColumn ( self, col : int ) -> ListItem: ...
	
	def GetColumnCount ( self ) -> int: ...
	
	def GetColumnOrder ( self, col : int ) -> int: ...
	
	def GetCountPerPage ( self ) -> int: ...
	
	def GetFirstSelected ( self ) -> int: ...
	
	def GetFocusedItem ( self ) -> int: ...
	
	def GetItem ( self, itemIdx : int, col : int = ... ) -> ListItem: ...
	
	def GetItemBackgroundColour ( self, item : long ) -> Colour: ...
	
	def GetItemCount ( self ) -> int: ...
	
	def GetItemData ( self, item : long ) -> long: ...
	
	def GetItemFont ( self, item : long ) -> Font: ...
	
	def GetItemPosition ( self, item : long ) -> Point: ...
	
	def GetItemRect ( self, item : long, code : int = ... ) -> Rect: ...
	
	def GetItemSpacing ( self ) -> Size: ...
	
	def GetItemState ( self, item : long, stateMask : long ) -> int: ...
	
	def GetItemText ( self, item : long ) -> Text: ...
	
	def GetItemTextColour ( self, item : long ) -> Colour: ...
	
	def GetMainWindow ( self ) -> Window: ...
	
	def GetNextItem ( self,
		item : long,
		geometry : int = ...,
		state : int  = ...,
	) -> long: ...
	
	def GetSelectedItemCount ( self ) -> int: ...
	
	def GetSubItemRect ( self,
		item : long,
		subitem : long,
		rect : Rect,
		code : int = ...,
	) -> bool: ...
	
	def GetTextColour ( self ) -> Colour: ...
	
	def GetTopItem ( self ) -> long: ...
	
	def GetViewRect ( self ) -> Rect: ...
	
	def HasColumnOrderSupport ( self ) -> bool: ...
	
	def HitTest ( self, point : Point ) -> Tuple[long,int]: ...
	
	def HitTestSubItem ( self, point : Point ) -> Tuple[long,int,long]: ...
	
	def InReportView ( self ) -> bool: ...
	
	@overload
	def InsertColumn ( self,
		col : long,
		info : ListItem,
	) -> long: ...
	
	@overload
	def InsertColumn ( self,
		col : long,
		heading : Text,
		format : int = ...,
		width : int = ...,
	) -> long: ...
	
	@overload
	def InsertItem ( self, info : ListItem ) -> long: ...
	
	@overload
	def InsertItem ( self, index : long, label : Text ) -> long: ...
	
	@overload
	def InsertItem ( self, index : long, imageIndex : int ) -> long: ...
	
	@overload
	def InsertItem ( self,
		index : long,
		label : Text,
		imageIndex : int,
	) -> long: ...
	
	def IsSelected ( self, idx : long ) -> bool: ...
	
	def IsVirtual ( self ) -> bool: ...
	
	def OnGetItemAttr ( self, item : long ) -> long: ...
	
	def OnGetItemColumnImage ( self, item : long, column : long ) -> int: ...
	
	def OnGetItemImage ( self, item : long ) -> int: ...
	
	def OnGetItemText ( self, item : long, column : long ) -> Text: ...
	
	def RefreshItem ( self, item : long ) -> None: ...
	
	def RefreshItems ( self,
		itemFrom : long,
		itemTo : long,
	) -> None: ...
	
	def ScrollList ( self, dx : int, dy : int ) -> bool: ...
	
	def Select ( self, idx : int, on : bool = ... ) -> None: ...
	
	def SetAlternateRowColour ( self, colour : Colour ) -> None: ...
	
	def SetBackgroundColour ( self, col : Colour ) -> bool: ...
	
	def SetColumn ( self, col : int, item : ListItem ) -> bool: ...
	
	def SetColumnImage ( self, col : int, image : Image ) -> None: ...
	
	def SetColumnWidth ( self, col : long, width : int ) -> bool: ...
	
	def SetColumnsOrder ( self, orders : Sequence[int] ) -> bool: ...
	
	def SetImageList ( self, imageList : ImageList, which : int ) -> None: ...
	
	@overload
	def SetItem ( self, info : ListItem ) -> bool: ...
	
	@overload
	def SetItem ( self,
		index : long,
		column : int,
		label : Text,
		imageId : int = ...,
	) -> long: ...
	
	def SetItemBackgroundColour ( self, item : long, col : Colour ) -> None: ...
	
	def SetItemColumnImage ( self,
		item : long,
		column : long,
		image : int,
	) -> bool: ...
	
	def SetItemCount ( self,
		count : long,
	) -> None: ...
	
	def SetItemData ( self, item : long, data : long ) -> bool: ...
	
	def SetItemFont ( self, item : long, font : Font ) -> None: ...
	
	def SetItemImage ( self, item : long, image : int, selImage : int ) -> bool: ...
	
	def SetItemPosition ( self, imte : long, pos : Point ) -> bool: ...
	
	def SetItemState ( self, item : long, state : long, stateMask : long ) -> bool: ...
	
	def SetItemText ( self, item : long, text : Text ) -> None: ...
	
	def SetItemTextColour ( self, item : long, col : Colour ) -> None: ...
	
	def SetSingleStyle ( self, style : long, add : bool ) -> None: ...
	
	def SetTextColour ( self, col : Colour ) -> None: ...
	
	def SetWindowStyleFlag ( self, style : long ) -> None: ...
	
	def SortItems ( self, fnSortCallBack : Callable[[long,long],int] ) -> bool: ...


class ListView ( ListCtrl ):
	FirstSelected : long
	FocusedItem : long
	
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		parent : Window,
		winid : WindowID = ...,
		pos : Point = ...,
		size : Size = ...,
		style : long = ...,
		validator : Validator = ...,
		name : Text = ...,
	) -> None: ...
	
	def ClearColumnImage ( self, col : int ) -> None: ...
	
	def Focus ( self, index : long ) -> None: ...
	
	def GetFirstSelected ( self ) -> long: ...
	
	def GetFocusedItem ( self ) -> long: ...
	
	def GetNextSelected ( self, item : long ) -> long: ...
	
	def IsSelected ( self, index : long ) -> bool: ...
	
	def Select ( self, n : long, on : bool ) -> None: ... # type: ignore # ( signature incompatible with supertype ListCtrl )
	
	def SetColumnImage ( self, col : int, image : int ) -> None: ... # type: ignore # ( signature incompatible with supertype ListCtrl )


class ComboBox ( ItemContainer, TextEntry, Control ): # type: ignore
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		parent : Window,
		id : WindowID = ...,
		value : Text = ...,
		pos : Point = ...,
		size : Size = ...,
		choices : Sequence[Text] = ...,
		style : long = ...,
		validator : Validator = ...,
		name : Text = ...,
	) -> None: ...
	
	def GetCurrentSelection ( self ) -> int: ...
	
	def Popup ( self ) -> None: ...


class AnyButton ( Control ):
	pass


class Button ( AnyButton ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		parent : Window,
		id : WindowID = ...,
		label : Text = ...,
		pos : Point = ...,
		size : Size = ...,
		style : long = ...,
		validator : Validator = ...,
		name : Text = ...,
	) -> None: ...


class SpinButton ( Control ):
	pass


class CheckBox ( Control ):
	ThreeStateValue : int
	Value : bool
	
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		parent : Window,
		id : WindowID = ...,
		label : Text = ...,
		pos : Point = ...,
		size : Size = ...,
		style : long = ...,
		validator : Validator = ...,
		name : Text = ...,
	) -> None: ...
	
	def GetValue ( self ) -> bool: ...
	
	def SetValue ( self, state : bool ) -> None: ...


class ToolBarToolBase ( Object ):
	pass


class ToolBar ( Control ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		parent : Window,
		id : WindowID = ...,
		pos : Point = ...,
		size : Size = ...,
		style : long = ...,
		name : Text = ...,
	) -> None: ...
	
	def AddSeparator ( self ) -> ToolBarToolBase: ...
	
	def AddControl ( self,
		control : Control,
		label : Text,
	) -> ToolBarToolBase: ...
	
	def EnableTool ( self,
		toolId : int,
		enable : bool,
	) -> None: ...
	
	def FindControl ( self, id : int ) -> Optional[Control]: ...
	
	def GetToolState ( self, toolId : int ) -> bool: ...
	
	def Realize ( self ) -> bool: ...
	
	def SetToolBitmapSize ( self,
		size : Size,
	) -> None: ...
	
	def SetToolNormalBitmap ( self, id : int, bitmap : Bitmap ) -> None: ...
	
	def ToggleTool ( self, toolId : int, toggle : bool ) -> None: ...


class StatusBar ( Control ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		parent : Window,
		id : WindowID = ...,
		style : long = ...,
		name : Text = ...,
	) -> None: ...
	
	def GetFieldsCount ( self ) -> int: ...
	
	def GetFieldRect ( self, i : int ) -> Rect: ...


class WithImages ( object ):
	pass


class BookCtrlBase ( WithImages, Control ):
	pass


class Notebook ( BookCtrlBase ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		parent : Window,
		id : WindowID = ...,
		pos : Point = ...,
		size : Size = ...,
		style : long = ...,
		name : Text = ...,
	) -> None: ...
	
	def AddPage ( self,
		page : Window,
		text : Text,
		select : bool = ...,
		imageId : int = ...,
	) -> bool: ...


class Event ( Object ):
	EventObject : Object
	EventType : PyEventBinder
	Id : int
	Skipped : bool
	Timestamp : long
	
	def __init__ ( self,
		id : int = ...,
		eventType : PyEventBinder = ...,
	) -> None: ...
	
	def Clone ( self ) -> Event: ...
	
	def GetEventCategory ( self ) -> EventCategory: ...
	
	def GetEventObject ( self ) -> Object: ...
	
	def GetEventType ( self ) -> PyEventBinder: ...
	
	def GetEventUserData ( self ) -> Object: ...
	
	def GetId ( self ) -> int: ...
	
	def GetSkipped ( self ) -> bool: ...
	
	def GetTimestamp ( self ) -> long: ...
	
	def IsCommandEvent ( self ) -> bool: ...
	
	def ResumePropagation ( self,
		propagationLevel : int,
	) -> None: ...
	
	def SetEventObject ( self,
		object : Object,
	) -> None: ...
	
	def SetEventType ( self,
		type : PyEventBinder,
	) -> None: ...
	
	def SetId ( self,
		id : int,
	) -> None: ...
	
	def SetTimestamp ( self,
		timeStamp : long = ...,
	) -> None: ...
	
	def ShouldPropagate ( self ) -> bool: ...
	
	def Skip ( self,
		skip : bool = ...,
	) -> None: ...
	
	def StopPropagation ( self ) -> int: ...


class CommandEvent ( Event ):
	ClientData : Any
	ExtraLong : long
	Int : int
	Selection : int
	String : Text
	
	def __init__ ( self,
		commandEventType : PyEventBinder = ...,
		id : int = ...,
	) -> None: ...
	
	def GetClientData ( self ) -> Any: ...
	
	def GetClientObject ( self ) -> Any: ...
	
	def GetExtraLong ( self ) -> long: ...
	
	def GetInt ( self ) -> int: ...
	
	def GetSelection ( self ) -> int: ...
	
	def GetString ( self ) -> Text: ...
	
	def IsChecked ( self ) -> bool: ...
	
	def IsSelection ( self ) -> bool: ...
	
	def SetClientData ( self,
		data : Any,
	) -> None: ...
	
	def SetClientObject ( self,
		data : Any,
	) -> None: ...
	
	def SetExtraLong ( self,
		extraLong : long,
	) -> None: ...
	
	def SetInt ( self,
		intCommand : int,
	) -> None: ...
	
	def SetString ( self,
		string : Text,
	) -> None: ...
	


class CloseEvent ( Event ):
	LoggingOff :  bool
	
	def CanVeto ( self ) -> bool: ...
	
	def GetLoggingOff ( self ) -> bool: ...
	
	def GetVeto ( self ) -> bool: ...
	
	def SetCanVeto ( self,
		canVeto : bool,
	) -> None: ...
	
	def SetLoggingOff ( self,
		loggingOff : bool,
	) -> None: ...
	
	def Veto ( self,
		veto : bool = ...,
	) -> None: ...


class WindowDestroyEvent ( CommandEvent ):
	Window : WindowType
	
	def Clone ( self ) -> Event: ...
	
	def GetWindow ( self ) -> WindowType: ...


class FocusEvent ( Event ):
	Window : WindowType
	
	def __init__ ( self,
		eventType : PyEventBinder = ...,
		id : int = ...,
	) -> None: ...
	
	def Clone ( self ) -> Event: ...
	
	def GetWindow ( self ) -> WindowType: ...
	
	def SetWindow ( self, win : WindowType ) -> None: ...


class TimerEvent ( Event ):
	pass


class NavigationKeyEvent ( Event ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		event : NavigationKeyEvent,
	) -> None: ...
	
	def GetCurrentFocus ( self ) -> Window: ...
	
	def GetDirection ( self ) -> bool: ...
	
	def IsFromTab ( self ) -> bool: ...
	
	def IsWindowChange ( self ) -> bool: ...
	
	def SetCurrentFocus ( self, currentFocus : Window ) -> None: ...
	
	def SetDirection ( self, direction : bool ) -> None: ...
	
	def SetFlags ( self, flags : long ) -> None: ...
	
	def SetFromTab ( self, fromTab : bool ) -> None: ...
	
	def SetWindowChange ( self, windowChange : bool ) -> None: ...


class SizeEvent ( Event ):
	pass


class EraseEvent ( Event ):
	pass


class PaintEvent ( Event ):
	pass


class ScrollWinEvent ( Event ):
	def GetOrientation ( self ) -> int: ...
	def GetPosition ( self ) -> int: ...


class KeyboardState ( object ): # TODO FIXME: sip.wrapper?
	altDown : bool
	cmdDown : bool
	controlDown : bool
	#m_altDown : bool
	#m_controlDown : bool
	#m_metaDown : bool
	#m_shiftDown : bool
	metaDown : bool
	rawControlDown : bool
	shiftDown : bool
	
	def AltDown ( self ) -> bool: ...
	
	def ControlDown ( self ) -> bool: ...
	
	def CmdDown ( self ) -> bool: ...
	
	def GetModifiers ( self ) -> int: ...
	
	def HasAnyModifiers ( self ) -> bool: ...
	
	def HasModifiers ( self ) -> bool: ...
	
	def MetaDown ( self ) -> bool: ...
	
	def RawControlDown ( self ) -> bool: ...
	
	def SetAltDown ( self, down : bool ) -> None: ...
	
	def SetControlDown ( self, down : bool ) -> None: ...
	
	def SetMetaDown ( self, down : bool ) -> None: ...
	
	def SetRawControlDown ( self, down : bool ) -> None: ...
	
	def SetShiftDown ( self, down : bool ) -> None: ...
	
	def ShiftDown ( self ) -> bool: ...


class KeyEvent ( Event, KeyboardState ):
	KeyCode : int
	Position : Point
	RawKeyCode : Uint32
	RawKeyFlags : Uint32
	UnicodeKey : int
	X : Coord
	Y : Coord
	
	def Clone ( self ) -> Event : ...
	
	def DoAllowNextEvent ( self ) -> None : ...
	
	def GetKeyCode ( self ) -> int : ...
	
	def GetPosition ( self ) -> Point : ...
	
	def GetRawKeyCode ( self ) -> Uint32 : ...
	
	def GetRawKeyFlags ( self ) -> Uint32 : ...
	
	def GetUnicodeKey ( self ) -> int : ...
	
	def GetX ( self ) -> Coord : ...
	
	def GetY ( self ) -> Coord : ...
	
	def IsKeyInCategory ( self, category : int ) -> bool : ...
	
	def IsNextEventAllowed ( self ) -> bool : ...
	


class MouseState ( KeyboardState ):
	Position : Point
	X : Coord
	Y : Coord
	aux1IsDown : bool
	aux2IsDown : bool
	leftIsDown : bool
	middleIsDown : bool
	rightIsDown : bool
	x : Coord
	y : Coord

	def GetPosition ( self ) -> Point: ...


class MouseEvent ( Event, MouseState ):
	LinesPerAction : int
	LogicalPosition : Point
	WheelDelta : int
	WheelRotation : int
	
	def __init__ ( self,
		mouseEventType : PyEventBinder = ...,
	) -> None: ...
	
	def Aux1DClick ( self ) -> bool: ...
	
	def Aux1Down ( self ) -> bool: ...
	
	def Aux1Up ( self ) -> bool: ...
	
	def Aux2DClick ( self ) -> bool: ...
	
	def Aux2Down ( self ) -> bool: ...
	
	def Aux2Up ( self ) -> bool: ...
	
	def Button ( self,
		but : MouseButton,
	) -> bool: ...
	
	def ButtonDClick ( self,
		but : MouseButton = ...,
	) -> bool: ...
	
	def ButtonDown ( self,
		but : MouseButton = ...,
	) -> bool: ...
	
	def ButtonUp ( self,
		but : MouseButton = ...,
	) -> bool: ...
	
	def Dragging ( self ) -> bool: ...
	
	def Entering ( self ) -> bool: ...
	
	def GetButton ( self ) -> int: ...
	
	def GetClickCount ( self ) -> int: ...
	
	def GetColumnsPerAction ( self ) -> int: ...
	
	def GetLinesPerAction ( self ) -> int: ...
	
	def GetLogicalPosition ( self ) -> Point: ...
	
	def GetWheelAxis ( self ) -> MouseWheelAxis: ...
	
	def GetWheelDelta ( self ) -> int: ...
	
	def GetWheelRotation ( self ) -> int: ...
	
	def IsButton ( self ) -> bool: ...
	
	def IsPageScroll ( self ) -> bool: ...
	
	def Leaving ( self ) -> bool: ...
	
	def LeftDClick ( self ) -> bool: ...
	
	def LeftDown ( self ) -> bool: ...
	
	def LeftUp ( self ) -> bool: ...
	
	def MetaDown ( self ) -> bool: ...
	
	def MiddleDClick ( self ) -> bool: ...
	
	def MiddleDown ( self ) -> bool: ...
	
	def MiddleUp ( self ) -> bool: ...
	
	def Moving ( self ) -> bool: ...
	
	def RightDClick ( self ) -> bool: ...
	
	def RightDown ( self ) -> bool: ...
	
	def RightUp ( self ) -> bool: ...
	


class NotifyEvent ( CommandEvent ):
	pass


class ListEvent ( NotifyEvent ):
	CacheFrom : long
	CacheTo : long
	Column : int
	Data : UIntPtr
	Image : int
	Index : long
	Item : ListItem
	KeyCode : int
	Label : Text
	Mask : long
	Point : PointType
	Text : TextType
	
	def GetCacheFrom ( self ) -> long: ...
	
	def GetCacheTo ( self ) -> long: ...
	
	def GetColumn ( self ) -> int: ...
	
	def GetData ( self ) -> UIntPtr: ...
	
	def GetImage ( self ) -> int: ...
	
	def GetIndex ( self ) -> long: ...
	
	def GetItem ( self ) -> ListItem: ...
	
	def GetKeyCode ( self ) -> int: ...
	
	def GetLabel ( self ) -> TextType: ...
	
	def GetMask ( self ) -> long: ...
	
	def GetPoint ( self ) -> PointType: ...
	
	def GetText ( self ) -> TextType: ...
	
	def IsEditCancelled ( self ) -> bool: ...
	
	def SetCacheFrom ( self, cacheFrom : long ) -> None: ...
	
	def SetCacheTo ( self, cacheTo : long ) -> None: ...
	
	def SetColumn ( self, col : int ) -> None: ...
	
	def SetIndex ( self, index : long ) -> None: ...
	
	def SetItem ( self, item : ListItem ) -> None: ...
	
	def SetKeyCode ( self, code : int ) -> None: ...
	
	def SetPoint ( self, point : PointType ) -> None: ...


class BookCtrlEvent ( NotifyEvent ):
	pass


class SystemSettings ( object ): # TODO FIXME: sip.wrapper?
	@staticmethod
	def GetColour (
		index : int,
	) -> Colour: ...
	
	@staticmethod
	def GetFont (
		index : int,
	) -> Font: ...


class AcceleratorTable ( Object ):
	@overload
	def __init__ ( self ) -> None: ...
	
	@overload
	def __init__ ( self,
		entries : Sequence[AcceleratorEntry], # TODO FIXME: This also supports a Tuple but the documentation isn't clear
	) -> None: ...
AcceleratorTableType = AcceleratorTable


class AcceleratorEntry ( object ):
	def Set ( self,
		flags : int,
		keyCode : int,
		cmd : int,
		item : MenuItem = ...,
	) -> None: ...


class ClientDataContainer ( object ):
	ClientData : Any
	
	def __init__ ( self ) -> None: ...
	
	def GetClientData ( self ) -> Any: ...
	
	def GetClientObject ( self ) -> Any: ...
	
	def SetClientData ( self,
		data : Any,
	) -> None: ...
	
	def SetClientObject ( self,
		data: Any,
	) -> None: ...


class RefCounter ( object ):
	RefCount : int
	
	def __init__ ( self ) -> None: ...
	
	def DecRef ( self ) -> None: ...
	
	def GetRefCount ( self ) -> int: ...
	
	def IncRef ( self ) -> None: ...


class EventLoopBase ( object ):
	def Exit ( self, rc : int = ... ) -> None: ...
	
	def Run ( self ) -> int: ...


class GUIEventLoop ( EventLoopBase ):
	def __init__ ( self ) -> None: ...
