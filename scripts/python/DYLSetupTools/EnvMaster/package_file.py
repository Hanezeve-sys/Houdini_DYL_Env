import os
import json
from collections import namedtuple
from typing import Dict, List

dyl_env_path = os.environ.get('DYL_ENV_HOME_DIRS')
dyl_script_path = dyl_env_path + '/scripts/python/DYLSetupTools/EnvMaster'
def_search_path = ['$HOUDINI_USER_PREF_DIR',
                   '$HOUDINI_PACKAGE_DIR',
                   '$HFS']
with open(dyl_script_path + '/env_variables.txt') as txt:
    env_var = txt.read()
    txt.close()


class PackageFile:
    def __init__(self, fdir: str):
        # super(PackageFile, self).__init__()
        self.fdir: str = fdir
        self.name: str = os.path.basename(self.fdir)
        self.data: Dict[str, List[str]] = self.get_package_file_data(self.fdir)
        self._info = namedtuple('pacf', ['Name', 'Dir', 'Data'])

        self.pacf_info = self._info(Name=self.name, Dir=self.fdir, Data=self.data)

    # -----------------------------------------#
    # get the packages keywords' data from "env", "package path" and "path"
    @staticmethod
    def get_package_file_data(fdir: str):
        try:
            with open(fdir) as f:
                s = f.read()
                s = s.replace('\t', '')
                s = s.replace('\n', '')
                s = s.replace(',}', '}')
                s = s.replace(',]', ']')
                data = json.loads(s)
            if data:
                if data.get('env'):
                    env_data = data.get('env')
                    if type(env_data) is str:
                        env_path = [env_data]
                    else:
                        env_path = env_data
                else:
                    env_path = []
                # print('the env path is:\n', env_path)
                if data.get('package_path'):
                    package_path_data = data.get('package_path')
                    if type(package_path_data) is str:
                        package_paths = [package_path_data]
                    else:
                        package_paths = package_path_data
                else:
                    package_paths = []
                # print('the package path is:\n', package_paths)
                if data.get('path'):
                    path_data = data.get('path')
                    if type(path_data) is str:
                        hou_path = [path_data]
                    else:
                        hou_path = path_data
                else:
                    hou_path = []
                # print('the houdini path is:\n', hou_path)
                return {'env_path': env_path, 'package_path': package_paths, 'houdini_path': hou_path}
            else:
                return {}
        except json.decoder.JSONDecodeError:
            return {}
