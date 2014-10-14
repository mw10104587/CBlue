str = "i love to code"
arr = str.split(" ")
arr.each{ |x| x.reverse! }
new_str = arr.join(" ")