# Subroutines

Subroutines are a way of wrapping some functionality, some set of instructions, together and giving the resulting process a name. This is then called a subroutine. This is useful because, rather than having to write out the same number of instructions over and over again, we can simply reference the definition of this chunk of code with the name we have given it. 

You should be aware of two kinds of subroutines, which in the exams will be differentiated vocabularically: Procedures and functions. We'll explain the difference between the two below, though it deserves to be mentioned that most languages (including Python) don't distinguish between the two and use "function" to describe all subroutines. 

## Procedures vs Functions
In the exam jargon, the distinction between "functions" and "procedures" is that functions `return` somethign while procedures do not. This means that while procedures may have some kind of effect, like altering memory or the value of global variables, or printing values to the console, they do not produce a result that can be stored in a variable after the procedure has finished running. Meanwhile, it is in the nature of functions to produce a certain value that is `return`ed by the function at its termination. This means that a function produces a value that can be assigned to a variable or used as if it were a value hard-coded into the program. 

This means that if we have the following code:
```vba
function one()
    return 1
end function

x = one()
```

the variable `x` will be given value `1`. The function is *called* in the last line, which means that the code jumps from there to the beginning of the *body* of the function until it finds a `return` keyword. The value that is `return`ed is then substituted for the function call in the last line and the returned value is assigned to `x`. 

In the exam-style pseudocode, the difference between procedures and functions is specified by the beginnings and ends of the subroutine definitions. In most programming languages, the effective difference is the presence or absence of the `return` keyword.

In languages such as C or Java which require their variables to be annotated with a type when they are declared, subroutines are also annotated by the type of data they return. This may look like the following:
```C
int square(int x){
    return x*x;
}
```
When defining procedures which do not return anything, these languages typically require the return type to be specified as `void`:
```C
void greeting(){
    printf("Hello!");
} 
```

In Python, no difference between functions and procedures is usually made. In the tasks for this topic, I'm only asking you to write functions that `return` something.

## Global and Local Variables

Subroutine bodies can contain any code at all, including the definition of and assignment to variables. So, let us consider teh following dilemma:
```vba
x = 1

procedure f()
    y = 1
    print(x)
end procedure

f()

print(y)
```

The last line will cause an error. That is because the variable `y` lives inside the procedure `f` and ceases to exist when the procedure `f` has finished executing. The technical vocabulary to describe this is that the *scope* of `y` is `f`, and after the procedure call to `f`, the variable `y` is *out of scope*. However, the call to `print(x)` within `f` will not fail because `x` is defined outside of `f` and is accessible anywhere. 

The difference is that `x` is a *global variable*, while `y` is a *local variable*. To be precise, `y` is local to `f`.

## Parameters

Subroutines that always do the same thing are usually fairly uninteresting. Perhaps it is useful to avoid having to write out many lines of code many times, but that benefit is in itself limited. It is more beneficial to be able to provide *similar* behaviour for various starting or input values. For instance, the `print` procedure shows the user whatever value is provided to it. That is what is called a `parameter`. 

We can in particular use this to compute input-dependent values with functions: For instance, the `sqrt(x)` function from the `math` library in Python calculates the square root of its input value. 

The parameters you specify in the function definition act as local variables within the function body. That means that if you have a global variable called `x`, you can define a function that takes a parameter called `x`; the latter `x` will not be the same as the global variable `x`! Thus, for instance, the below code will print 2, not 1:
```vba
x = 1

procedure f(x)
    print(x)
end procedure

f(2)
```

A vocabularic note: The technical vocabulary you are required to be able to use and understand makes a difference between the words "parameter" and "argument". A "parameter" is the local variable used in the definition of a subroutine. An argument, in contrast, is the value that is passed into the subroutine when it is actually called. Perhaps the following example clarifies this:
```vba
procedure greeting(name)
    print("Hello", name)
end procedure

greeting("Mr Rattle")
```

In the above code, `name` is a parameter for the procedure `greeting`. However,`Mr Rattle` is an argument to the procedure call in the last line. As with "function" vs "procedure", most languages do not make a distinction between these two terms in practice. 

### Passing By Value vs Passing By Reference
Now, a little dilemma:
```vba
x = 1

procedure p(param)
    param = param + 1
    print(param)
end procedure

p(x)
print(x)
```

The first function call to `p` will certainly print `2`, because the value of `x` that is passed into `p` is `1` so after increasing the parameter `param` by `1`, `print(param)` outputs 1+1=`2`. 

What should the last line print, though? The value of `x`, of course. But what is that? Remember, `x` was passed into `p` as `param`, which was then increased by 1. So should `x` have changed in value? Maybe not, because after all, `param` is not the same thing as `x`, surely!? 

Whether `x` has changed because of the call to `p` is a question of how the value `x` was passed to the procedure `p`. Was the variable itself handed to `p`, or was its value passed to `p`? In other words, was the value of the variable `x` looked up, copied and then the copy handed to `p`? Or was the variable `x` taken as-was and the procedure `p` told "There is the bit of memory that you should use for `param`."? 

This is the difference between *passing by value* and *passing by reference*, respectively. In passing by value, subroutine arguments are copied before being used in the subroutine; this means that the original version of the variable does not change. In passing by reference, the suborutine is handed a pointer to the variable, giving it complete access to read **and** modify the value of the argument variable. In passing by reference, therefore, the value of an argument variable may change. 

By default, the parameters in exams are passed by value. Should this not be the case, the exam will either explicitly state this or annotate their pseudocode in the following way: 
```vba
procedure example(x: byVal, y: byRef)
    x = x+1
    y = y+1
end procedure

x = 0
y = 0
example(x, y)
print(x, y)
```
The above code would print `0 1` because `y` was passed by reference while `x` was passed by value. 