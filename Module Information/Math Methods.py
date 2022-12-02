#######################################################################################################################
#                                                 MATH METHODS                                                        #
#######################################################################################################################
"""
Using C standard code behind the scenes this lets you access math functions that can't be used for more complex things
but for the most part general to advanced math, to use complex math functions you would need to use the module cmath.
Getting an exception instead of results that may be confusing lets you know what the complex number was and why it was
created.
"""

#######################################################################################################################
#                                                 FUNCTIONS                                                           #
#######################################################################################################################

########################################## Number-theoretic and Representation ########################################
import math

ceil = "math.ceil()"  # returns the smallest integer >= to x
floor = "math.floor()"  # returns the smallest integer <= to x
comb, perm = "math.comb()", "perm()"  # returns the amount of ways to choose k from n items without repeating and order
copy = "math.copysign()"  # return a float with the absolute value of x but sign of y
fabs = "math.fabs()"  # returns the absolute value of x
factorial = "math.factorial()"  # returns x as an integer, factorial multiplies full chosen numbers down to 1
fmod = "math.fmod()"  # returns the remainder of x/y, mainly used for floats
frexp = "math.frexp()"  # picks apart the internal representation of a float in a portable way

fsum = "math.fsum()"  # returns an accurate floating point sum of values in the iterable
gcd = "math.gcd()"  # returns the greatest divisor of the int arguments, non-0 returns the largest int of all args
isclose = "math.isclose()"  # returns true if a and b are close to each other
isfinite = "math.isfinite()"  # returns true if neither an infinity nor NaN
isinf = "math.isinf()"  # return true if x is a positive or negative infinity
isnan = "math.isnan()"  # return true if x is a NaN
isqrt = "math.isqrt()"  # return the positive int square root, removing the "i" gives a float
lcm = "math.lcm()"  # return the least common multiple of the specified int arguments

ldexp = "math.ldexp()"  # the reverse of the frexp function
modf = "math.modf()"  # return the fractional and int of x, both are floats and carry the sign of x
nextafter = "math.nextafter()"  # returns the next floating point value after x towards y
prod = "math.prod()"  # calculate the product of all elements in the input iterable, value starts at 1 for the product
remainder = "math.remainder()"  # return the IEEE 754-style of x with respect to y
trunc = "math.trunc()"  # return x without the fractional part
ulp = "math.ulp()"  # returns the value with the least significant bit of a float

########################################### Power and Logarithmic #####################################################
exp = "math.exp()"  # returns e raised to the power x
expm1 = "math.expm1()"  # return e raised to the power x - 1, gets result to full precision
log = "math.log()"  # with 1 arg return, natural logarithm of x to base e, with 2 logarithm of x to the given base

log1p = "math.log1p()"  # return the natural logarithm of 1 + x (base e)
log2 = "math.log2()", "log10()"  # return the base-2, base-10 logarithm of x, more accurate than log(x, 2), log(x, 10)
power = "math.pow()"  # returns x raised to the power of y

########################################### Trigonometric #############################################################
acos = "math.acos()"  # return the arc cosine of x results between 0 and pi
asin = "math.asin()"  # return the arc sine of x in radians, results between -pi/2 and pi/2
atan, atan2 = "math.atan()", "atan2()"  # return in radians, returns -pi and pi, atan2 are known to both inputs
cos = "math.cos()"  # return the cosine of x radians
dist = "math.dist()"  # return the euclidean distance between p and q, must have the same dimension, given as iterables
hypot = "math.hypot()"  # return the euclidean norm, the length of the vector from the origin to the coordinates given
sin = "math.sin()"  # return the sin of x radians
tan = "math.tan()"  # return the tan of x radians

########################################### Angular Conversion ########################################################
degrees = "math.degrees()"  # convert angle x from radians to degrees
radians = "math.radians()"  # convert angle x from degrees to radians

########################################### Hyperbolic ################################################################
acosh = "math.acosh()"  # return the reverse hyperbolic cosine of x
asinh = "math.asinh()"  # return the reverse hyperbolic sine of x
atanh = "math.atanh()"  # return the reverse hyperbolic tangent of x

cosh = "math.cosh()"  # return the reverse hyperbolic cosine of x
sinh = "math.sinh()"  # return the reverse hyperbolic sine of x
tanh = "math.tanh()"  # return the reverse hyperbolic tangent of x

########################################### Special ###################################################################
erf = "math.erf()"  # return the error function at x
erfc = "math.erfc()"  # return the complimentary function at x
gamma = "math.gamma()"  # return the gamma function at x
lgamma = "math.lgamma()"  # return the natural logarithm of the absolute value of the gamma function at x

#######################################################################################################################
#                                                 CONSTANTS                                                           #
#######################################################################################################################
pi = "math.pi"  # the constant of π = 3.141592
e = "math.e"  # the constant of e = 2.718281
tau = "math.tau"  # the constant of τ = 6.283185
inf = "math.inf"  # a floating point positive infinity, same as float("inf")
nan = "math.nan"  # a floating point "not a number" (NaN) value
