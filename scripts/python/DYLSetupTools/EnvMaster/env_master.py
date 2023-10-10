import hou
import subprocess
import webbrowser
from configparser import ConfigParser
from PySide2.QtWidgets import QWidget, QFileDialog, QCheckBox, QMessageBox, QTreeWidgetItem
from PySide2.QtCore import Qt
from EnvMaster.package_file import *
from EnvMaster.env_master_ui import Ui_EnvMaster
# from DYLSetupTools.EnvMaster.env_master_ui import Ui_EnvMaster
# from DYLSetupTools.EnvMaster.package_file import *

dyl_env_path = os.environ.get('DYL_ENV_HOME_DIRS')
dyl_script_path = dyl_env_path + '/scripts/python/DYLSetupTools/EnvMaster'
package_file_path_list = ['$HOUDINI_USER_PREF_DIR',
                          '$HOUDINI_PACKAGE_DIR',
                          '$HFS']
# This file include all the environment variables crawled from web
with open(dyl_script_path + '/env_variables.txt') as txt:
    env_var = txt.read()
    txt.close()

default_editor_dir = 'C:/Windows/notepad.exe'
config_dir = dyl_script_path + '/config.ini'


# If the path to check is the keyword of 'package path', use this function
def check_path_with_hpp(path: str, pac_fdir: str) -> str:
    head = path.split('/')[0]
    try:
        body = path.split(f'{head}/')[1]
        body = body.replace('../', '')
    except IndexError:
        body = ''
    if head == '$HOUDINI_PACKAGE_PATH':
        hou_path = os.path.split(pac_fdir)[0]
        if body:
            trans_path = os.path.join(hou_path, body).replace('\\', '/')
        else:
            trans_path = hou_path.replace('\\', '/')
        return trans_path
    elif os.path.isdir(path):
        return path
    else:
        hou_path = hou.hscriptExpandString(f'{head}')
        if body:
            trans_path = os.path.join(hou_path, body).replace('\\', '/')
        else:
            trans_path = hou_path.replace('\\', '/')
        return trans_path


# if the path is script path like, translate to normally
def check_path(path: str) -> str:
    head = path.split('/')[0]
    try:
        body = path.split(f'{head}/')[1]
        body = body.replace('../', '')
    except IndexError:
        body = ''
    if os.path.isdir(path):
        return path
    else:
        if head.replace('$', '') in env_var:
            if head != '$HOUDINI_PACKAGE_DIR':
                trans_path = hou.hscriptExpandString(path) + '/packages'
            else:
                trans_path = hou.hscriptExpandString(path)
            return trans_path
        else:
            hou_path = hou.hscriptExpandString(f'{head}')
            if body:
                trans_path = os.path.join(hou_path, body).replace('\\', '/')
            else:
                trans_path = hou_path.replace('\\', '/')
        return trans_path


# get processed path from data's' environment variable
def trans_data(datas) -> List[str]:
    paths = []
    if type(datas) is list:
        # print('list')
        for data in datas:
            if type(data) is str:
                paths.append(check_path(data))
            elif type(data) is dict:
                # find custom environment variable
                for k in data:
                    if k not in env_var:
                        custom_env_path = data[k]
                        paths.append(check_path(custom_env_path))
        return paths
    elif type(datas) is dict:
        # print('dict')
        # find custom environment variable
        for k in datas:
            if k not in env_var:
                custom_env_path = datas[k]
                paths.append(check_path(custom_env_path))
        return paths
    elif type(datas) is str:
        # print('str')
        paths = [check_path(datas)]
        return paths
    else:
        return []


def get_all_package_files(search_path):
    file_dict = {}
    for path in search_path:
        file_dict.update(search_package_files(path))
    return file_dict


# search for package files from a package file path
def search_package_files(search_path: str) -> dict:
    # get search path from houdini path
    hou_path = check_path(search_path)
    # scan directory and get package(json) file
    file_dict: Dict[str, List[str]] = {}
    if os.path.exists(hou_path):
        scanned_dir = os.scandir(hou_path)
        # if scanned_dir:
        file_name_list = []
        for file_dir_entry in scanned_dir:
            file_dir = file_dir_entry.path
            file_dir = file_dir.replace('\\', '/')
            if os.path.exists(file_dir) and os.path.isfile(file_dir):
                file_name = os.path.basename(file_dir)
                if file_name.endswith('.json'):
                    file_name_list.append(f"{file_name}")
        file_dict[search_path] = file_name_list
        return file_dict
    else:
        file_dict[search_path] = []
        return file_dict


class EnvMaster(QWidget, Ui_EnvMaster):
    def __init__(self):
        super(EnvMaster, self).__init__()
        self.setParent(hou.ui.mainQtWindow(), Qt.Window)
        self.setupUi(self)

        self.file_dict = get_all_package_files(package_file_path_list)
        # print(self.file_dict)

        # Env Manager
        self.set_env_path_tree()
        self.env_path_tree.itemClicked.connect(lambda: self.on_env_path_tree_item_clicked())
        self.env_path_tree.itemDoubleClicked.connect(lambda: self.open(self.env_path_tree.currentItem()))
        self.packages_tree.itemDoubleClicked.connect(lambda: self.open(self.packages_tree.currentItem()))
        self.package_files_tree.itemDoubleClicked.connect(lambda: self.open(self.package_files_tree.currentItem()))
        self.refresh_btn.clicked.connect(lambda: self.on_refresh_btn_clicked())

        # Env Creator
        # folder choose button
        tool_btn = self.toolButton
        tool_btn.clicked.connect(lambda: self.set_folder_path())

        # whether custom json file name
        custom_name_cb = self.custom_json_name
        custom_name_cb.toggled.connect(lambda: self.set_custom_name_frame())

        # preset contents button
        edit_home_btn = self.edit_contents_home
        edit_package_btn = self.edit_contents_package
        # script_path = os.environ.get('DYL_ENV_DIRS') + '/scripts/python/DYLSetupTools/EnvMaster'
        edit_home_btn.clicked.connect(lambda: self.open_preset_contents_file(dyl_script_path, location='Home'))
        edit_package_btn.clicked.connect(lambda: self.open_preset_contents_file(dyl_script_path, location='Package'))

        # for create button
        create_btn = self.env_create
        create_btn.clicked.connect(lambda: self.on_create_button_pressed())

        # Options
        self.config = ConfigParser()
        self.config_contents = self.config.read(config_dir)
        self.editor = self.config.get('Options', 'editor')
        # choose for external editor
        self.check_external_editor()
        editor_choose_btn = self.external_editor_choose
        editor_choose_btn.clicked.connect(lambda: self.set_external_editor())

    # Env Manager
    # -----------------------------------------#
    # this section is to set tree widget at app
    def set_env_path_tree(self):
        tree = self.env_path_tree
        tree.header().setMinimumSectionSize(200)
        for i in range(len(package_file_path_list)):
            # add houdini search path to top level
            top_level = QTreeWidgetItem(tree)
            top_level.setExpanded(True)
            top_level.setText(0, package_file_path_list[i])
            top_lvl_path = check_path(package_file_path_list[i])
            top_level.setData(1, 0, top_lvl_path)
            files = self.file_dict[package_file_path_list[i]]
            # add children to top level with json file name
            if files:
                for j in range(len(files)):
                    package_file_level = QTreeWidgetItem(top_level)
                    package_file_level.setText(0, files[j])
                    package_file_level.setData(1, 0, top_lvl_path + '/' + files[j])
            else:
                pass

    def set_packages_tree(self, cur_item: QTreeWidgetItem):
        pacs_tree = self.packages_tree
        item_name = QTreeWidgetItem.text(cur_item, 0)
        parent = QTreeWidgetItem.parent(cur_item)
        if parent:
            parent_name = QTreeWidgetItem.text(parent, 0)
        else:
            parent_name = ''
        # find packages folders
        pac_folders = []
        if item_name.endswith('.json'):
            files = self.file_dict.get(parent_name)
            if item_name in files:
                file_dir = check_path(parent_name) + '/' + item_name
                try:
                    # print(PackageFile(file_dir).data)
                    pac_folders = PackageFile(file_dir).data['houdini_path']
                except KeyError:
                    pass
                for i in range(len(pac_folders)):
                    if pac_folders[i]:
                        pac_folder = check_path_with_hpp(pac_folders[i], file_dir)
                        top_level = QTreeWidgetItem(pacs_tree)
                        top_level.setExpanded(True)
                        folder_name = pac_folder.split('/')[-1]
                        # print(pac_folder)
                        top_level.setText(0, folder_name)
                        top_level.setData(1, 0, pac_folder)
                    else:
                        pass
            else:
                pass
        else:
            pass

    def set_package_files_tree(self, cur_item: QTreeWidgetItem):
        pacs_tree = self.package_files_tree
        item_name = QTreeWidgetItem.text(cur_item, 0)
        parent = QTreeWidgetItem.parent(cur_item)
        if parent:
            parent_name = QTreeWidgetItem.text(parent, 0)
        else:
            parent_name = ''
        # find packages folders
        pacf_paths = []
        if item_name.endswith('.json'):
            files = self.file_dict.get(parent_name)
            if item_name in files:
                file_dir = check_path(parent_name) + '/' + item_name
                try:
                    # print(PackageFile(file_dir).data)
                    pacf_paths = PackageFile(file_dir).data['package_path']
                except KeyError:
                    pass
                for i in range(len(pacf_paths)):
                    pacf_path = check_path_with_hpp(pacf_paths[i], file_dir)
                    if os.path.exists(pacf_path):
                        subf = search_package_files(pacf_path)
                        path_level = QTreeWidgetItem(pacs_tree)
                        path_level.setExpanded(True)
                        path_level.setText(0, (pacf_path.split('/')[-1] + f'{i}'))
                        path_level.setData(1, 0, pacf_path)
                        fnames = subf[pacf_path]
                        for j in range(len(fnames)):
                            file_level = QTreeWidgetItem(path_level)
                            file_level.setExpanded(True)
                            file_level.setText(0, fnames[j])
                            file_level.setData(1, 0, (pacf_path + '/' + fnames[j]))
                    else:
                        pass
            else:
                pass
        else:
            pass

    def on_env_path_tree_item_clicked(self):
        # clear tree items
        self.env_path_tree.itemClicked.connect(self.packages_tree.clear())
        self.env_path_tree.itemClicked.connect(self.package_files_tree.clear())

        current_item = self.env_path_tree.currentItem()
        self.set_packages_tree(current_item)
        self.set_package_files_tree(current_item)

    # -----------------------------------------#
    # this function is used for open file or folder
    # by double click the item on the tree widget
    def open(self, cur_item: QTreeWidgetItem):
        parent = QTreeWidgetItem.parent(cur_item)
        if parent:
            parent_name = QTreeWidgetItem.text(parent, 0)
            if parent_name:
                fdir = QTreeWidgetItem.data(cur_item, 1, 0)
                if os.path.isfile(fdir):
                    subprocess.Popen([r'{}'.format(self.editor), r'{}'.format(fdir)])
                elif os.path.isdir(fdir):
                    webbrowser.open(fdir)
        else:
            fdir = QTreeWidgetItem.data(cur_item, 1, 0)
            if os.path.isdir(fdir):
                webbrowser.open(fdir)

    # refresh all the tree widgets
    def on_refresh_btn_clicked(self):
        self.env_path_tree.clear()
        self.packages_tree.clear()
        self.package_files_tree.clear()
        self.set_env_path_tree()

    # Env Creator
    # if folder chooser button clicked, select a folder path
    def set_folder_path(self):
        default_path = os.getcwd()
        file_path = QFileDialog.getExistingDirectory(self, "Choose Path", default_path)
        self.FolderPath.setText(file_path)

    # whether custom json file name
    def set_custom_name_frame(self):
        if self.custom_json_name.isChecked():
            self.custom_name_frame.setEnabled(True)
        else:
            self.custom_name_frame.setEnabled(False)

    # read the contents in the two text line edit
    def get_json_name(self):
        if self.custom_json_name.isChecked():
            name_at_home = self.name_at_home.text()
            name_at_package = self.name_at_package.text()
            return [name_at_home, name_at_package]
        else:
            env_folder_name = os.path.split(self.FolderPath.text())[-1]
            return [env_folder_name, env_folder_name]

    # open the preset contents file stored at 'dyl_script_path'
    @staticmethod
    def open_preset_contents_file(folder_path, location='Home'):
        config_dir = dyl_script_path + '/config.ini'
        config = ConfigParser()
        config.read(config_dir)
        editor = config.get('Options', 'editor')
        if location == 'Home':
            file_dir = folder_path + '/contents_to_home.json'
            subprocess.Popen([r'{}'.format(editor), r'{}'.format(file_dir)])
        elif location == 'Package':
            file_dir = folder_path + '/contents_to_package.json'
            subprocess.Popen([r'{}'.format(editor), r'{}'.format(file_dir)])
        else:
            return None

    # on create button pressed
    def on_create_button_pressed(self):
        if self.create_sub_folder():
            self.create_json_file(location='Home')
            self.create_json_file(location='Package')

    # write the preset contents to the new file that to be created
    def write_contents(self, json_file_dir, contens_file_name, home_name, package_name, location='Home'):
        with open(json_file_dir, 'w') as json_file:
            preset_contents_dir = dyl_script_path + '/' + f'{contens_file_name}'
            with open(preset_contents_dir) as preset:
                contents = preset.read()
                if location == 'Home':
                    contents = contents.replace('@___HOME_NAME___@', home_name)
                    contents = contents.replace('@___FOLDER_PATH___@', self.FolderPath.text())
                    contents = json.loads(contents)
                    json.dump(contents, json_file, indent=4, sort_keys=True)
                elif location == 'Package':
                    contents = contents.replace('@___HOME_NAME___@', home_name)
                    contents = contents.replace('@___PACKAGE_NAME___@', package_name)
                    contents = json.loads(contents)
                    json.dump(contents, json_file, indent=4, sort_keys=True)
                else:
                    raise ValueError
                preset.close()
                json_file.close()
                text = json_file_dir.split('/')[-1]
                hou.ui.displayMessage(f'Success to create {text}!', buttons=('OK',))

    # create all the sub package folder which are checked true
    def create_sub_folder(self):
        # Check whether the check boxes are enabled or not
        check_boxes = self.frame_6.findChildren(QCheckBox)
        # Get sub folder list
        sub_folder_list = []

        for check_box in check_boxes:
            if check_box.isChecked():
                name = check_box.text()
                sub_folder_list.append(name)

        # Create sub folder
        folder_path = self.FolderPath.text()

        if folder_path == '':
            QMessageBox.critical(self, "Critical", "Please choose or input the folder path!", QMessageBox.Ok)
            return False
        else:
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            for sub_folder in sub_folder_list:
                sub_folder_path = folder_path + '/' + sub_folder
                if not os.path.exists(sub_folder_path):
                    os.makedirs(sub_folder_path)
            return True

    # create two new json files to the path given by user
    def create_json_file(self, location):
        # Confirm the create info
        # get json file name to write
        location = location
        home_name = self.get_json_name()[0]
        package_name = self.get_json_name()[1]
        if home_name == '' or package_name == '':
            # Error by none name
            QMessageBox.critical(self,
                                 'Except name',
                                 f'Please input json file name at {location} while custom name check box is checked!',
                                 QMessageBox.Ok)
        else:
            # get preset contents file directory and set contents file name
            if location == 'Home':
                json_to_home_path = hou.getenv('HOUDINI_USER_PREF_DIR')
                json_file_dir = json_to_home_path + '/packages/' + f'{home_name}.json'
                contens_file_name = 'contents_to_home.json'
            elif location == 'Package':
                json_file_dir = self.FolderPath.text() + '/packages/' + f'{package_name}.json'
                contens_file_name = 'contents_to_package.json'
            else:
                return None

            if os.path.exists(json_file_dir):
                reply = QMessageBox.warning(self,
                                            'Except Name',
                                            f'The json file at "{json_file_dir}" have already exist, '
                                            f'are you sure to replace it?',
                                            QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.write_contents(json_file_dir, contens_file_name, home_name, package_name,
                                        location)
            else:
                self.write_contents(json_file_dir, contens_file_name, home_name, package_name,
                                    location)

    # Options
    # check whether the external editor dir is valid, if not, set it to notepad.exe
    def check_external_editor(self):
        if not self.editor:
            self.config.set('Options', 'editor', default_editor_dir)
            with open(config_dir, 'w') as config_file:
                self.config.write(config_file)
            return self.external_editor_dir.setText(default_editor_dir)
        else:
            if os.path.exists(self.editor):
                return self.external_editor_dir.setText(self.editor)
            else:
                self.config.set('Options', 'editor', default_editor_dir)
                with open(config_dir, 'w') as config_file:
                    self.config.write(config_file)
                return self.external_editor_dir.setText(default_editor_dir)

    # custom the external editor when running
    def set_external_editor(self):
        default_dir = os.getcwd()
        file_path = QFileDialog.getOpenFileName(self,
                                                "Choose Editor",
                                                default_dir,
                                                '*.exe')
        choosen_path = str(file_path[0])
        self.external_editor_dir.setText(choosen_path)

        self.editor = self.external_editor_dir.text()
        self.config.set('Options', 'editor', self.editor)
        with open(config_dir, 'w') as config_file:
            self.config.write(config_file)
        self.check_external_editor()


widget = EnvMaster()
widget.show()
