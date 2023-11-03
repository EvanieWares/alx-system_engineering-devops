#!/usr/bin/env ruby
# Displays the sender and receiver's phone number as well as the flags
# that were used
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")