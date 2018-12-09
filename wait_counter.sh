#!/bin/bash
# Waits for all currently active counters to expire
counters=("0")
for x in $(curl -s http://localhost/counter/); do
	counters+=("$(curl -s http://localhost/counter/${x}/)")
done
sleep $( printf '%s\n' "${counters[@]}" | sort -nr | head -n1 )