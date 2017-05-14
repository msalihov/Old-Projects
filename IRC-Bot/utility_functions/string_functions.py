def datatostring(data):
    return str(data).strip()


def getsenderarr(sender):
    send_arr = sender.split('!')
    send_sub_arr = send_arr[1].split('@')
    return {'nickname': send_arr[0], 'hostname': send_sub_arr[1]}


def getsender(sender):
    send_arr = getsenderarr(sender)
    return send_arr['nickname']


def getdataarray(args):
    return {'sender': args[0][1:], 'type': args[1], 'target': args[2], 'msg': args[3][1:]}