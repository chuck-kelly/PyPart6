from typing import Iterable, Tuple


def convert_to_celsius(fahrenheit_temp: float) -> float:
    """
    Given a float representing a temperature in fahrenheit, return the corresponding value in celsius.

    :param fahrenheit_temp: A float representing a temperature in fahrenheit
    :return: A float representing the corresponding value of the fahrenheit_temp parameter in celsius
    """
    return round((fahrenheit_temp-32)/1.8,2)


def convert_to_fahrenheit(celsius_temp: float) -> int:
    """
    Given a float representing a temperature in celsius, return the corresponding value in fahrenheit.

    :param celsius_temp: A float representing a temperature in celsius
    :return:  A float representing the corresponding value of the celsius_temp parameter in fahrenheit
    """
    temp = ( celsius_temp * 1.8 )+32
    return int(temp)


def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str) -> Tuple[Tuple[float, float]]:
    """
    Given a tuple or a list of temperatures, this function returns a tuple of tuples.
    Each tuple contains two values. The first is the value of the temperatures parameter. The second is the the value of
    the first converted to the unit of measurement specified in the input_unit_of_measurement parameter.

    :param temperatures: An iterable containing temperatures
    :param input_unit_of_measurement: The unit a measure to use to convert the values in the temperatures parameter
    :return: A tuple of tuples
    """
    list_of_temp_tuples=[]
    for temp_to_change in temperatures:
    
        if input_unit_of_measurement == 'f':
            new_temp = convert_to_celsius(temp_to_change)
            tup_of_temps =(temp_to_change,new_temp)
            list_of_temp_tuples.append(tup_of_temps)
        elif input_unit_of_measurement == 'c':
            new_temp = convert_to_fahrenheit(temp_to_change)
            tup_of_temps =(temp_to_change,new_temp)
            list_of_temp_tuples.append(tup_of_temps)
        
    tuple_of_tuple = tuple(list_of_temp_tuples)
    return tuple_of_tuple
    

    
