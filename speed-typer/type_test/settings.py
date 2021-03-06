from PyQt5 import QtWidgets

from source_ui import settings_window
from .components import Switch


# CONSTANTS
DARK_COLOURS = dict(
    bg="hsl(217, 35%, 15%)",
    bg_lighter="hsl(217, 35%, 19%)",
    text="hsl(0, 0%, 85%)",
    text_button="hsl(0, 0%, 62%)",
)

LIGHT_COLOURS = dict(
    bg="hsl(217, 35%, 82%)",
    bg_lighter="hsl(217, 35%, 86%)",
    text="hsl(0, 0%, 14%)",
    text_button="hsl(0, 0%, 47%)",
)

# Graph colours
DARK_GRAPH = dict(
    axes="#d9d9d9",
    curve="#136c19",
)

LIGHT_GRAPH = dict(
    axes="#000000",
    curve="#1ca025",
)

# Colours for custom switch widget
# Must be hex string for QColor object
SWITCH_COLOURS = dict(
    bg_colour="#9e9e9e",
    circle_colour="#d9d9d9",
    active_bg_colour="#3381ff",
)

# Colours for rich text highlighting
RICH_TEXT_COLOURS = dict(
    dark=["hsl(124, 70%, 21%)", "hsl(0, 65%, 38%)"],
    light=["hsl(124, 60%, 45%)", "hsl(0, 80%, 55%)"],
)


# DEFAULT STYLESHEET AND SETTINGS
def _get_style_sheet_(bg="", bg_lighter="", text="", text_button="", **kwargs):
    """
    Returns a string representing the style sheet.

    Usage: _get_style_sheet(**DARK_COLOURS) or _get_style_sheet(**LIGHT_COLOURS)
    """

    try:
        return f"""QWidget {{
                background: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:1, y2:1,
                    stop:0 {bg}, stop:0.807107 {bg_lighter}
                );
                color: {text}; font-size: 24pt;
                font-weight: bold; font-family: "Inconsolata Bold";
            }}
            QPushButton, QComboBox {{
                background: transparent; font-size: 25pt; border-radius: 5;
                padding: 8px; text-align: left; color: {text_button};
            }}
            QPushButton::hover, QComboBox::hover, QPushButton::focus, QComboBox::focus {{
                background: transparent; color: {text}; outline: none;
            }}
            QComboBox::down-arrow {{
                background: transparent;
            }}
            QComboBox::item {{
                background: {bg_lighter};
            }}
            QComboBox::item:selected {{
                font-weight: bold; color: {text};
            }}
            QLabel, QRadioButton, QScrollArea, QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical, #graphView {{
                background: transparent; border: none;
            }}
            QScrollBar {{
                background: {bg};
            }}
            QScrollBar::handle {{
                background: {text_button}; border: none;
            }}
            QScrollBar::handle:pressed {{
                background: {text};
            }}
            #labelMainMenu, #labelTitle, #labelStatistics {{
                font-size: 50pt;
            }}
            #labelDaysAgo {{
                color: {text_button}
            }}"""

    except NameError as e:
        print(e)
        raise NameError(
            "Pass in either DARK_COLOURS or LIGHT_COLOURS dictionaries as unpacked"
            " kwargs i.e. _get_style_sheet(**DARK_COLOURS)"
        )


BASE_STYLE_SHEET = _get_style_sheet_(**DARK_COLOURS)

DEFAULT_SETTINGS = [
    False,  # Play key sound (True or False)
    "key_2.wav",  # Name of sound file to play (str)
    BASE_STYLE_SHEET,  # Stylesheet for all windows (list)
    True,  # Dark mode (True or False)
    DARK_GRAPH,  # Colours for graph (dict)
    RICH_TEXT_COLOURS["dark"],  # Rich text colours (dict[list])
]


class SettingsWindow(QtWidgets.QWidget, settings_window.Ui_settingsWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        # Replace placeholder checkboxes with custom toggle switches
        self.toggleDarkMode = Switch(**SWITCH_COLOURS)
        self.layoutDarkMode.replaceWidget(self.checkBoxDarkMode, self.toggleDarkMode)
        self.checkBoxDarkMode.close()

        self.toggleKeystrokeSound = Switch(**SWITCH_COLOURS)
        self.layoutKeystrokeSounds.replaceWidget(
            self.checkBoxToggleSounds, self.toggleKeystrokeSound
        )
        self.checkBoxToggleSounds.close()

    # Helper methods
    def _get_values(self) -> None:
        """Updates all relevant settings into instance variables."""

        self.is_dark_mode = self.toggleDarkMode.isChecked()  # False means light mode

        self.graph_colours = DARK_GRAPH if self.is_dark_mode else LIGHT_GRAPH

        self.rich_text_colours = (
            RICH_TEXT_COLOURS["dark"]
            if self.is_dark_mode
            else RICH_TEXT_COLOURS["light"]
        )

        self.play_key_sound = (
            self.toggleKeystrokeSound.isChecked()
        )  # False means key sound off

        self.key_sound = str(
            self.comboSelectSound.currentText()
        )  # Sound to play on keystroke

        self.style_sheet = self._get_style_sheet()

    def _get_style_sheet(self) -> str:
        """
        Returns a string representing the stylesheet.

        The stylesheet returned is to be used in main.py to set the
        styling for all windows.
        """

        colours = DARK_COLOURS if self.is_dark_mode else LIGHT_COLOURS

        return _get_style_sheet_(**colours)

    # Public Method
    def get_settings(self) -> list:
        """Returns a list of settings variables which control various attributes."""

        self._get_values()

        return [
            self.play_key_sound,
            self.key_sound,
            self.style_sheet,
            self.is_dark_mode,
            self.graph_colours,
            self.rich_text_colours,
        ]


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = SettingsWindow()
    window.show()

    app.exec_()
