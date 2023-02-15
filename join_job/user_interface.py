import data_provider as prov
import logger as log

def tempereture_viev(senson):
    data = prov.get_temperature(senson)
    log.temperature_logger(data)
    return data


def pressure_viev(senson):
    data = prov.get_pressure(senson)
    log.pressure_logger(data)
    return data


def wind_speed_viev(senson):
    data = prov.get_wind_speed(senson)
    log.wind_speed_logger(data)
    return data