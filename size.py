from PIL import Image


def re(self):
        # Image Filtering
        i = Image.open(self)
        ir = i.resize((1080, 1080))

        ir.show()
