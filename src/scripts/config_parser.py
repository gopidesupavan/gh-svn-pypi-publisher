import os
import sys
import json
import yaml

DEFAULT_SVN_CHECKER_SCRIPT = "{github_action_path}/src/scripts/svn_checker.py"
DEFAULT_CHECK_SUM_SCRIPT = "{github_action_path}/src/scripts/checksum_check.sh"
DEFAULT_SIGNATURE_CHECK_SCRIPT = "{github_action_path}/src/scripts/signature_check.sh"


def set_default_config(config_data: dict):
    svn_checker_script = config_data.get("publishers", {}).get("rules", {}).get("svn-check", {}).get("script")
    if not svn_checker_script:
        config_data["publishers"]["rules"]["svn-check"]["script"] = DEFAULT_SVN_CHECKER_SCRIPT.format(github_action_path=os.environ.get("GITHUB_ACTION_PATH"))

    check_sum_script = config_data.get("publishers", {}).get("rules", {}).get("checksum-check", {}).get("script")
    if not check_sum_script:
        config_data["publishers"]["rules"]["checksum-check"]["script"] = DEFAULT_CHECK_SUM_SCRIPT.format(github_action_path=os.environ.get("GITHUB_ACTION_PATH"))

    signature_check_script = config_data.get("publishers", {}).get("rules", {}).get("signature-check", {}).get("script")
    if not signature_check_script:
        config_data["publishers"]["rules"]["signature-check"]["script"] = DEFAULT_SIGNATURE_CHECK_SCRIPT.format(github_action_path=os.environ.get("GITHUB_ACTION_PATH"))

    return config_data


def parse_config(path: str):
    with open(path, 'r') as file:
        config_data = yaml.safe_load(file)

    updated_config_data = set_default_config(config_data)

    def set_multiline_output(name, updated_data):
        with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
            value = json.dumps(updated_data)
            f.write(f'{name}={value}')
            
    set_multiline_output("pub_config", updated_config_data)



if __name__ == '__main__':
    config_path = sys.argv[1]
    parse_config(config_path)
