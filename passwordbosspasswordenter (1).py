import os
from pywinauto.application import Application
from pywinauto import Desktop
from pywinauto.keyboard import send_keys
app = Application(backend="uia").start(r"c:\Users\BrettRaper\AppData\Local\PasswordBoss\PasswordBoss.exe").connect(title="Password Boss", timeout=20)

passwordEnter = app.PasswordBoss.child_window(auto_id="GlobalPasswordTextBox", control_type="Edit").wrapper_object()

passwordEnter.type_keys("Password{ENTER}")
