package problems

import (
	"fmt"
	"io/ioutil"
	logger "log"
	"regexp"
	"strings"
	"time"
)

const (
	layout                = "2/Jan/2006:15:04:05 -0700"
	delimiterSemiColon    = ";"
	delimiterOpenBracket  = "("
	delimiterCloseBracket = ")"
	delimiterForwardSlash = "/"

	osWindows    = "Windows"
	osAndroid    = "Android"
	osLinux      = "Linux"
	osNokia      = "NOKIAN78"
	osNokiaShort = "Nokia"
	osIOS        = "iPhone OS"
	osIOSOnIPad  = "iPad; CPU OS"
	osIOSShort   = "iOS"

	sv1                     = "SV1"
	browserInternetExplorer = "Internet Explorer"
	browserFirefox          = "Firefox"
	browserChrome           = "Chrome"
	browserSafari           = "Safari"
	browserOpera            = "Opera"
	browserAppleWebKit      = "AppleWebKit"
	browserUCWeb            = "UCWEB"

	trident = "Trident"

	logPattern = `^(?P<IP>(\S+)) (\S+) (\S+) \[(?P<DateTime>([^:]+):(\d+:\d+:\d+) ([^\]]+))\] \"(\S+) (?P<FileRequested>(.*?)) (\S+)\" (\S+) (\S+) "(?P<Referer>([^"]*))" "(?P<Agent>([^"]*))"$`
)

// LogIndex provides methods to search HTTP access logs.
type LogIndex struct {
	cache map[string][]string
}

// Load reads the given load file, and calls build to construct its internal log cache.
func (l *LogIndex) Load(logFile string) error {
	b, err := ioutil.ReadFile(logFile)
	if err != nil {
		return err
	}

	rawLogs := strings.Split(string(b), "\n")
	return l.build(rawLogs...)
}

// Get retrieves the value of keys from the LogIndex's internal cache.
// If a single key is provided, Get retrieves that key exclusively.
// If more than one key is provided, Get performs an inclusive search and returns only logs
// that satisfy all the keys.
func (l *LogIndex) Get(keys ...string) ([]string, bool) {
	result := []string{}
	for i := 0; i < len(keys); i++ {
		logs, exist := l.cache[keys[i]]
		if !exist {
			continue
		}

		for _, log := range logs {
			var found int
			for j := i + 1; j < len(keys); j++ {
				needles := []string{}
				switch keys[j] {
				case browserInternetExplorer:
					needles = append(needles, trident, sv1)
				case osIOSShort:
					needles = append(needles, osIOSOnIPad, osIOS)
				case osNokiaShort:
					needles = append(needles, osNokia)
				default:
					needles = append(needles, keys[j])
				}

				for _, needle := range needles {
					if strings.Contains(log, needle) {
						found++
					}
				}
			}
			if found == len(keys)-1 {
				result = append(result, log)
			}
		}
	}

	return result, len(result) > 0
}

// Build builds populates the internal cache of the LogIndexer. The index is a map of log attribute values (i.e. IP addresses, browsers, OS, referers - as defined by the AccessLog struct) to log lines that contain these attribute values.
func (l *LogIndex) build(rawLogs ...string) error {
	errors := []error{}
	l.cache = make(map[string][]string)
	for _, rawLog := range rawLogs {
		if rawLog == "" {
			continue
		}

		accessLog, err := ParseLog(rawLog)
		if err != nil {
			errors = append(errors, err)
			continue
		}

		if _, exist := l.cache[accessLog.IP]; !exist {
			l.cache[accessLog.IP] = make([]string, 0, len(rawLogs))
		}
		l.cache[accessLog.IP] = append(l.cache[accessLog.IP], rawLog)

		if _, exist := l.cache[accessLog.OS]; !exist {
			l.cache[accessLog.OS] = make([]string, 0, len(rawLogs))
		}
		l.cache[accessLog.OS] = append(l.cache[accessLog.OS], rawLog)

		if _, exist := l.cache[accessLog.Browser]; !exist {
			l.cache[accessLog.Browser] = make([]string, 0, len(rawLogs))
		}
		l.cache[accessLog.Browser] = append(l.cache[accessLog.Browser], rawLog)

		if _, exist := l.cache[accessLog.Referer]; !exist {
			l.cache[accessLog.Referer] = make([]string, 0, len(rawLogs))
		}
		l.cache[accessLog.Referer] = append(l.cache[accessLog.Referer], rawLog)

		fileRequested := accessLog.FileRequested
		if strings.HasPrefix(fileRequested, "/") {
			fileRequested = strings.TrimPrefix(fileRequested, "/")
		}
		if _, exist := l.cache[fileRequested]; !exist {
			l.cache[fileRequested] = make([]string, 0, len(rawLogs))
		}
		l.cache[fileRequested] = append(l.cache[fileRequested], rawLog)

		dateTime := accessLog.DateTime.Format(layout)
		if _, exist := l.cache[dateTime]; !exist {
			l.cache[dateTime] = make([]string, 0, len(rawLogs))
		}
		l.cache[dateTime] = append(l.cache[dateTime], rawLog)
	}

	var err error
	for _, e := range errors {
		err = fmt.Errorf("%s%s\n", err, e)
	}

	return err
}

// AccessLog represents a single entry in the log file.
type AccessLog struct {
	IP            string
	DateTime      time.Time
	FileRequested string
	Referer       string
	OS            string
	Browser       string
}

// ParseLog converts log into an AccessLog instance.
func ParseLog(log string) (*AccessLog, error) {
	pattern := regexp.MustCompile(logPattern)
	match := pattern.FindStringSubmatch(log)
	if match == nil {
		return nil, fmt.Errorf("Failed to parse log line %q. Make sure it's a well-formed Apache HTTP Access Log.", log)
	}

	accessLog := &AccessLog{}
	for index, name := range pattern.SubexpNames() {
		if name == "" {
			continue
		}

		switch name {
		case "IP":
			accessLog.IP = match[index]
		case "DateTime":
			datetime, err := time.Parse(layout, match[index])
			if err != nil {
				return nil, err
			}
			accessLog.DateTime = datetime
		case "FileRequested":
			accessLog.FileRequested = match[index]
		case "Referer":
			accessLog.Referer = match[index]
		case "Agent":
			agent := match[index]
			if agent != "" {
				// windows agent logs
				w := &WindowsAgentParser{}
				os, found := w.ParseOS(agent)
				if found {
					accessLog.OS = os
					if accessLog.Browser, found = w.ParseBrowser(agent); !found {
						logger.Println("Can't detect browser for", log)
					}
					continue
				}

				// android agent logs
				a := &AndroidAgentParser{}
				os, found = a.ParseOS(agent)
				if found {
					accessLog.OS = os
					if accessLog.Browser, found = a.ParseBrowser(agent); !found {
						logger.Println("Can't detect browser for", log)
					}
					continue
				}

				// linux agent logs
				l := &LinuxAgentParser{}
				os, found = l.ParseOS(agent)
				if found {
					accessLog.OS = os
					if accessLog.Browser, found = l.ParseBrowser(agent); !found {
						logger.Println("Can't detect browser for", log)
					}
					continue
				}

				// nokia agent logs
				n := &NokiaAgentParser{}
				os, found = n.ParseOS(agent)
				if found {
					accessLog.OS = os
					if accessLog.Browser, found = n.ParseBrowser(agent); !found {
						logger.Println("Can't detect browser for", log)
					}
					continue
				}

				// iOS agent logs
				ios := &IOSAgentParser{}
				os, found = ios.ParseOS(agent)
				if found {
					accessLog.OS = os
					if accessLog.Browser, found = ios.ParseBrowser(agent); !found {
						logger.Println("Can't detect browser for", log)
					}
					continue
				}
			}
		}
	}

	return accessLog, nil
}

// AgentParser provides interfaces to extract OS and browser information from agent log entries
// in HTTP access logs.
type AgentParser interface {
	// ParseOS looks for and returns specified os in the given log.
	// It expects the receiver to define its os.
	// If not found, it returns an empty string and false.
	ParseOS(log string) (string, bool)

	// ParseBrowser looks for and returns predefined browsers in the given log
	// If not found, it returns an empty string and false.
	ParseBrowser(log string) (string, bool)
}

// WindowsAgentParser provides methods to parse Windows access logs.
type WindowsAgentParser struct {
	AgentParser
}

// ParseOS parses for Windows OS strings in the given log.
// If not found, it returns false and an empty string.
func (w *WindowsAgentParser) ParseOS(log string) (string, bool) {
	if !strings.Contains(log, osWindows) {
		return "", false
	}
	return osWindows, true
}

// ParseBrowser parses for Windows browser strings in the given log.
// If not found, it returns an empty string and false.
func (w *WindowsAgentParser) ParseBrowser(log string) (string, bool) {
	var browser string
	if strings.Contains(log, trident) || strings.Contains(log, sv1) {
		browser = browserInternetExplorer
	} else if strings.Contains(log, browserChrome) {
		browser = browserChrome
	} else if strings.Contains(log, browserFirefox) {
		browser = browserFirefox
	} else if strings.Contains(log, browserOpera) {
		browser = browserOpera
	} else {
		browser = strings.TrimSpace(log)
	}

	return browser, true
}

// AndroidAgentParser provides methods to parse Android access logs.
type AndroidAgentParser struct {
	AgentParser
}

// ParseOS parses for Android OS strings in the given log.
// If not found, it returns false and an empty string.
func (a *AndroidAgentParser) ParseOS(log string) (string, bool) {
	if !strings.Contains(log, osAndroid) {
		return "", false
	}

	return osAndroid, true
}

// ParseBrowser parses for Android browser strings in the given log.
// If not found, it returns false and an empty string.
func (a *AndroidAgentParser) ParseBrowser(log string) (string, bool) {
	start := strings.Index(log, delimiterOpenBracket)
	if start == -1 {
		if strings.Contains(log, browserAppleWebKit) {
			return browserAppleWebKit, true
		}
		return "", false
	}

	browser := log[start:]
	start = strings.Index(browser, delimiterSemiColon)
	if start == -1 {
		return "", false
	}

	if strings.Contains(browser[start:], browserOpera) {
		return browserOpera, true
	} else if strings.Contains(browser[start:], browserSafari) {
		return browserSafari, true
	}

	return strings.TrimSpace(browser[start:]), true
}

// LinuxAgentParser provides methods to parse Linux access logs.
type LinuxAgentParser struct {
	AgentParser
}

// ParseOS parses for Linux OS strings in the given log.
// If not found, it returns false and an empty string.
func (l *LinuxAgentParser) ParseOS(log string) (string, bool) {
	if !strings.Contains(log, osLinux) {
		return "", false
	}

	return osLinux, true
}

// ParseBrowser parses for Linux browser strings in the given log.
// If not found, it returns false and an empty string.
func (l *LinuxAgentParser) ParseBrowser(log string) (string, bool) {
	start := strings.LastIndex(log, delimiterCloseBracket)
	if start == -1 {
		return "", false
	}

	if strings.Contains(log, browserUCWeb) {
		return browserUCWeb, true
	}

	return strings.TrimSpace(log[start+1:]), true
}

// NokiaAgentParser provides methods to parse Linux access logs.
type NokiaAgentParser struct {
	AgentParser
}

// ParseOS parses for Nokia OS strings in the given log.
// If not found, it returns false and an empty string.
func (n *NokiaAgentParser) ParseOS(log string) (string, bool) {
	if !strings.Contains(log, osNokia) {
		return "", false
	}

	return osNokiaShort, true
}

// ParseBrowser parses for Nokia browser strings in the given log.
// If not found, it returns an empty string and false.
func (n *NokiaAgentParser) ParseBrowser(log string) (string, bool) {
	start := strings.Index(log, delimiterForwardSlash) + 1
	if start == -1 {
		return "", false
	}

	if strings.Contains(log, browserUCWeb) {
		return browserUCWeb, true
	}

	return log[start:], true
}

// IOSAgentParser provides methods to parse Linux access logs.
type IOSAgentParser struct {
	AgentParser
}

// ParseOS parses for iOS strings in the given log.
// If not found, it returns false and an empty string.
func (i *IOSAgentParser) ParseOS(log string) (string, bool) {
	if !strings.Contains(log, osIOS) && !strings.Contains(log, osIOSOnIPad) {
		return "", false
	}

	return osIOSShort, true
}

// ParseBrowser parses for IOS browser strings in the given log.
// If not found, it returns an empty string and false.
func (i *IOSAgentParser) ParseBrowser(log string) (string, bool) {
	if strings.Contains(log, browserSafari) {
		return browserSafari, true
	} else if strings.Contains(log, browserAppleWebKit) {
		return browserAppleWebKit, true
	}

	return "", false
}
