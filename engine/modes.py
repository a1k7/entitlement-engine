from enum import Enum

class ExecutionMode(str, Enum):
    PREVIEW = "PREVIEW"
    SHADOW = "SHADOW"
    EXECUTE = "EXECUTE"
