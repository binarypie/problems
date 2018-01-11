def fibonacci(n)
  if n == 0
    return []
  elsif n == 1
    return [0]
  elsif n==2
    return [0,1]
  else
    fib_array = fibonacci(n-1)
    fib_array << fib_array[-1] + fib_array[-2]
  end
  return fib_array.join(', ')
end


puts fibonacci(3)
