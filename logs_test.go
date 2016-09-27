package problems

import (
	"io/ioutil"
	"os"
	"reflect"
	"testing"
	"time"
)

func TestLoadIndexFromFile(t *testing.T) {
	t.Run("given a log file", func(t *testing.T) {
		tempFile, err := ioutil.TempFile("", "")
		if err != nil {
			t.Fatal("Unexpected error ", err)
		}
		defer func() {
			if err := os.Remove(tempFile.Name()); err != nil {
				t.Fatal("Unexpected error: ", err)
			}
		}()

		input := []byte(`
127.0.0.1 - - [19/Jun/2012:09:16:22 +0100] "GET /GO.jpg HTTP/1.1" 499 0 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; SE 2.X MetaSr 1.0)"
127.0.0.1 - - [19/Jun/2012:09:16:25 +0100] "GET /Zyb.gif HTTP/1.1" 499 0 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QQDownload 711; SV1; .NET4.0C; .NET4.0E; 360SE)"
127.0.0.1 - - [19/Jun/2012:09:16:30 +0100] "GET /Zyb.gif HTTP/1.1" 499 0 "http://domain.com/htm_data/7/1206/758536.html" "Opera/9.80 (Android; Opera Mini/6.7.29878/27.1667; U; zh) Presto/2.8.119 Version/11.10"`)
		if _, err := tempFile.Write(input); err != nil {
			t.Fatal("Unexpected error ", err)
		}

		logIndex := &LogIndex{}
		if err := logIndex.Load(tempFile.Name()); err != nil {
			t.Fatal("Unexpected error ", err)
		}

		t.Run("loads logs into index", func(t *testing.T) {
			var osTests = []struct {
				attribute string
			}{
				{attribute: "127.0.0.1"},
				{attribute: osWindows},
				{attribute: osAndroid},
				{attribute: "GO.jpg"},
				{attribute: "Zyb.gif"},
				{attribute: browserInternetExplorer},
				{attribute: browserOpera},
				{attribute: "19/Jun/2012:09:16:22 +0100"},
				{attribute: "19/Jun/2012:09:16:25 +0100"},
				{attribute: "19/Jun/2012:09:16:30 +0100"},
				{attribute: "http://domain.com/htm_data/7/1206/758536.html"},
			}
			for _, test := range osTests {
				if _, exist := logIndex.Get(test.attribute); !exist {
					t.Errorf("Expected logs with %s to exist", test.attribute)
				}
			}
		})
	})
}

func TestGet(t *testing.T) {
	input := []string{
		`127.0.0.1 - - [19/Jun/2012:09:16:22 +0100] "GET /GO.jpg HTTP/1.1" 499 0 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; SE 2.X MetaSr 1.0)"`,
		`127.0.0.1 - - [19/Jun/2012:09:16:25 +0100] "GET /Zyb.gif HTTP/1.1" 499 0 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QQDownload 711; SV1; .NET4.0C; .NET4.0E; 360SE)"`,
		`127.0.0.1 - - [19/Jun/2012:09:16:30 +0100] "GET /Zyb.gif HTTP/1.1" 499 0 "http://domain.com/htm_data/7/1206/758536.html" "Opera/9.80 (Android; Opera Mini/6.7.29878/27.1667; U; zh) Presto/2.8.119 Version/11.10"`,
		`127.0.0.1 - - [19/Jun/2012:09:16:32 +0100] "GET /Yyb.gif HTTP/1.1" 499 0 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; 360SE)"`,
		`127.0.0.1 - - [19/Jun/2012:09:16:37 +0100] "GET /Zyb.gif HTTP/1.1" 499 0 "http://domain.com/htm_data/7/1206/758536.html" "JUC (Linux; U; 2.3.5; zh-cn; HTC_G20_T9399__For_Sprint; 480*854) UCWEB7.9.4.145/139/999"`,
		`127.0.0.1 - - [19/Jun/2012:09:16:53 +0100] "GET /GO.jpg HTTP/1.1" 200 34412 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; TencentTraveler 4.0)"`,
		`127.0.0.1 - - [19/Jun/2012:09:16:53 +0100] "GET /GO.jpg HTTP/1.1" 200 34412 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.12 (KHTML, like Gecko) Maxthon/3.4.1.600 Chrome/18.0.966.0 Safari/535.12"`,
		`127.0.0.1 - - [19/Jun/2012:09:18:24 +0100] "GET /Yyb.gif HTTP/1.1" 499 0 "http://domain.com/Yyb" "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0a1"`,
		`127.0.0.1 - - [19/Jun/2012:09:17:42 +0100] "GET /Zyb.gif HTTP/1.1" 499 0 "http://domain.com/htm_data/7/1206/758536.html" "NOKIAN78/UCWEB8.0.3.99/28/999"`,
		`127.0.0.1 - - [19/Jun/2012:09:17:47 +0100] "GET /Yyb.gif HTTP/1.1" 200 44630 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3"`,
		`127.0.0.1 - - [19/Jun/2012:09:17:44 +0100] "GET /GO.jpg HTTP/1.1" 200 34412 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/5.0 (iPad; CPU OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3"`,
		`127.0.0.1 - - [19/Jun/2012:09:20:23 +0100] "GET /Zyb.gif HTTP/1.1" 200 1275074 "http://domain.com/htm_data/7/1206/758536.html" "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.10.229 Version/11.62"`,
		`127.0.0.1 - - [19/Jun/2012:09:32:13 +0100] "GET /Zyb.gif HTTP/1.1" 200 4756 "http://domain.com/htm_data/7/1206/758536.html" "SAMSUNG-GT-I9228_TD/1.0 Android/2.3.5 Release/9.15.2011 Browser/AppleWebKit533.1 Profile/MIDP-2.1 Configuration/CLDC-1.1"`,
		`127.0.0.1 - - [19/Jun/2012:09:38:39 +0100] "GET /Zyb.gif HTTP/1.1" 200 4756 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; HTC HD2 Build/MIUI) UC AppleWebKit/534+ (KHTML, like Gecko) Mobile Safari/533.16"`}

	logIndex := LogIndex{}
	if err := logIndex.build(input...); err != nil {
		t.Fatal("Unexpected error ", err)
	}

	t.Run("given more than one keys", func(t *testing.T) {
		var tests = []struct {
			keys     []string
			expected []string
		}{
			{keys: []string{"127.0.0.1", osAndroid, browserOpera}, expected: []string{input[2]}},
			{keys: []string{osWindows, browserOpera, "Zyb.gif"}, expected: []string{input[11]}},
			{keys: []string{browserInternetExplorer, "127.0.0.1", osWindows}, expected: []string{input[0], input[1], input[3], input[5]}},
			{keys: []string{"GO.jpg", browserInternetExplorer, osWindows}, expected: []string{input[0], input[5]}},
			{keys: []string{"Zyb.gif", osWindows, "http://domain.com/htm_data/7/1206/758536.html"}, expected: []string{input[1], input[11]}},
			{keys: []string{"Zyb.gif"}, expected: []string{input[1], input[2], input[4], input[8], input[11], input[12], input[13]}},
			{keys: []string{"Yyb.gif", "19/Jun/2012:09:16:32 +0100"}, expected: []string{input[3]}},
			{keys: []string{"19/Jun/2012:09:17:44 +0100", osIOSShort}, expected: []string{input[10]}},
			{keys: []string{"Zyb.gif", browserUCWeb}, expected: []string{input[4], input[8]}},
			{keys: []string{"Zyb.gif", osNokiaShort, browserUCWeb}, expected: []string{input[8]}},
		}

		for _, test := range tests {
			actual, exist := logIndex.Get(test.keys...)
			if !exist {
				t.Fatalf("Expected logs to exist for keys: [%v]", test.keys)
			}
			if !reflect.DeepEqual(actual, test.expected) {
				t.Errorf("Mismatch logs.\nExpected %q\nBut got %q", test.expected, actual)
			}
		}
	})
}

func TestBuildIndex(t *testing.T) {
	t.Run("given raw access logs", func(t *testing.T) {
		input := []string{
			`127.0.0.1 - - [19/Jun/2012:09:16:22 +0100] "GET /GO.jpg HTTP/1.1" 499 0 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; SE 2.X MetaSr 1.0)"`,
			`127.0.0.1 - - [19/Jun/2012:09:16:25 +0100] "GET /Zyb.gif HTTP/1.1" 499 0 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QQDownload 711; SV1; .NET4.0C; .NET4.0E; 360SE)"`,
			`127.0.0.1 - - [19/Jun/2012:09:16:30 +0100] "GET /Zyb.gif HTTP/1.1" 499 0 "http://domain.com/htm_data/7/1206/758536.html" "Opera/9.80 (Android; Opera Mini/6.7.29878/27.1667; U; zh) Presto/2.8.119 Version/11.10"`,
			`127.0.0.1 - - [19/Jun/2012:09:16:32 +0100] "GET /Yyb.gif HTTP/1.1" 499 0 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; 360SE)"`,
			`127.0.0.1 - - [19/Jun/2012:09:16:37 +0100] "GET /Zyb.gif HTTP/1.1" 499 0 "http://domain.com/htm_data/7/1206/758536.html" "JUC (Linux; U; 2.3.5; zh-cn; HTC_G20_T9399__For_Sprint; 480*854) UCWEB7.9.4.145/139/999"`,
			`127.0.0.1 - - [19/Jun/2012:09:16:53 +0100] "GET /GO.jpg HTTP/1.1" 200 34412 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; TencentTraveler 4.0)"`,
			`127.0.0.1 - - [19/Jun/2012:09:16:53 +0100] "GET /GO.jpg HTTP/1.1" 200 34412 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.12 (KHTML, like Gecko) Maxthon/3.4.1.600 Chrome/18.0.966.0 Safari/535.12"`,
			`127.0.0.1 - - [19/Jun/2012:09:18:24 +0100] "GET /Yyb.gif HTTP/1.1" 499 0 "http://domain.com/Yyb" "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0a1"`,
			`127.0.0.1 - - [19/Jun/2012:09:17:42 +0100] "GET /Zyb.gif HTTP/1.1" 499 0 "http://domain.com/htm_data/7/1206/758536.html" "NOKIAN78/UCWEB8.0.3.99/28/999"`,
			`127.0.0.1 - - [19/Jun/2012:09:17:47 +0100] "GET /Yyb.gif HTTP/1.1" 200 44630 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3"`,
			`127.0.0.1 - - [19/Jun/2012:09:17:44 +0100] "GET /GO.jpg HTTP/1.1" 200 34412 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/5.0 (iPad; CPU OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3"`,
			`127.0.0.1 - - [19/Jun/2012:09:20:23 +0100] "GET /Zyb.gif HTTP/1.1" 200 1275074 "http://domain.com/htm_data/7/1206/758536.html" "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.10.229 Version/11.62"`,
			`127.0.0.1 - - [19/Jun/2012:09:32:13 +0100] "GET /Zyb.gif HTTP/1.1" 200 4756 "http://domain.com/htm_data/7/1206/758536.html" "SAMSUNG-GT-I9228_TD/1.0 Android/2.3.5 Release/9.15.2011 Browser/AppleWebKit533.1 Profile/MIDP-2.1 Configuration/CLDC-1.1"`,
			`127.0.0.1 - - [19/Jun/2012:09:38:39 +0100] "GET /Zyb.gif HTTP/1.1" 200 4756 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; HTC HD2 Build/MIUI) UC AppleWebKit/534+ (KHTML, like Gecko) Mobile Safari/533.16"`,
		}

		logIndex := LogIndex{}
		if err := logIndex.build(input...); err != nil {
			t.Fatal("Unexpected error ", err)
		}

		t.Run("the log index is built correctly", func(t *testing.T) {
			var tests = []struct {
				attribute     string
				expectedCount int
			}{
				{attribute: "127.0.0.1", expectedCount: 14},
				{attribute: osWindows, expectedCount: 7},
				{attribute: osAndroid, expectedCount: 3},
				{attribute: osLinux, expectedCount: 1},
				{attribute: osIOSShort, expectedCount: 2},
				{attribute: osNokiaShort, expectedCount: 1},
				{attribute: browserInternetExplorer, expectedCount: 4},
				{attribute: browserFirefox, expectedCount: 1},
				{attribute: browserChrome, expectedCount: 1},
				{attribute: browserSafari, expectedCount: 3},
				{attribute: browserOpera, expectedCount: 2},
				{attribute: browserAppleWebKit, expectedCount: 1},
				{attribute: browserUCWeb, expectedCount: 2},
				{attribute: "http://domain.com/htm_data/7/1206/758536.html", expectedCount: 13},
				{attribute: "http://domain.com/Yyb", expectedCount: 1},
				{attribute: "GO.jpg", expectedCount: 4},
				{attribute: "Zyb.gif", expectedCount: 7},
				{attribute: "Yyb.gif", expectedCount: 3},
				{attribute: "19/Jun/2012:09:16:22 +0100", expectedCount: 1},
				{attribute: "19/Jun/2012:09:16:25 +0100", expectedCount: 1},
				{attribute: "19/Jun/2012:09:16:30 +0100", expectedCount: 1},
				{attribute: "19/Jun/2012:09:16:32 +0100", expectedCount: 1},
				{attribute: "19/Jun/2012:09:16:37 +0100", expectedCount: 1},
				{attribute: "19/Jun/2012:09:16:53 +0100", expectedCount: 2},
				{attribute: "19/Jun/2012:09:18:24 +0100", expectedCount: 1},
				{attribute: "19/Jun/2012:09:17:42 +0100", expectedCount: 1},
				{attribute: "19/Jun/2012:09:17:47 +0100", expectedCount: 1},
				{attribute: "19/Jun/2012:09:17:44 +0100", expectedCount: 1},
				{attribute: "19/Jun/2012:09:20:23 +0100", expectedCount: 1},
				{attribute: "19/Jun/2012:09:32:13 +0100", expectedCount: 1},
				{attribute: "19/Jun/2012:09:38:39 +0100", expectedCount: 1},
			}

			for _, test := range tests {
				logs, exist := logIndex.Get(test.attribute)
				if !exist {
					t.Errorf("Expected log lines with %q to exist", test.attribute)
				}
				if len(logs) != test.expectedCount {
					t.Errorf("Mismatch log count for logs with %q. Expected %d, but got %d", test.attribute, test.expectedCount, len(logs))
				}
			}
		})
	})
}

func TestParseLog(t *testing.T) {
	var tests = []struct {
		log      string
		datetime string
		expected *AccessLog
	}{
		{log: `127.0.0.1 - - [19/Jun/2012:09:16:22 +0100] "GET /GO.jpg HTTP/1.1" 499 0 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; SE 2.X MetaSr 1.0)"`,
			expected: &AccessLog{
				IP:            "127.0.0.1",
				DateTime:      genDateTime("19/Jun/2012:09:16:22 +0100"),
				FileRequested: "/GO.jpg",
				Referer:       "http://domain.com/htm_data/7/1206/758536.html",
				OS:            "Windows",
				Browser:       browserInternetExplorer,
			},
		},
		{log: `127.0.0.1 - - [19/Jun/2012:09:16:25 +0100] "GET /Zyb.gif HTTP/1.1" 499 0 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QQDownload 711; SV1; .NET4.0C; .NET4.0E; 360SE)"`,
			expected: &AccessLog{
				IP:            "127.0.0.1",
				DateTime:      genDateTime("19/Jun/2012:09:16:25 +0100"),
				FileRequested: "/Zyb.gif",
				Referer:       "http://domain.com/htm_data/7/1206/758536.html",
				OS:            "Windows",
				Browser:       browserInternetExplorer,
			},
		},
		{log: `127.0.0.1 - - [19/Jun/2012:09:16:30 +0100] "GET /Zyb.gif HTTP/1.1" 499 0 "http://domain.com/htm_data/7/1206/758536.html" "Opera/9.80 (Android; Opera Mini/6.7.29878/27.1667; U; zh) Presto/2.8.119 Version/11.10"`,
			expected: &AccessLog{
				IP:            "127.0.0.1",
				DateTime:      genDateTime("19/Jun/2012:09:16:30 +0100"),
				FileRequested: "/Zyb.gif",
				Referer:       "http://domain.com/htm_data/7/1206/758536.html",
				OS:            "Android",
				Browser:       browserOpera,
			},
		},
		{log: `127.0.0.1 - - [19/Jun/2012:09:16:32 +0100] "GET /Yyb.gif HTTP/1.1" 499 0 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; 360SE)"`,
			expected: &AccessLog{
				IP:            "127.0.0.1",
				DateTime:      genDateTime("19/Jun/2012:09:16:32 +0100"),
				FileRequested: "/Yyb.gif",
				Referer:       "http://domain.com/htm_data/7/1206/758536.html",
				OS:            "Windows",
				Browser:       browserInternetExplorer,
			},
		},
		{log: `127.0.0.1 - - [19/Jun/2012:09:16:37 +0100] "GET /Zyb.gif HTTP/1.1" 499 0 "http://domain.com/htm_data/7/1206/758536.html" "JUC (Linux; U; 2.3.5; zh-cn; HTC_G20_T9399__For_Sprint; 480*854) UCWEB7.9.4.145/139/999"`,
			expected: &AccessLog{
				IP:            "127.0.0.1",
				DateTime:      genDateTime("19/Jun/2012:09:16:37 +0100"),
				FileRequested: "/Zyb.gif",
				Referer:       "http://domain.com/htm_data/7/1206/758536.html",
				OS:            "Linux",
				Browser:       browserUCWeb,
			},
		},
		{log: `127.0.0.1 - - [19/Jun/2012:09:16:53 +0100] "GET /GO.jpg HTTP/1.1" 200 34412 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; TencentTraveler 4.0)"`,
			expected: &AccessLog{
				IP:            "127.0.0.1",
				DateTime:      genDateTime("19/Jun/2012:09:16:53 +0100"),
				FileRequested: "/GO.jpg",
				Referer:       "http://domain.com/htm_data/7/1206/758536.html",
				OS:            "Windows",
				Browser:       browserInternetExplorer,
			},
		},
		{log: `127.0.0.1 - - [19/Jun/2012:09:16:53 +0100] "GET /GO.jpg HTTP/1.1" 200 34412 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.12 (KHTML, like Gecko) Maxthon/3.4.1.600 Chrome/18.0.966.0 Safari/535.12"`,
			expected: &AccessLog{
				IP:            "127.0.0.1",
				DateTime:      genDateTime("19/Jun/2012:09:16:53 +0100"),
				FileRequested: "/GO.jpg",
				Referer:       "http://domain.com/htm_data/7/1206/758536.html",
				OS:            "Windows",
				Browser:       browserChrome,
			},
		},
		{log: `127.0.0.1 - - [19/Jun/2012:09:18:24 +0100] "GET /Yyb.gif HTTP/1.1" 499 0 "http://domain.com/Yyb" "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0a1"`,
			expected: &AccessLog{
				IP:            "127.0.0.1",
				DateTime:      genDateTime("19/Jun/2012:09:18:24 +0100"),
				FileRequested: "/Yyb.gif",
				Referer:       "http://domain.com/Yyb",
				OS:            "Windows",
				Browser:       browserFirefox,
			},
		},
		{log: `127.0.0.1 - - [19/Jun/2012:09:17:42 +0100] "GET /Zyb.gif HTTP/1.1" 499 0 "http://domain.com/htm_data/7/1206/758536.html" "NOKIAN78/UCWEB8.0.3.99/28/999"`,
			expected: &AccessLog{
				IP:            "127.0.0.1",
				DateTime:      genDateTime("19/Jun/2012:09:17:42 +0100"),
				FileRequested: "/Zyb.gif",
				Referer:       "http://domain.com/htm_data/7/1206/758536.html",
				OS:            "Nokia",
				Browser:       browserUCWeb,
			},
		},
		{log: `127.0.0.1 - - [19/Jun/2012:09:17:47 +0100] "GET /Yyb.gif HTTP/1.1" 200 44630 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3"`,
			expected: &AccessLog{
				IP:            "127.0.0.1",
				DateTime:      genDateTime("19/Jun/2012:09:17:47 +0100"),
				FileRequested: "/Yyb.gif",
				Referer:       "http://domain.com/htm_data/7/1206/758536.html",
				OS:            "iOS",
				Browser:       browserSafari,
			},
		},
		{log: `127.0.0.1 - - [19/Jun/2012:09:17:44 +0100] "GET /GO.jpg HTTP/1.1" 200 34412 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/5.0 (iPad; CPU OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3"`,
			expected: &AccessLog{
				IP:            "127.0.0.1",
				DateTime:      genDateTime("19/Jun/2012:09:17:44 +0100"),
				FileRequested: "/GO.jpg",
				Referer:       "http://domain.com/htm_data/7/1206/758536.html",
				OS:            "iOS",
				Browser:       browserSafari,
			},
		},
		{log: `127.0.0.1 - - [19/Jun/2012:09:20:23 +0100] "GET /Zyb.gif HTTP/1.1" 200 1275074 "http://domain.com/htm_data/7/1206/758536.html" "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.10.229 Version/11.62"`,
			expected: &AccessLog{
				IP:            "127.0.0.1",
				DateTime:      genDateTime("19/Jun/2012:09:20:23 +0100"),
				FileRequested: "/Zyb.gif",
				Referer:       "http://domain.com/htm_data/7/1206/758536.html",
				OS:            "Windows",
				Browser:       browserOpera,
			},
		},
		{log: `127.0.0.1 - - [19/Jun/2012:09:32:13 +0100] "GET /Zyb.gif HTTP/1.1" 200 4756 "http://domain.com/htm_data/7/1206/758536.html" "SAMSUNG-GT-I9228_TD/1.0 Android/2.3.5 Release/9.15.2011 Browser/AppleWebKit533.1 Profile/MIDP-2.1 Configuration/CLDC-1.1"`,
			expected: &AccessLog{
				IP:            "127.0.0.1",
				DateTime:      genDateTime("19/Jun/2012:09:32:13 +0100"),
				FileRequested: "/Zyb.gif",
				Referer:       "http://domain.com/htm_data/7/1206/758536.html",
				OS:            "Android",
				Browser:       browserAppleWebKit,
			},
		},
		{log: `127.0.0.1 - - [19/Jun/2012:09:38:39 +0100] "GET /Zyb.gif HTTP/1.1" 200 4756 "http://domain.com/htm_data/7/1206/758536.html" "Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; HTC HD2 Build/MIUI) UC AppleWebKit/534+ (KHTML, like Gecko) Mobile Safari/533.16"`,
			expected: &AccessLog{
				IP:            "127.0.0.1",
				DateTime:      genDateTime("19/Jun/2012:09:38:39 +0100"),
				FileRequested: "/Zyb.gif",
				Referer:       "http://domain.com/htm_data/7/1206/758536.html",
				OS:            "Android",
				Browser:       browserSafari,
			},
		},
	}

	for _, test := range tests {
		actual, err := ParseLog(test.log)
		if err != nil {
			t.Fatal("Unexpected error: ", err)
		}

		if !reflect.DeepEqual(test.expected, actual) {
			t.Errorf("Mismatch log.\nBad input: [%s].\nExpected %+v\nBut got  %+v", test.log, test.expected, actual)
		}
	}
}

func genDateTime(datetime string) time.Time {
	dt, _ := time.Parse(layout, datetime)
	return dt
}
