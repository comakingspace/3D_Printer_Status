import json

def save():
    with open('3DPrinter.json', 'w') as config_file:
        json.dump(configuration, config_file, indent=4, separators=(',', ': '))
def defaultValues():
    #configuration = configparser.SafeConfigParser()
    configuration['Server'] = {'Port': '8080'}
    configuration['Printers'] = {'Printer1': {'Alias': 'P1', 'Serial device': '/dev/ttyUSB0', 'type': 'Prusa Mk2'}, 'Printer2': {'Alias': 'P6', 'Serial device': '/dev/ttyUSB0', 'type': 'Prusa Mk2 MM'}}
    save()

configuration = {}

try:
    with open('3DPrinter.json') as config_file:
        configuration = json.load(config_file)
        print(configuration['Server'])
except:
    defaultValues()

def setValues(newSettings):
    try:
        for section in newSettings:
            for setting in newSettings[section]:
                if section in configuration:
                    configuration[section][setting[0]] = setting[1]
                else:
                    configuration[section] = {}
                    configuration[section][setting[0]] = setting[1]
        save()
        return 'Successfully changed the settings. Please restart the server to reload them.'
    except Exception as e:
        return e
