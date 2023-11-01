#!/usr/bin/env ruby
if ARGV.length != 1
	puts "Usage: #{$PROGRAM_NAME} <log_file>"
	exit(1)
end
  
log_file = ARGV[0]
  
File.open(log_file, 'r').each_line do |line|
	if line =~ /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/
		sender = $1
		receiver = $2
		flags = $3
		puts "#{sender},#{receiver},#{flags}"
	end
end  