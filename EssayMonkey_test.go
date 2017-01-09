package essaymonkey

import (
	"testing"
)

func TestGenerate(t *testing.T) {

	//Generate and log 5 paragraphs, each with 4 pseudo-randomly created sentances
	essay := Generate(5, 4)
	t.Log(*essay)

	//Generate and log 10 paragraphs, each with 10 pseudo-randomly created sentances
	essay = Generate(10, 10)
	t.Log(*essay)
}
