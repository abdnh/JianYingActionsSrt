from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

from actions import *


class Dialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_ui()

    def setup_ui(self) -> None:
        self.setWindowTitle("JianYing Desktop Automator")
        self.setMinimumSize(400, 300)
        layout = QFormLayout()
        srcdir_button = QPushButton("...")
        srcdir_button.clicked.connect(self.on_choose_dir)
        self.srcdir_lineedit = srcdir_lineedit = QLineEdit()
        self.status_label = status_label = QLabel("")
        status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        start_button = QPushButton("Start")
        start_button.clicked.connect(self.on_start)
        layout.addRow(srcdir_button, srcdir_lineedit)
        layout.addRow(start_button)
        layout.addRow(status_label)
        self.setLayout(layout)

    def on_choose_dir(self) -> None:
        src_dir = QFileDialog.getExistingDirectory(self)
        self.srcdir_lineedit.setText(src_dir)

    def on_start(self) -> None:
        srcidr = self.srcdir_lineedit.text()
        Etcs().Get_Paths()
        Actions().Took_Draft_Content_Path()
        ui.CONFIG["draft_content_directory"] = Config["Draft_Content_Json"]
        ui.CONFIG["JianYing_Exe_Path"] = Config["JianYing_App_Path"]
        ui.Multi_Video_Process(video_path=srcidr)
        self.status_label.setText("Done!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    app.exec()
