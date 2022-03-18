numerator, denominator = 19134702400093278081449423917, 1066340417491710595814572169
a, remainder = 123, 123
function_value = 0
while remainder!=0:
    a = int(numerator / denominator)
    function_value += a
    remainder = numerator - a*denominator
    numerator = denominator
    denominator = remainder
print(function_value)