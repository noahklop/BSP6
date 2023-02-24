import yaml


def write(arguments):
    try:
        name = arguments[1]

    except:
        name = ''

    last_char_index = name.rfind("/")

    directory = name[:last_char_index]

    file = name[last_char_index+1:]

    try:
        top = int(arguments[2])

    except:
        top = None

    try:
        extensions = [arguments[3]]

    except:
        extensions = []

    if directory and file:
        configuration = {'directory': directory,
                         'name': file,
                         'extensions': extensions,
                         'algorithms': {},
                         'top': top}

        file = open('configuration_command.yaml', 'w')

        yaml.dump(configuration, file)
