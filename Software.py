# import psutil

# def get_running_processes():
#     for proc in psutil.process_iter(['name', 'status']):
#         try:
#             if proc.info['status'] == psutil.STATUS_RUNNING:
#                 print(proc.info['name'])
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             pass

# if __name__ == "__main__":
#     print("Currently running processes:")
#     get_running_processes()



# import psutil

# def get_user_opened_apps():
#     user_apps = []
#     for proc in psutil.process_iter(['name', 'exe', 'status']):
#         try:
#             # Filter for running processes with a GUI
#             if proc.info['status'] == psutil.STATUS_RUNNING and proc.info['exe']:
#                 # This list can be expanded based on common user applications
#                 if proc.info['name'] in [
#                     'Asana.exe', 'brave.exe', 'chrome.exe', 'MySQLWorkbench.exe',
#                     'notepad.exe', 'slack.exe', 'Taskmgr.exe', 'Code.exe', 'winbox64.exe',
#                     'explorer.exe'
#                 ]:
#                     user_apps.append(proc.info['name'])
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             pass
#     return list(set(user_apps))  # Remove duplicates

# if __name__ == "__main__":
#     print("Currently open user applications:")
#     for app in get_user_opened_apps():
#         print(app)



import psutil
import win32gui
import win32process

def get_open_windows():
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            hwnds.append((hwnd, pid))
        return True
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds

def get_user_opened_apps():
    open_windows = get_open_windows()
    user_apps = {}
    
    for _, pid in open_windows:
        try:
            process = psutil.Process(pid)
            app_name = process.name()
            if app_name not in user_apps:
                user_apps[app_name] = {
                    'name': app_name,
                    'exe': process.exe(),
                    'memory_usage': process.memory_info().rss / (1024 * 1024)  # Convert to MB
                }
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    return list(user_apps.values())

if __name__ == "__main__":
    print("Currently open user applications:")
    for app in get_user_opened_apps():
        print(f"Name: {app['name']}")
        print(f"Executable: {app['exe']}")
        print(f"Memory Usage: {app['memory_usage']:.2f} MB")
        print("-----------------------")