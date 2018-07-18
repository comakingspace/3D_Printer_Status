import ConfigParser


def save():
    with open('3DPrinter.conf', 'wb') as config_file:
        configuration.write(config_file)
def defaultValues():
    #configuration = ConfigParser.SafeConfigParser()
    configuration.add_section('Server')
    configuration.set('Server','PORT','8080')
    save()

configuration = ConfigParser.SafeConfigParser()

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


