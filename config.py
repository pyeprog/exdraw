import os


FuncType = {"draw_single_shapely" : 0,
            "draw_shapely_one_by_one" : 1,
            "draw_all_shapely" : 2,
            "compare_two_shapely": 3}

cwd = os.path.dirname(__file__)
cwd = "./" if len(cwd) == 0 else cwd
inject_path = os.getcwd()
inject_path = "./" if len(inject_path) else inject_path
info_dict = {"cwd": cwd,
             "inject_path": inject_path,
             "inject_module_path": os.path.join(inject_path, "_probe"),
             "module_src_path": os.path.join(cwd, "probe"),
             "watching_path": os.path.join(cwd, "watching"),
             "probe_config_path": os.path.join(cwd, "probe", "_config"),
             "func_type": FuncType}
 

