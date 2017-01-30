from utility import FileReader
import re


class LogReader:
    def __init__(self, file_reader=FileReader()):
        self._file_reader = file_reader

    def read_log(self, filename):
        file_contents = self._file_reader.read_file(filename)
        log_items = []

        for entry in file_contents.split('\n'):
            log_items.append(LogItem(entry))

        return log_items


class LogItem:
    def __init__(self, log_entry):
        expression = r'(?P<ip>[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+).*\[(?P<date>[0-9]{2}/[A-Za-z]{3}/[0-9]{4}):(?P<time>[' \
                     r'0-9]{2}:[0-9]{2}:[0-9]{2}).*] "[A-Z]* /?(?P<file>.*\..*) [A-Z]+/[0-9]+\.[0-9]+" [0-9]+ [0-9]+ ' \
                     r'"(?P<referrer>.*)" '
        p = re.compile(expression)

        match = p.match(log_entry)

        if match:
            self._ip = match.group("ip")
            self._date = match.group("date")
            self._time = match.group("time")
            self._file = match.group("file")
            self._referrer = match.group("referrer")

        self._entry = log_entry

    def ip(self):
        return self._ip

    def date(self):
        return self._date

    def time(self):
        return self._time

    def file(self):
        return self._file

    def referrer(self):
        return self._referrer

    def entry(self):
        return self._entry

# class LogSearch:


if __name__ == '__main__':
    None
