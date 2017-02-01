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
        else:
            self._ip = ""
            self._date = ""
            self._time = ""
            self._file = ""
            self._referrer = ""

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


class LogSearch:
    def __init__(self, filename, log_reader=LogReader()):
        self._log_items = log_reader.read_log(filename)
        self._strategy = ""
        self._results = set()

    def execute(self):
        query_result = [self._log_items[i].entry() for i in self._results]

        self._strategy = ""
        self._results = set()

        return query_result

    def inclusive(self):
        self._strategy = "incl"
        return self

    def exclusive(self):
        self._strategy = "excl"
        return self

    def _step_query(self, query, filter_func):
        if self._results and not self._strategy:
            raise SyntaxError("Two queries were performed without setting the strategy")

        matches = set([index for index, log in enumerate(self._log_items) if (filter_func(query, log))])
        prior_results = self._results

        if prior_results:
            if self._strategy == "incl":
                self._results = prior_results.union(matches)
            else:
                self._results = prior_results.intersection(matches)
        else:
            self._results = matches

    def ip(self, query):
        filter_func = lambda qry, log: qry in log.ip()
        self._step_query(query, filter_func)
        return self

    def date(self, query):
        filter_func = lambda qry, log: qry == log.date()
        self._step_query(query, filter_func)
        return self

    def time(self, query):
        filter_func = lambda qry, log: qry == log.time()
        self._step_query(query, filter_func)
        return self

    def file(self, query):
        filter_func = lambda qry, log: qry in log.file()
        self._step_query(query, filter_func)
        return self

    def referrer(self, query):
        filter_func = lambda qry, log: qry in log.referrer()
        self._step_query(query, filter_func)
        return self


if __name__ == '__main__':
    None
