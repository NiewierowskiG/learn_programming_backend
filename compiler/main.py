from fastapi import FastAPI
from schemas import LanguageCompileData
from js2py.internals.simplex import JsException
from custom_errors import PythonCompilerError, CCompilerError
from javascript import javascript_compile
from python import python_compile
from c import c_compile

app = FastAPI()


@app.post('/language_test')
def test_compile(data: LanguageCompileData):
    print(data.model_dump())
    language = data.language
    result = {
        'msg': '',
        'error': False
    }
    try:
        if language == 'JavaScript':
            output = javascript_compile(
                src_code=data.compile_code
            )
        elif language == 'python':
            output = python_compile(
                src_code=data.compile_code
            )
        elif language == 'c':
            output = c_compile(
                src_code=data.compile_code
            )
        else:
            raise AssertionError(f"language {language} does not exist")

        if not result['error'] and output.strip() != data.expected_result:
            result['msg'] = "result did not match expected result"
            result['error'] = True
    except (JsException, PythonCompilerError, CCompilerError):
        result['msg'] = 'Compilation error'
        result['error'] = True
    return result
