import js2py
from contextlib import redirect_stdout
import io


def javascript_compile(src_code: str):
    stdout = io.StringIO()
    with redirect_stdout(stdout):
        js2py.eval_js(src_code)
    result = stdout.getvalue()

    return str(result)
