package main

import (
    "fmt"
    "regexp"
    "flag"
    "os"
    "bufio"
    "bytes"
    "strings"
)


func main() {
    // arguments
    log_file := flag.String("log_file", "Logs.txt", "file containing logs")
    agent := flag.String("agent", "", "user agent (partial match)")
    date := flag.String("date", "", "date string (partial match)") 
    ip := flag.String("ip", "", "ip address (exact match)")
    url := flag.String("url", "", "requested url (partial match)")
    referer := flag.String("referer", "", "referer (partial match)")
    flag.Parse()

    // our regex for named capture groups against the log
    re := regexp.MustCompile(`(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<date>\d{2}\/[a-zA-Z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(.+) )(?P<url>.+)(HTTP\/1\..")) (\d{3}) (\d+) (["](?P<referer>(\-)|(.+))["]) (["](?P<agent>.+)["])`)

    // open log file
    file, error := os.Open(string(*log_file))
    if error != nil {
        fmt.Fprintf(os.Stderr, "%v\n", error)
        os.Exit(1)
    }
    defer file.Close()

    // start scanner
    s := bufio.NewScanner(file)
    for s.Scan() {
        // ignore blank lines
        if len(bytes.TrimSpace(s.Bytes())) == 0 {
            continue
        }

        // emtpy map to store log data
        log := make(map[string]string)
    
        // boolean to show we matched
        var match bool
        
        // apply regex to line and send capture groups to log map
        line := re.FindStringSubmatch(s.Text())
        for x, name := range re.SubexpNames() {
            if x != 0 {
                log[name] = line[x]
            }
        }

        // find matches
        // strings.Contains will return true with an empty substr
        // there's got to be a better way to do this.
        if strings.Contains(log["agent"], *agent) && 
           strings.Contains(log["date"], *date) &&
           strings.Contains(log["referer"], *referer) &&
           strings.Contains(log["url"], *url) {
            match = true

            if *ip != "" {
                if log["ip"] != *ip {
                    match = false
                }
            }
        }
                
        if match == true {
            fmt.Println(s.Text())
        }
    }
}
