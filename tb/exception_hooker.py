import sys
import json
from types import TracebackType

def raise_some_error():
    raise AssertionError("Some error")


class ErrorReport:

    message:str
    trace:dict
    name:str

    def __init__(self, e_type:type[BaseException], e_value:BaseException, e_traceback:TracebackType) -> None:
        self.name = e_type.__name__
        self.message = repr(e_value)
        self.trace = {}
        while e_traceback:
            self.trace = {   
                "file": e_traceback.tb_frame.f_code.co_filename,
                "line": e_traceback.tb_lineno,
                "module": e_traceback.tb_frame.f_code.co_name,
                "trace": self.trace
            }
            e_traceback = e_traceback.tb_next

    def __repr__(self) -> str:
        return json.dumps(self.trace, indent=4)
            



def exception_hook(type:type[BaseException], value:BaseException, traceback:TracebackType) -> ErrorReport:
    error_report = ErrorReport(type, value, traceback)
    print(error_report)

sys.excepthook = exception_hook

raise_some_error()