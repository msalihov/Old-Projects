def get(value):
    config = {}
    execfile('botconfig.conf', config)
    return config[value]