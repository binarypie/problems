# Jesus Galvan's Solutions

This is a collection of solutions for the logs, common substring, common subsequence, essay monkey, and pig latin problems.


## Installation

You will need to have Python installed on your machine.

To verify that you have Python installed and configured correctly you can run the ```python --version``` command.

Once you have that, clone this repository to your machine with ```git clone https://github.com/newbootz/problems``` and you can begin running the solutions.

## Usage


### Common substrings

This tool will find the longest commmon substring between two strings (provided as arguments).

Please see the [Common Substrings Readme](https://github.com/newbootz/problems/blob/master/CommonStrings.md) for more information.
```
python common_string.py "Everything is awesome" "Hello World is awesome"
is awesome
```

### Common susbsequence

This tool will process a list (provided as an argument) of string pairs and find the longest non-contigous subsequence between each pair in the file.

Please see the [Common Subsequence Readme](https://github.com/newbootz/problems/blob/master/CommonSubsequence.md) for more information.

```
cat common_subsequence_SAMPLE.txt
XMJYAUZ;MZJAWXU

python common_subsequence.py common_subsequence_SAMPLE.txt
MJAU
```

### Pig Latin

This program will translate your sentences (provided as an argument) into Pig Latin.

Please see the [Pig Latin Readme](https://github.com/newbootz/problems/blob/master/PigLatin.md) for more information.

```
python pig_latin.py "HeLLo World! I can't wait to explore your VAST forests. The-End!"
ElLOhay Orldway! I antca'y aitway otay exploreway ouryay ASTVay orestsfay. Hetay-Endway!
```


### Essay Monkey

This program will generate an essay provided word banks and number of paragraphs and number of sentences per paragraph arguments.

Please see the [Essay Monkey Readme](https://github.com/newbootz/problems/blob/master/EssayMonkey.md) for more information.
```
python essay_monkey.py 5 12
        The school lose the old community. A story borrow the bad team. The teacher give a political government. A right call the legal door. A back stood a possible water. A head agreed the open issue. The team decide a cold book. The day bring a national issue. A problem opened the other game. The month told the great team. The kid mean the cold study. A place closed the good book.

        The life became a real kind. A teacher show a short year. A story brought a open job. The face wrote the cold Name. The kid borrowed the poor city. A minute set the common home. A president bring the national year. A world went a single father. A kind promised a large thing. A state play a good history. A end suggest a whole case. The people seemed the physical student.

        The woman make the best health. The team be the old student. The research work a cold woman. The water fell a ready issue. The education worked a national house. The country left a little house. The health listened a able guy. The month want a whole government. A power show the cold Name. A power meant a other program. The research hold a special guy. A service understood the environmental way.

        The month wanted the young president. The room may a international educationent. The city like a different man. The friend tell the popular hour. A minute move the hot kind. The company borrowed a likely change. A change ran a likely back. A water held a hot city. A day seemed the old result. The head bring a real study. The hand used (to) the happy door. A story travel the certain house.

        A hour call a democratic kind. A girl use a full girl. The side turned a human minute. A word might a special book. The group carry the traditional member. The country finish a dead study. A eye needed the important teacher. A home looked a American number. A state learn a popular business. The war show a religious change. A parent thought the whole question. A home got a serious line.

```

### Logs

![Cool gif](images/demo.gif)

This tool parses `logs.txt`, creates a cache, and allows inclusive and exclusive log search functionality by operating system, browser, ip address, date, time, file requested, and referrer.

Please see the [Logs Readme](https://github.com/newbootz/problems/blob/master/Logs.md) for more information.

```
python logs.py --help

USAGE:


        NAME
            logs - Parse "logs.txt" file and allows the user to search inclusively and exclusively by the following:

                OS
                Browser
                IP
                Date
                Time
                File Requested
                Referrer


        SYNOPSIS
            logs.py [command]  [global options] [arguments]

        VERSION
            0.0.1

        GLOBAL OPTIONS
            --os=arg        - Search by operating system (example: --os="Windows")
            --browser=arg   - Search by browser (example: --browser="Internet Explorer")
            --ip=arg        - Search by IP address (example: --ip="127.0.0.1")
            --date=arg      - Search by date (example: --date="19/Jun/2012")
            --time=arg      - Search by time (example: --time="09:16:22")
            --file=arg      - Search by file (example: --file="0xb.jpg")
            --referrer=arg  - Search by referrer (example: --referrer="http://domain.com/azb")
            --version       - Display the program version
            --help          - Show this message

        COMMANDS
            inclusive  - Search the logs with search filters inclusively
            exclusive  - Search the logs with search filters exclusively
            load       - Parses provided log files and creates logs-cache.json

```

