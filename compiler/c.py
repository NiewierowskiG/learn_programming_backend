import subprocess
import uuid
import os
from custom_errors import CCompilerError


def c_compile(src_code: str):
    filename = str(uuid.uuid4())

    result = subprocess.run(['gcc', '-xc', '-', '-o', filename], input=src_code,
                            text=True, capture_output=True)
    if result.returncode == 0:
        execution_result = subprocess.run([f'./{filename}'],
                                          capture_output=True,
                                          text=True)
        print(execution_result.stdout)
        os.remove(filename)
        return execution_result.stdout
    else:
        raise CCompilerError()
