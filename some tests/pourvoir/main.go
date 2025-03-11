package main

import (
	"fmt"
	"net/http"
)

const (
	specificHeaderKey   = "amine"
	specificHeaderValue = "9arnouna"
	// specificCookieName  = "specific_cookie"
	// specificCookieValue = "cookie-value"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {

		headerValue := r.Header.Get(specificHeaderKey)
		if headerValue == specificHeaderValue {
			fmt.Fprintf(w, "abobi\n")
			return
		}

		// cookie, err := r.Cookie(specificCookieName)
		// if err == nil && cookie.Value == specificCookieValue {
		// 	fmt.Fprintf(w, "Data served based on cookie value: %s\n", cookie.Value)
		// 	return
		// }

		http.Error(w, "Forbidden", http.StatusForbidden)
	})

	fmt.Println("Server started at :8080")
	http.ListenAndServe(":8080", nil)
}
