#!/usr/bin/ruby
# calculate the PPI from resolution and screen size

def usage()
	puts "Usage: #{$0} [width resolution in pixels] [height resolution in pixels] [diagnonal size in inch]"
end

def compare()
	puts
	puts "examples:"
	puts "lenovo x220:	1366x768 12.50 \" ->\t125.367427987 ppi"
	puts "macbook air: 	1440x900 13.30 \" ->\t127.677940133 ppi"
	puts "nexus s:   	 480x800  4.00 \" ->\t233.238075794 ppi"
	puts "galaxy nexus:	1280x720  4.65 \" ->\t315.828984958 ppi"
	puts "iphone 4s: 	 960x640  3.50 \" ->\t329.650402328 ppi"
	puts "#########################################################"
end


if ARGV.length < 3
	usage
else
	w, h, di = ARGV[0].to_i, ARGV[1].to_i, ARGV[2].to_f
	dp = Math.sqrt((w**2) + (h**2))
	ppi = (dp/di)
	compare
	puts "your entry:\t#{w}x#{h} #{di} \" ->\t#{ppi} ppi"
end
