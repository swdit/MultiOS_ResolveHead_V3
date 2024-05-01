import sys

# defining multi OS Resolve loader
def load_resolve():
    # Set the path to the DaVinci Resolve Scripting API accordingly
    if sys.platform.startswith("win"):
        sys.path.append("C:/ProgramData/Blackmagic Design/DaVinci Resolve/Support/Developer/Scripting/Modules/")
    elif sys.platform.startswith("darwin"):
        sys.path.append("/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules/")
    elif sys.platform.startswith("linux"):
        sys.path.append("/opt/resolve/libs/Fusion/")

    try:
        import DaVinciResolveScript as dvr_script
        print("DaVinciResolveScript module loaded successfully.")
    except ImportError as e:
        print("Error loading DaVinciResolveScript module:", e)
        sys.exit(1)

    # Attempt to initialize the DaVinci Resolve application
    resolve = dvr_script.scriptapp("Resolve")
    if resolve is None:
        print("Could not initialize the DaVinci Resolve application. Is DaVinci Resolve open?")
    else:
        print("DaVinci Resolve application successfully initialized.")

    # Attempt to get the ProjectManager object
    project_manager = resolve.GetProjectManager()
    if project_manager is None:
        print("Could not access the ProjectManager.")
    else:
        print("ProjectManager successfully retrieved.")

    # Attempt to get the current project
    project = project_manager.GetCurrentProject()
    if project is None:
        print("No current project loaded.")
    else:
        print(f"Current project '{project.GetName()}' successfully loaded.")

    return dvr_script, resolve, project_manager, project

# execute load_resolve function
dvr_script, resolve, project_manager, project = load_resolve()

# basic resolve loading of current assets
media_pool = project.GetMediaPool()
current_folder = media_pool.GetCurrentFolder()
clip_list = current_folder.GetClipList()