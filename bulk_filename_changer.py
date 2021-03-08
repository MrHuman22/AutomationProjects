import os

path = r"C:\Users\pwn394\The University of Newcastle\SEC - SEC\RESOURCES\Activities\Teacher PD Development\Crash Course CAD\Online Course Assets and Plan\02 Phase 2 - Reverse Engineering\QR Codes"


file_list = os.listdir(path)
# [print(file) for file in file_list]


def remove_start(file_name: str) -> str:
    return file_name[15:]

def append_QR(file_name: str) -> str:
    return f"{file_name[:1]}_QR_{file_name[2:]}"

path2 = r"C:\Users\pwn394\The University of Newcastle\SEC - SEC\RESOURCES\Activities\Teacher PD Development\Crash Course CAD\Online Course Assets and Plan\02 Phase 2 - Reverse Engineering\New Reverse Engineering\Fusion 360 QR Codes V2"
file_list2 = os.listdir(path2)

from_clipboard = """
B_F360_Telescope Lens Cap.png
C_F360_Surface Skimmer Guard.png
D_F360_Hex.png
E_F360_Door Handle.png
F_F360_Light Switch Knob.png
G_F360_Bearing Spindle.png
H_F360_Toothpaste Squeezer.png
I_F360_Door Hold.png
J_F360_AAA Battery Dispenser.png
K_F360_UHooks.png
L_F360_MicroSD Card Holder.png
M_F360_SD Card Holder Lvl2.png
N_F360_Simple SD Card Holder.png
O_F360_Self-Watering Planter.png
P_F360_Wrench.png
Q_F360_Door Stop.png
R_F360_Dyson Vacuum Nozzle.png
S_F360_Phone Stand.png
"""

f360_file_list = from_clipboard.split("\n")
# print(f360_file_list[1:len(f360_file_list)-2])

f360_names = f360_file_list[1:len(f360_file_list)-1]
# print(f360_names)



for eachSrc, eachDst in zip(file_list2,f360_names):
    # print(f"{eachSrc} --> {eachDst}")
    src = os.path.join(path2,eachSrc)
    dst = os.path.join(path2,eachDst )
    # print(f"Source: {src}\nTarget: {dst}\n\n")
    os.rename(src, dst)