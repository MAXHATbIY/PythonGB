from user_interface import tempereture_viev
from user_interface import wind_speed_viev
from user_interface import pressure_viev

def create(device = 1):
    xml = '<xml>\n'
    xml += '   <temperature units = "c">{}</temperature>\n'\
        .format(tempereture_viev(device))
    xml += '   <wind_speed_viev units = "m/s">{}</wind_speed_viev>\n'\
        .format(wind_speed_viev(device))
    xml += '   <pressure units = "mnHg">{}</pressure>\n'\
        .format(pressure_viev(device))
    xml += '   </xml>'

    with open('data.xml', 'w') as page:
        page.write(xml)
    
    return xml


def new_create(data, device = 1):
    t, p, w = data
    t = t * 1.8 + 32
    xml = '<xml>\n'
    xml += '   <temperature units = "f">{}</temperature>\n'\
        .format(t)
    xml += '   <wind_speed_viev units = "m/s">{}</wind_speed_viev>\n'\
        .format(w)
    xml += '   <pressure units = "mnHg">{}</pressure>\n'\
        .format(p)
    xml += '   </xml>'

    with open('new_data.xml', 'w') as page:
        page.write(xml)
    
    return data