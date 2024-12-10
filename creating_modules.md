# Creating Modules
- File: temperature.py
- In a module we store (code) functions
- Module name: temperature (filename without extension)
- To use the functions in the module: import module
- Syntax:
    import <module_name>
    import temperature

- The module temperature contains to_celsius() and to_fahrenheit().
- To use the functions in the module:
    <module_name>.<function_name()>

    import temperature
    temperature.to_celsius()
    temperature.to_fahrenheit()

    Alternatively;

    import temperature as t
    t.to_celsius()
    t.to_fahrenheit()

    Directly loading the function:

    from temperature import to_celsius, to_fahrenheit

