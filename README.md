# problems
A collection of coding problems.

## Getting Started

Prerequisite to run tests:
* [Golang 1.7](https://golang.org/dl/)

This solutions to the list of assigned problems are found in the following files. Note that [Golang 1.7](https://golang.org/dl/) must be installed to run the tests.

Problems          | Source                | Tests                       | Remark
----------------- | --------------------- | --------------------------- | ------
CommonString      | common_strings.go     | common_strings_test.go      |
CommonSubsequence | common_subsequence.go | common_subsequence_test.go  |
EssayMonkey       | essay_monkey.go       | essay_monkey_test.go        | Didn't do the unique sentence length requirement


To run all the tests with basic coverage information:
```sh
$ go test -v -cover ./...
```
