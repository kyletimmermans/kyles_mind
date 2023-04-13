/*
If we want to check if the current player
is the host, we can use a function called isHost()
and it's used like: player isHost()
which will return true or false.

However, to get the name of the current player,
we can use self.name and since we cannot use self.name
with isHost(), we need a way to combine the 'self'
and 'player' objects.

We can do this by going through all of the player
names in the lobby and then comparing the self.name
and the player.name. This bridges the gap between
self and player, because one of those player.name
values will match self.name, and if they match,
we can use that matching player.name value in leu
of self.name because we know they're the same with
an if-statement.

Now that player.name is being used as self.name, we
can check if the player isHost().

The process looks something like this, we go through
all the player.name values and see if it matches self.name,
and if it does, we can then check for isHost()

Essentially, we're checking a name against a record system,
with one record being a name and a isHost() value e.g. ["XeXKyle", true]

self.name == player.name --> Make sure we have the correct record for current user

player.isHost() --> If correct record, check if they are the host

And if we have the correct record for self.name and isHost() is true,
self.name is the host.

### We are checking the same value, just in a different compatible vessel.
*/

foreach(player in level.players) {
		if (self.name == player.name && player isHost()) {
			self thread doHostThings();
	}
}
