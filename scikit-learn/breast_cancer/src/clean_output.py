#!/usr/bin/env python3

import os
import glob
from datetime import datetime, timedelta

for file in glob.glob("output/*"):
    if os.path.isfile(file):
        file_time = datetime.fromtimestamp(os.path.getmtime(file))
        if datetime.now() - file_time > timedelta(hours=1):
            os.remove(file)
            print(f"Deleted {file}")
