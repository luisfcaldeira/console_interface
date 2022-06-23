# An interface for interacting with user

## Installing

```
pip install console-interface
```

## Reading

For reading inputs from user, you can use this tool like this:

```python
console_reader = ConsoleReader()
console_reader.read_input()
```
## Writting

You can use ```ConsoleLogger()``` for the purpose of writting something to user. 

```python

c = ConsoleLogger()
c.log_this(msg="Message", profile=ErrorLoggerProfile()) #this will write in the red color. 
```
