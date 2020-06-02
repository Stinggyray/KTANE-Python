# KTANE - Python Version
This is a repository aimed at attempting to solve the Centurion with one person and one person only.
Honestly, I'm not sure if this is possible, but I'm sure as hell going to try.

Perhaps I'll discover that I can actually program. Or maybe I can't. I don't know.

The `standalone_modules` folder is for modules that stand on their own. They do not require any sort of edgework,
it's just calculations based on given values. All of these files are desigend to run on their own - none of them need
to be supplied anything. Just run them and they will solve the module for you. Alternatively, the cmd_main.py file should also be able to run them.

The `modules` folder all require a Bomb object to be passed to them, meaning they require edgework.
They shouldn't be excruciating to solve.

Anything that would be extraordinarily painful to code a solver for (like Colored Switches) or would be very
impractical to design a program around (like Memory) is instead included in the `manualpages` folder,
with a condensed manual page if I can find one. Some of the pages in there also have programs, I just wanted to make a condensed manual version
or found a good manual page.

# Formatting
When constructing your `Bomb` object, this is the formatting that should be followed.

|       Field      |       Type      |       Example       |
|:----------------:|:---------------:|:-------------------:|
| Serial Number    | str             | "AB5SD3"            |
| Lit Indicators   | list            | ["NSA", "FRQ"]      |
| Unlit Indicators | list            | ["NSA", "FRQ"]      |
| Batteries        | int             | 9                   |
| Battery Holders  | int             | 23                  |
| Module Count     | int             | 15                  |
| Time Limit       | float (minutes) | 15.5                |
| Port Plates      | list of lists   | [[], ["RJ", "RCA"]] |

Note that for port plates, each list within the lists is a port plate. As such the first [] within Port Plates
is actually an empty port plate.

# Standardized Inputs
Naturally, we have to standardize the things inputted in order to compare them programmatically.
## Colors
Just the color name, in all caps. (i.e. WHITE)
## Ports
The names are standardized. Omit any unnecessary details.

- PARALLEL
- SERIAL
- RJ
- RCA
- DVI
- PS2