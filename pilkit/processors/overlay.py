from pilkit.lib import Image, ImageColor
from pilkit.utils import dominant_color

class ColorOverlay(object):
    """
    Overlay a color mask with a the given opacity
    """

    def __init__(self, color, overlay_opacity=0.5):
        """
        :pamra color: The color to use on the overlay
        :param overlay_opacity: Define the fusion factor for the overlay mask

        """
        self.color = ImageColor.getrgb(color)
        self.overlay_opacity = overlay_opacity

    def process(self, img):
        original = img = img.convert('RGB')
        overlay = Image.new('RGB', original.size, self.color)
        mask = Image.new('RGBA', original.size, (0,0,0,int((1.0 - self.overlay_opacity)*255)))
        img = Image.composite(original, overlay, mask).convert('RGB')
        return img


class DominantColorOverlay(ColorOverlay):
    """
    Overlay the dominant color with the defined opacity

    NB: We could maybe enhance the algorithm by using a clustering algorithm
        like describe http://stackoverflow.com/questions/3241929/python-find-dominant-most-common-color-in-an-image
    """

    def __init__(self, overlay_opacity=0.5):
        """
        :param overlay_opacity: Define the fusion factor for the overlay mask

        """
        self.overlay_opacity = overlay_opacity

    def process(self, img):
        self.color = dominant_color(img)
        return super(DominantColorOverlay, self).process(img)
