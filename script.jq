.index as $data |
[ $data[0] | keys | map(select(. != "id" and . != "datum")) ] as $keys |
[ $data[] | .datum ] as $dates |
$keys[] |
[
	.[] |
	"\(.)" as $key |
	{
		key: $key,
		value: [ $data[] | .[$key] | tonumber ]
	}
] | { dates: $dates } + from_entries
