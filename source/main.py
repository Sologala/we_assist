from controllers import *
from enum import IntEnum
import os


class cmd_header(IntEnum):
    exit = 0
    get_all_imgs = 1

def show_cmd_helper() :
    help_str = " \n" + str(int(cmd_header.exit)) + " : exit"
    help_str += " \n" + str(int(cmd_header.get_all_imgs)) + ' : get all head imgs'
    return help_str

def main() :
    v_world_controller = world_controller.world_controller()
    v_world_controller.start()

    cmd = -1
    print( show_cmd_helper() )
    while True:
        cmd = input()
        if cmd == str(int(cmd_header.exit)):
            #exit
            v_world_controller.close()
            break 
        elif cmd == str(int(cmd_header.get_all_imgs)):
            v_world_controller.v_itchat_controller.get_all_friend_head_imgs()
            print('done')
        else :
            print(show_cmd_helper())

    try :
        sys.exit()
    except Exception as e :

        # I don't know how to exit itchat thread gracefully
        # I can't call logout in itchat as I don't want to scan qr code every time
        os._exit(0)
        pass


main()