import configparser

def save():
    with open('3DPrinter.conf', 'w') as config_file:
        configuration.write(config_file)
def defaultValues():
    #configuration = configparser.SafeConfigParser()
    configuration.add_section('Server')
    configuration.set('Server','PORT','8080')
    configuration['Printers'] = {'Printer1': {'Alias': 'P1', 'Serial Port': 'Serial1'}, 'Printer2': {'Alias': 'P2', 'Serial Port': 'Serial2'}}
    save()

configuration = configparser.SafeConfigParser()

try:
    #with open('Asmo.conf','r') as config_file:
    configuration.read('3DPrinter.conf')
    print(configuration.get('Server','port'))
except:
    defaultValues()

def setValues(newSettings):
    try:
        for section in newSettings:
            for setting in newSettings[section]:
                if configuration.has_section(section):
                    configuration.set(section,setting[0],setting[1])
                else:
                    configuration.add_section(section)
                    configuration.set(section,setting[0],setting[1])
        save()
        return 'Successfully changed the settings. Please restart the server to reload them.'
    except Exception as e:
        return e
