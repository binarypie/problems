# problems
A collection of coding problems.

## Getting Started

Prerequisite to run tests:
* [Golang 1.7](https://golang.org/dl/)

The solutions to the list of assigned problems are found in the following files.

Problems          | Source                | Tests                       | Remark
----------------- | --------------------- | --------------------------- | ------
CommonString      | common_strings.go     | common_strings_test.go      |
CommonSubsequence | common_subsequence.go | common_subsequence_test.go  |
EssayMonkey       | essay_monkey.go       | essay_monkey_test.go        | Didn't do the unique sentence length requirement
Logs              | logs.go               | logs_test.go                | Use either `go build` or `go install` to build the `logs-search` application

To run all the tests with basic coverage information:
```sh
$ go test -v -cover ./...
```

To build and run the `logs-search` application:
```sh
$ go build problems/cmd/logs-search
$ chmod +x logs-search
$ ./logs-search
$ ./logs-search 127.0.0.1 "Internet Explorer" Windows
$ ./logs-search Chrome iOS
$ ./logs-search Safari iOS
$ ./logs-search Linux http://domain.com/htm_data/7/1206/758536.html
$ ./logs-search Zyb.gif Nokia "19/Jun/2012:09:17:42 +0100"
$ ./logs-search AppleWebKit
$ ./logs-search "19/Jun/2012:09:32:15 +0100"
$ ./logs-search Firefox Windows
```
