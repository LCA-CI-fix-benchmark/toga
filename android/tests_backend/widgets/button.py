import pytest
from java import jclass

from toga.colors import TRANSPARENT

from .label import LabelProbe


# On Android, a Button is just a TextView with a state-dependent background image.
class ButtonProbe(LabelProbe):
    native_class = jclass("android.widget.Button")

    # Heavier than sans-serif, but lighter than sans-serif bold
    default_font_family = "sans-serif-medium"

    def assert_no_icon(self):
        pytest.skip("Android doesn't support icons on buttons")
        # return self.native.Image is None

    def assert_icon_size(self):
        pytest.skip("Android doesn't support icons on buttons")
        # icon = self.native.Image
        # if icon:
        #     assert (icon.Size.Width, icon.Size.Height) == (32, 32)
        # else:
        #     pytest.fail("Icon does not exist")

    @property
    def background_color(self):
        color = super().background_color
        return None if color == TRANSPARENT else color
