import json
from datetime import (timedelta,)
import pandas as pd

class Optimine(object):
    """

    """


    def __init__(self):
        """

        :param json:
        """

        self.__raw_json = None
        self.__start_time = None
        self.__end_time = None
        self.__profile = None
        self.__pressure = None
        self.__temperature = None
        self.__pressure_unit = None
        self.__pressure_unit_scale_factor = 1.0
        self.__acoustics = None
        self.__operator = None
        self.__pressure_sn = None
        self.__pressure_vessel = None
        self.__test_item = {}
        self.delimiter = '\t'
        self.line_ending = '\r\n'

    def read_json(self, filename):
        """

        :param filename:
        :return:
        """
        with open(filename, 'r') as fid:
            self.__raw_json = json.load(fid)

        # Get pressure unit
        self.__pressure_unit = self.__raw_json['PressureUnit']['Data']['Value']
        tmp_ = self.__pressure_unit.lower().strip()

        # Set the scale factor to convert to psi
        if tmp_ == 'psi':
            self.__pressure_unit_scale_factor = 1.0
        elif tmp_ == 'mpa':
            self.__pressure_unit_scale_factor = 145.03773773
        elif tmp_ == 'bar':
            self.__pressure_unit_scale_factor = 14.503773773
        elif tmp_ == 'msw':
            self.__pressure_unit_scale_factor = 1.4503773773

        # Get Start and Stop times
        self.__start_time = pd.to_datetime(self.__raw_json['StartTime']['Data']['Value'])
        self.__end_time = pd.to_datetime(self.__raw_json['EndTime']['Data']['Value'])

        # Get operator name
        self.__operator = self.__raw_json['ExecuteProfile']['Metadata']['Operator']

        # Pressure Transducer Serial Number
        self.__pressure_sn = self.__raw_json['PTSerialNumber']['Data']['Value']

        # Pressure Vessel "Install Name"
        self.__pressure_vessel = self.__raw_json['InstallationName']['Data']['Value']

        # Test Item metadata
        dict_ = self.__raw_json['TestItem']['Data']
        self.__test_item = dict(
            description=dict_['Description'],
            part_number=dict_['PartNumber'],
            serial_number=dict_['SerialNumber'],
            test_report=dict_['TestReport']
        )

        # Load pressure profile
        dict_ = self.__raw_json['Profile']['Data']['ListItems']
        size = len(dict_)
        tmp_ = {
            'pressure': [None] * size,
            'rate': [None] * size,
            'hold_time': [None] * size,
            'low_tolerance': [None] * size,
            'high_tolerance': [None] * size
        }

        for i, value in enumerate(dict_):
            tmp_['pressure'][i] = float(value['Pressure'])
            tmp_['hold_time'][i] = self.str2timedelta(value['HoldTime'])
            tmp_['rate'][i] = float(value['RateOfChange'])
            tmp_['low_tolerance'][i] = float(value['LowTolerance'])
            tmp_['high_tolerance'][i] = float(value['HighTolerance'])

        self.__profile = pd.DataFrame(data=tmp_, columns=['hold_time', 'pressure', 'rate', 'low_tolerance', 'high_tolerance'])

        # Load pressure data
        dict_ = self.__raw_json['Pressure']
        size = len(dict_)
        tmp_ = {
            'pressure': [None] * size,
            'timestamp': [None] * size
        }

        for i, value in enumerate(dict_):
            tmp_['pressure'][i] = float(value['Data']['Value']) * 145.038
            tmp_['timestamp'][i] = pd.to_datetime(value['Metadata']['DateTime'])

        self.__pressure = pd.Series(data=tmp_['pressure'], index=tmp_['timestamp'])

        # Load temperature data
        dict_ = self.__raw_json['Temperature']
        size = len(dict_)
        tmp_ = {
            'temperature': [None] * size,
            'timestamp': [None] * size
        }

        for i, value in enumerate(dict_):
            tmp_['temperature'][i] = float(value['Data']['Value'])
            tmp_['timestamp'][i] = pd.to_datetime(value['Metadata']['DateTime'])

        self.__temperature = pd.Series(data=tmp_['temperature'], index=tmp_['timestamp'])

    def read_acoustics(self, filename):
        raise NotImplementedError("Acoustic data not implemented yet")

    @classmethod
    def str2timedelta(cls, delta_string):
        """
        Convert a timedelta string in the format ddd:hh:mm:ss.ms into a python timedelta object

        Example:

        >>> OptimineJson.str2timedelta('2:04:30:20.32523').total_seconds()
        189020.32523

        >>> OptimineJson.str2timedelta('0:0:0:20.32523').total_seconds()
        20.32523

        :param delta_string:
        :return:
        """

        d, h, m, s = delta_string.split(':')
        return timedelta(days=int(d), hours=int(h), minutes=int(m), seconds=float(s))

    @property
    def delimiter(self):
        return self.__delim

    @delimiter.setter
    def delimiter(self, delim):
        if not isinstance(delim, str):
            raise ValueError("Delimiter is not of type 'str'")

        self.__delim = delim

    @property
    def line_ending(self):
        return self.__line_ending

    @line_ending.setter
    def line_ending(self, end):
        if not isinstance(end, str):
            raise ValueError("Line ending is not of type 'str'")

        self.__line_ending = end

    @property
    def pressure_unit(self):
        return self.__pressure_unit

    @property
    def pressure(self):
        return self.__pressure

    @property
    def operator(self):
        return self.__operator

    @property
    def pressure_vessel(self):
        return self.__pressure_vessel

    @property
    def pressure_transducer_serial_number(self):
        return self.__pressure_sn

    @property
    def test_description(self):
        return self.__test_item.get('description', '')

    @property
    def test_part_number(self):
        return self.__test_item.get('part_number', '')

    @property
    def test_serial_number(self):
        return self.__test_item.get('serial_number', '')

    @property
    def test_report(self):
        return self.__test_item.get('test_report', '')

    @property
    def profile(self):
        return self.__profile

    @property
    def temperature(self):
        return self.__temperature

    @property
    def acoustics(self):
        return self.__acoustics

    @property
    def start_time(self):
        return self.__start_time

    # @start_time.setter
    # def start_time(self, start):
    #     if not isinstance(start, pd.datetime):
    #         raise ValueError("Expected 'datetime' instance, found %s" % (type(start),))
    #     self.__start_time = start

    @property
    def end_time(self):
        return self.__end_time

    # @end_time.setter
    # def end_time(self, end):
    #     if not isinstance(end, pd.datetime):
    #         raise ValueError("Expected 'datetime' instance, found %s" % (type(end),))
    #     self.__end_time = end

    @property
    def raw_json(self):
        """
        Access the raw json dictionary

        :return:
        """
        if self.__raw_json is None:
            return None

        return self.__raw_json.copy()


    def to_dat(self, filename):
        """

        :param filename:
        :return:
        """

        if self.pressure is None:
            raise ValueError("No pressure data loaded")

        if self.pressure.empty:
            raise ValueError("Pressure data is empty!")

        # Start with a dataframe from the pressure series
        df = self.pressure.to_frame(name='pressure')

        # Add a column with the rounded integer value of the pressure
        df['pressure_int'] = df['pressure'].apply(pd.np.round, 'index').astype('int64')

        # Add a dummy volt column
        df['pressure_volts'] = df['pressure'] / (2500 / 10.013) - 0.013

        #
        # This is where we'll eventually use df.merge() to pull in acoustic data, but for now
        # we'll just add two more dummy columns
        #

        df['acoustic_count_interval'] = pd.np.nan
        df['acoustic_count_total'] = pd.np.nan

        # Now write out the file
        result = df.to_csv(
            filename,
            sep=self.delimiter,
            line_terminator=self.__line_ending,
            na_rep='',
            float_format='%.6f',
            columns=['pressure_volts', 'pressure', 'pressure_int', 'acoustic_count_interval', 'acoustic_count_total'],
            header=['Raw Pressure (V)', 'Presure (psi)', 'Pressure (psi)', 'Counts/Read Interval', 'Total Counts'],
            index=True,
            index_label='Time',
            date_format='%I:%M:%S.%f %p %m/%d/%Y',
        )

        if filename is None:
            return result
