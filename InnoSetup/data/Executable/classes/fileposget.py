import win32gui
import win32con
import time

def get_desktop_icons_positions(max_retries=5):
    positions = {}
    retries = 0

    while retries < max_retries:
        try:
            # Find the handle to the desktop window
            desktop = win32gui.GetDesktopWindow()

            # Find the list view control that contains the icons
            progman = win32gui.FindWindow("Progman", None)
            if not progman:
                raise RuntimeError("Could not find Progman window.")

            # Send a message to the shell to refresh the desktop, ensuring icons are loaded
            win32gui.SendMessageTimeout(progman, 0x052C, 0, 0, win32con.SMTO_NORMAL, 1000)

            # Find the desktop list view control
            hwnd = 0
            while True:
                print(f"Attempt {retries}/{max_retries}")
                hwnd = win32gui.FindWindowEx(desktop, hwnd, "SysListView32", None)
                if not hwnd:
                    print("no hwnd, fuck")

                # Get the number of icons
                num_icons = win32gui.SendMessage(hwnd, win32con.LVM_GETITEMCOUNT)

                for index in range(num_icons):
                    # Get the position of each icon
                    lvitem = win32gui.LVITEM()
                    lvitem.mask = win32con.LVIF_TEXT | win32con.LVIF_PARAM
                    lvitem.iItem = index
                    lvitem.iSubItem = 0
                    buffer = win32gui.PyMakeBuffer(255)
                    lvitem.pszText = buffer
                    lvitem.cchTextMax = len(buffer)
                    win32gui.SendMessage(hwnd, win32con.LVM_GETITEMTEXT, index, lvitem)
                    text = buffer[:lvitem.cchTextMax].decode('utf-16')

                    # Get the position of the icon
                    rect = win32gui.GetWindowRect(hwnd)
                    x, y, _, _ = rect
                    positions[text] = (x, y)

            # If we successfully retrieved positions, break out of the loop
            break

        except Exception as e:
            print(f"Error retrieving desktop icons: {e}")
            retries += 1
            time.sleep(1)  # Wait before retrying

    return positions

# Example usage
if __name__ == "__main__":
    desktop_positions = get_desktop_icons_positions(100)
    if desktop_positions:
        print("Desktop icon positions:")
        for name, pos in desktop_positions.items():
            print(f"{name}: {pos}")
    else:
        print("No desktop icons found or error retrieving positions.")
input()