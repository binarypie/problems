package main

import (
	"flag"
	"fmt"
	"os"
	. "problems"
)

const defaultLogFile = "./Logs.txt"

var logFile *string

func init() {
	logFile = flag.String("logfile", defaultLogFile, "Path to the log file to be loaded.")
}

func main() {
	flag.Parse()
	if len(flag.Args()) == 0 {
		usage()
		os.Exit(1)
	}

	logIndex := &LogIndex{}
	if err := logIndex.Load(*logFile); err != nil {
		fmt.Printf("Failed to load log file at %q. Make sure the filepath is correct and the content is well-formed.\nError: %s", *logFile, err)
		os.Exit(1)
	}

	logs, exist := logIndex.Get(flag.Args()...)
	if !exist {
		fmt.Printf("No log entries found for keys %v\n", flag.Args())
		os.Exit(0)
	}

	for _, log := range logs {
		fmt.Println(log)
	}
}

func usage() {
	fmt.Println(`NAME
    logs-search

SYNOPSIS
    logs-search [-f logFile] keys ...

DESCRIPTION
    logs-search searches the provided log file for log lines that satisfy the provided keys. The content of the log file must satisfy the Apache HTTP access logs regex pattern. Any other pattern is considered malformed.

    logs-search uses the values of the following attributes found in the provided log file as keys to its internal index:
    * OS             (Windows, Android, Linux, Nokia, iOS)
    * Browser        (Internet Explorer, Firefox, Chrome, Safari, Opera, AppleWebKit, UCWEB)
    * IP             (127.0.0.1)
    * Date and Time  (For example, 19/Jun/2012:09:16:22 +0100, 19/Jun/2012:09:16:30 +0100)
    * File Requested (For example, GO.jpg, Zyb.gif,Yyb.gif)
    * Referer        (For example, http://domain.com/htm_data/7/1206/758536.html, http://domain.com/htm_data/7/1206/758536.html)

    Note that keys are case-sensitive. At least one key must be provided. When exactly one key is provided, logs-search performs an exclusive search for log lines satisfying that key. If more than one keys are provided, only log lines that satisfy all the keys inclusively are returned.

    -f    Path to the log file to be loaded.

EXAMPLE
    logs-search 127.0.0.1 "Internet Explorer"
    logs-search 127.0.0.1 Opera
    logs-search 127.0.0.1 Chrome
    logs-search Nokia
    logs-search Internet
    logs-search "Internet Explorer"
    logs-search 127.0.0.1 "Internet Explorer"
    logs-search "Internet Explorer" 127.0.0.1
    logs-search Firefox
    logs-search "19/Jun/2012:09:20:42 +0100"
    logs-search "19/Jun/2012:09:20:42 +0100" Nokia
    logs-search "19/Jun/2012:09:20:42 +0100" Windows
    logs-search "19/Jun/2012:09:20:42 +0100" Linux
    logs-search "19/Jun/2012:09:20:42 +0100" 127.0.0.1
    logs-search 127.0.0.1 "19/Jun/2012:09:20:42 +0100"
    logs-search 127.0.0.1 "19/Jun/2012:09:20:42 +0100" Linux
    logs-search 127.0.0.1 "19/Jun/2012:09:20:42 +0100" Windows
    logs-search "Internet Explorer"
    logs-search 127.0.0.1
 `)
}
