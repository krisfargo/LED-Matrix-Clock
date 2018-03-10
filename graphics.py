#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
from PIL import Image
from PIL import ImageDraw
import datetime
import time


class GraphicsTest(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GraphicsTest, self).__init__(*args, **kwargs)

    def run(self):
        canvas = self.matrix
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("./matrix/fonts/6x12.bdf")
        # font.LoadFont("./tom-thumb.bdf")
        pos = offscreen_canvas.width

        text = "Tea"
        length = len(text)
        color = graphics.Color(255, 255, 255);
   
        while True:
            
            canvas.Clear()

            graphics.DrawLine(canvas, 1, 10, 30, 10, graphics.Color(255, 0, 0))

            text = datetime.datetime.now().strftime("%I:%M") # :%S")
           
            # image = Image.new("RGB", (32, 5))  # Can be larger than matrix if wanted!!
            # draw = ImageDraw.Draw(image)  # Declare Draw instance before prims
            # Draw some shapes into image (no immediate effect on matrix)...
            # draw.rectangle((28, 0, 31, 31), fill=(255, 0, 0), outline=(255, 0, 255))            
            
            graphics.DrawText(canvas, font, center_text_position(text, pos), 8, color, text)
            time.sleep(0.25)

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("./matrix/fonts/7x13.bdf")
        textColor = graphics.Color(255, 255, 0)
        pos = offscreen_canvas.width
        my_text = self.args.text

        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 11, textColor, my_text)
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width

            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

def center_text_position(text, canvas_width):
  return ((canvas_width - (len(text) * 6)) / 2)


# Main function
if __name__ == "__main__":
    # run_text = RunText()
    # if (not run_text.process()):
    #     run_text.print_help()
    graphics_test = GraphicsTest()
    if (not graphics_test.process()):
        graphics_test.print_help()


