import random
import unittest
import os


class FileWordReader:
    def read_words(self, filename):
        with open(filename, 'r') as f:
            lines = f.read().splitlines()

        words = set()
        for line in lines:
            line_words = line.split(',')
            words.update(line_words)

        return words


class EssayMonkey:
    """A class that writes essays of variable sentence and paragraph count. Pool of words comes
        from external files"""
    def __init__(self, paragraph_count, sentence_count, *files, word_reader=FileWordReader()):
        if not isinstance(paragraph_count, int):
            raise ValueError("paragraph_count input '{}' is not an integer".format(paragraph_count))

        if not isinstance(sentence_count, int):
            raise ValueError("sentence_count input '{}' is not an integer".format(sentence_count))

        if len(files) < 1:
            raise ValueError("No word files were provided")

        self._paragraph_count = paragraph_count
        self._sentence_count = sentence_count

        words = set()
        for file in files:
            words.update(word_reader.read_words(file))

        self._words = words

    def write_essay(self):
        """Produces an essay based on the current paragraph and sentence counts, using the words
            provided when the object was created"""
        essay = ""
        words_count = len(self._words)

#        for _ in range(self._paragraph_count):
#            for _ in range(self._sentence_count):


        return essay

    def set_paragraph_count(self, paragraph_count):
        self._paragraph_count = paragraph_count

    def set_sentence_count(self, sentence_count):
        self._sentence_count = sentence_count




class EssayMonkeyTests(unittest.TestCase):
    """Tests for the ``EssayMonkey`` class"""

    def setUp(self):
        self.verbs_filename = "verbs.txt"
        with open(self.verbs_filename, 'w') as f:
            f.write("agree,agreed,do,did,know,knew,read,read,suggest,suggested,allow,allowed,eat,ate,learn,learned,"
                    "remember,remembered,take,took,answer,answered,explain,explained,leave,left,run,ran,talk,talked,"
                    "ask,asked,fall,fell,like,liked,say,said,tell,told,be,was/were,feel,felt,listen,listened,see,saw,"
                    "think,thought,become,became,fill,filled,live,lived,sell,sold,travel,travelled,begin,began,find,"
                    "found,look,looked,seem,seemed,try,tried,believe,believed,finish,finished,lose,lost,send,sent,turn,"
                    "turned,borrow,borrowed,follow,followed,make,made,set,set,understand,understood,break,broke,fly,"
                    "flew,may,might,shall,use,used (to),bring,brought,forget,forgot,mean,meant,should,wait,waited,buy,"
                    "bought,get,got,meet,met,show,showed,wake up,woke up,call,called,give,gave,move,moved,sit,sat,walk,"
                    "walked,can,could,go,went,must,sleep,slept,want,wanted,carry,carried,happen,happened,need,needed,"
                    "speak,spoke,watch,watched,change,changed,have,had,open,opened,spend,spent,will,would,close,closed,"
                    "hear,heard,pay,paid,stand,stood,win,won,come,came,help,helped,play,played,start,started,work,"
                    "worked,cut,cut,hold,held,promise,promised,stop,stopped,worry,worried,decide\t,decided,keep,kept,"
                    "put,put,study,studied,write,wrote")

        self.nouns_filename = "nouns.txt"
        with open(self.nouns_filename, 'w') as f:
            f.write("time,year,people,way,day,man,thing,woman,life,child,world,school,state,family,student,group,"
                    "country,problem,hand,part,place,case,week,company,system,program,question,work,government,number,"
                    "night,point,home,water,room,mother,area,money,story,fact,month,lot,right,study,book,eye,job,word,"
                    "business,issue,side,kind,head,house,service,friend,father,power,hour,game,line,end,member,law,car,"
                    "city,community,Name,president,team,minute,idea,kid,body,information,back,parent,face,others,level,"
                    "office,door,health,person,art,war,history,party,result,change,morning,reason,research,girl,guy,"
                    "momtime,year,people,way,day,man,thing,woman,life,child,world,school,state,family,student,group,"
                    "country,problem,hand,part,place,case,week,company,system,program,question,work,government,number,"
                    "night,point,home,water,room,mother,area,money,story,fact,month,lot,right,study,book,eye,job,word,"
                    "business,issue,side,kind,head,house,service,friend,father,power,hour,game,line,end,member,law,car,"
                    "city,community,Name,president,team,minute,idea,kid,body,information,back,parent,face,others,level,"
                    "office,door,health,person,art,war,history,party,result,change,morning,reason,research,girl,guy,"
                    "moment,air,teacher,force,educationent,air,teacher,force,education")

        self.adjectives_filename = "adjectives.txt"
        with open(self.adjectives_filename, 'w') as f:
            f.write("other,new,good,high,old,great,big,American,small,large,national,young,different,black,long,little,"
                    "important,political,bad,white,real,best,right,social,only,public,sure,low,early,able,human,local,"
                    "late,hard,major,better,economic,strong,possible,whole,free,military,true,federal,international,"
                    "full,special,easy,clear,recent,certain,personal,open,red,difficult,available,likely,short,single,"
                    "medical,current,wrong,private,past,foreign,fine,common,poor,natural,significant,similar,hot,dead,"
                    "central,happy,serious,ready,simple,left,physical,general,environmental,financial,blue,democratic,"
                    "dark,various,entire,close,legal,religious,cold,final,main,green,nice,huge,popular,traditional,"
                    "cultural,")

    def tearDown(self):
        try:
            os.remove(self.verbs_filename)
            os.remove(self.nouns_filename)
            os.remove(self.adjectives_filename)
        except:
            pass

    def test_write_essay_runs(self):
        monkey = EssayMonkey(1, 1, self.verbs_filename)

        monkey.write_essay()

    def test_no_deletion(self):
        monkey = EssayMonkey(1, 1, self.verbs_filename)

        monkey.write_essay()

        self.assertTrue(os.path.exists(self.verbs_filename))
        self.assertTrue(os.path.exists(self.nouns_filename))
        self.assertTrue(os.path.exists(self.adjectives_filename))

    def test_write_essay_returns_string(self):
        monkey = EssayMonkey(1, 1, self.verbs_filename)

        actual = monkey.write_essay()

        self.assertIsInstance(actual, str)

    def test_one_sentence(self):
        monkey = EssayMonkey(1, 1, self.verbs_filename)
        expected = 1

        actual = monkey.write_essay().count('.')

        self.assertEqual(expected, actual)

    def test_three_sentence(self):
        monkey = EssayMonkey(1, 3, self.verbs_filename)
        expected = 3

        actual = monkey.write_essay().count('.')

        self.assertEqual(expected, actual)

    def test_nine_sentence(self):
        monkey = EssayMonkey(3, 3, self.verbs_filename)
        expected = 9

        actual = monkey.write_essay().count('.')

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
