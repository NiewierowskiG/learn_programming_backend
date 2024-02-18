import sys
import io
from custom_errors import PythonCompilerError


def python_compile(src_code: str):
    captured_output = io.StringIO()
    sys.stdout = captured_output

    try:
        try:
            exec(compile(src_code, '', 'exec'), globals())
        except Exception as e:
            raise PythonCompilerError(e)
        # Get the captured output
        captured_messages = captured_output.getvalue()
        return captured_messages
    finally:
        # Reset stdout to the original stream
        sys.stdout = sys.__stdout__
    return ""
