from random import choices

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # text control widget
        vbox.Add(wx.TextCtrl(panel, value='initial text'),flag= wx.ALL, border=5)
        vbox.Add(wx.TextCtrl(panel, style=wx.TE_PASSWORD),flag= wx.ALL, border=5)

        #radiobutton widget
        vbox.Add(wx.RadioButton(panel, label='Male',style=wx.RB_GROUP),flag= wx.ALL, border=5)
        vbox.Add(wx.RadioButton(panel, label='Female'),flag= wx.ALL, border=5)

        #STATICTEXT widget
        vbox.Add(wx.StaticText(panel, label="Enter your name:"),flag= wx.ALL, border=5)

        #checkbox widget
        vbox.Add(wx.CheckBox(panel, label="Black"),flag= wx.ALL, border=5)

        #combobox widget
        items=["Apple", "Rice", "Cheese cake"]
        vbox.Add(wx.ComboBox(panel, choices= items),flag= wx.ALL, border=5)

        #slider widget
        vbox.Add(wx.Slider(panel, value= 50, minValue=0, maxValue=100),flag= wx.ALL, border=5)

        # button widget
        vbox.Add(wx.Button(panel, label='Press Me'),flag= wx.ALL, border=5)

        panel.SetSizer(vbox)
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()