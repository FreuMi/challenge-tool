#!/usr/bin/env python3

from docker import Docker

class MorphRDB(Docker):
    def __init__(self):
        super().__init__()

    def load(self):
        pass
