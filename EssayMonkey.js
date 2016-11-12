var NumberOfParagraphs = prompt("How many paragraphs?");
var NumberOfSentences = prompt("How many sentences?");
console.log("Sentences: " + NumberOfSentences + " Paragraphs: " + NumberOfParagraphs);



var nouns_txt = "time,year,people,way,day,man,thing,woman,life,child,world,school,state,family,student,group,country,problem,hand,part,place,case,week,company,system,program,question,work,government,number,night,point,home,water,room,mother,area,money,story,fact,month,lot,right,study,book,eye,job,word,business,issue,side,kind,head,house,service,friend,father,power,hour,game,line,end,member,law,car,city,community,Name,president,team,minute,idea,kid,body,information,back,parent,face,others,level,office,door,health,person,art,war,history,party,result,change,morning,reason,research,girl,guy,momtime,year,people,way,day,man,thing,woman,life,child,world,school,state,family,student,group,country,problem,hand,part,place,case,week,company,system,program,question,work,government,number,night,point,home,water,room,mother,area,money,story,fact,month,lot,right,study,book,eye,job,word,business,issue,side,kind,head,house,service,friend,father,power,hour,game,line,end,member,law,car,city,community,Name,president,team,minute,idea,kid,body,information,back,parent,face,others,level,office,door,health,person,art,war,history,party,result,change,morning,reason,research,girl,guy,moment,air,teacher,force,educationent,air,teacher,force,education";
var verbs_txt = "agree,agreed,do,did,know,knew,read,read,suggest,suggested,allow,allowed,eat,ate,learn,learned,remember,remembered,take,took,answer,answered,explain,explained,leave,left,run,ran,talk,talked,ask,asked,fall,fell,like,liked,say,said,tell,told,be,was/were,feel,felt,listen,listened,see,saw,think,thought,become,became,fill,filled,live,lived,sell,sold,travel,travelled,begin,began,find,found,look,looked,seem,seemed,try,tried,believe,believed,finish,finished,lose,lost,send,sent,turn,turned,borrow,borrowed,follow,followed,make,made,set,set,understand,understood,break,broke,fly,flew,may,might,shall,use,used (to),bring,brought,forget,forgot,mean,meant,should,wait,waited,buy,bought,get,got,meet,met,show,showed,wake up,woke up,call,called,give,gave,move,moved,sit,sat,walk,walked,can,could,go,went,must,sleep,slept,want,wanted,carry,carried,happen,happened,need,needed,speak,spoke,watch,watched,change,changed,have,had,open,opened,spend,spent,will,would,close,closed,hear,heard,pay,paid,stand,stood,win,won,come,came,help,helped,play,played,start,started,work,worked,cut,cut,hold,held,promise,promised,stop,stopped,worry,worried,decide     ,decided,keep,kept,put,put,study,studied,write,wrote";
var adj_txt = "other,new,good,high,old,great,big,American,small,large,national,young,different,black,long,little,important,political,bad,white,real,best,right,social,only,public,sure,low,early,able,human,local,late,hard,major,better,economic,strong,possible,whole,free,military,true,federal,international,full,special,easy,clear,recent,certain,personal,open,red,difficult,available,likely,short,single,medical,current,wrong,private,past,foreign,fine,common,poor,natural,significant,similar,hot,dead,central,happy,serious,ready,simple,left,physical,general,environmental,financial,blue,democratic,dark,various,entire,close,legal,religious,cold,final,main,green,nice,huge,popular,traditional,cultural,";

var nouns = new Array();
var adj = new Array();
var verbs = new Array();

var essay = "";
var nlength;
var alength;
var vlength;

ParseWordBank();
GenerateEssay();
console.log(essay);

function ParseWordBank() { //parses text file into word bank arrays for nouns, adjs, and verbs
    nouns = nouns_txt.split(',');
    adj = adj_txt.split(',');
    verbs = verbs_txt.split(',');
    nlength = nouns.length;
    alength = adj.length;
    vlength = verbs.length;

    /*
        $.get('EssayMonkeyNouns.txt', function(data) {
            nouns = data.split(',');
            nlength = nouns.length;
            console.log("testing here");
            console.log(nouns);

        });

            $.get('EssayMonkeyAdjectives.txt', function(data) {
                adj = data.split(',');
                alength = adj.length;
                //document.getElementById("demo").innerHTML = adj;
            });
            $.get('EssayMonkeyVerbs.txt', function(data) {
                verbs = data.split(',');
                vlength = verbs.length;
                //document.getElementById("demo").innerHTML = verbs;
            });
        */

}


function GenerateEssay() {
    for (i = 0; i < NumberOfParagraphs; i++) {
        for (j = 0; j < NumberOfSentences; j++) {
            console.log("--------------------");
            y = randomNum(3);
            console.log(y);
            if (y == 1) {
                GenerateSimpleSentence();
            }
            if (y == 2) {
                GenerateCompoundSentence();
            }
            if (y == 3) {
                GenerateComplexSentence();
            }

        }
        essay += "\n\n";
    }


}



function testing() {
x = randomNum(3);
if (x == 1) 
  console.log("it's 1");
if (x == 2)
  console.log("it's 2");
if (x == 3) 
  console.log("it's 3");
}


function randomNum(max) {
    var x = Math.floor(Math.random() * max + 1);
    return x;
}

function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

function GenerateSimpleSentence() {
    console.log("simple");
    console.log("X before assignment: " + x);
    var x = randomNum(3);
    console.log("X before if: " + x);
    if (x == 1) {
        var sentence = verbs[randomNum(verbs.length)] + " " + adj[randomNum(adj.length)] + " " + nouns[randomNum(nouns.length)];
        sentence = capitalizeFirstLetter(sentence);
        sentence += GeneratePunctuation();
        essay += sentence;
        console.log("x= " + x + "\n" + sentence);
    }


    if (x == 2) {
        var sentence = verbs[randomNum(verbs.length)] + " " + adj[randomNum(adj.length)] + " " + adj[randomNum(adj.length)] + " " + nouns[randomNum(nouns.length)];
        sentence = capitalizeFirstLetter(sentence);
        sentence += GeneratePunctuation();
        essay += sentence;
        console.log("x= " + x + "\n" + sentence);
    }

    if (x == 3) {
        var sentence = adj[randomNum(adj.length)] + " " + adj[randomNum(adj.length)] + " " + nouns[randomNum(nouns.length)] + " " + verbs[randomNum(verbs.length)];
        sentence = capitalizeFirstLetter(sentence);
        sentence += GeneratePunctuation();
        essay += sentence;
        console.log("x= " + x + "\n" + sentence);
    }

}

function GenerateCompoundSentence() {
    console.log("compound");
    var sentence = verbs[randomNum(verbs.length)] + " " + adj[randomNum(adj.length)] + " " + adj[randomNum(adj.length)] + " " +
        nouns[randomNum(nouns.length)] + GenerateConjunction() + adj[randomNum(adj.length)] + " " +
        nouns[randomNum(nouns.length)] + " " + verbs[randomNum(verbs.length)];
    sentence = capitalizeFirstLetter(sentence);
    sentence += GeneratePunctuation();
    essay += sentence;
}

function GenerateComplexSentence() {
    console.log("complex");
    var sentence = verbs[randomNum(verbs.length)] + " " + adj[randomNum(adj.length)] + " " + adj[randomNum(adj.length)] + " " +
        nouns[randomNum(nouns.length)] + GenerateSubordinateConjunction() + adj[randomNum(adj.length)] + " " +
        nouns[randomNum(nouns.length)] + " " + verbs[randomNum(verbs.length)];
    sentence = capitalizeFirstLetter(sentence);
    sentence += GeneratePunctuation();
    essay += sentence;
}

//function GenerateCompoundComplexSentence() {}
//An additional feature

function GeneratePunctuation() {

 var   x = randomNum(3);
    if (x == 1) {
        return "! ";
    }
    if (x == 2) {
        return ". ";
    }
    if (x == 3) {
        return "? ";
    }
}

function GenerateConjunction() {
 var   x = randomNum(3);
    if (x == 1) {
        return " and ";
    }
    if (x == 2) {
        return " or ";
    }
    if (x == 3) {
        return " but ";
    }
}

function GenerateSubordinateConjunction() {
 var   x = randomNum(3);
    if (x == 1) {
        return " because ";
    }
    if (x == 2) {
        return " since ";
    }
    if (x == 3) {
        return " when ";
    }
}

