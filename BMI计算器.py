import wx


class BMICalculator(wx.Frame):
    def __init__(self):
        super().__init__(None, title="BMI Calculator", size=(300, 200))
        panel = wx.Panel(self)

        
        height_label = wx.StaticText(panel, label="身高 (米)")
        weight_label = wx.StaticText(panel, label="体重 (千克)")
        self.height_input = wx.TextCtrl(panel)  # Set panel as the parent
        self.weight_input = wx.TextCtrl(panel)  # Set panel as the parent
        calculate_button = wx.Button(panel, label="计算BMI")

        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(height_label, 0, wx.EXPAND | wx.LEFT | wx.TOP, 10)
        sizer.Add(self.height_input, 0, wx.EXPAND | wx.LEFT | wx.TOP, 5)
        sizer.Add(weight_label, 0, wx.EXPAND | wx.LEFT | wx.TOP, 10)
        sizer.Add(self.weight_input, 0, wx.EXPAND | wx.LEFT | wx.TOP, 5)
        sizer.Add(calculate_button, 0, wx.ALIGN_RIGHT | wx.TOP | wx.RIGHT, 10)
        panel.SetSizer(sizer)

        # Bind button event
        calculate_button.Bind(wx.EVT_BUTTON, self.on_calculate)
        self.Show()

    def on_calculate(self, event):
        height = float(self.height_input.GetValue())
        weight = float(self.weight_input.GetValue())
        bmi = weight / (height * height)

        
        if bmi < 18.5:
            result = "您的体重过轻,不太接近2004-2018年的全球平均BMI24.4 kg/m2"
        elif 18.5 <= bmi < 24.9:
            result = "您的体重正常，与一个体质健康的人无异"
        elif 24.9 <= bmi < 29.9:
            result = "您的体重过重，超出了正常的BMI范围"
        else:
            result = "肥胖，您的体质可能出现了问题"

        wx.MessageBox(result, "BMI结果", style=wx.OK | wx.ICON_INFORMATION)


if __name__ == '__main__':
    app = wx.App()
    BMICalculator()
    app.MainLoop()
