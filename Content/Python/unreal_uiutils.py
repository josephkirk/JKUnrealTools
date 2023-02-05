import unreal

from unreal import ToolMenus, ToolMenu, ToolMenuEntry, ToolMenuEntryScript, ToolMenuEntryScriptData, ToolMenuInsertType, UserInterfaceActionType, AppReturnType, EditorDialog

# Singlon that store main ToolMenus object and handle/store all registered new menu
def get_toolmenus()-> ToolMenus:
    return unreal.ToolMenus.get()

def refresh_toolmenus():
    get_toolmenus().refresh_all_widgets()

def extend_toolmenus(new_menu:str) -> ToolMenu:
    return get_toolmenus().extend_menu(new_menu)

# Get Main Menu

def get_mainmenu() -> ToolMenu:
    return find_menu("MainFrame.MainMenu")

def get_file_menu() -> ToolMenu:
    return find_menu("MainFrame.MainMenu.File")

def get_edit_menu() -> ToolMenu:
    return find_menu("MainFrame.MainMenu.Edit")

def get_asset_menu() -> ToolMenu:
    return find_menu("MainFrame.MainMenu.Window")

def get_window_menu() -> ToolMenu:
    return find_menu("MainFrame.MainMenu.Help")

def get_mainmenu_item(name) -> ToolMenu:
    return find_menu("MainFrame.MainMenu.{}".format(name))

# Get Toolbar

def find_menu(menu_name:str) -> ToolMenu:
    return get_toolmenus().find_menu(menu_name)

def get_toolbar() -> ToolMenu:
    return find_menu("LevelEditor.LevelEditorToolBar.PlayToolBar")

def get_staticmesh_toolbar() -> ToolMenu:
    return find_menu("AssetEditor.StaticMeshEditor.ToolBar")

def get_skeletalmesh_toolbar() -> ToolMenu:
    return find_menu("AssetEditor.SkeletalMeshEditor.ToolBar")

# Get Toolbar SubMenu

def get_buildcombo_sub_menu() -> ToolMenu:
    return find_menu("LevelEditor.LevelEditorToolBar.BuildComboButton")

def get_buildcombo_ligtingquality_sub_menu() -> ToolMenu:
    return find_menu("LevelEditor.LevelEditorToolBar.BuildComboButton.LightingQuality")

def get_buildcombo_ligtinginfo_sub_menu() -> ToolMenu:
    return find_menu("LevelEditor.LevelEditorToolBar.BuildComboButton.LightingInfo")

def get_buildcombo_ligtingdensity_sub_menu() -> ToolMenu:
    return find_menu("LevelEditor.LevelEditorToolBar.BuildComboButton.LightingInfo.LightingDensity")

def get_buildcombo_ligtingresolution_sub_menu() -> ToolMenu:
    return find_menu("LevelEditor.LevelEditorToolBar.BuildComboButton.LightingInfo.LightingResolution")

def get_leveltoolbar_setttings_sub_menu() -> ToolMenu:
    return find_menu("LevelEditor.LevelEditorToolBar.LevelToolbarQuickSettings")

def get_sourcecontrol_sub_menu() -> ToolMenu:
    return find_menu("LevelEditor.LevelEditorToolBar.SourceControl")

def get_editormodes_sub_menu() -> ToolMenu:
    return find_menu("LevelEditor.LevelEditorToolBar.EditorModes")

def get_openblueprint_sub_menu() -> ToolMenu:
    return find_menu("LevelEditor.LevelEditorToolBar.OpenBlueprint")

def get_cinematics_sub_menu() -> ToolMenu:
    return find_menu("LevelEditor.LevelEditorToolBar.Cinematics")

def get_compilecombo_sub_menu() -> ToolMenu:
    return find_menu("LevelEditor.LevelEditorToolBar.CompileComboButton")

# Get Context Menu

def get_asset_context_menu() -> ToolMenu:
    return find_menu("ContentBrowser.AssetContextMenu")

def get_folder_context_menu() -> ToolMenu:
    return find_menu("ContentBrowser.FolderContextMenu")

def get_actor_context_menu() -> ToolMenu:
    return find_menu("LevelEditor.ActorContextMenu")

def get_dragdrop_context_menu() -> ToolMenu:
    return find_menu("ContentBrowser.DragDropContextMenu")

def get_sequence_asset_context_menu() -> ToolMenu:
    return find_menu("ContentBrowser.AssetContextMenu.LevelSequence")

def get_cameraanim_asset_context_menu() -> ToolMenu:
    return find_menu("ContentBrowser.AssetContextMenu.CameraAnim")

def get_mediaplayer_assetpicker_context_menu() -> ToolMenu:
    return find_menu("MediaPlayer.AssetPickerAssetContextMenu")

def get_soundwave_asset_context_menu() -> ToolMenu:
    return find_menu("ContentBrowser.AssetContextMenu.SoundWave")

def get_addnew_context_menu() -> ToolMenu:
    return find_menu("ContentBrowser.AddNewContextMenu")

def get_toolbar_item(name) -> ToolMenu:
    return find_menu(
        "LevelEditor.LevelEditorToolBar.{}".format(name)
    )


# Utils Functions


def create_python_tool_menu_entry(
    name:str, label:str, owner:str = "None", command_string:str="", entry_type: unreal.MultiBlockType =unreal.MultiBlockType.MENU_ENTRY
) -> ToolMenuEntry:
    menu_entry = ToolMenuEntry(name, unreal.ToolMenuOwner(owner), type=entry_type)
    menu_entry.set_label(label)
    if command_string:
        menu_entry.set_string_command(
            unreal.ToolMenuStringCommandType.PYTHON, "python", command_string
        )
    return menu_entry

def create_toolbar_button(
    name:str, label:str, section_name:str="", icons =["EditorStyle", "LevelEditor.EditorModes", "LevelEditor.EditorModes"], command_string="", register_button=True
) -> ToolMenuEntry:
    button = create_python_tool_menu_entry(
        name, label, command_string, entry_type=unreal.MultiBlockType.TOOL_BAR_BUTTON
    )
    button.set_icon(*icons)
    if register_button:
        get_toolbar().add_menu_entry(section_name, button)
    return button


def create_toolbar_combo_button(name, section_name, tool_tip="", register_button=True) -> ToolMenuEntry:
    # menu_name = ".".join([str(get_toolbar().menu_name),menu])
    # section_name = ".".join([str(get_toolbar().menu_name), menu, section])
    # get_toolbar().add_section(section_name)
    # menu_entry_script = EditorToolbarMenuEntry(get_toolbar().menu_name, section_name, name, "", tool_tip, ["EditorStyle", "DetailsView.PulldownArrow.Down", "DetailsView.PulldownArrow.Down"], get_toolbar().menu_name, ["None", unreal.ToolMenuInsertType.DEFAULT], ["None", unreal.MultiBlockType.TOOL_BAR_COMBO_BUTTON, unreal.UserInterfaceActionType.BUTTON, True, True, True, False])
    # menu_entry_script.register_menu_entry()
    menu_entry = ToolMenuEntry(
        name, type=unreal.MultiBlockType.TOOL_BAR_COMBO_BUTTON
    )
    if register_button:
        get_toolbar().add_menu_entry(section_name, menu_entry)
    return menu_entry


def create_editable_text(name, label) -> ToolMenuEntry:
    menu_entry = ToolMenuEntry(name, type=unreal.MultiBlockType.EDITABLE_TEXT)
    menu_entry.set_label(label)
    return menu_entry


def create_widget(name) -> ToolMenuEntry:
    return ToolMenuEntry(name, type=unreal.MultiBlockType.WIDGET)


def create_heading(name) -> ToolMenuEntry:
    return ToolMenuEntry(name, type=unreal.MultiBlockType.HEADING)


def create_separator(name="Separator") -> ToolMenuEntry:
    return ToolMenuEntry(name, type=unreal.MultiBlockType.SEPARATOR)


def extend_mainmenu_item(mainmenu_name, section_name, name, label, tooltips="") -> ToolMenu:
    parent_menu = get_mainmenu_item(mainmenu_name)
    return parent_menu.add_sub_menu(
        parent_menu.menu_name, section_name, name, label, tooltips
    )

def extend_file_menu(section_name, name, label, tooltips="") -> ToolMenu:
    extend_mainmenu_item("File", section_name, name, label, tooltips="")

def extend_edit_menu(section_name, name, label, tooltips="") -> ToolMenu:
    extend_mainmenu_item("Edit", section_name, name, label, tooltips="")

def extend_asset_menu(section_name, name, label, tooltips="") -> ToolMenu:
    extend_mainmenu_item("Asset", section_name, name, label, tooltips="")

def extend_mesh_menu(section_name, name, label, tooltips="") -> ToolMenu:
    extend_mainmenu_item("Mesh", section_name, name, label, tooltips="")

def extend_help_menu(section_name, name, label, tooltips="") -> ToolMenu:
    extend_mainmenu_item("Help", section_name, name, label, tooltips="")

def extend_mainmenu(name, label, tooltip="") -> ToolMenu:
    main_menu = get_mainmenu()
    return main_menu.add_sub_menu(
        main_menu.menu_name, unreal.Name(), f"{main_menu.menu_name}.{name}", label, tooltip
    )

def extend_toolmenu(owner, name, label, section_name=unreal.Name(), tooltip="") -> ToolMenu:
    return owner.add_sub_menu(
        owner.menu_name, section_name, "{owner.menu_name}.{name}", label, tooltip
    )

def extend_toolbar(name, label, tooltip="") -> ToolMenu:
    toolbar = get_toolbar()
    return toolbar.add_sub_menu(toolbar.menu_name, unreal.Name(), name, label, tooltip)

def add_sequencer_toolbarbutton(
    name, label, section_name="Asset", icons = None, command_string="", register_button=True
) -> ToolMenuEntry:
    button = create_python_tool_menu_entry(
        name, label, command_string, entry_type=unreal.MultiBlockType.TOOL_BAR_BUTTON
    )
    if icons:
        button.set_icon(*icons)
    if register_button:
        get_sequencer_toolbar().add_menu_entry(section_name, button)
    return button

def parent_qt_window(qt_widget):
    unreal.parent_external_window_to_slate(qt_widget.winId())

def show_message(title, message, message_type, default_value=unreal.AppReturnType.NO) -> AppReturnType:
    return EditorDialog.show_message(title, message, message_type, default_value)
