# Combination Lock

Requires 3 numbers to unlock.

- Turn dial to the right to the first number.
- Turn dial to the left to the second number.
- Turn dial to the right to to the last number.

If two numbers are the same, perform a full revolution.

Find the combination using the following calculations:

## Numbers
If you have 2-factor codes for some reason, this will change.

These numbers are all mod 20 (add/subtract 20 until within range 0-19).

First number:
- Last digit of serial
- \+ \# of solved modules
- \+ \# of batteries

Second number:
- Number of modules (including needy)
- \+ \# of solved modules

Third number:
- Sum of first + second number