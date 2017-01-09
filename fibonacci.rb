=begin
 Author: Xini Yang
 Project: Fibonacci Sequence
 Date: 01/09/20178
=end




# function generate the fibonacci sequence
def fib_r(a,b,n)
	if n <= 1
		return a 
	
	else  
		print (a.to_s + ', ')
		return fib_r(b,a+b,n-1)
	end 

end 

#  get user input
flag = true
while flag
    puts "Please enter nth fibonacci number you want to generate or Q to quit:  "
    n = gets.chomp
    # make sure user input is valid
    if (n == "Q")
        flag = false
    else
        n = n.to_i
        if (n < 1)
            puts("Please enter a integer greater than 0")
        else
            puts fib_r(0,1,n)
        end
        
    end
end


