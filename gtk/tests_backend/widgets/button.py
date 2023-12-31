import pytest

from toga.colors import TRANSPARENT
from toga_gtk.libs import Gtk

from .base import SimpleProbe


class ButtonProbe(SimpleProbe):
    native_class = Gtk.Button

    @property
    def text(self):
        return self.native.get_label()

    def assert_no_icon(self):
        pytest.skip("GTK doesn't support icons on buttons")

    def assert_icon_size(self):
        pytest.skip("GTK doesn't support icons on buttons")

    @property
    def background_color(self):
        color = super().background_color
        # Background color of TRANSPARENT is treated as a reset.
        if color == TRANSPARENT:
            return None
        return color

    async def press(self):
        self.native.clicked()
