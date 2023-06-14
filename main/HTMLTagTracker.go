package main

import (
	"fmt"
	"strings"
)

func main () {
	/*
		If we are parsing an HTML file and we have several <DL>
		elements with closing tags </DL>, all of which have
		<A> tags in them, how can we get all of the <A> tags
		in just the level of a specific <DL> </DL> pair 
		i.e. same indetation? As there may be nested <DL>
		tags within our target <DL> tags that we are trying to
		extract from.

		In order to do this, we can start at the <DL> tag we want to
		get <A> tags from, and create a tracker that keeps track of
		which of how far / close we are to the target <DL> tags we are.
		If we find an inner <DL> tag within the current <DL> tag we're at,
		we increment the tracker, and when we find another </DL> close tag
		for that inner <DL> tag, we can decrement the tracker.

		When we get back to 0, we know that all of the non-target <DL> tags
		are closed, and we're back at the target <DL> tag level we want to
		collect at in the HTML tree. Effectively using the tracker to keep
		track of the indent level we're at.

		Methods of Thought:
		-------------------

		If we take 4 steps off the path, we need to take 4 steps back to the path
		to get back on track.

		Think of a line graph, it can go up (+1), but also go down (-1),
		until we get back to the original point.

		If we open issues, we need to close them. Once we get back to 0,
		we closed all the issues.
	*/

	// HTML tree
	html := `
        <DL>
        	<A>TEST_1</A>
        	<DL>
        		<A>TEST_2</A>
        		<DL>
        			<A>TEST_3</A>
        		</DL>
        	</DL>
        	<A>TEST_4</A>
        </DL>
    `

    lines := strings.Split(html, "\n")

    // Keep track of HTML tree indent level
    tracker := 0;

    // Collect all <A> tags in the outer-most <DL> tags
    // and not from any other level
	for _, line := range lines[2:] {
		if strings.Contains(line, "<DL>") {
			tracker++
		} else if strings.Contains(line, "</DL>") {
			tracker--
		} else if strings.Contains(line, "<A>") {
			if (tracker == 0) {
				fmt.Println(line)
			}
		}
	}
}
