import os
import sys

def create_bash_script(python_file_name, script_file_name):
    src_path = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(os.path.realpath(os.path.join(src_path, os.pardir)), script_file_name)
    file_path = os.path.join(src_path, python_file_name)
    bash_sctipt_string= "#!/usr/bin/env bash" \
                        "\n" \
                        "\nstr=\"$*\"" \
                        "\n" \
                        "\npython3 {} \"$str\"".format(file_path)
    # print(bash_sctipt_string)
    with open(script_path, 'x') as f:
        f.write(bash_sctipt_string)
    return script_path


if __name__ == "__main__":
    python_file_name = "tc_check.py"
    script_file_name = "tc_check.sh"
    script_path = create_bash_script(python_file_name=python_file_name, script_file_name=script_file_name)
    st = os.stat(script_path)
    os.chmod(script_path, st.st_mode | 0o111)

