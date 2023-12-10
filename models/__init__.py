#!/usr/bin/python3
''' init file for models '''
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
