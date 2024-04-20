from dataclasses import dataclass

try:
    from PySide6 import QtCore

    @dataclass
    class ProgressBars:
        item: QtCore.Signal
        item_name: QtCore.Signal
        list_item: QtCore.Signal
        list_name: QtCore.Signal

except ModuleNotFoundError:

    class ProgressBars:
        pass


@dataclass
class ResultItem:
    position: int
    artist: str
    title: str
    album: str
    duration_sec: int
    obj: object
    quality: str
    explicit: bool


@dataclass
class StatusbarMessage:
    message: str
    timout: int = 0


@dataclass
class QueueDownloadItem:
    status: str
    name: str
    type_media: str
    quality: str
    obj: object
