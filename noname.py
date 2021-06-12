# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class login
###########################################################################

class login ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 274,198 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.input_username = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		bSizer1.Add( self.input_username, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.input_password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		bSizer1.Add( self.input_password, 0, wx.ALL, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button2, 0, wx.ALL, 5 )

		self.m_button19 = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button19, 0, wx.ALL, 5 )


		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.exit )
		self.m_button19.Bind( wx.EVT_BUTTON, self.masuk )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def exit( self, event ):
		event.Skip()

	def masuk( self, event ):
		event.Skip()


###########################################################################
## Class home1
###########################################################################

class home1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 373,172 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Laporan Pembangunan Jalan yang belum selesai", wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		bSizer2.Add( self.m_button3, 0, wx.ALL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Laporan Pembangunan Jalan Yang Belum DIlaksanakan", wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		bSizer2.Add( self.m_button4, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Laporan Pembangunan Jalan Yang Rusak", wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		bSizer2.Add( self.m_button5, 0, wx.ALL, 5 )

		self.m_button29 = wx.Button( self, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		bSizer2.Add( self.m_button29, 0, wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button3.Bind( wx.EVT_BUTTON, self.usermenu1 )
		self.m_button4.Bind( wx.EVT_BUTTON, self.usermenu2 )
		self.m_button5.Bind( wx.EVT_BUTTON, self.usermenu3 )
		self.m_button29.Bind( wx.EVT_BUTTON, self.exit1 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def usermenu1( self, event ):
		event.Skip()

	def usermenu2( self, event ):
		event.Skip()

	def usermenu3( self, event ):
		event.Skip()

	def exit1( self, event ):
		event.Skip()


###########################################################################
## Class menu1
###########################################################################

class menu1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,528 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Nama Kabupaten", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		bSizer3.Add( self.m_staticText24, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		bSizer3.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Nama Desa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer3.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		bSizer3.Add( self.m_textCtrl4, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Nama User", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer3.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		bSizer3.Add( self.m_textCtrl5, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Nama Jalan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer3.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		bSizer3.Add( self.m_textCtrl6, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Panjang jalan yang sudah selesai", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer3.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		bSizer3.Add( self.m_textCtrl7, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Panjang jalan yang seharusnya diselesaikan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer3.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		bSizer3.Add( self.m_textCtrl8, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Alasan ingin cepat diselesaikan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer3.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,70 ), 0 )
		bSizer3.Add( self.m_textCtrl9, 0, wx.ALL, 5 )

		gSizer4 = wx.GridSizer( 0, 2, 0, 270 )

		self.m_button25 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_button25, 0, wx.ALL, 5 )

		self.m_button26 = wx.Button( self, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_button26, 0, wx.ALL, 5 )


		bSizer3.Add( gSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button25.Bind( wx.EVT_BUTTON, self.cancel1 )
		self.m_button26.Bind( wx.EVT_BUTTON, self.submit1 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def cancel1( self, event ):
		event.Skip()

	def submit1( self, event ):
		event.Skip()


###########################################################################
## Class menu2
###########################################################################

class menu2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,467 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Nama Kabupaten", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		bSizer10.Add( self.m_staticText22, 0, wx.ALL, 5 )

		self.m_textCtrl22 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_textCtrl22, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Nama Desa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		bSizer10.Add( self.m_staticText23, 0, wx.ALL, 5 )

		self.m_textCtrl23 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_textCtrl23, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Nama User", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		bSizer10.Add( self.m_staticText24, 0, wx.ALL, 5 )

		self.m_textCtrl24 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_textCtrl24, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Nama Jalan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		bSizer10.Add( self.m_staticText25, 0, wx.ALL, 5 )

		self.m_textCtrl25 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_textCtrl25, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Panjang Jalan yang harus dibangun", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		bSizer10.Add( self.m_staticText26, 0, wx.ALL, 5 )

		self.m_textCtrl26 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_textCtrl26, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Alasan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		bSizer10.Add( self.m_staticText27, 0, wx.ALL, 5 )

		self.m_textCtrl27 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl27.SetMinSize( wx.Size( -1,70 ) )

		bSizer10.Add( self.m_textCtrl27, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button21 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_button21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button22 = wx.Button( self, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_button22, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )


		bSizer10.Add( gSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer10 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button21.Bind( wx.EVT_BUTTON, self.cancel2 )
		self.m_button22.Bind( wx.EVT_BUTTON, self.submit2 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def cancel2( self, event ):
		event.Skip()

	def submit2( self, event ):
		event.Skip()


###########################################################################
## Class menu3
###########################################################################

class menu3 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,465 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Nama Kabupaten", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		bSizer5.Add( self.m_staticText17, 0, wx.ALL, 5 )

		self.m_textCtrl16 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		bSizer5.Add( self.m_textCtrl16, 0, wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Nama Desa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		bSizer5.Add( self.m_staticText18, 0, wx.ALL, 5 )

		self.m_textCtrl17 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		bSizer5.Add( self.m_textCtrl17, 0, wx.ALL, 5 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Nama User", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		bSizer5.Add( self.m_staticText19, 0, wx.ALL, 5 )

		self.m_textCtrl18 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		bSizer5.Add( self.m_textCtrl18, 0, wx.ALL, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Nama Jalan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		bSizer5.Add( self.m_staticText20, 0, wx.ALL, 5 )

		self.m_textCtrl19 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		bSizer5.Add( self.m_textCtrl19, 0, wx.ALL, 5 )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Panjang jalan yang harus diperbaiki", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		bSizer5.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.m_textCtrl20 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		bSizer5.Add( self.m_textCtrl20, 0, wx.ALL, 5 )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Alasan ingin cepat diperbaiki", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		bSizer5.Add( self.m_staticText22, 0, wx.ALL, 5 )

		self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,70 ), 0 )
		bSizer5.Add( self.m_textCtrl21, 0, wx.ALL, 5 )

		gSizer5 = wx.GridSizer( 0, 2, 0, 270 )

		self.m_button27 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_button27, 0, wx.ALL, 5 )

		self.m_button28 = wx.Button( self, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_button28, 0, wx.ALL, 5 )


		bSizer5.Add( gSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button27.Bind( wx.EVT_BUTTON, self.cancel3 )
		self.m_button28.Bind( wx.EVT_BUTTON, self.submit3 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def cancel3( self, event ):
		event.Skip()

	def submit3( self, event ):
		event.Skip()


###########################################################################
## Class home2
###########################################################################

class home2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 425,217 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_button20 = wx.Button( self, wx.ID_ANY, u"Tambah Pengguna", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button20, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button12 = wx.Button( self, wx.ID_ANY, u"Data Jalan yang belum selesai", wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		bSizer9.Add( self.m_button12, 0, wx.ALL, 5 )

		self.m_button13 = wx.Button( self, wx.ID_ANY, u"Data Jalan Yang belum dilaksanakan", wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		bSizer9.Add( self.m_button13, 0, wx.ALL, 5 )

		self.m_button14 = wx.Button( self, wx.ID_ANY, u"Data Jalan Yang Rusak", wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		bSizer9.Add( self.m_button14, 0, wx.ALL, 5 )

		self.m_button15 = wx.Button( self, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		bSizer9.Add( self.m_button15, 0, wx.ALL, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button20.Bind( wx.EVT_BUTTON, self.adduser )
		self.m_button12.Bind( wx.EVT_BUTTON, self.adminmenu1 )
		self.m_button13.Bind( wx.EVT_BUTTON, self.adminmenu2 )
		self.m_button14.Bind( wx.EVT_BUTTON, self.adminmenu3 )
		self.m_button15.Bind( wx.EVT_BUTTON, self.exitadmin )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def adduser( self, event ):
		event.Skip()

	def adminmenu1( self, event ):
		event.Skip()

	def adminmenu2( self, event ):
		event.Skip()

	def adminmenu3( self, event ):
		event.Skip()

	def exitadmin( self, event ):
		event.Skip()


###########################################################################
## Class user
###########################################################################

class user ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 420,205 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		bSizer11.Add( self.m_staticText28, 0, wx.ALL, 5 )

		self.m_textCtrl28 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_textCtrl28, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		bSizer11.Add( self.m_staticText29, 0, wx.ALL, 5 )

		self.m_textCtrl29 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_textCtrl29, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button24 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_button24, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button25 = wx.Button( self, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_button25, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer11.Add( gSizer6, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button24.Bind( wx.EVT_BUTTON, self.cancel4 )
		self.m_button25.Bind( wx.EVT_BUTTON, self.submit4 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def cancel4( self, event ):
		event.Skip()

	def submit4( self, event ):
		event.Skip()


###########################################################################
## Class menu1A
###########################################################################

class menu1A ( wx.Frame ):

	def __init__( self, parent,panjangbaris ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 960,210 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid1.CreateGrid( panjangbaris[0] , 8 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )

		# Columns
		self.m_grid1.SetColSize( 0, 120 )
		self.m_grid1.SetColSize( 1, 95 )
		self.m_grid1.SetColSize( 2, 101 )
		self.m_grid1.SetColSize( 3, 107 )
		self.m_grid1.SetColSize( 4, 68 )
		self.m_grid1.SetColSize( 5, 69 )
		self.m_grid1.SetColSize( 6, 69 )
		self.m_grid1.SetColSize( 7, 300 )
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelValue( 0, u"ID" )
		self.m_grid1.SetColLabelValue( 1, u"Nama Kabupaten" )
		self.m_grid1.SetColLabelValue( 2, u"Nama Desa" )
		self.m_grid1.SetColLabelValue( 3, u"Nama User" )
		self.m_grid1.SetColLabelValue( 4, u"Nama Jalan" )
		self.m_grid1.SetColLabelValue( 5, u"Panjang SS" )
		self.m_grid1.SetColLabelValue( 6, u"Panjang BS" )
		self.m_grid1.SetColLabelValue( 7, u"Alasan" )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid1.AutoSizeRows()
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer6.Add( self.m_grid1, 0, wx.ALL, 5 )

		self.m_button16 = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button16, 0, wx.ALL, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button16.Bind( wx.EVT_BUTTON, self.kembali1 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def kembali1( self, event ):
		event.Skip()


###########################################################################
## Class menu2A
###########################################################################

class menu2A ( wx.Frame ):

	def __init__( self, parent, panjangbaris ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 860,196 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid3 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid3.CreateGrid( panjangbaris[0], 7 )
		self.m_grid3.EnableEditing( True )
		self.m_grid3.EnableGridLines( True )
		self.m_grid3.EnableDragGridSize( True )
		self.m_grid3.SetMargins( 0, 0 )

		# Columns
		self.m_grid3.SetColSize( 0, 95 )
		self.m_grid3.SetColSize( 1, 95 )
		self.m_grid3.SetColSize( 2, 91 )
		self.m_grid3.SetColSize( 3, 84 )
		self.m_grid3.SetColSize( 4, 69 )
		self.m_grid3.SetColSize( 5, 69 )
		self.m_grid3.SetColSize( 6, 300 )
		self.m_grid3.EnableDragColMove( False )
		self.m_grid3.EnableDragColSize( True )
		self.m_grid3.SetColLabelSize( 30 )
		self.m_grid3.SetColLabelValue( 0, u"ID" )
		self.m_grid3.SetColLabelValue( 1, u"Nama Kabupaten" )
		self.m_grid3.SetColLabelValue( 2, u"Nama Desa" )
		self.m_grid3.SetColLabelValue( 3, u"Nama User" )
		self.m_grid3.SetColLabelValue( 4, u"Nama Jalan" )
		self.m_grid3.SetColLabelValue( 5, u"Panjang BS" )
		self.m_grid3.SetColLabelValue( 6, u"Alasan" )
		self.m_grid3.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid3.EnableDragRowSize( True )
		self.m_grid3.SetRowLabelSize( 80 )
		self.m_grid3.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid3.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer7.Add( self.m_grid3, 0, wx.ALL, 5 )

		self.m_button17 = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button17, 0, wx.ALL, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button17.Bind( wx.EVT_BUTTON, self.kembali2 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def kembali2( self, event ):
		event.Skip()


###########################################################################
## Class menu3A
###########################################################################

class menu3A ( wx.Frame ):

	def __init__( self, parent, panjangbaris ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 860,206 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid5 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid5.CreateGrid( panjangbaris[0], 7 )
		self.m_grid5.EnableEditing( True )
		self.m_grid5.EnableGridLines( True )
		self.m_grid5.EnableDragGridSize( False )
		self.m_grid5.SetMargins( 0, 0 )

		# Columns
		self.m_grid5.SetColSize( 0, 120 )
		self.m_grid5.SetColSize( 1, 95 )
		self.m_grid5.SetColSize( 2, 91 )
		self.m_grid5.SetColSize( 3, 84 )
		self.m_grid5.SetColSize( 4, 69 )
		self.m_grid5.SetColSize( 5, 70 )
		self.m_grid5.SetColSize( 6, 300 )
		self.m_grid5.EnableDragColMove( False )
		self.m_grid5.EnableDragColSize( True )
		self.m_grid5.SetColLabelSize( 30 )
		self.m_grid5.SetColLabelValue( 0, u"ID" )
		self.m_grid5.SetColLabelValue( 1, u"Nama Kabupaten" )
		self.m_grid5.SetColLabelValue( 2, u"Nama Desa" )
		self.m_grid5.SetColLabelValue( 3, u"Nama User" )
		self.m_grid5.SetColLabelValue( 4, u"Nama Jalan" )
		self.m_grid5.SetColLabelValue( 5, u"Panjang BS" )
		self.m_grid5.SetColLabelValue( 6, u"Alasan" )
		self.m_grid5.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid5.EnableDragRowSize( True )
		self.m_grid5.SetRowLabelSize( 80 )
		self.m_grid5.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid5.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer8.Add( self.m_grid5, 0, wx.ALL, 5 )

		self.m_button18 = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button18, 0, wx.ALL, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button18.Bind( wx.EVT_BUTTON, self.kembali3 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def kembali3( self, event ):
		event.Skip()


